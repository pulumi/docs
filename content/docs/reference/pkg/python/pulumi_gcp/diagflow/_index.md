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
<span class="target" id="module-pulumi_gcp.diagflow"></span><dl class="class">
<dt id="pulumi_gcp.diagflow.Agent">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.diagflow.</code><code class="sig-name descname">Agent</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_version=None</em>, <em class="sig-param">avatar_uri=None</em>, <em class="sig-param">classification_threshold=None</em>, <em class="sig-param">default_language_code=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enable_logging=None</em>, <em class="sig-param">match_mode=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">supported_language_codes=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">time_zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.Agent" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dialogflow_agent.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dialogflow_agent.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – API version displayed in Dialogflow console. If not specified, V2 API is assumed. Clients are free to query different
service endpoints for different API versions. However, bots connectors and webhook calls will follow the specified API
version. * API_VERSION_V1: Legacy V1 API. * API_VERSION_V2: V2 API. * API_VERSION_V2_BETA_1: V2beta1 API.</p></li>
<li><p><strong>avatar_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the agent’s avatar, which are used throughout the Dialogflow console. When an image URL is entered into this
field, the Dialogflow will save the image in the backend. The address of the backend image returned from the API will be
shown in the [avatarUriBackend] field.</p></li>
<li><p><strong>classification_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – To filter out false positive results and still get variety in matched natural language inputs for your agent, you can
tune the machine learning classification threshold. If the returned score value is less than the threshold value, then a
fallback intent will be triggered or, if there are no fallback intents defined, no intent will be triggered. The score
values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the default of 0.3 is used.</p></li>
<li><p><strong>default_language_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default language of the agent as a language tag. <a class="reference external" href="https://cloud.google.com/dialogflow/docs/reference/language">See Language
Support</a> for a list of the currently supported language
codes. This field cannot be updated after creation.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this agent. The maximum length is 500 characters. If exceeded, the request is rejected.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this agent.</p></li>
<li><p><strong>enable_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether this agent should log conversation queries.</p></li>
<li><p><strong>match_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines how intents are detected from user queries. * MATCH_MODE_HYBRID: Best for agents with a small number of
examples in intents and/or wide use of templates syntax and composite entities. * MATCH_MODE_ML_ONLY: Can be used for
agents with a large number of examples in intents, especially the ones using &#64;sys.any or very large developer entities.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>supported_language_codes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of all languages supported by this agent (except for the defaultLanguageCode).</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The agent tier. If not specified, TIER_STANDARD is assumed. * TIER_STANDARD: Standard tier. * TIER_ENTERPRISE:
Enterprise tier (Essentials). * TIER_ENTERPRISE_PLUS: Enterprise tier (Plus). NOTE: Due to consistency issues, the
provider will not read this field from the API. Drift is possible between the Terraform state and Dialogflow if the
agent tier is changed outside of Terraform.</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time zone of this agent from the <a class="reference external" href="https://www.iana.org/time-zones">time zone database</a>, e.g., America/New_York,
Europe/Paris.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.diagflow.Agent.api_version">
<code class="sig-name descname">api_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.api_version" title="Permalink to this definition">¶</a></dt>
<dd><p>API version displayed in Dialogflow console. If not specified, V2 API is assumed. Clients are free to query different
service endpoints for different API versions. However, bots connectors and webhook calls will follow the specified API
version. * API_VERSION_V1: Legacy V1 API. * API_VERSION_V2: V2 API. * API_VERSION_V2_BETA_1: V2beta1 API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.diagflow.Agent.avatar_uri">
<code class="sig-name descname">avatar_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.avatar_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the agent’s avatar, which are used throughout the Dialogflow console. When an image URL is entered into this
field, the Dialogflow will save the image in the backend. The address of the backend image returned from the API will be
shown in the [avatarUriBackend] field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.diagflow.Agent.avatar_uri_backend">
<code class="sig-name descname">avatar_uri_backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.avatar_uri_backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the agent’s avatar as returned from the API. Output only. To provide an image URL for the agent avatar, the
[avatarUri] field can be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.diagflow.Agent.classification_threshold">
<code class="sig-name descname">classification_threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.classification_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>To filter out false positive results and still get variety in matched natural language inputs for your agent, you can
tune the machine learning classification threshold. If the returned score value is less than the threshold value, then a
fallback intent will be triggered or, if there are no fallback intents defined, no intent will be triggered. The score
values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the default of 0.3 is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.diagflow.Agent.default_language_code">
<code class="sig-name descname">default_language_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.default_language_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The default language of the agent as a language tag. <a class="reference external" href="https://cloud.google.com/dialogflow/docs/reference/language">See Language
Support</a> for a list of the currently supported language
codes. This field cannot be updated after creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.diagflow.Agent.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this agent. The maximum length is 500 characters. If exceeded, the request is rejected.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.diagflow.Agent.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this agent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.diagflow.Agent.enable_logging">
<code class="sig-name descname">enable_logging</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.enable_logging" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether this agent should log conversation queries.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.diagflow.Agent.match_mode">
<code class="sig-name descname">match_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.match_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines how intents are detected from user queries. * MATCH_MODE_HYBRID: Best for agents with a small number of
examples in intents and/or wide use of templates syntax and composite entities. * MATCH_MODE_ML_ONLY: Can be used for
agents with a large number of examples in intents, especially the ones using &#64;sys.any or very large developer entities.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.diagflow.Agent.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.diagflow.Agent.supported_language_codes">
<code class="sig-name descname">supported_language_codes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.supported_language_codes" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of all languages supported by this agent (except for the defaultLanguageCode).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.diagflow.Agent.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The agent tier. If not specified, TIER_STANDARD is assumed. * TIER_STANDARD: Standard tier. * TIER_ENTERPRISE:
Enterprise tier (Essentials). * TIER_ENTERPRISE_PLUS: Enterprise tier (Plus). NOTE: Due to consistency issues, the
provider will not read this field from the API. Drift is possible between the Terraform state and Dialogflow if the
agent tier is changed outside of Terraform.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.diagflow.Agent.time_zone">
<code class="sig-name descname">time_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.time_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The time zone of this agent from the <a class="reference external" href="https://www.iana.org/time-zones">time zone database</a>, e.g., America/New_York,
Europe/Paris.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.diagflow.Agent.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_version=None</em>, <em class="sig-param">avatar_uri=None</em>, <em class="sig-param">avatar_uri_backend=None</em>, <em class="sig-param">classification_threshold=None</em>, <em class="sig-param">default_language_code=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enable_logging=None</em>, <em class="sig-param">match_mode=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">supported_language_codes=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">time_zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Agent resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – API version displayed in Dialogflow console. If not specified, V2 API is assumed. Clients are free to query different
service endpoints for different API versions. However, bots connectors and webhook calls will follow the specified API
version. * API_VERSION_V1: Legacy V1 API. * API_VERSION_V2: V2 API. * API_VERSION_V2_BETA_1: V2beta1 API.</p></li>
<li><p><strong>avatar_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the agent’s avatar, which are used throughout the Dialogflow console. When an image URL is entered into this
field, the Dialogflow will save the image in the backend. The address of the backend image returned from the API will be
shown in the [avatarUriBackend] field.</p></li>
<li><p><strong>avatar_uri_backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the agent’s avatar as returned from the API. Output only. To provide an image URL for the agent avatar, the
[avatarUri] field can be used.</p></li>
<li><p><strong>classification_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – To filter out false positive results and still get variety in matched natural language inputs for your agent, you can
tune the machine learning classification threshold. If the returned score value is less than the threshold value, then a
fallback intent will be triggered or, if there are no fallback intents defined, no intent will be triggered. The score
values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the default of 0.3 is used.</p></li>
<li><p><strong>default_language_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The default language of the agent as a language tag. <a class="reference external" href="https://cloud.google.com/dialogflow/docs/reference/language">See Language
Support</a> for a list of the currently supported language
codes. This field cannot be updated after creation.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this agent. The maximum length is 500 characters. If exceeded, the request is rejected.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this agent.</p></li>
<li><p><strong>enable_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether this agent should log conversation queries.</p></li>
<li><p><strong>match_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines how intents are detected from user queries. * MATCH_MODE_HYBRID: Best for agents with a small number of
examples in intents and/or wide use of templates syntax and composite entities. * MATCH_MODE_ML_ONLY: Can be used for
agents with a large number of examples in intents, especially the ones using &#64;sys.any or very large developer entities.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>supported_language_codes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of all languages supported by this agent (except for the defaultLanguageCode).</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The agent tier. If not specified, TIER_STANDARD is assumed. * TIER_STANDARD: Standard tier. * TIER_ENTERPRISE:
Enterprise tier (Essentials). * TIER_ENTERPRISE_PLUS: Enterprise tier (Plus). NOTE: Due to consistency issues, the
provider will not read this field from the API. Drift is possible between the Terraform state and Dialogflow if the
agent tier is changed outside of Terraform.</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The time zone of this agent from the <a class="reference external" href="https://www.iana.org/time-zones">time zone database</a>, e.g., America/New_York,
Europe/Paris.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.diagflow.Agent.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.diagflow.Agent.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.diagflow.Agent.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
