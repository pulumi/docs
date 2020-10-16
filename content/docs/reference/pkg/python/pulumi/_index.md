---
title: Package pulumi
title_tag: Package pulumi | Python SDK
linktitle: pulumi
notitle: true
---

{{< resource-docs-alert "pulumi" >}}

<div class="section" id="pulumi-python-sdk">
<h1>Pulumi Python SDK<a class="headerlink" href="#pulumi-python-sdk" title="Permalink to this headline">¶</a></h1>
<p>The Pulumi Python SDK (<cite>pulumi</cite>) is the core package used when writing Pulumi programs in Python. It contains everything
that you’ll need in order to interact with Pulumi resource providers and express infrastructure using Python code.
Pulumi resource providers all depend on this library and express their resources in terms of the types defined in this
module.</p>
<blockquote class="epigraph">
<div><p><strong>Note</strong>: The Pulumi Python SDK requires Python version 3.6 or greater. Please see the
<a class="reference external" href="/docs/reference/python/#getting-started">Python getting started</a> documentation for details on how to get started with
Python.</p>
</div></blockquote>
<div class="section" id="the-pulumi-python-resource-model">
<h2>The Pulumi Python Resource Model<a class="headerlink" href="#the-pulumi-python-resource-model" title="Permalink to this headline">¶</a></h2>
<p>Like most languages usable with Pulumi, Pulumi represents cloud resources as classes and Python programs can instantiate
those classes. All classes that can be instantiated to produce actual resources derive from the <cite>pulumi.Resource</cite> class.</p>
<p>A class that derives from <cite>pulumi.Resource</cite> will, when instantiated, communicate with the Pulumi Engine and record that
a piece of infrastructure that the instantiated class represents should be provisioned. All resources whose provisioning
is implemented in a resource provider derive from the <cite>pulumi.CustomResource</cite> class.</p>
<p>It is also possible to write your own resources, written in Python, that are themselves composed of custom resources.
Resources written in Python are called “component resources” and they are written by deriving from the
<cite>pulumi.ComponentResource</cite> class.</p>
<p>Finally, Pulumi allows for resource providers to directly project themselves into Python, so that provider instances
can be instantiated and used to create other resources. These “provider resources” derive from the
<cite>pulumi.ProviderResource</cite> class.</p>
</div>
<div class="section" id="configuration-and-metadata">
<h2>Configuration and Metadata<a class="headerlink" href="#configuration-and-metadata" title="Permalink to this headline">¶</a></h2>
<p>Pulumi programs can receive configuration that is specified by the command-line using <cite>pulumi config</cite>. This
configuration information can be retrieved at runtime using the <cite>pulumi.Config</cite> class:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="c1"># After running `pulumi config set myconfig 42`</span>

<span class="n">conf</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">conf</span><span class="o">.</span><span class="n">get_int</span><span class="p">(</span><span class="s2">&quot;myconfig&quot;</span><span class="p">))</span> <span class="c1"># prints 42</span>
</pre></div>
</div>
<p>Pulumi programs also have the ability to query the current project and stack, as well as whether or not the current run
of the program is a preview or not.</p>
</div>
<div class="section" id="outputs-and-inputs">
<h2>Outputs and Inputs<a class="headerlink" href="#outputs-and-inputs" title="Permalink to this headline">¶</a></h2>
<p>Like other languages in the Pulumi ecosystem, all Resources in Python have two kinds of properties: <em>inputs</em> and
<em>outputs</em>. Inputs are specified as arguments to resource constructors, to be used as inputs to the resource itself.
Outputs are <em>returned</em> as properties on the instantiated resource object. Outputs are similar to futures in that they
are resolved asynchronously, but they also contain information about the dependency graph of resources within your
program.</p>
<p>Pulumi does not offer direct access to the values contained within Outputs. Instead, you must use the <cite>apply</cite> function
on the Output class in order to observe the value of an output. See
<a class="reference external" href="/docs/intro/concepts/programming-model/#outputs">the documentation</a> for more details on this part of the Pulumi programming model.</p>
</div>
<div class="section" id="logging">
<h2>Logging<a class="headerlink" href="#logging" title="Permalink to this headline">¶</a></h2>
<p>The Pulumi SDK contains a few helper functions for logging to the console. Messages logged using these functions are
sent directly to the Pulumi Engine and rendered with the rest of the CLI output.</p>
</div>
<div class="section" id="stack-exports">
<h2>Stack Exports<a class="headerlink" href="#stack-exports" title="Permalink to this headline">¶</a></h2>
<p>Python programs can export values. Exported values are attached to the program’s Stack resource and accessed using the
<cite>pulumi stack output</cite> CLI command:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>

<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;the-answer&quot;</span><span class="p">,</span> <span class="mi">42</span><span class="p">)</span>

<span class="c1"># pulumi stack export:</span>
<span class="c1"># Current stack outputs (1):</span>
<span class="c1"># OUTPUT      VALUE</span>
<span class="c1"># the-answer  42</span>
</pre></div>
</div>
</div>
</div>
