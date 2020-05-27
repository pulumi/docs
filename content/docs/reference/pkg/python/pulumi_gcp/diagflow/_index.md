---
title: Module diagflow
title_tag: Module diagflow | Package pulumi_gcp | Python SDK
linktitle: diagflow
notitle: true
---

<div class="section" id="diagflow">
<h1>diagflow<a class="headerlink" href="#diagflow" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.diagflow"></span><dl class="py class">
<dt id="pulumi_gcp.diagflow.Agent">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.diagflow.</code><code class="sig-name descname">Agent</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">avatar_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">classification_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_language_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_logging</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">supported_language_codes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.Agent" title="Permalink to this definition">¶</a></dt>
<dd><p>A Dialogflow agent is a virtual agent that handles conversations with your end-users. It is a natural language
understanding module that understands the nuances of human language. Dialogflow translates end-user text or audio
during a conversation to structured data that your apps and services can understand. You design and build a Dialogflow
agent to handle the types of conversations required for your system.</p>
<p>To get more information about Agent, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/dialogflow/docs/reference/rest/v2/projects/agent">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/dialogflow/docs/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">full_agent</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">diagflow</span><span class="o">.</span><span class="n">Agent</span><span class="p">(</span><span class="s2">&quot;fullAgent&quot;</span><span class="p">,</span>
    <span class="n">api_version</span><span class="o">=</span><span class="s2">&quot;API_VERSION_V2_BETA_1&quot;</span><span class="p">,</span>
    <span class="n">avatar_uri</span><span class="o">=</span><span class="s2">&quot;https://cloud.google.com/_static/images/cloud/icons/favicons/onecloud/super_cloud.png&quot;</span><span class="p">,</span>
    <span class="n">classification_threshold</span><span class="o">=</span><span class="mf">0.3</span><span class="p">,</span>
    <span class="n">default_language_code</span><span class="o">=</span><span class="s2">&quot;en&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Example description.&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;dialogflow-agent&quot;</span><span class="p">,</span>
    <span class="n">enable_logging</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">match_mode</span><span class="o">=</span><span class="s2">&quot;MATCH_MODE_ML_ONLY&quot;</span><span class="p">,</span>
    <span class="n">supported_language_codes</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;fr&quot;</span><span class="p">,</span>
        <span class="s2">&quot;de&quot;</span><span class="p">,</span>
        <span class="s2">&quot;es&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">tier</span><span class="o">=</span><span class="s2">&quot;TIER_STANDARD&quot;</span><span class="p">,</span>
    <span class="n">time_zone</span><span class="o">=</span><span class="s2">&quot;America/New_York&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – API version displayed in Dialogflow console. If not specified, V2 API is assumed. Clients are free to query
different service endpoints for different API versions. However, bots connectors and webhook calls will follow
the specified API version.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">API_VERSION_V1</span><span class="p">:</span> <span class="n">Legacy</span> <span class="n">V1</span> <span class="n">API</span><span class="o">.</span>
<span class="o">*</span> <span class="n">API_VERSION_V2</span><span class="p">:</span> <span class="n">V2</span> <span class="n">API</span><span class="o">.</span>
<span class="o">*</span> <span class="n">API_VERSION_V2_BETA_1</span><span class="p">:</span> <span class="n">V2beta1</span> <span class="n">API</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>avatar_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the agent’s avatar, which are used throughout the Dialogflow console. When an image URL is entered
into this field, the Dialogflow will save the image in the backend. The address of the backend image returned
from the API will be shown in the [avatarUriBackend] field.</p></li>
<li><p><strong>classification_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – To filter out false positive results and still get variety in matched natural language inputs for your agent,
you can tune the machine learning classification threshold. If the returned score value is less than the threshold
value, then a fallback intent will be triggered or, if there are no fallback intents defined, no intent will be
triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the
default of 0.3 is used.</p></li>
<li><p><strong>default_language_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default language of the agent as a language tag. <a class="reference external" href="https://cloud.google.com/dialogflow/docs/reference/language">See Language Support</a>
for a list of the currently supported language codes. This field cannot be updated after creation.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this agent. The maximum length is 500 characters. If exceeded, the request is rejected.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this agent.</p></li>
<li><p><strong>enable_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether this agent should log conversation queries.</p></li>
<li><p><strong>match_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines how intents are detected from user queries.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">MATCH_MODE_HYBRID</span><span class="p">:</span> <span class="n">Best</span> <span class="k">for</span> <span class="n">agents</span> <span class="k">with</span> <span class="n">a</span> <span class="n">small</span> <span class="n">number</span> <span class="n">of</span> <span class="n">examples</span> <span class="ow">in</span> <span class="n">intents</span> <span class="ow">and</span><span class="o">/</span><span class="ow">or</span> <span class="n">wide</span> <span class="n">use</span> <span class="n">of</span> <span class="n">templates</span>
<span class="n">syntax</span> <span class="ow">and</span> <span class="n">composite</span> <span class="n">entities</span><span class="o">.</span>
<span class="o">*</span> <span class="n">MATCH_MODE_ML_ONLY</span><span class="p">:</span> <span class="n">Can</span> <span class="n">be</span> <span class="n">used</span> <span class="k">for</span> <span class="n">agents</span> <span class="k">with</span> <span class="n">a</span> <span class="n">large</span> <span class="n">number</span> <span class="n">of</span> <span class="n">examples</span> <span class="ow">in</span> <span class="n">intents</span><span class="p">,</span> <span class="n">especially</span> <span class="n">the</span> <span class="n">ones</span>
<span class="n">using</span> <span class="nd">@sys</span><span class="o">.</span><span class="n">any</span> <span class="ow">or</span> <span class="n">very</span> <span class="n">large</span> <span class="n">developer</span> <span class="n">entities</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>supported_language_codes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of all languages supported by this agent (except for the defaultLanguageCode).</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The agent tier. If not specified, TIER_STANDARD is assumed.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">TIER_STANDARD</span><span class="p">:</span> <span class="n">Standard</span> <span class="n">tier</span><span class="o">.</span>
<span class="o">*</span> <span class="n">TIER_ENTERPRISE</span><span class="p">:</span> <span class="n">Enterprise</span> <span class="n">tier</span> <span class="p">(</span><span class="n">Essentials</span><span class="p">)</span><span class="o">.</span>
<span class="o">*</span> <span class="n">TIER_ENTERPRISE_PLUS</span><span class="p">:</span> <span class="n">Enterprise</span> <span class="n">tier</span> <span class="p">(</span><span class="n">Plus</span><span class="p">)</span><span class="o">.</span>
<span class="n">NOTE</span><span class="p">:</span> <span class="n">Due</span> <span class="n">to</span> <span class="n">consistency</span> <span class="n">issues</span><span class="p">,</span> <span class="n">the</span> <span class="n">provider</span> <span class="n">will</span> <span class="ow">not</span> <span class="n">read</span> <span class="n">this</span> <span class="n">field</span> <span class="kn">from</span> <span class="nn">the</span> <span class="n">API</span><span class="o">.</span> <span class="n">Drift</span> <span class="ow">is</span> <span class="n">possible</span> <span class="n">between</span>
<span class="n">the</span> <span class="n">the</span> <span class="n">provider</span> <span class="n">state</span> <span class="ow">and</span> <span class="n">Dialogflow</span> <span class="k">if</span> <span class="n">the</span> <span class="n">agent</span> <span class="n">tier</span> <span class="ow">is</span> <span class="n">changed</span> <span class="n">outside</span> <span class="n">of</span> <span class="n">the</span> <span class="n">provider</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time zone of this agent from the <a class="reference external" href="https://www.iana.org/time-zones">time zone database</a>, e.g., America/New_York,
Europe/Paris.</p>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Agent.api_version">
<code class="sig-name descname">api_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.api_version" title="Permalink to this definition">¶</a></dt>
<dd><p>API version displayed in Dialogflow console. If not specified, V2 API is assumed. Clients are free to query
different service endpoints for different API versions. However, bots connectors and webhook calls will follow
the specified API version.</p>
<ul class="simple">
<li><p>API_VERSION_V1: Legacy V1 API.</p></li>
<li><p>API_VERSION_V2: V2 API.</p></li>
<li><p>API_VERSION_V2_BETA_1: V2beta1 API.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Agent.avatar_uri">
<code class="sig-name descname">avatar_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.avatar_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the agent’s avatar, which are used throughout the Dialogflow console. When an image URL is entered
into this field, the Dialogflow will save the image in the backend. The address of the backend image returned
from the API will be shown in the [avatarUriBackend] field.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Agent.avatar_uri_backend">
<code class="sig-name descname">avatar_uri_backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.avatar_uri_backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the agent’s avatar as returned from the API. Output only. To provide an image URL for the agent avatar, the
[avatarUri] field can be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Agent.classification_threshold">
<code class="sig-name descname">classification_threshold</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.classification_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>To filter out false positive results and still get variety in matched natural language inputs for your agent,
you can tune the machine learning classification threshold. If the returned score value is less than the threshold
value, then a fallback intent will be triggered or, if there are no fallback intents defined, no intent will be
triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the
default of 0.3 is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Agent.default_language_code">
<code class="sig-name descname">default_language_code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.default_language_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The default language of the agent as a language tag. <a class="reference external" href="https://cloud.google.com/dialogflow/docs/reference/language">See Language Support</a>
for a list of the currently supported language codes. This field cannot be updated after creation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Agent.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this agent. The maximum length is 500 characters. If exceeded, the request is rejected.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Agent.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this agent.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Agent.enable_logging">
<code class="sig-name descname">enable_logging</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.enable_logging" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether this agent should log conversation queries.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Agent.match_mode">
<code class="sig-name descname">match_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.match_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines how intents are detected from user queries.</p>
<ul class="simple">
<li><p>MATCH_MODE_HYBRID: Best for agents with a small number of examples in intents and/or wide use of templates
syntax and composite entities.</p></li>
<li><p>MATCH_MODE_ML_ONLY: Can be used for agents with a large number of examples in intents, especially the ones
using &#64;sys.any or very large developer entities.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Agent.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Agent.supported_language_codes">
<code class="sig-name descname">supported_language_codes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.supported_language_codes" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of all languages supported by this agent (except for the defaultLanguageCode).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Agent.tier">
<code class="sig-name descname">tier</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The agent tier. If not specified, TIER_STANDARD is assumed.</p>
<ul class="simple">
<li><p>TIER_STANDARD: Standard tier.</p></li>
<li><p>TIER_ENTERPRISE: Enterprise tier (Essentials).</p></li>
<li><p>TIER_ENTERPRISE_PLUS: Enterprise tier (Plus).
NOTE: Due to consistency issues, the provider will not read this field from the API. Drift is possible between
the the provider state and Dialogflow if the agent tier is changed outside of the provider.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Agent.time_zone">
<code class="sig-name descname">time_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.time_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The time zone of this agent from the <a class="reference external" href="https://www.iana.org/time-zones">time zone database</a>, e.g., America/New_York,
Europe/Paris.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.diagflow.Agent.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">avatar_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">avatar_uri_backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">classification_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_language_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_logging</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">supported_language_codes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Agent resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – API version displayed in Dialogflow console. If not specified, V2 API is assumed. Clients are free to query
different service endpoints for different API versions. However, bots connectors and webhook calls will follow
the specified API version.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">API_VERSION_V1</span><span class="p">:</span> <span class="n">Legacy</span> <span class="n">V1</span> <span class="n">API</span><span class="o">.</span>
<span class="o">*</span> <span class="n">API_VERSION_V2</span><span class="p">:</span> <span class="n">V2</span> <span class="n">API</span><span class="o">.</span>
<span class="o">*</span> <span class="n">API_VERSION_V2_BETA_1</span><span class="p">:</span> <span class="n">V2beta1</span> <span class="n">API</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>avatar_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the agent’s avatar, which are used throughout the Dialogflow console. When an image URL is entered
into this field, the Dialogflow will save the image in the backend. The address of the backend image returned
from the API will be shown in the [avatarUriBackend] field.</p></li>
<li><p><strong>avatar_uri_backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the agent’s avatar as returned from the API. Output only. To provide an image URL for the agent avatar, the
[avatarUri] field can be used.</p></li>
<li><p><strong>classification_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – To filter out false positive results and still get variety in matched natural language inputs for your agent,
you can tune the machine learning classification threshold. If the returned score value is less than the threshold
value, then a fallback intent will be triggered or, if there are no fallback intents defined, no intent will be
triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the
default of 0.3 is used.</p></li>
<li><p><strong>default_language_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The default language of the agent as a language tag. <a class="reference external" href="https://cloud.google.com/dialogflow/docs/reference/language">See Language Support</a>
for a list of the currently supported language codes. This field cannot be updated after creation.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this agent. The maximum length is 500 characters. If exceeded, the request is rejected.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this agent.</p></li>
<li><p><strong>enable_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether this agent should log conversation queries.</p></li>
<li><p><strong>match_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines how intents are detected from user queries.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">MATCH_MODE_HYBRID</span><span class="p">:</span> <span class="n">Best</span> <span class="k">for</span> <span class="n">agents</span> <span class="k">with</span> <span class="n">a</span> <span class="n">small</span> <span class="n">number</span> <span class="n">of</span> <span class="n">examples</span> <span class="ow">in</span> <span class="n">intents</span> <span class="ow">and</span><span class="o">/</span><span class="ow">or</span> <span class="n">wide</span> <span class="n">use</span> <span class="n">of</span> <span class="n">templates</span>
<span class="n">syntax</span> <span class="ow">and</span> <span class="n">composite</span> <span class="n">entities</span><span class="o">.</span>
<span class="o">*</span> <span class="n">MATCH_MODE_ML_ONLY</span><span class="p">:</span> <span class="n">Can</span> <span class="n">be</span> <span class="n">used</span> <span class="k">for</span> <span class="n">agents</span> <span class="k">with</span> <span class="n">a</span> <span class="n">large</span> <span class="n">number</span> <span class="n">of</span> <span class="n">examples</span> <span class="ow">in</span> <span class="n">intents</span><span class="p">,</span> <span class="n">especially</span> <span class="n">the</span> <span class="n">ones</span>
<span class="n">using</span> <span class="nd">@sys</span><span class="o">.</span><span class="n">any</span> <span class="ow">or</span> <span class="n">very</span> <span class="n">large</span> <span class="n">developer</span> <span class="n">entities</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>supported_language_codes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of all languages supported by this agent (except for the defaultLanguageCode).</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The agent tier. If not specified, TIER_STANDARD is assumed.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">TIER_STANDARD</span><span class="p">:</span> <span class="n">Standard</span> <span class="n">tier</span><span class="o">.</span>
<span class="o">*</span> <span class="n">TIER_ENTERPRISE</span><span class="p">:</span> <span class="n">Enterprise</span> <span class="n">tier</span> <span class="p">(</span><span class="n">Essentials</span><span class="p">)</span><span class="o">.</span>
<span class="o">*</span> <span class="n">TIER_ENTERPRISE_PLUS</span><span class="p">:</span> <span class="n">Enterprise</span> <span class="n">tier</span> <span class="p">(</span><span class="n">Plus</span><span class="p">)</span><span class="o">.</span>
<span class="n">NOTE</span><span class="p">:</span> <span class="n">Due</span> <span class="n">to</span> <span class="n">consistency</span> <span class="n">issues</span><span class="p">,</span> <span class="n">the</span> <span class="n">provider</span> <span class="n">will</span> <span class="ow">not</span> <span class="n">read</span> <span class="n">this</span> <span class="n">field</span> <span class="kn">from</span> <span class="nn">the</span> <span class="n">API</span><span class="o">.</span> <span class="n">Drift</span> <span class="ow">is</span> <span class="n">possible</span> <span class="n">between</span>
<span class="n">the</span> <span class="n">the</span> <span class="n">provider</span> <span class="n">state</span> <span class="ow">and</span> <span class="n">Dialogflow</span> <span class="k">if</span> <span class="n">the</span> <span class="n">agent</span> <span class="n">tier</span> <span class="ow">is</span> <span class="n">changed</span> <span class="n">outside</span> <span class="n">of</span> <span class="n">the</span> <span class="n">provider</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The time zone of this agent from the <a class="reference external" href="https://www.iana.org/time-zones">time zone database</a>, e.g., America/New_York,
Europe/Paris.</p>
</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.diagflow.Agent.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.diagflow.Agent.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.diagflow.EntityType">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.diagflow.</code><code class="sig-name descname">EntityType</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_fuzzy_extraction</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.EntityType" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents an entity type. Entity types serve as a tool for extracting parameter values from natural language queries.</p>
<p>To get more information about EntityType, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/dialogflow/docs/reference/rest/v2/projects.agent.entityTypes">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/dialogflow/docs/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">basic_agent</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">diagflow</span><span class="o">.</span><span class="n">Agent</span><span class="p">(</span><span class="s2">&quot;basicAgent&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;example_agent&quot;</span><span class="p">,</span>
    <span class="n">default_language_code</span><span class="o">=</span><span class="s2">&quot;en&quot;</span><span class="p">,</span>
    <span class="n">time_zone</span><span class="o">=</span><span class="s2">&quot;America/New_York&quot;</span><span class="p">)</span>
<span class="n">basic_entity_type</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">diagflow</span><span class="o">.</span><span class="n">EntityType</span><span class="p">(</span><span class="s2">&quot;basicEntityType&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
    <span class="n">kind</span><span class="o">=</span><span class="s2">&quot;KIND_MAP&quot;</span><span class="p">,</span>
    <span class="n">entities</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;value1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;synonyms&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="s2">&quot;synonym1&quot;</span><span class="p">,</span>
                <span class="s2">&quot;synonym2&quot;</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;value2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;synonyms&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="s2">&quot;synonym3&quot;</span><span class="p">,</span>
                <span class="s2">&quot;synonym4&quot;</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">},</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this entity type to be displayed on the console.</p></li>
<li><p><strong>enable_fuzzy_extraction</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables fuzzy entity extraction during classification.</p></li>
<li><p><strong>entities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of entity entries associated with the entity type.  Structure is documented below.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates the kind of entity type.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">KIND_MAP</span><span class="p">:</span> <span class="n">Map</span> <span class="n">entity</span> <span class="n">types</span> <span class="n">allow</span> <span class="n">mapping</span> <span class="n">of</span> <span class="n">a</span> <span class="n">group</span> <span class="n">of</span> <span class="n">synonyms</span> <span class="n">to</span> <span class="n">a</span> <span class="n">reference</span> <span class="n">value</span><span class="o">.</span>
<span class="o">*</span> <span class="n">KIND_LIST</span><span class="p">:</span> <span class="n">List</span> <span class="n">entity</span> <span class="n">types</span> <span class="n">contain</span> <span class="n">a</span> <span class="nb">set</span> <span class="n">of</span> <span class="n">entries</span> <span class="n">that</span> <span class="n">do</span> <span class="ow">not</span> <span class="nb">map</span> <span class="n">to</span> <span class="n">reference</span> <span class="n">values</span><span class="o">.</span> <span class="n">However</span><span class="p">,</span> <span class="nb">list</span> <span class="n">entity</span>
<span class="n">types</span> <span class="n">can</span> <span class="n">contain</span> <span class="n">references</span> <span class="n">to</span> <span class="n">other</span> <span class="n">entity</span> <span class="n">types</span> <span class="p">(</span><span class="k">with</span> <span class="ow">or</span> <span class="n">without</span> <span class="n">aliases</span><span class="p">)</span><span class="o">.</span>
<span class="o">*</span> <span class="n">KIND_REGEXP</span><span class="p">:</span> <span class="n">Regexp</span> <span class="n">entity</span> <span class="n">types</span> <span class="n">allow</span> <span class="n">to</span> <span class="n">specify</span> <span class="n">regular</span> <span class="n">expressions</span> <span class="ow">in</span> <span class="n">entries</span> <span class="n">values</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd>
</dl>
<p>The <strong>entities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">synonyms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A collection of value synonyms. For example, if the entity type is vegetable, and value is scallions, a synonym
could be green onions.
For KIND_LIST entity types:</p>
<ul>
<li><p>This collection must contain exactly one synonym equal to value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The primary value associated with this entity entry. For example, if the entity type is vegetable, the value
could be scallions.
For KIND_MAP entity types:</p>
<ul>
<li><p>A reference value to be used in place of synonyms.
For KIND_LIST entity types:</p></li>
<li><p>A string that can contain references to other entity types (with or without aliases).</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.EntityType.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.EntityType.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this entity type to be displayed on the console.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.EntityType.enable_fuzzy_extraction">
<code class="sig-name descname">enable_fuzzy_extraction</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.EntityType.enable_fuzzy_extraction" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables fuzzy entity extraction during classification.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.EntityType.entities">
<code class="sig-name descname">entities</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.EntityType.entities" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of entity entries associated with the entity type.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">synonyms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A collection of value synonyms. For example, if the entity type is vegetable, and value is scallions, a synonym
could be green onions.
For KIND_LIST entity types:</p>
<ul>
<li><p>This collection must contain exactly one synonym equal to value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The primary value associated with this entity entry. For example, if the entity type is vegetable, the value
could be scallions.
For KIND_MAP entity types:</p>
<ul>
<li><p>A reference value to be used in place of synonyms.
For KIND_LIST entity types:</p></li>
<li><p>A string that can contain references to other entity types (with or without aliases).</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.EntityType.kind">
<code class="sig-name descname">kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.EntityType.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the kind of entity type.</p>
<ul class="simple">
<li><p>KIND_MAP: Map entity types allow mapping of a group of synonyms to a reference value.</p></li>
<li><p>KIND_LIST: List entity types contain a set of entries that do not map to reference values. However, list entity
types can contain references to other entity types (with or without aliases).</p></li>
<li><p>KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.EntityType.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.EntityType.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the entity type. Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/entityTypes/<span class="raw-html-m2r"><Entity type ID></span>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.EntityType.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.EntityType.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.diagflow.EntityType.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_fuzzy_extraction</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.EntityType.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EntityType resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this entity type to be displayed on the console.</p></li>
<li><p><strong>enable_fuzzy_extraction</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables fuzzy entity extraction during classification.</p></li>
<li><p><strong>entities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of entity entries associated with the entity type.  Structure is documented below.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates the kind of entity type.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">KIND_MAP</span><span class="p">:</span> <span class="n">Map</span> <span class="n">entity</span> <span class="n">types</span> <span class="n">allow</span> <span class="n">mapping</span> <span class="n">of</span> <span class="n">a</span> <span class="n">group</span> <span class="n">of</span> <span class="n">synonyms</span> <span class="n">to</span> <span class="n">a</span> <span class="n">reference</span> <span class="n">value</span><span class="o">.</span>
<span class="o">*</span> <span class="n">KIND_LIST</span><span class="p">:</span> <span class="n">List</span> <span class="n">entity</span> <span class="n">types</span> <span class="n">contain</span> <span class="n">a</span> <span class="nb">set</span> <span class="n">of</span> <span class="n">entries</span> <span class="n">that</span> <span class="n">do</span> <span class="ow">not</span> <span class="nb">map</span> <span class="n">to</span> <span class="n">reference</span> <span class="n">values</span><span class="o">.</span> <span class="n">However</span><span class="p">,</span> <span class="nb">list</span> <span class="n">entity</span>
<span class="n">types</span> <span class="n">can</span> <span class="n">contain</span> <span class="n">references</span> <span class="n">to</span> <span class="n">other</span> <span class="n">entity</span> <span class="n">types</span> <span class="p">(</span><span class="k">with</span> <span class="ow">or</span> <span class="n">without</span> <span class="n">aliases</span><span class="p">)</span><span class="o">.</span>
<span class="o">*</span> <span class="n">KIND_REGEXP</span><span class="p">:</span> <span class="n">Regexp</span> <span class="n">entity</span> <span class="n">types</span> <span class="n">allow</span> <span class="n">to</span> <span class="n">specify</span> <span class="n">regular</span> <span class="n">expressions</span> <span class="ow">in</span> <span class="n">entries</span> <span class="n">values</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the entity type. Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/entityTypes/<span class="raw-html-m2r"><Entity type ID></span>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>entities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">synonyms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A collection of value synonyms. For example, if the entity type is vegetable, and value is scallions, a synonym
could be green onions.
For KIND_LIST entity types:</p>
<ul>
<li><p>This collection must contain exactly one synonym equal to value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The primary value associated with this entity entry. For example, if the entity type is vegetable, the value
could be scallions.
For KIND_MAP entity types:</p>
<ul>
<li><p>A reference value to be used in place of synonyms.
For KIND_LIST entity types:</p></li>
<li><p>A string that can contain references to other entity types (with or without aliases).</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.diagflow.EntityType.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.EntityType.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.diagflow.EntityType.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.EntityType.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.diagflow.Intent">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.diagflow.</code><code class="sig-name descname">Intent</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_response_platforms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input_context_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_fallback</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ml_disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_followup_intent_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_contexts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhook_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.Intent" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a Dialogflow intent. Intents convert a number of user expressions or patterns into an action. An action
is an extraction of a user command or sentence semantics.</p>
<p>To get more information about Intent, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/dialogflow/docs/reference/rest/v2/projects.agent.intents">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/dialogflow/docs/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">basic_agent</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">diagflow</span><span class="o">.</span><span class="n">Agent</span><span class="p">(</span><span class="s2">&quot;basicAgent&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;example_agent&quot;</span><span class="p">,</span>
    <span class="n">default_language_code</span><span class="o">=</span><span class="s2">&quot;en&quot;</span><span class="p">,</span>
    <span class="n">time_zone</span><span class="o">=</span><span class="s2">&quot;America/New_York&quot;</span><span class="p">)</span>
<span class="n">basic_intent</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">diagflow</span><span class="o">.</span><span class="n">Intent</span><span class="p">(</span><span class="s2">&quot;basicIntent&quot;</span><span class="p">,</span> <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;basic-intent&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the action associated with the intent.
Note: The action name must not contain whitespaces.</p></li>
<li><p><strong>default_response_platforms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of platforms for which the first responses will be copied from the messages in PLATFORM_UNSPECIFIED
(i.e. default platform).</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this intent to be displayed on the console.</p></li>
<li><p><strong>events</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of event names that trigger the intent. If the collection of input contexts is not empty, all of
the contexts must be present in the active user session for an event to trigger this intent. See the
<a class="reference external" href="https://cloud.google.com/dialogflow/docs/events-overview">events reference</a> for more details.</p></li>
<li><p><strong>input_context_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of context names required for this intent to be triggered.
Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/sessions/-/contexts/<span class="raw-html-m2r"><Context ID></span>.</p></li>
<li><p><strong>is_fallback</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether this is a fallback intent.</p></li>
<li><p><strong>ml_disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether Machine Learning is disabled for the intent.
Note: If mlDisabled setting is set to true, then this intent is not taken into account during inference in ML
ONLY match mode. Also, auto-markup in the UI is turned off.</p></li>
<li><p><strong>parent_followup_intent_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the parent intent in the chain of followup intents.
Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/intents/<span class="raw-html-m2r"><Intent ID></span>.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of this intent. Higher numbers represent higher priorities.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">If</span> <span class="n">the</span> <span class="n">supplied</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">unspecified</span> <span class="ow">or</span> <span class="mi">0</span><span class="p">,</span> <span class="n">the</span> <span class="n">service</span> <span class="n">translates</span> <span class="n">the</span> <span class="n">value</span> <span class="n">to</span> <span class="mi">500</span><span class="p">,</span><span class="mi">000</span><span class="p">,</span> <span class="n">which</span> <span class="n">corresponds</span>
<span class="n">to</span> <span class="n">the</span> <span class="n">Normal</span> <span class="n">priority</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">console</span><span class="o">.</span>
<span class="o">-</span> <span class="n">If</span> <span class="n">the</span> <span class="n">supplied</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">negative</span><span class="p">,</span> <span class="n">the</span> <span class="n">intent</span> <span class="ow">is</span> <span class="n">ignored</span> <span class="ow">in</span> <span class="n">runtime</span> <span class="n">detect</span> <span class="n">intent</span> <span class="n">requests</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>reset_contexts</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to delete all contexts in the current session when this intent is matched.</p></li>
<li><p><strong>webhook_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether webhooks are enabled for the intent.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">WEBHOOK_STATE_ENABLED</span><span class="p">:</span> <span class="n">Webhook</span> <span class="ow">is</span> <span class="n">enabled</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">agent</span> <span class="ow">and</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">intent</span><span class="o">.</span>
<span class="o">*</span> <span class="n">WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING</span><span class="p">:</span> <span class="n">Webhook</span> <span class="ow">is</span> <span class="n">enabled</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">agent</span> <span class="ow">and</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">intent</span><span class="o">.</span> <span class="n">Also</span><span class="p">,</span> <span class="n">each</span> <span class="n">slot</span>
<span class="n">filling</span> <span class="n">prompt</span> <span class="ow">is</span> <span class="n">forwarded</span> <span class="n">to</span> <span class="n">the</span> <span class="n">webhook</span><span class="o">.</span>
</pre></div>
</div>
<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.action">
<code class="sig-name descname">action</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the action associated with the intent.
Note: The action name must not contain whitespaces.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.default_response_platforms">
<code class="sig-name descname">default_response_platforms</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.default_response_platforms" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of platforms for which the first responses will be copied from the messages in PLATFORM_UNSPECIFIED
(i.e. default platform).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this intent to be displayed on the console.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.events">
<code class="sig-name descname">events</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.events" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of event names that trigger the intent. If the collection of input contexts is not empty, all of
the contexts must be present in the active user session for an event to trigger this intent. See the
<a class="reference external" href="https://cloud.google.com/dialogflow/docs/events-overview">events reference</a> for more details.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.followup_intent_infos">
<code class="sig-name descname">followup_intent_infos</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.followup_intent_infos" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about all followup intents that have this intent as a direct or indirect parent. We populate this field only
in the output.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">followupIntentName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parent_followup_intent_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier of the parent intent in the chain of followup intents.
Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/intents/<span class="raw-html-m2r"><Intent ID></span>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.input_context_names">
<code class="sig-name descname">input_context_names</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.input_context_names" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of context names required for this intent to be triggered.
Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/sessions/-/contexts/<span class="raw-html-m2r"><Context ID></span>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.is_fallback">
<code class="sig-name descname">is_fallback</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.is_fallback" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether this is a fallback intent.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.ml_disabled">
<code class="sig-name descname">ml_disabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.ml_disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Machine Learning is disabled for the intent.
Note: If mlDisabled setting is set to true, then this intent is not taken into account during inference in ML
ONLY match mode. Also, auto-markup in the UI is turned off.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of this intent. Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/intents/<span class="raw-html-m2r"><Intent ID></span>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.parent_followup_intent_name">
<code class="sig-name descname">parent_followup_intent_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.parent_followup_intent_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the parent intent in the chain of followup intents.
Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/intents/<span class="raw-html-m2r"><Intent ID></span>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of this intent. Higher numbers represent higher priorities.</p>
<ul class="simple">
<li><p>If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds
to the Normal priority in the console.</p></li>
<li><p>If the supplied value is negative, the intent is ignored in runtime detect intent requests.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.reset_contexts">
<code class="sig-name descname">reset_contexts</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.reset_contexts" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether to delete all contexts in the current session when this intent is matched.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.root_followup_intent_name">
<code class="sig-name descname">root_followup_intent_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.root_followup_intent_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the root intent in the chain of followup intents. It identifies the correct followup intents
chain for this intent. Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/intents/<span class="raw-html-m2r"><Intent ID></span>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.diagflow.Intent.webhook_state">
<code class="sig-name descname">webhook_state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.webhook_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether webhooks are enabled for the intent.</p>
<ul class="simple">
<li><p>WEBHOOK_STATE_ENABLED: Webhook is enabled in the agent and in the intent.</p></li>
<li><p>WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING: Webhook is enabled in the agent and in the intent. Also, each slot
filling prompt is forwarded to the webhook.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.diagflow.Intent.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_response_platforms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">followup_intent_infos</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input_context_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_fallback</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ml_disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_followup_intent_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_contexts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_followup_intent_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhook_state</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Intent resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the action associated with the intent.
Note: The action name must not contain whitespaces.</p></li>
<li><p><strong>default_response_platforms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of platforms for which the first responses will be copied from the messages in PLATFORM_UNSPECIFIED
(i.e. default platform).</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this intent to be displayed on the console.</p></li>
<li><p><strong>events</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>The collection of event names that trigger the intent. If the collection of input contexts is not empty, all of
the contexts must be present in the active user session for an event to trigger this intent. See the
<a class="reference external" href="https://cloud.google.com/dialogflow/docs/events-overview">events reference</a> for more details.</p>
</p></li>
<li><p><strong>followup_intent_infos</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Information about all followup intents that have this intent as a direct or indirect parent. We populate this field only
in the output.</p></li>
<li><p><strong>input_context_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of context names required for this intent to be triggered.
Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/sessions/-/contexts/<span class="raw-html-m2r"><Context ID></span>.</p></li>
<li><p><strong>is_fallback</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether this is a fallback intent.</p></li>
<li><p><strong>ml_disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether Machine Learning is disabled for the intent.
Note: If mlDisabled setting is set to true, then this intent is not taken into account during inference in ML
ONLY match mode. Also, auto-markup in the UI is turned off.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of this intent. Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/intents/<span class="raw-html-m2r"><Intent ID></span>.</p></li>
<li><p><strong>parent_followup_intent_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the parent intent in the chain of followup intents.
Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/intents/<span class="raw-html-m2r"><Intent ID></span>.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of this intent. Higher numbers represent higher priorities.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">If</span> <span class="n">the</span> <span class="n">supplied</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">unspecified</span> <span class="ow">or</span> <span class="mi">0</span><span class="p">,</span> <span class="n">the</span> <span class="n">service</span> <span class="n">translates</span> <span class="n">the</span> <span class="n">value</span> <span class="n">to</span> <span class="mi">500</span><span class="p">,</span><span class="mi">000</span><span class="p">,</span> <span class="n">which</span> <span class="n">corresponds</span>
<span class="n">to</span> <span class="n">the</span> <span class="n">Normal</span> <span class="n">priority</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">console</span><span class="o">.</span>
<span class="o">-</span> <span class="n">If</span> <span class="n">the</span> <span class="n">supplied</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">negative</span><span class="p">,</span> <span class="n">the</span> <span class="n">intent</span> <span class="ow">is</span> <span class="n">ignored</span> <span class="ow">in</span> <span class="n">runtime</span> <span class="n">detect</span> <span class="n">intent</span> <span class="n">requests</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>reset_contexts</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to delete all contexts in the current session when this intent is matched.</p></li>
<li><p><strong>root_followup_intent_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the root intent in the chain of followup intents. It identifies the correct followup intents
chain for this intent. Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/intents/<span class="raw-html-m2r"><Intent ID></span>.</p></li>
<li><p><strong>webhook_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether webhooks are enabled for the intent.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">WEBHOOK_STATE_ENABLED</span><span class="p">:</span> <span class="n">Webhook</span> <span class="ow">is</span> <span class="n">enabled</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">agent</span> <span class="ow">and</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">intent</span><span class="o">.</span>
<span class="o">*</span> <span class="n">WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING</span><span class="p">:</span> <span class="n">Webhook</span> <span class="ow">is</span> <span class="n">enabled</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">agent</span> <span class="ow">and</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">intent</span><span class="o">.</span> <span class="n">Also</span><span class="p">,</span> <span class="n">each</span> <span class="n">slot</span>
<span class="n">filling</span> <span class="n">prompt</span> <span class="ow">is</span> <span class="n">forwarded</span> <span class="n">to</span> <span class="n">the</span> <span class="n">webhook</span><span class="o">.</span>
</pre></div>
</div>
<p>The <strong>followup_intent_infos</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">followupIntentName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parent_followup_intent_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the parent intent in the chain of followup intents.
Format: projects/<span class="raw-html-m2r"><Project ID></span>/agent/intents/<span class="raw-html-m2r"><Intent ID></span>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.diagflow.Intent.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.diagflow.Intent.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.Intent.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
