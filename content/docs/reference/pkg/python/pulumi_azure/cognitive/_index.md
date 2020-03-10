---
title: Module cognitive
title_tag: Module cognitive | Package pulumi_azure | Python SDK
linktitle: cognitive
notitle: true
---

<div class="section" id="cognitive">
<h1>cognitive<a class="headerlink" href="#cognitive" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.cognitive"></span><dl class="class">
<dt id="pulumi_azure.cognitive.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cognitive.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">kind=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cognitive.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Cognitive Services Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of Cognitive Service Account that should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Academic</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Autosuggest</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Autosuggest.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.CustomSearch</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Search</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Search.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Speech</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.SpellCheck</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.SpellCheck.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">CognitiveServices</span></code>, <code class="docutils literal notranslate"><span class="pre">ComputerVision</span></code>, <code class="docutils literal notranslate"><span class="pre">ContentModerator</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomSpeech</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomVision.Prediction</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomVision.Training</span></code>, <code class="docutils literal notranslate"><span class="pre">Emotion</span></code>, <code class="docutils literal notranslate"><span class="pre">Face</span></code>,<code class="docutils literal notranslate"><span class="pre">FormRecognizer</span></code>, <code class="docutils literal notranslate"><span class="pre">ImmersiveReader</span></code>, <code class="docutils literal notranslate"><span class="pre">LUIS</span></code>, <code class="docutils literal notranslate"><span class="pre">LUIS.Authoring</span></code>, <code class="docutils literal notranslate"><span class="pre">QnAMaker</span></code>, <code class="docutils literal notranslate"><span class="pre">Recommendations</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeakerRecognition</span></code>, <code class="docutils literal notranslate"><span class="pre">Speech</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeechServices</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeechTranslation</span></code>, <code class="docutils literal notranslate"><span class="pre">TextAnalytics</span></code>, <code class="docutils literal notranslate"><span class="pre">TextTranslation</span></code> and <code class="docutils literal notranslate"><span class="pre">WebLM</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cognitive Service Account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cognitive Service Account is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the SKU Name for this Cognitive Service Account. Possible values are <code class="docutils literal notranslate"><span class="pre">F0</span></code>, <code class="docutils literal notranslate"><span class="pre">F1</span></code>, <code class="docutils literal notranslate"><span class="pre">S0</span></code>, <code class="docutils literal notranslate"><span class="pre">S1</span></code>, <code class="docutils literal notranslate"><span class="pre">S2</span></code>, <code class="docutils literal notranslate"><span class="pre">S3</span></code>, <code class="docutils literal notranslate"><span class="pre">S4</span></code>, <code class="docutils literal notranslate"><span class="pre">S5</span></code>, <code class="docutils literal notranslate"><span class="pre">S6</span></code>, <code class="docutils literal notranslate"><span class="pre">P0</span></code>, <code class="docutils literal notranslate"><span class="pre">P1</span></code>, and <code class="docutils literal notranslate"><span class="pre">P2</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cognitive_account.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cognitive_account.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint used to connect to the Cognitive Service Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of Cognitive Service Account that should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Academic</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Autosuggest</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Autosuggest.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.CustomSearch</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Search</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Search.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Speech</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.SpellCheck</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.SpellCheck.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">CognitiveServices</span></code>, <code class="docutils literal notranslate"><span class="pre">ComputerVision</span></code>, <code class="docutils literal notranslate"><span class="pre">ContentModerator</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomSpeech</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomVision.Prediction</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomVision.Training</span></code>, <code class="docutils literal notranslate"><span class="pre">Emotion</span></code>, <code class="docutils literal notranslate"><span class="pre">Face</span></code>,<code class="docutils literal notranslate"><span class="pre">FormRecognizer</span></code>, <code class="docutils literal notranslate"><span class="pre">ImmersiveReader</span></code>, <code class="docutils literal notranslate"><span class="pre">LUIS</span></code>, <code class="docutils literal notranslate"><span class="pre">LUIS.Authoring</span></code>, <code class="docutils literal notranslate"><span class="pre">QnAMaker</span></code>, <code class="docutils literal notranslate"><span class="pre">Recommendations</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeakerRecognition</span></code>, <code class="docutils literal notranslate"><span class="pre">Speech</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeechServices</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeechTranslation</span></code>, <code class="docutils literal notranslate"><span class="pre">TextAnalytics</span></code>, <code class="docutils literal notranslate"><span class="pre">TextTranslation</span></code> and <code class="docutils literal notranslate"><span class="pre">WebLM</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Cognitive Service Account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.primary_access_key">
<code class="sig-name descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>A primary access key which can be used to connect to the Cognitive Service Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Cognitive Service Account is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.secondary_access_key">
<code class="sig-name descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key which can be used to connect to the Cognitive Service Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the SKU Name for this Cognitive Service Account. Possible values are <code class="docutils literal notranslate"><span class="pre">F0</span></code>, <code class="docutils literal notranslate"><span class="pre">F1</span></code>, <code class="docutils literal notranslate"><span class="pre">S0</span></code>, <code class="docutils literal notranslate"><span class="pre">S1</span></code>, <code class="docutils literal notranslate"><span class="pre">S2</span></code>, <code class="docutils literal notranslate"><span class="pre">S3</span></code>, <code class="docutils literal notranslate"><span class="pre">S4</span></code>, <code class="docutils literal notranslate"><span class="pre">S5</span></code>, <code class="docutils literal notranslate"><span class="pre">S6</span></code>, <code class="docutils literal notranslate"><span class="pre">P0</span></code>, <code class="docutils literal notranslate"><span class="pre">P1</span></code>, and <code class="docutils literal notranslate"><span class="pre">P2</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.cognitive.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">kind=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_access_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_access_key=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cognitive.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint used to connect to the Cognitive Service Account.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of Cognitive Service Account that should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Academic</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Autosuggest</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Autosuggest.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.CustomSearch</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Search</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Search.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Speech</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.SpellCheck</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.SpellCheck.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">CognitiveServices</span></code>, <code class="docutils literal notranslate"><span class="pre">ComputerVision</span></code>, <code class="docutils literal notranslate"><span class="pre">ContentModerator</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomSpeech</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomVision.Prediction</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomVision.Training</span></code>, <code class="docutils literal notranslate"><span class="pre">Emotion</span></code>, <code class="docutils literal notranslate"><span class="pre">Face</span></code>,<code class="docutils literal notranslate"><span class="pre">FormRecognizer</span></code>, <code class="docutils literal notranslate"><span class="pre">ImmersiveReader</span></code>, <code class="docutils literal notranslate"><span class="pre">LUIS</span></code>, <code class="docutils literal notranslate"><span class="pre">LUIS.Authoring</span></code>, <code class="docutils literal notranslate"><span class="pre">QnAMaker</span></code>, <code class="docutils literal notranslate"><span class="pre">Recommendations</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeakerRecognition</span></code>, <code class="docutils literal notranslate"><span class="pre">Speech</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeechServices</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeechTranslation</span></code>, <code class="docutils literal notranslate"><span class="pre">TextAnalytics</span></code>, <code class="docutils literal notranslate"><span class="pre">TextTranslation</span></code> and <code class="docutils literal notranslate"><span class="pre">WebLM</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cognitive Service Account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A primary access key which can be used to connect to the Cognitive Service Account.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cognitive Service Account is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary access key which can be used to connect to the Cognitive Service Account.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the SKU Name for this Cognitive Service Account. Possible values are <code class="docutils literal notranslate"><span class="pre">F0</span></code>, <code class="docutils literal notranslate"><span class="pre">F1</span></code>, <code class="docutils literal notranslate"><span class="pre">S0</span></code>, <code class="docutils literal notranslate"><span class="pre">S1</span></code>, <code class="docutils literal notranslate"><span class="pre">S2</span></code>, <code class="docutils literal notranslate"><span class="pre">S3</span></code>, <code class="docutils literal notranslate"><span class="pre">S4</span></code>, <code class="docutils literal notranslate"><span class="pre">S5</span></code>, <code class="docutils literal notranslate"><span class="pre">S6</span></code>, <code class="docutils literal notranslate"><span class="pre">P0</span></code>, <code class="docutils literal notranslate"><span class="pre">P1</span></code>, and <code class="docutils literal notranslate"><span class="pre">P2</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cognitive_account.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cognitive_account.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.cognitive.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cognitive.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cognitive.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cognitive.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
