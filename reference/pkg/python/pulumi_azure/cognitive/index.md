<div class="section" id="module-pulumi_azure.cognitive">
<span id="cognitive"></span><h1>cognitive<a class="headerlink" href="#module-pulumi_azure.cognitive" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.cognitive.Account">
<em class="property">class </em><code class="descclassname">pulumi_azure.cognitive.</code><code class="descname">Account</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>kind=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cognitive.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Cognitive Services Account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of Cognitive Service Account that should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Academic</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Autosuggest</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Autosuggest.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.CustomSearch</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Search</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Search.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Speech</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.SpellCheck</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.SpellCheck.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">ComputerVision</span></code>, <code class="docutils literal notranslate"><span class="pre">ContentModerator</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomSpeech</span></code>, <code class="docutils literal notranslate"><span class="pre">Emotion</span></code>, <code class="docutils literal notranslate"><span class="pre">Face</span></code>, <code class="docutils literal notranslate"><span class="pre">LUIS</span></code>, <code class="docutils literal notranslate"><span class="pre">Recommendations</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeakerRecognition</span></code>, <code class="docutils literal notranslate"><span class="pre">Speech</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeechServices</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeechTranslation</span></code>, <code class="docutils literal notranslate"><span class="pre">TextAnalytics</span></code>, <code class="docutils literal notranslate"><span class="pre">TextTranslation</span></code> and <code class="docutils literal notranslate"><span class="pre">WebLM</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cognitive Service Account. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cognitive Service Account is created. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</li>
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
<dd><p>Specifies the type of Cognitive Service Account that should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Academic</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Autosuggest</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Autosuggest.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.CustomSearch</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Search</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Search.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.Speech</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.SpellCheck</span></code>, <code class="docutils literal notranslate"><span class="pre">Bing.SpellCheck.v7</span></code>, <code class="docutils literal notranslate"><span class="pre">ComputerVision</span></code>, <code class="docutils literal notranslate"><span class="pre">ContentModerator</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomSpeech</span></code>, <code class="docutils literal notranslate"><span class="pre">Emotion</span></code>, <code class="docutils literal notranslate"><span class="pre">Face</span></code>, <code class="docutils literal notranslate"><span class="pre">LUIS</span></code>, <code class="docutils literal notranslate"><span class="pre">Recommendations</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeakerRecognition</span></code>, <code class="docutils literal notranslate"><span class="pre">Speech</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeechServices</span></code>, <code class="docutils literal notranslate"><span class="pre">SpeechTranslation</span></code>, <code class="docutils literal notranslate"><span class="pre">TextAnalytics</span></code>, <code class="docutils literal notranslate"><span class="pre">TextTranslation</span></code> and <code class="docutils literal notranslate"><span class="pre">WebLM</span></code>. Changing this forces a new resource to be created.</p>
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
<dt id="pulumi_azure.cognitive.Account.primary_access_key">
<code class="descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>A primary access key which can be used to connect to the Cognitive Service Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Cognitive Service Account is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.secondary_access_key">
<code class="descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key which can be used to connect to the Cognitive Service Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cognitive.Account.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cognitive.Account.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p>
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
<dt id="pulumi_azure.cognitive.Account.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cognitive.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
