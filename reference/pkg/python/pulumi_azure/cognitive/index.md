<div class="section" id="module-pulumi_azure.cognitive">
<span id="cognitive"></span><h1>cognitive<a class="headerlink" href="#module-pulumi_azure.cognitive" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.cognitive.Account">
<em class="property">class </em><code class="descclassname">pulumi_azure.cognitive.</code><code class="descname">Account</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>kind=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cognitive.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Cognitive Services Account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of Cognitive Service Account that should be created. Possible values are <cite>Academic</cite>, <cite>Bing.Autosuggest</cite>, <cite>Bing.Autosuggest.v7</cite>, <cite>Bing.CustomSearch</cite>, <cite>Bing.Search</cite>, <cite>Bing.Search.v7</cite>, <cite>Bing.Speech</cite>, <cite>Bing.SpellCheck</cite>, <cite>Bing.SpellCheck.v7</cite>, <cite>ComputerVision</cite>, <cite>ContentModerator</cite>, <cite>CustomSpeech</cite>, <cite>Emotion</cite>, <cite>Face</cite>, <cite>LUIS</cite>, <cite>Recommendations</cite>, <cite>SpeakerRecognition</cite>, <cite>Speech</cite>, <cite>SpeechServices</cite>, <cite>SpeechTranslation</cite>, <cite>TextAnalytics</cite>, <cite>TextTranslation</cite> and <cite>WebLM</cite>. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cognitive Service Account. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cognitive Service Account is created. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>sku</cite> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint used to connect to the Cognitive Service Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.kind">
<code class="descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of Cognitive Service Account that should be created. Possible values are <cite>Academic</cite>, <cite>Bing.Autosuggest</cite>, <cite>Bing.Autosuggest.v7</cite>, <cite>Bing.CustomSearch</cite>, <cite>Bing.Search</cite>, <cite>Bing.Search.v7</cite>, <cite>Bing.Speech</cite>, <cite>Bing.SpellCheck</cite>, <cite>Bing.SpellCheck.v7</cite>, <cite>ComputerVision</cite>, <cite>ContentModerator</cite>, <cite>CustomSpeech</cite>, <cite>Emotion</cite>, <cite>Face</cite>, <cite>LUIS</cite>, <cite>Recommendations</cite>, <cite>SpeakerRecognition</cite>, <cite>Speech</cite>, <cite>SpeechServices</cite>, <cite>SpeechTranslation</cite>, <cite>TextAnalytics</cite>, <cite>TextTranslation</cite> and <cite>WebLM</cite>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Cognitive Service Account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Cognitive Service Account is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>sku</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.cognitive.Account.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cognitive.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.cognitive.Account.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cognitive.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
