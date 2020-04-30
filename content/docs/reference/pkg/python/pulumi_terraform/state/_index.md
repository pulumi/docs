---
title: Module state
title_tag: Module state | Package pulumi_terraform | Python SDK
linktitle: state
notitle: true
---

<div class="section" id="state">
<h1>state<a class="headerlink" href="#state" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-terraform">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-terraform/issues">pulumi/pulumi-terraform repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-terraform/issues">terraform-providers/terraform-provider-terraform repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_terraform.state"></span><dl class="py class">
<dt id="pulumi_terraform.state.ArtifactoryBackendArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">ArtifactoryBackendArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">repo</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">subpath</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.ArtifactoryBackendArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration options for a Terraform Remote State stored in the Artifactory backend.</p>
<p>Constructs an ArtifactoryBackendArgs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>repo</strong> – The username with which to authenticate to Artifactory. Sourced from <code class="docutils literal notranslate"><span class="pre">ARTIFACTORY_USERNAME</span></code> in the
environment, if unset</p></li>
<li><p><strong>subpath</strong> – Path within the repository.</p></li>
<li><p><strong>url</strong> – The Artifactory URL. Note that this is the base URL to artifactory, not the full repo and subpath.</p></li>
</ul>
</dd>
</dl>
<p>However, it must include the path to the artifactory installation - likely this will end in <code class="docutils literal notranslate"><span class="pre">/artifactory</span></code>.
Sourced from <code class="docutils literal notranslate"><span class="pre">ARTIFACTORY_URL</span></code> in the environment, if unset.
:param username: The username with which to authenticate to Artifactory. Sourced from <code class="docutils literal notranslate"><span class="pre">ARTIFACTORY_USERNAME</span></code>
in the environment, if unset.
:param password: The password with which to authenticate to Artifactory. Sourced from <code class="docutils literal notranslate"><span class="pre">ARTIFACTORY_PASSWORD</span></code>
in the environment, if unset.
:param workspace: The Terraform workspace from which to read state.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_terraform.state.AzureRMBackendArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">AzureRMBackendArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">storage_account_name</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">container_name</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_msi</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subscription_id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">msi_endpoint</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sas_token</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.AzureRMBackendArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration options for a Terraform Remote State stored in the AzureRM backend.</p>
<blockquote>
<div><p>Constructs an AzureRMBackendArgs</p>
<dl class="field-list simple">
<dt class="field-odd">param storage_account_name</dt>
<dd class="field-odd"><p>The name of the storage account.</p>
</dd>
<dt class="field-even">param container_name</dt>
<dd class="field-even"><p>The name of the storage container within the storage account.</p>
</dd>
<dt class="field-odd">param key</dt>
<dd class="field-odd"><p>The name of the blob in representing the Terraform State file inside the storage container.</p>
</dd>
<dt class="field-even">param environment</dt>
<dd class="field-even"><p>The Azure environment which should be used. Possible values are <code class="docutils literal notranslate"><span class="pre">public</span></code> (default), <code class="docutils literal notranslate"><span class="pre">china</span></code>,</p>
</dd>
</dl>
</div></blockquote>
<dl>
<dt><code class="docutils literal notranslate"><span class="pre">german</span></code>, <code class="docutils literal notranslate"><span class="pre">stack</span></code> and <code class="docutils literal notranslate"><span class="pre">usgovernment</span></code>. Sourced from <code class="docutils literal notranslate"><span class="pre">ARM_ENVIRONMENT</span></code>, if unset.</dt><dd><dl class="field-list simple">
<dt class="field-odd">param endpoint</dt>
<dd class="field-odd"><p>The custom endpoint for Azure Resource Manager. Sourced from <code class="docutils literal notranslate"><span class="pre">ARM_ENDPOINT</span></code>, if unset.</p>
</dd>
<dt class="field-even">param use_msi</dt>
<dd class="field-even"><p>Whether to authenticate using Managed Service Identity (MSI). Sourced from <code class="docutils literal notranslate"><span class="pre">ARM_USE_MSI</span></code> if</p>
</dd>
</dl>
<p>unset. Defaults to false if no value is specified.
:param subscription_id: The Subscription ID in which the Storage Account exists. Used when authenticating using
the Managed Service Identity (MSI) or a service principal. Sourced from <code class="docutils literal notranslate"><span class="pre">ARM_SUBSCRIPTION_ID</span></code>, if unset.
:param tenant_id: The Tenant ID in which the Subscription exists. Used when authenticating using the
Managed Service Identity (MSI) or a service principal. Sourced from <code class="docutils literal notranslate"><span class="pre">ARM_TENANT_ID</span></code>, if unset.
:param msi_endpoint: The path to a custom Managed Service Identity endpoint. Used when authenticating using the
Managed Service Identity (MSI). Sourced from <code class="docutils literal notranslate"><span class="pre">ARM_MSI_ENDPOINT</span></code> in the environment, if unset. Automatically
determined, if no value is provided.
:param sas_token: The SAS Token used to access the Blob Storage Account. Used when authenticating using a SAS
Token. Sourced from <code class="docutils literal notranslate"><span class="pre">ARM_SAS_TOKEN</span></code> in the environment, if unset.
:param access_key: The Access Key used to access the blob storage account. Used when authenticating using an
access key. Sourced from <code class="docutils literal notranslate"><span class="pre">ARM_ACCESS_KEY</span></code> in the environment, if unset.
:param resource_group_name: The name of the resource group in which the storage account exists. Used when
authenticating using a service principal.
:param client_id: The client ID of the service principal. Used when authenticating using a service principal.
Sourced from <code class="docutils literal notranslate"><span class="pre">ARM_CLIENT_ID</span></code> in the environment, if unset.
:param client_secret: The client secret of the service principal. Used when authenticating using a service
principal. Sourced from <code class="docutils literal notranslate"><span class="pre">ARM_CLIENT_SECRET</span></code> in the environment, if unset.
:param workspace: The Terraform workspace from which to read state.</p>
</dd>
</dl>
</dd></dl>

<dl class="py class">
<dt id="pulumi_terraform.state.ConsulBackendArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">ConsulBackendArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">access_token</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheme</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_auth</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gzip</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_file</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cert_file</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_file</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.ConsulBackendArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration options for a Terraform Remote State stored in the Consul backend.</p>
<p>Constructs a ConsulBackendArgs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>path</strong> – Path in the Consul KV store.</p></li>
<li><p><strong>access_token</strong> – Consul Access Token. Sourced from <code class="docutils literal notranslate"><span class="pre">CONSUL_HTTP_TOKEN</span></code> in the environment, if unset.</p></li>
<li><p><strong>address</strong> – DNS name and port of the Consul HTTP endpoint specified in the format <code class="docutils literal notranslate"><span class="pre">dnsname:port</span></code>. Defaults</p></li>
</ul>
</dd>
</dl>
<p>to the local agent HTTP listener.
:param scheme: Specifies which protocol to use when talking to the given address - either <code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">https</span></code>. TLS
support can also be enabled by setting the environment variable <code class="docutils literal notranslate"><span class="pre">CONSUL_HTTP_SSL</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
:param datacenter: The datacenter to use. Defaults to that of the agent.
:param http_auth: HTTP Basic Authentication credentials to be used when communicating with Consul, in the format
of either <code class="docutils literal notranslate"><span class="pre">user</span></code> or <code class="docutils literal notranslate"><span class="pre">user:pass</span></code>. Sourced from <code class="docutils literal notranslate"><span class="pre">CONSUL_HTTP_AUTH</span></code>, if unset.
:param gzip: Whether to compress the state data using gzip. Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to compress the state data using gzip,
or <code class="docutils literal notranslate"><span class="pre">false</span></code> (default) to leave it uncompressed.
:param ca_file: A path to a PEM-encoded certificate authority used to verify the remote agent’s certificate.
Sourced from <code class="docutils literal notranslate"><span class="pre">CONSUL_CAFILE</span></code> in the environment, if unset.
:param cert_file: A path to a PEM-encoded certificate provided to the remote agent; requires use of key_file.
Sourced from <code class="docutils literal notranslate"><span class="pre">CONSUL_CLIENT_CERT</span></code> in the environment, if unset.
:param key_file: A path to a PEM-encoded private key, required if cert_file is specified. Sourced from
<code class="docutils literal notranslate"><span class="pre">CONSUL_CLIENT_KEY</span></code> in the environment, if unset.
:param workspace: The Terraform workspace from which to read state.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_terraform.state.EtcdV2BackendArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">EtcdV2BackendArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">endpoints</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.EtcdV2BackendArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration options for a Terraform Remote State stored in the etcd v2 backend. Note that there is a separate
configuration class for state stored in the ectd v3 backend.</p>
<p>Constructs an EtcdV2BackendArgs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>path</strong> – The path at which to store the state.</p></li>
<li><p><strong>endpoints</strong> – A space-separated list of the etcd endpoints.</p></li>
<li><p><strong>username</strong> – The username with which to authenticate to etcd.</p></li>
<li><p><strong>password</strong> – The username with which to authenticate to etcd.</p></li>
<li><p><strong>workspace</strong> – The Terraform workspace from which to read state.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py class">
<dt id="pulumi_terraform.state.EtcdV3BackendArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">EtcdV3BackendArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">endpoints</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cacert_path</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cert_path</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_path</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.EtcdV3BackendArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration options for a Terraform Remote State stored in the etcd v3 backend. Note that there is a separate
configuration class for state stored in the ectd v2 backend.</p>
<p>Constructs an EtcdV3BackendArgs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>endpoints</strong> – A list of the etcd endpoints.</p></li>
<li><p><strong>username</strong> – The username with which to authenticate to etcd. Sourced from <code class="docutils literal notranslate"><span class="pre">ETCDV3_USERNAME</span></code> in the</p></li>
</ul>
</dd>
</dl>
<p>environment, if unset.
:param password: The username with which to authenticate to etcd. Sourced from <code class="docutils literal notranslate"><span class="pre">ETCDV3_PASSWORD</span></code> in the
environment, if unset.
:param prefix: An optional prefix to be added to keys when storing state in etcd.
:param cacert_path: Path to a PEM-encoded certificate authority bundle with which to verify certificates of
TLS-enabled etcd servers.
:param cert_path: Path to a PEM-encoded certificate to provide to etcd for client authentication.
:param key_path: Path to a PEM-encoded key to use for client authentication.
:param workspace: The Terraform workspace from which to read state.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_terraform.state.GcsBackendArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">GcsBackendArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">bucket</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">credentials</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_key</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.GcsBackendArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration options for a Terraform Remote State stored in the Google Cloud Storage backend.</p>
<p>Constructs a GcsBackendArgs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>bucket</strong> – The name of the Google Cloud Storage bucket.</p></li>
<li><p><strong>credentials</strong> – Local path to Google Cloud Platform account credentials in JSON format. Sourced from</p></li>
</ul>
</dd>
</dl>
<p><code class="docutils literal notranslate"><span class="pre">GOOGLE_CREDENTIALS</span></code> in the environment if unset. If no value is provided Google Application Default Credentials
are used.
:param prefix: Prefix used inside the Google Cloud Storage bucket. Named states for workspaces are stored in an
object named <code class="docutils literal notranslate"><span class="pre">&lt;prefix&gt;/&lt;name&gt;.tfstate</span></code>.
:param encryption_key: A 32 byte, base64-encoded customer supplied encryption key used to encrypt the state.
Sourced from <code class="docutils literal notranslate"><span class="pre">GOOGLE_ENCRYPTION_KEY</span></code> in the environment, if unset.
:param workspace: The Terraform workspace from which to read state.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_terraform.state.HttpBackendArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">HttpBackendArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">update_method</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lock_address</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lock_method</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unlock_address</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unlock_method</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_cert_validation</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.HttpBackendArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration options for a Terraform Remote State stored in the HTTP backend.</p>
<p>Constructs an HttpBackendArgs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>address</strong> – The address of the HTTP endpoint.</p></li>
<li><p><strong>update_method</strong> – HTTP method to use when updating state. Defaults to <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><strong>lock_address</strong> – The address of the lock REST endpoint. Not setting a value disables locking.</p></li>
<li><p><strong>lock_method</strong> – The HTTP method to use when locking. Defaults to <code class="docutils literal notranslate"><span class="pre">LOCK</span></code>.</p></li>
<li><p><strong>unlock_address</strong> – The address of the unlock REST endpoint. Not setting a value disables locking.</p></li>
<li><p><strong>unlock_method</strong> – The HTTP method to use when unlocking. Defaults to <code class="docutils literal notranslate"><span class="pre">UNLOCK</span></code>.</p></li>
<li><p><strong>username</strong> – The username used for HTTP basic authentication.</p></li>
<li><p><strong>password</strong> – The password used for HTTP basic authentication.</p></li>
<li><p><strong>skip_cert_validation</strong> – Whether to skip TLS verification. Defaults to false.</p></li>
<li><p><strong>workspace</strong> – The Terraform workspace from which to read state.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py class">
<dt id="pulumi_terraform.state.LocalBackendArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">LocalBackendArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.LocalBackendArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration options for a Terraform Remote State stored in the local enhanced backend.</p>
<p>Constructs a LocalBackendArgs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>path</strong> – The path to the Terraform state file.</p>
</dd>
</dl>
</dd></dl>

<dl class="py class">
<dt id="pulumi_terraform.state.MantaBackendArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">MantaBackendArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">user</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_material</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insecure_skip_tls_verify</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.MantaBackendArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration options for a Terraform Remote State stored in the Manta backend.</p>
<p>Constructs a MantaBackendArgs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>account</strong> – The name of the Manta account. Sourced from <code class="docutils literal notranslate"><span class="pre">SDC_ACCOUNT</span></code> or <code class="docutils literal notranslate"><span class="pre">_ACCOUNT</span></code> in the environment, if</p>
</dd>
</dl>
<p>unset.
:param user: The username of the Manta account with which to authenticate.
:param url: The Manta API Endpoint. Sourced from <code class="docutils literal notranslate"><span class="pre">MANTA_URL</span></code> in the environment, if unset. Defaults to
<code class="docutils literal notranslate"><span class="pre">https://us-east.manta.joyent.com</span></code>.
:param key_material: The private key material corresponding with the SSH key whose fingerprint is specified in
keyId. Sourced from <code class="docutils literal notranslate"><span class="pre">SDC_KEY_MATERIAL</span></code> or <code class="docutils literal notranslate"><span class="pre">TRITON_KEY_MATERIAL</span></code> in the environment, if unset. If no value is
specified, the local SSH agent is used for signing requests.
:param key_id: The fingerprint of the public key matching the key material specified in keyMaterial, or in the
local SSH agent.
:param path: The path relative to your private storage directory (<code class="docutils literal notranslate"><span class="pre">/$MANTA_USER/stor</span></code>) where the state file
will be stored.
:param insecure_skip_tls_verify: Skip verifying the TLS certificate presented by the Manta endpoint. This can be</p>
<blockquote>
<div><p>useful for installations which do not have a certificate signed by a trusted root CA. Defaults to false.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>workspace</strong> – The Terraform workspace from which to read state.</p>
</dd>
</dl>
</dd></dl>

<dl class="py class">
<dt id="pulumi_terraform.state.PostgresBackendArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">PostgresBackendArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">conn_str</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">schema_name</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.PostgresBackendArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration options for a Terraform Remote State stored in the Postgres backend.</p>
<p>Constructs a PostgresBackendArgs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>conn_str</strong> – Postgres connection string; a <code class="docutils literal notranslate"><span class="pre">postgres://</span></code> URL.</p></li>
<li><p><strong>schema_name</strong> – Name of the automatically-managed Postgres schema. Defaults to <code class="docutils literal notranslate"><span class="pre">terraform_remote_state</span></code>.</p></li>
<li><p><strong>workspace</strong> – The Terraform workspace from which to read state.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py class">
<dt id="pulumi_terraform.state.RemoteBackendArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">RemoteBackendArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">organization</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace_name</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace_prefix</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.RemoteBackendArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration options for a workspace for use with the remote enhanced backend.</p>
<p>Constructs a RemoteBackendArgs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>organization</strong> – The name of the organization containing the targeted workspace(s).</p></li>
<li><p><strong>token</strong> – The token used to authenticate with the remote backend.</p></li>
<li><p><strong>hostname</strong> – The remote backend hostname to which to connect. Defaults to <code class="docutils literal notranslate"><span class="pre">app.terraform.io</span></code>.</p></li>
<li><p><strong>workspace_name</strong> – The full name of one remote workspace. When configured, only the default workspace can</p></li>
</ul>
</dd>
</dl>
<p>be used. This option conflicts with workspace_prefix.
:param workspace_prefix: A prefix used in the names of one or more remote workspaces, all of which can be used
with this configuration. If unset, only the default workspace can be used. This option conflicts with
workspace_name.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_terraform.state.RemoteStateReference">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">RemoteStateReference</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">backend_type</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">args</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>pulumi_terraform.state.remote_state_reference.ArtifactoryBackendArgs<span class="p">, </span>pulumi_terraform.state.remote_state_reference.AzureRMBackendArgs<span class="p">, </span>pulumi_terraform.state.remote_state_reference.ConsulBackendArgs<span class="p">, </span>pulumi_terraform.state.remote_state_reference.EtcdV2BackendArgs<span class="p">, </span>pulumi_terraform.state.remote_state_reference.EtcdV3BackendArgs<span class="p">, </span>pulumi_terraform.state.remote_state_reference.GcsBackendArgs<span class="p">, </span>pulumi_terraform.state.remote_state_reference.HttpBackendArgs<span class="p">, </span>pulumi_terraform.state.remote_state_reference.LocalBackendArgs<span class="p">, </span>pulumi_terraform.state.remote_state_reference.MantaBackendArgs<span class="p">, </span>pulumi_terraform.state.remote_state_reference.PostgresBackendArgs<span class="p">, </span>pulumi_terraform.state.remote_state_reference.RemoteBackendArgs<span class="p">, </span>pulumi_terraform.state.remote_state_reference.S3BackendArgs<span class="p">, </span>pulumi_terraform.state.remote_state_reference.SwiftBackendArgs<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">pulumi.resource.ResourceOptions</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.RemoteStateReference" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a reference to a Terraform Remote State. The root outputs of the remote state are available via the
<code class="docutils literal notranslate"><span class="pre">outputs</span></code> property or the <code class="docutils literal notranslate"><span class="pre">getOutput</span></code> method.</p>
<p>Create a RemoteStateReference resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_type</strong> (<em>str</em>) – The name of the Remote State Backend</p></li>
<li><p><strong>args</strong> (<em>BackendArgs</em>) – The arguments for the Remote State backend, which must match the given backend_type.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_terraform.state.RemoteStateReference.outputs">
<code class="sig-name descname">outputs</code><em class="property">: pulumi.Output[Mapping[str, Any]]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_terraform.state.RemoteStateReference.outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>The root outputs of the referenced Terraform state.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_terraform.state.RemoteStateReference.get_output">
<code class="sig-name descname">get_output</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.RemoteStateReference.get_output" title="Permalink to this definition">¶</a></dt>
<dd><p>Fetches the value of a root output from the Terraform Remote State.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> – The name of the output to fetch. The name is formatted exactly as per the “output” block in the</p>
</dd>
</dl>
<p>Terraform configuration.
:return: A pulumi.Output representing the value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_terraform.state.RemoteStateReference.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.RemoteStateReference.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_terraform.state.RemoteStateReference.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.RemoteStateReference.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_terraform.state.S3BackendArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">S3BackendArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">bucket</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_key</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profile</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_credentials_file</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_name</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace_key_prefix</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_endpoint</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sts_endpoint</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.S3BackendArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration options for a Terraform Remote State stored in the S3 backend.</p>
<p>Constructs an S3BackendArgs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>bucket</strong> – The name of the S3 bucket.</p></li>
<li><p><strong>key</strong> – The path to the state file inside the bucket. When using a non-default workspace, the state path</p></li>
</ul>
</dd>
</dl>
<p>will be <code class="docutils literal notranslate"><span class="pre">/workspace_key_prefix/workspace_name/key</span></code>.
:param region: The region of the S3 bucket. Also sourced from <code class="docutils literal notranslate"><span class="pre">AWS_DEFAULT_REGION</span></code> in the environment, if unset.
:param endpoint: A custom endpoint for the S3 API. Also sourced from <code class="docutils literal notranslate"><span class="pre">AWS_S3_ENDPOINT</span></code> in the environment, if
unset.
:param access_key: AWS Access Key. Sourced from the standard credentials pipeline, if unset.
:param secret_key: AWS Secret Access Key. Sourced from the standard credentials pipeline, if unset.
:param profile: The AWS profile name as set in the shared credentials file.
:param shared_credentials_file: The path to the shared credentials file. If this is not set and a profile is
specified, <code class="docutils literal notranslate"><span class="pre">~/.aws/credentials</span></code> will be used by default.
:param token: An MFA token. Sourced from <code class="docutils literal notranslate"><span class="pre">AWS_SESSION_TOKEN</span></code> in the environment if needed and unset.
:param role_arn: The ARN of an IAM Role to be assumed in order to read the state from S3.
:param external_id: The external ID to use when assuming the IAM role.
:param session_name: The session name to use when assuming the IAM role.
:param workspace_key_prefix: The prefix applied to the state path inside the bucket. This is only relevant when
using a non-default workspace, and defaults to <code class="docutils literal notranslate"><span class="pre">env:</span></code>.
:param iam_endpoint: A custom endpoint for the IAM API. Sourced from <code class="docutils literal notranslate"><span class="pre">AWS_IAM_ENDPOINT</span></code>, if unset.
:param sts_endpoint: A custom endpoint for the STS API. Sourced from <code class="docutils literal notranslate"><span class="pre">AWS_STS_ENDPOINT</span></code>, if unset.
:param workspace: The Terraform workspace from which to read state.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_terraform.state.SwiftBackendArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_terraform.state.</code><code class="sig-name descname">SwiftBackendArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">auth_url</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">container</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region_name</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_name</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insecure</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cacert_file</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cert</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_terraform.state.SwiftBackendArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration options for a Terraform Remote State stored in the Swift backend.</p>
<p>Constructs a SwiftBackendArgs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>auth_url</strong> – The Identity authentication URL. Sourced from <code class="docutils literal notranslate"><span class="pre">OS_AUTH_URL</span></code> in the environment, if unset.</p></li>
<li><p><strong>container</strong> – The name of the container in which the Terraform state file is stored.</p></li>
<li><p><strong>username</strong> – The username with which to log in. Sourced from <code class="docutils literal notranslate"><span class="pre">OS_USERNAME</span></code> in the environment, if unset.</p></li>
<li><p><strong>user_id</strong> – The user ID with which to log in. Sourced from <code class="docutils literal notranslate"><span class="pre">OS_USER_ID</span></code> in the environment, if unset.</p></li>
<li><p><strong>password</strong> – The password with which to log in. Sourced from <code class="docutils literal notranslate"><span class="pre">OS_PASSWORD</span></code> in the environment, if unset.</p></li>
<li><p><strong>token</strong> – Access token with which to log in in stead of a username and password. Sourced from</p></li>
</ul>
</dd>
</dl>
<p><code class="docutils literal notranslate"><span class="pre">OS_AUTH_TOKEN</span></code> in the environment, if unset.
:param region_name: The region in which the state file is stored. Sourced from <code class="docutils literal notranslate"><span class="pre">OS_REGION_NAME</span></code>, if unset.
:param tenant_id: The ID of the tenant (for identity v2) or project (identity v3) which which to log in. Sourced
from <code class="docutils literal notranslate"><span class="pre">OS_TENANT_ID</span></code> or <code class="docutils literal notranslate"><span class="pre">OS_PROJECT_ID</span></code> in the environment, if unset.
:param tenant_name: The name of the tenant (for identity v2) or project (identity v3) which which to log in.
Sourced from <code class="docutils literal notranslate"><span class="pre">OS_TENANT_NAME</span></code> or <code class="docutils literal notranslate"><span class="pre">OS_PROJECT_NAME</span></code> in the environment, if unset.
:param domain_id: The ID of the domain to scope the log in to (identity v3). Sourced from <code class="docutils literal notranslate"><span class="pre">OS_USER_DOMAIN_ID</span></code>,
<code class="docutils literal notranslate"><span class="pre">OS_PROJECT_DOMAIN_ID</span></code> or <code class="docutils literal notranslate"><span class="pre">OS_DOMAIN_ID</span></code> in the environment, if unset.
:param domain_name:  The name of the domain to scope the log in to (identity v3). Sourced from
<code class="docutils literal notranslate"><span class="pre">OS_USER_DOMAIN_NAME</span></code>, <code class="docutils literal notranslate"><span class="pre">OS_PROJECT_DOMAIN_NAME</span></code> or <code class="docutils literal notranslate"><span class="pre">OS_DOMAIN_NAME</span></code> in the environment, if unset.
:param insecure: Whether to disable verification of the server TLS certificate. Sourced from <code class="docutils literal notranslate"><span class="pre">OS_INSECURE</span></code> in
the environment, if unset.
:param cacert_file: A path to a CA root certificate for verifying the server TLS certificate. Sourced from
<code class="docutils literal notranslate"><span class="pre">OS_CACERT</span></code> in the environment, if unset.
:param cert: A path to a client certificate for TLS client authentication. Sourced from <code class="docutils literal notranslate"><span class="pre">OS_CERT</span></code> in the
environment, if unset.
:param key: A path to the private key corresponding to the client certificate for TLS client authentication.
Sourced from <code class="docutils literal notranslate"><span class="pre">OS_KEY</span></code> in the environment, if unset.</p>
</dd></dl>

</div>
