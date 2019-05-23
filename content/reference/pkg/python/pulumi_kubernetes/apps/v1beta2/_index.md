<div class="section" id="module-pulumi_kubernetes.apps.v1beta2">
<span id="v1beta2"></span><h1>v1beta2<a class="headerlink" href="#module-pulumi_kubernetes.apps.v1beta2" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_kubernetes.apps.v1beta2.ControllerRevision">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.apps.v1beta2.</code><code class="descname">ControllerRevision</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>data=None</em>, <em>metadata=None</em>, <em>revision=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.ControllerRevision" title="Permalink to this definition">¶</a></dt>
<dd><p>DEPRECATED - This group version of ControllerRevision is deprecated by
apps/v1/ControllerRevision. See the release notes for more information. ControllerRevision
implements an immutable snapshot of state data. Clients are responsible for serializing and
deserializing the objects that contain their internal state. Once a ControllerRevision has been
successfully created, it can not be updated. The API Server will fail validation of all requests
that attempt to mutate the Data field. ControllerRevisions may, however, be deleted. Note that,
due to its use by both the DaemonSet and StatefulSet controllers for update and rollback, this
object is beta. However, it may be subject to name and representation changes in future
releases, and clients should not depend on its stability. It is primarily for internal use by
controllers.</p>
<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta2.ControllerRevision.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.ControllerRevision.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta2.ControllerRevision.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.ControllerRevision.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_kubernetes.apps.v1beta2.ControllerRevisionList">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.apps.v1beta2.</code><code class="descname">ControllerRevisionList</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>items=None</em>, <em>metadata=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.ControllerRevisionList" title="Permalink to this definition">¶</a></dt>
<dd><p>ControllerRevisionList is a resource containing a list of ControllerRevision objects.</p>
<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta2.ControllerRevisionList.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.ControllerRevisionList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta2.ControllerRevisionList.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.ControllerRevisionList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_kubernetes.apps.v1beta2.DaemonSet">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.apps.v1beta2.</code><code class="descname">DaemonSet</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>metadata=None</em>, <em>spec=None</em>, <em>status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.DaemonSet" title="Permalink to this definition">¶</a></dt>
<dd><p>DEPRECATED - This group version of DaemonSet is deprecated by apps/v1/DaemonSet. See the release
notes for more information. DaemonSet represents the configuration of a daemon set.</p>
<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta2.DaemonSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.DaemonSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta2.DaemonSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.DaemonSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_kubernetes.apps.v1beta2.DaemonSetList">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.apps.v1beta2.</code><code class="descname">DaemonSetList</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>items=None</em>, <em>metadata=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.DaemonSetList" title="Permalink to this definition">¶</a></dt>
<dd><p>DaemonSetList is a collection of daemon sets.</p>
<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta2.DaemonSetList.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.DaemonSetList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta2.DaemonSetList.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.DaemonSetList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_kubernetes.apps.v1beta2.Deployment">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.apps.v1beta2.</code><code class="descname">Deployment</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>metadata=None</em>, <em>spec=None</em>, <em>status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.Deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>DEPRECATED - This group version of Deployment is deprecated by apps/v1/Deployment. See the
release notes for more information. Deployment enables declarative updates for Pods and
ReplicaSets.</p>
<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta2.Deployment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.Deployment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta2.Deployment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.Deployment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_kubernetes.apps.v1beta2.DeploymentList">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.apps.v1beta2.</code><code class="descname">DeploymentList</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>items=None</em>, <em>metadata=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.DeploymentList" title="Permalink to this definition">¶</a></dt>
<dd><p>DeploymentList is a list of Deployments.</p>
<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta2.DeploymentList.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.DeploymentList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta2.DeploymentList.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.DeploymentList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_kubernetes.apps.v1beta2.ReplicaSet">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.apps.v1beta2.</code><code class="descname">ReplicaSet</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>metadata=None</em>, <em>spec=None</em>, <em>status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.ReplicaSet" title="Permalink to this definition">¶</a></dt>
<dd><p>DEPRECATED - This group version of ReplicaSet is deprecated by apps/v1/ReplicaSet. See the
release notes for more information. ReplicaSet ensures that a specified number of pod replicas
are running at any given time.</p>
<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta2.ReplicaSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.ReplicaSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta2.ReplicaSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.ReplicaSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_kubernetes.apps.v1beta2.ReplicaSetList">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.apps.v1beta2.</code><code class="descname">ReplicaSetList</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>items=None</em>, <em>metadata=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.ReplicaSetList" title="Permalink to this definition">¶</a></dt>
<dd><p>ReplicaSetList is a collection of ReplicaSets.</p>
<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta2.ReplicaSetList.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.ReplicaSetList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta2.ReplicaSetList.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.ReplicaSetList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_kubernetes.apps.v1beta2.StatefulSet">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.apps.v1beta2.</code><code class="descname">StatefulSet</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>metadata=None</em>, <em>spec=None</em>, <em>status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.StatefulSet" title="Permalink to this definition">¶</a></dt>
<dd><p>DEPRECATED - This group version of StatefulSet is deprecated by apps/v1/StatefulSet. See the
release notes for more information. StatefulSet represents a set of pods with consistent
identities. Identities are defined as:</p>
<ul class="simple">
<li>Network: A single stable DNS and hostname.</li>
<li>Storage: As many VolumeClaims as requested.
The StatefulSet guarantees that a given network identity will always map to the same storage
identity.</li>
</ul>
<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta2.StatefulSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.StatefulSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta2.StatefulSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.StatefulSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_kubernetes.apps.v1beta2.StatefulSetList">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.apps.v1beta2.</code><code class="descname">StatefulSetList</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>items=None</em>, <em>metadata=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.StatefulSetList" title="Permalink to this definition">¶</a></dt>
<dd><p>StatefulSetList is a collection of StatefulSets.</p>
<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta2.StatefulSetList.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.StatefulSetList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta2.StatefulSetList.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta2.StatefulSetList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
