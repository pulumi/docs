---
title: Module guardduty
title_tag: Module guardduty | Package pulumi_aws | Python SDK
linktitle: guardduty
notitle: true
---

<div class="section" id="guardduty">
<h1>guardduty<a class="headerlink" href="#guardduty" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.guardduty"></span><dl class="py class">
<dt id="pulumi_aws.guardduty.AwaitableGetDetectorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.guardduty.</code><code class="sig-name descname">AwaitableGetDetectorResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">finding_publishing_frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.AwaitableGetDetectorResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.guardduty.Detector">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.guardduty.</code><code class="sig-name descname">Detector</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">finding_publishing_frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Detector" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage a GuardDuty detector.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Deleting this resource is equivalent to “disabling” GuardDuty for an AWS region, which removes all existing findings. You can set the <code class="docutils literal notranslate"><span class="pre">enable</span></code> attribute to <code class="docutils literal notranslate"><span class="pre">false</span></code> to instead “suspend” monitoring and feedback reporting while keeping existing data. See the <a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_suspend-disable.html">Suspending or Disabling Amazon GuardDuty documentation</a> for more information.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">my_detector</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">Detector</span><span class="p">(</span><span class="s2">&quot;myDetector&quot;</span><span class="p">,</span> <span class="n">enable</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable monitoring and feedback reporting. Setting to <code class="docutils literal notranslate"><span class="pre">false</span></code> is equivalent to “suspending” GuardDuty. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>finding_publishing_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the frequency of notifications sent for subsequent finding occurrences. If the detector is a GuardDuty member account, the value is determined by the GuardDuty master account and cannot be modified, otherwise defaults to <code class="docutils literal notranslate"><span class="pre">SIX_HOURS</span></code>. For standalone and GuardDuty master accounts, it must be configured in this provider to enable drift detection. Valid values for standalone and master accounts: <code class="docutils literal notranslate"><span class="pre">FIFTEEN_MINUTES</span></code>, <code class="docutils literal notranslate"><span class="pre">ONE_HOUR</span></code>, <code class="docutils literal notranslate"><span class="pre">SIX_HOURS</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html#guardduty_findings_cloudwatch_notification_frequency">AWS Documentation</a> for more information.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.guardduty.Detector.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Detector.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID of the GuardDuty detector</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.Detector.enable">
<code class="sig-name descname">enable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Detector.enable" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable monitoring and feedback reporting. Setting to <code class="docutils literal notranslate"><span class="pre">false</span></code> is equivalent to “suspending” GuardDuty. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.Detector.finding_publishing_frequency">
<code class="sig-name descname">finding_publishing_frequency</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Detector.finding_publishing_frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the frequency of notifications sent for subsequent finding occurrences. If the detector is a GuardDuty member account, the value is determined by the GuardDuty master account and cannot be modified, otherwise defaults to <code class="docutils literal notranslate"><span class="pre">SIX_HOURS</span></code>. For standalone and GuardDuty master accounts, it must be configured in this provider to enable drift detection. Valid values for standalone and master accounts: <code class="docutils literal notranslate"><span class="pre">FIFTEEN_MINUTES</span></code>, <code class="docutils literal notranslate"><span class="pre">ONE_HOUR</span></code>, <code class="docutils literal notranslate"><span class="pre">SIX_HOURS</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html#guardduty_findings_cloudwatch_notification_frequency">AWS Documentation</a> for more information.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.Detector.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">finding_publishing_frequency</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Detector.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Detector resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account ID of the GuardDuty detector</p></li>
<li><p><strong>enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable monitoring and feedback reporting. Setting to <code class="docutils literal notranslate"><span class="pre">false</span></code> is equivalent to “suspending” GuardDuty. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>finding_publishing_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the frequency of notifications sent for subsequent finding occurrences. If the detector is a GuardDuty member account, the value is determined by the GuardDuty master account and cannot be modified, otherwise defaults to <code class="docutils literal notranslate"><span class="pre">SIX_HOURS</span></code>. For standalone and GuardDuty master accounts, it must be configured in this provider to enable drift detection. Valid values for standalone and master accounts: <code class="docutils literal notranslate"><span class="pre">FIFTEEN_MINUTES</span></code>, <code class="docutils literal notranslate"><span class="pre">ONE_HOUR</span></code>, <code class="docutils literal notranslate"><span class="pre">SIX_HOURS</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html#guardduty_findings_cloudwatch_notification_frequency">AWS Documentation</a> for more information.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.Detector.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Detector.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.guardduty.Detector.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Detector.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.guardduty.GetDetectorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.guardduty.</code><code class="sig-name descname">GetDetectorResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">finding_publishing_frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.GetDetectorResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDetector.</p>
<dl class="py attribute">
<dt id="pulumi_aws.guardduty.GetDetectorResult.finding_publishing_frequency">
<code class="sig-name descname">finding_publishing_frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.GetDetectorResult.finding_publishing_frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The frequency of notifications sent about subsequent finding occurrences.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.GetDetectorResult.service_role_arn">
<code class="sig-name descname">service_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.GetDetectorResult.service_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The service-linked role that grants GuardDuty access to the resources in the AWS account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.GetDetectorResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.GetDetectorResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the detector.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.guardduty.IPSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.guardduty.</code><code class="sig-name descname">IPSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detector_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.IPSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage a GuardDuty IPSet.</p>
<blockquote>
<div><p><strong>Note:</strong> Currently in GuardDuty, users from member accounts cannot upload and further manage IPSets. IPSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the <a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/create-ip-set.html">GuardDuty API Documentation</a></p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">master</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">Detector</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">,</span> <span class="n">enable</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">bucket</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">s3</span><span class="o">.</span><span class="n">Bucket</span><span class="p">(</span><span class="s2">&quot;bucket&quot;</span><span class="p">,</span> <span class="n">acl</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">)</span>
<span class="n">my_ip_set_bucket_object</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">s3</span><span class="o">.</span><span class="n">BucketObject</span><span class="p">(</span><span class="s2">&quot;myIPSetBucketObject&quot;</span><span class="p">,</span>
    <span class="n">acl</span><span class="o">=</span><span class="s2">&quot;public-read&quot;</span><span class="p">,</span>
    <span class="n">bucket</span><span class="o">=</span><span class="n">bucket</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">content</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;10.0.0.0/8</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;MyIPSet&quot;</span><span class="p">)</span>
<span class="n">my_ip_set_ip_set</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">IPSet</span><span class="p">(</span><span class="s2">&quot;myIPSetIPSet&quot;</span><span class="p">,</span>
    <span class="n">activate</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">detector_id</span><span class="o">=</span><span class="n">master</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">format</span><span class="o">=</span><span class="s2">&quot;TXT&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">Output</span><span class="o">.</span><span class="n">all</span><span class="p">(</span><span class="n">my_ip_set_bucket_object</span><span class="o">.</span><span class="n">bucket</span><span class="p">,</span> <span class="n">my_ip_set_bucket_object</span><span class="o">.</span><span class="n">key</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">bucket</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;https://s3.amazonaws.com/</span><span class="si">{</span><span class="n">bucket</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether GuardDuty is to start using the uploaded IPSet.</p></li>
<li><p><strong>detector_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detector ID of the GuardDuty.</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of the file that contains the IPSet. Valid values: <code class="docutils literal notranslate"><span class="pre">TXT</span></code> | <code class="docutils literal notranslate"><span class="pre">STIX</span></code> | <code class="docutils literal notranslate"><span class="pre">OTX_CSV</span></code> | <code class="docutils literal notranslate"><span class="pre">ALIEN_VAULT</span></code> | <code class="docutils literal notranslate"><span class="pre">PROOF_POINT</span></code> | <code class="docutils literal notranslate"><span class="pre">FIRE_EYE</span></code></p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the file that contains the IPSet.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name to identify the IPSet.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.guardduty.IPSet.activate">
<code class="sig-name descname">activate</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.activate" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether GuardDuty is to start using the uploaded IPSet.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.IPSet.detector_id">
<code class="sig-name descname">detector_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.detector_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The detector ID of the GuardDuty.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.IPSet.format">
<code class="sig-name descname">format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of the file that contains the IPSet. Valid values: <code class="docutils literal notranslate"><span class="pre">TXT</span></code> | <code class="docutils literal notranslate"><span class="pre">STIX</span></code> | <code class="docutils literal notranslate"><span class="pre">OTX_CSV</span></code> | <code class="docutils literal notranslate"><span class="pre">ALIEN_VAULT</span></code> | <code class="docutils literal notranslate"><span class="pre">PROOF_POINT</span></code> | <code class="docutils literal notranslate"><span class="pre">FIRE_EYE</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.IPSet.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the file that contains the IPSet.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.IPSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name to identify the IPSet.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.IPSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detector_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IPSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether GuardDuty is to start using the uploaded IPSet.</p></li>
<li><p><strong>detector_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detector ID of the GuardDuty.</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of the file that contains the IPSet. Valid values: <code class="docutils literal notranslate"><span class="pre">TXT</span></code> | <code class="docutils literal notranslate"><span class="pre">STIX</span></code> | <code class="docutils literal notranslate"><span class="pre">OTX_CSV</span></code> | <code class="docutils literal notranslate"><span class="pre">ALIEN_VAULT</span></code> | <code class="docutils literal notranslate"><span class="pre">PROOF_POINT</span></code> | <code class="docutils literal notranslate"><span class="pre">FIRE_EYE</span></code></p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the file that contains the IPSet.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name to identify the IPSet.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.IPSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.guardduty.IPSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.guardduty.InviteAccepter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.guardduty.</code><code class="sig-name descname">InviteAccepter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detector_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.InviteAccepter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to accept a pending GuardDuty invite on creation, ensure the detector has the correct master account on read, and disassociate with the master account upon removal.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">master</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">Detector</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">)</span>
<span class="n">member_detector</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">Detector</span><span class="p">(</span><span class="s2">&quot;memberDetector&quot;</span><span class="p">)</span>
<span class="n">dev</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">Member</span><span class="p">(</span><span class="s2">&quot;dev&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="n">member_detector</span><span class="o">.</span><span class="n">account_id</span><span class="p">,</span>
    <span class="n">detector_id</span><span class="o">=</span><span class="n">master</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;required@example.com&quot;</span><span class="p">,</span>
    <span class="n">invite</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">member_invite_accepter</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">InviteAccepter</span><span class="p">(</span><span class="s2">&quot;memberInviteAccepter&quot;</span><span class="p">,</span>
    <span class="n">detector_id</span><span class="o">=</span><span class="n">member_detector</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">master_account_id</span><span class="o">=</span><span class="n">master</span><span class="o">.</span><span class="n">account_id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>detector_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detector ID of the member GuardDuty account.</p></li>
<li><p><strong>master_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account ID for master account.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.guardduty.InviteAccepter.detector_id">
<code class="sig-name descname">detector_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.InviteAccepter.detector_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The detector ID of the member GuardDuty account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.InviteAccepter.master_account_id">
<code class="sig-name descname">master_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.InviteAccepter.master_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS account ID for master account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.InviteAccepter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detector_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_account_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.InviteAccepter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InviteAccepter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>detector_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detector ID of the member GuardDuty account.</p></li>
<li><p><strong>master_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account ID for master account.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.InviteAccepter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.InviteAccepter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.guardduty.InviteAccepter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.InviteAccepter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.guardduty.Member">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.guardduty.</code><code class="sig-name descname">Member</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detector_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_email_notification</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invitation_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invite</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Member" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage a GuardDuty member. To accept invitations in member accounts, see the <cite>``guardduty.InviteAccepter`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/guardduty_invite_accepter.html">https://www.terraform.io/docs/providers/aws/r/guardduty_invite_accepter.html</a>&gt;`_.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">master</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">Detector</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">,</span> <span class="n">enable</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">member_detector</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">Detector</span><span class="p">(</span><span class="s2">&quot;memberDetector&quot;</span><span class="p">,</span> <span class="n">enable</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">member_member</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">Member</span><span class="p">(</span><span class="s2">&quot;memberMember&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="n">member_detector</span><span class="o">.</span><span class="n">account_id</span><span class="p">,</span>
    <span class="n">detector_id</span><span class="o">=</span><span class="n">master</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;required@example.com&quot;</span><span class="p">,</span>
    <span class="n">invite</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">invitation_message</span><span class="o">=</span><span class="s2">&quot;please accept guardduty invitation&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account ID for member account.</p></li>
<li><p><strong>detector_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detector ID of the GuardDuty account where you want to create member accounts.</p></li>
<li><p><strong>disable_email_notification</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether an email notification is sent to the accounts. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address for member account.</p></li>
<li><p><strong>invitation_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Message for invitation.</p></li>
<li><p><strong>invite</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether to invite the account to GuardDuty as a member. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. To detect if an invitation needs to be (re-)sent, the this provider state value is <code class="docutils literal notranslate"><span class="pre">true</span></code> based on a <code class="docutils literal notranslate"><span class="pre">relationship_status</span></code> of <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Invited</span></code>, or <code class="docutils literal notranslate"><span class="pre">EmailVerificationInProgress</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.guardduty.Member.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS account ID for member account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.Member.detector_id">
<code class="sig-name descname">detector_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.detector_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The detector ID of the GuardDuty account where you want to create member accounts.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.Member.disable_email_notification">
<code class="sig-name descname">disable_email_notification</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.disable_email_notification" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether an email notification is sent to the accounts. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.Member.email">
<code class="sig-name descname">email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address for member account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.Member.invitation_message">
<code class="sig-name descname">invitation_message</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.invitation_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Message for invitation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.Member.invite">
<code class="sig-name descname">invite</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.invite" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether to invite the account to GuardDuty as a member. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. To detect if an invitation needs to be (re-)sent, the this provider state value is <code class="docutils literal notranslate"><span class="pre">true</span></code> based on a <code class="docutils literal notranslate"><span class="pre">relationship_status</span></code> of <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Invited</span></code>, or <code class="docutils literal notranslate"><span class="pre">EmailVerificationInProgress</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.Member.relationship_status">
<code class="sig-name descname">relationship_status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.relationship_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the relationship between the member account and its master account. More information can be found in <a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/get-members.html">Amazon GuardDuty API Reference</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.Member.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detector_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_email_notification</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invitation_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invite</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">relationship_status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Member.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Member resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account ID for member account.</p></li>
<li><p><strong>detector_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detector ID of the GuardDuty account where you want to create member accounts.</p></li>
<li><p><strong>disable_email_notification</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether an email notification is sent to the accounts. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address for member account.</p></li>
<li><p><strong>invitation_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Message for invitation.</p></li>
<li><p><strong>invite</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether to invite the account to GuardDuty as a member. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. To detect if an invitation needs to be (re-)sent, the this provider state value is <code class="docutils literal notranslate"><span class="pre">true</span></code> based on a <code class="docutils literal notranslate"><span class="pre">relationship_status</span></code> of <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Invited</span></code>, or <code class="docutils literal notranslate"><span class="pre">EmailVerificationInProgress</span></code>.</p></li>
<li><p><strong>relationship_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The status of the relationship between the member account and its master account. More information can be found in <a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/get-members.html">Amazon GuardDuty API Reference</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.Member.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Member.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.guardduty.Member.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Member.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.guardduty.OrganizationAdminAccount">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.guardduty.</code><code class="sig-name descname">OrganizationAdminAccount</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.OrganizationAdminAccount" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a GuardDuty Organization Admin Account. The AWS account utilizing this resource must be an Organizations master account. More information about Organizations support in GuardDuty can be found in the <a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html">GuardDuty User Guide</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example_organization</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">Organization</span><span class="p">(</span><span class="s2">&quot;exampleOrganization&quot;</span><span class="p">,</span>
    <span class="n">aws_service_access_principals</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;guardduty.amazonaws.com&quot;</span><span class="p">],</span>
    <span class="n">feature_set</span><span class="o">=</span><span class="s2">&quot;ALL&quot;</span><span class="p">)</span>
<span class="n">example_detector</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">Detector</span><span class="p">(</span><span class="s2">&quot;exampleDetector&quot;</span><span class="p">)</span>
<span class="n">example_organization_admin_account</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">OrganizationAdminAccount</span><span class="p">(</span><span class="s2">&quot;exampleOrganizationAdminAccount&quot;</span><span class="p">,</span> <span class="n">admin_account_id</span><span class="o">=</span><span class="s2">&quot;123456789012&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account identifier to designate as a delegated administrator for GuardDuty.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.guardduty.OrganizationAdminAccount.admin_account_id">
<code class="sig-name descname">admin_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.OrganizationAdminAccount.admin_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS account identifier to designate as a delegated administrator for GuardDuty.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.OrganizationAdminAccount.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_account_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.OrganizationAdminAccount.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationAdminAccount resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account identifier to designate as a delegated administrator for GuardDuty.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.OrganizationAdminAccount.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.OrganizationAdminAccount.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.guardduty.OrganizationAdminAccount.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.OrganizationAdminAccount.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.guardduty.OrganizationConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.guardduty.</code><code class="sig-name descname">OrganizationConfiguration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detector_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.OrganizationConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the GuardDuty Organization Configuration in the current AWS Region. The AWS account utilizing this resource must have been assigned as a delegated Organization administrator account, e.g. via the <cite>``guardduty.OrganizationAdminAccount`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/guardduty_organization_admin_account.html">https://www.terraform.io/docs/providers/aws/r/guardduty_organization_admin_account.html</a>&gt;`_. More information about Organizations support in GuardDuty can be found in the <a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html">GuardDuty User Guide</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This is an advanced resource. The provider will automatically assume management of the GuardDuty Organization Configuration without import and perform no actions on removal from the resource configuration.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example_detector</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">Detector</span><span class="p">(</span><span class="s2">&quot;exampleDetector&quot;</span><span class="p">,</span> <span class="n">enable</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">example_organization_configuration</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">OrganizationConfiguration</span><span class="p">(</span><span class="s2">&quot;exampleOrganizationConfiguration&quot;</span><span class="p">,</span>
    <span class="n">auto_enable</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">detector_id</span><span class="o">=</span><span class="n">example_detector</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When this setting is enabled, all new accounts that are created in, or added to, the organization are added as a member accounts of the organization’s GuardDuty delegated administrator and GuardDuty is enabled in that AWS Region.</p></li>
<li><p><strong>detector_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detector ID of the GuardDuty account.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.guardduty.OrganizationConfiguration.auto_enable">
<code class="sig-name descname">auto_enable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.OrganizationConfiguration.auto_enable" title="Permalink to this definition">¶</a></dt>
<dd><p>When this setting is enabled, all new accounts that are created in, or added to, the organization are added as a member accounts of the organization’s GuardDuty delegated administrator and GuardDuty is enabled in that AWS Region.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.OrganizationConfiguration.detector_id">
<code class="sig-name descname">detector_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.OrganizationConfiguration.detector_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The detector ID of the GuardDuty account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.OrganizationConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detector_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.OrganizationConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When this setting is enabled, all new accounts that are created in, or added to, the organization are added as a member accounts of the organization’s GuardDuty delegated administrator and GuardDuty is enabled in that AWS Region.</p></li>
<li><p><strong>detector_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detector ID of the GuardDuty account.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.OrganizationConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.OrganizationConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.guardduty.OrganizationConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.OrganizationConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.guardduty.ThreatIntelSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.guardduty.</code><code class="sig-name descname">ThreatIntelSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detector_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage a GuardDuty ThreatIntelSet.</p>
<blockquote>
<div><p><strong>Note:</strong> Currently in GuardDuty, users from member accounts cannot upload and further manage ThreatIntelSets. ThreatIntelSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the <a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/create-threat-intel-set.html">GuardDuty API Documentation</a></p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">master</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">Detector</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">,</span> <span class="n">enable</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">bucket</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">s3</span><span class="o">.</span><span class="n">Bucket</span><span class="p">(</span><span class="s2">&quot;bucket&quot;</span><span class="p">,</span> <span class="n">acl</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">)</span>
<span class="n">my_threat_intel_set_bucket_object</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">s3</span><span class="o">.</span><span class="n">BucketObject</span><span class="p">(</span><span class="s2">&quot;myThreatIntelSetBucketObject&quot;</span><span class="p">,</span>
    <span class="n">acl</span><span class="o">=</span><span class="s2">&quot;public-read&quot;</span><span class="p">,</span>
    <span class="n">bucket</span><span class="o">=</span><span class="n">bucket</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">content</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;10.0.0.0/8</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;MyThreatIntelSet&quot;</span><span class="p">)</span>
<span class="n">my_threat_intel_set_threat_intel_set</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">ThreatIntelSet</span><span class="p">(</span><span class="s2">&quot;myThreatIntelSetThreatIntelSet&quot;</span><span class="p">,</span>
    <span class="n">activate</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">detector_id</span><span class="o">=</span><span class="n">master</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">format</span><span class="o">=</span><span class="s2">&quot;TXT&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">Output</span><span class="o">.</span><span class="n">all</span><span class="p">(</span><span class="n">my_threat_intel_set_bucket_object</span><span class="o">.</span><span class="n">bucket</span><span class="p">,</span> <span class="n">my_threat_intel_set_bucket_object</span><span class="o">.</span><span class="n">key</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">bucket</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;https://s3.amazonaws.com/</span><span class="si">{</span><span class="n">bucket</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.</p></li>
<li><p><strong>detector_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detector ID of the GuardDuty.</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of the file that contains the ThreatIntelSet. Valid values: <code class="docutils literal notranslate"><span class="pre">TXT</span></code> | <code class="docutils literal notranslate"><span class="pre">STIX</span></code> | <code class="docutils literal notranslate"><span class="pre">OTX_CSV</span></code> | <code class="docutils literal notranslate"><span class="pre">ALIEN_VAULT</span></code> | <code class="docutils literal notranslate"><span class="pre">PROOF_POINT</span></code> | <code class="docutils literal notranslate"><span class="pre">FIRE_EYE</span></code></p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the file that contains the ThreatIntelSet.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name to identify the ThreatIntelSet.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.activate">
<code class="sig-name descname">activate</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.activate" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.detector_id">
<code class="sig-name descname">detector_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.detector_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The detector ID of the GuardDuty.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.format">
<code class="sig-name descname">format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of the file that contains the ThreatIntelSet. Valid values: <code class="docutils literal notranslate"><span class="pre">TXT</span></code> | <code class="docutils literal notranslate"><span class="pre">STIX</span></code> | <code class="docutils literal notranslate"><span class="pre">OTX_CSV</span></code> | <code class="docutils literal notranslate"><span class="pre">ALIEN_VAULT</span></code> | <code class="docutils literal notranslate"><span class="pre">PROOF_POINT</span></code> | <code class="docutils literal notranslate"><span class="pre">FIRE_EYE</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the file that contains the ThreatIntelSet.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name to identify the ThreatIntelSet.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detector_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ThreatIntelSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.</p></li>
<li><p><strong>detector_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detector ID of the GuardDuty.</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of the file that contains the ThreatIntelSet. Valid values: <code class="docutils literal notranslate"><span class="pre">TXT</span></code> | <code class="docutils literal notranslate"><span class="pre">STIX</span></code> | <code class="docutils literal notranslate"><span class="pre">OTX_CSV</span></code> | <code class="docutils literal notranslate"><span class="pre">ALIEN_VAULT</span></code> | <code class="docutils literal notranslate"><span class="pre">PROOF_POINT</span></code> | <code class="docutils literal notranslate"><span class="pre">FIRE_EYE</span></code></p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the file that contains the ThreatIntelSet.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name to identify the ThreatIntelSet.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.guardduty.ThreatIntelSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_aws.guardduty.get_detector">
<code class="sig-prename descclassname">pulumi_aws.guardduty.</code><code class="sig-name descname">get_detector</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.get_detector" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about a GuardDuty detector.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">guardduty</span><span class="o">.</span><span class="n">get_detector</span><span class="p">()</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>id</strong> (<em>str</em>) – The ID of the detector.</p>
</dd>
</dl>
</dd></dl>

</div>
