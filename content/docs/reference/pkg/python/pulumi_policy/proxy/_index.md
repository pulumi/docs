---
title: Module proxy
title_tag: Module proxy | Package pulumi_policy | Python SDK
linktitle: proxy
notitle: true
---

{{< resource-docs-alert "policy" >}}

<section id="module-pulumi_policy.proxy">
<span id="proxy"></span><h1>proxy<a class="headerlink" href="#module-pulumi_policy.proxy" title="Permalink to this headline"></a></h1>
<dl class="py class">
<dt id="pulumi_policy.proxy.Mapping">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_policy.proxy.</code><code class="sig-name descname">Mapping</code><a class="headerlink" href="#pulumi_policy.proxy.Mapping" title="Permalink to this definition"></a></dt>
<dd><p>A Mapping is a generic container for associating key/value
pairs.</p>
<p>This class provides concrete generic implementations of all
methods except for <strong>getitem</strong>, <strong>iter</strong>, and <strong>len</strong>.</p>
<dl class="py method">
<dt id="pulumi_policy.proxy.Mapping.get">
<code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">k</em><span class="optional">[</span>, <em class="sig-param">d</em><span class="optional">]</span><span class="sig-paren">)</span> &#x2192; D[k] if k in D, else d.  d defaults to None.<a class="headerlink" href="#pulumi_policy.proxy.Mapping.get" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt id="pulumi_policy.proxy.Mapping.items">
<code class="sig-name descname">items</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; a set-like object providing a view on D’s items<a class="headerlink" href="#pulumi_policy.proxy.Mapping.items" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt id="pulumi_policy.proxy.Mapping.keys">
<code class="sig-name descname">keys</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; a set-like object providing a view on D’s keys<a class="headerlink" href="#pulumi_policy.proxy.Mapping.keys" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt id="pulumi_policy.proxy.Mapping.values">
<code class="sig-name descname">values</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; an object providing a view on D’s values<a class="headerlink" href="#pulumi_policy.proxy.Mapping.values" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_policy.proxy.Sequence">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_policy.proxy.</code><code class="sig-name descname">Sequence</code><a class="headerlink" href="#pulumi_policy.proxy.Sequence" title="Permalink to this definition"></a></dt>
<dd><p>All the operations on a read-only sequence.</p>
<p>Concrete subclasses must override <strong>new</strong> or <strong>init</strong>,
<strong>getitem</strong>, and <strong>len</strong>.</p>
<dl class="py method">
<dt id="pulumi_policy.proxy.Sequence.count">
<code class="sig-name descname">count</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">value</span></em><span class="sig-paren">)</span> &#x2192; integer – return number of occurrences of value<a class="headerlink" href="#pulumi_policy.proxy.Sequence.count" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt id="pulumi_policy.proxy.Sequence.index">
<code class="sig-name descname">index</code><span class="sig-paren">(</span><em class="sig-param">value</em><span class="optional">[</span>, <em class="sig-param">start</em><span class="optional">[</span>, <em class="sig-param">stop</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span> &#x2192; integer – return first index of value.<a class="headerlink" href="#pulumi_policy.proxy.Sequence.index" title="Permalink to this definition"></a></dt>
<dd><p>Raises ValueError if the value is not present.</p>
<p>Supporting start and stop arguments is optional, but
recommended.</p>
</dd></dl>

</dd></dl>

<dl class="py exception">
<dt id="pulumi_policy.proxy.UnknownValueError">
<em class="property">exception </em><code class="sig-prename descclassname">pulumi_policy.proxy.</code><code class="sig-name descname">UnknownValueError</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">unknown_type_sentinel</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">props</span><span class="p">:</span> <span class="n">List<span class="p">[</span>str<span class="p">]</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.proxy.UnknownValueError" title="Permalink to this definition"></a></dt>
<dd><p>Exception raised to indicate that a property we attempted to access in some cloud resource is
unknown. For example, during preview, some resource fields (such as an allocated IP address)
can’t be known until the update is executed; an attempt to access such a field will result in
this exception.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_policy.proxy.unknown_checking_proxy">
<code class="sig-prename descclassname">pulumi_policy.proxy.</code><code class="sig-name descname">unknown_checking_proxy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">props</span><span class="p">:</span> <span class="n">Dict<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span></span></em><span class="sig-paren">)</span> &#x2192; Dict<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><a class="headerlink" href="#pulumi_policy.proxy.unknown_checking_proxy" title="Permalink to this definition"></a></dt>
<dd><p>Takes a set of resource inputs, and returns a wrapped version that
intercepts all property accesses to check if they are unknown, raising an <code class="docutils literal notranslate"><span class="pre">UnknownValueError</span></code> if
so. For example, if the resource inputs contains a reference to an IP address that can’t be known
until the resource has been initialized by the cloud provider, this value would be unknown during
<code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">preview</span></code>, and only filled in during the update.</p>
</dd></dl>

</section>
