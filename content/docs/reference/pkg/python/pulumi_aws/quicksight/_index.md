---
title: Module quicksight
title_tag: Module quicksight | Package pulumi_aws | Python SDK
linktitle: quicksight
notitle: true
---

<div class="section" id="quicksight">
<h1>quicksight<a class="headerlink" href="#quicksight" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.quicksight"></span><dl class="py class">
<dt id="pulumi_aws.quicksight.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.quicksight.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource for managing QuickSight Group</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the group.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the group.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace. Currently, you should set this to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.quicksight.Group.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of group</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.quicksight.Group.aws_account_id">
<code class="sig-name descname">aws_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.aws_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.quicksight.Group.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.quicksight.Group.group_name">
<code class="sig-name descname">group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.quicksight.Group.namespace">
<code class="sig-name descname">namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace. Currently, you should set this to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.quicksight.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of group</p></li>
<li><p><strong>aws_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the group.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the group.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace. Currently, you should set this to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.quicksight.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.quicksight.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.quicksight.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.quicksight.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource for managing QuickSight User</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user that you want to register.</p></li>
<li><p><strong>iam_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM user or role that you are registering with Amazon QuickSight.</p></li>
<li><p><strong>identity_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon QuickSight supports several ways of managing the identity of users. This parameter accepts either  <code class="docutils literal notranslate"><span class="pre">IAM</span></code> or <code class="docutils literal notranslate"><span class="pre">QUICKSIGHT</span></code>.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace. Currently, you should set this to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
<li><p><strong>session_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IAM session to use when assuming roles that can embed QuickSight dashboards.</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon QuickSight user name that you want to create for the user you are registering.</p></li>
<li><p><strong>user_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon QuickSight role of the user. The user role can be one of the following: <code class="docutils literal notranslate"><span class="pre">READER</span></code>, <code class="docutils literal notranslate"><span class="pre">AUTHOR</span></code>, or <code class="docutils literal notranslate"><span class="pre">ADMIN</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.quicksight.User.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.User.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the user</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.quicksight.User.aws_account_id">
<code class="sig-name descname">aws_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.User.aws_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.quicksight.User.email">
<code class="sig-name descname">email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address of the user that you want to register.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.quicksight.User.iam_arn">
<code class="sig-name descname">iam_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.User.iam_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM user or role that you are registering with Amazon QuickSight.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.quicksight.User.identity_type">
<code class="sig-name descname">identity_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.User.identity_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon QuickSight supports several ways of managing the identity of users. This parameter accepts either  <code class="docutils literal notranslate"><span class="pre">IAM</span></code> or <code class="docutils literal notranslate"><span class="pre">QUICKSIGHT</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.quicksight.User.namespace">
<code class="sig-name descname">namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.User.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace. Currently, you should set this to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.quicksight.User.session_name">
<code class="sig-name descname">session_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.User.session_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IAM session to use when assuming roles that can embed QuickSight dashboards.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.quicksight.User.user_name">
<code class="sig-name descname">user_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.User.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon QuickSight user name that you want to create for the user you are registering.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.quicksight.User.user_role">
<code class="sig-name descname">user_role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.User.user_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon QuickSight role of the user. The user role can be one of the following: <code class="docutils literal notranslate"><span class="pre">READER</span></code>, <code class="docutils literal notranslate"><span class="pre">AUTHOR</span></code>, or <code class="docutils literal notranslate"><span class="pre">ADMIN</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.quicksight.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the user</p></li>
<li><p><strong>aws_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user that you want to register.</p></li>
<li><p><strong>iam_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM user or role that you are registering with Amazon QuickSight.</p></li>
<li><p><strong>identity_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon QuickSight supports several ways of managing the identity of users. This parameter accepts either  <code class="docutils literal notranslate"><span class="pre">IAM</span></code> or <code class="docutils literal notranslate"><span class="pre">QUICKSIGHT</span></code>.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace. Currently, you should set this to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
<li><p><strong>session_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IAM session to use when assuming roles that can embed QuickSight dashboards.</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon QuickSight user name that you want to create for the user you are registering.</p></li>
<li><p><strong>user_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon QuickSight role of the user. The user role can be one of the following: <code class="docutils literal notranslate"><span class="pre">READER</span></code>, <code class="docutils literal notranslate"><span class="pre">AUTHOR</span></code>, or <code class="docutils literal notranslate"><span class="pre">ADMIN</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.quicksight.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.quicksight.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
