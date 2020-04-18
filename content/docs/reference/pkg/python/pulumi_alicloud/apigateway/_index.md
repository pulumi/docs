---
title: Module apigateway
title_tag: Module apigateway | Package pulumi_alicloud | Python SDK
linktitle: apigateway
notitle: true
---

<div class="section" id="apigateway">
<h1>apigateway<a class="headerlink" href="#apigateway" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.apigateway"></span><dl class="class">
<dt id="pulumi_alicloud.apigateway.Api">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">Api</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_type=None</em>, <em class="sig-param">constant_parameters=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">fc_service_config=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">http_service_config=None</em>, <em class="sig-param">http_vpc_service_config=None</em>, <em class="sig-param">mock_service_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">request_config=None</em>, <em class="sig-param">request_parameters=None</em>, <em class="sig-param">service_type=None</em>, <em class="sig-param">stage_names=None</em>, <em class="sig-param">system_parameters=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.Api" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Api resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] auth_type: The authorization Type including APP and ANONYMOUS. Defaults to null.
:param pulumi.Input[list] constant_parameters: constant_parameters defines the constant parameters of the api.
:param pulumi.Input[str] description: The description of Constant parameter.
:param pulumi.Input[dict] fc_service_config: fc_service_config defines the config when service_type selected ‘FunctionCompute’.
:param pulumi.Input[str] group_id: The api gateway that the api belongs to. Defaults to null.
:param pulumi.Input[dict] http_service_config: http_service_config defines the config when service_type selected ‘HTTP’.
:param pulumi.Input[dict] http_vpc_service_config: http_vpc_service_config defines the config when service_type selected ‘HTTP-VPC’.
:param pulumi.Input[dict] mock_service_config: http_service_config defines the config when service_type selected ‘MOCK’.
:param pulumi.Input[str] name: System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a>
:param pulumi.Input[dict] request_config: Request_config defines how users can send requests to your API.
:param pulumi.Input[list] request_parameters: request_parameters defines the request parameters of the api.
:param pulumi.Input[str] service_type: The type of backend service. Type including HTTP,VPC and MOCK. Defaults to null.
:param pulumi.Input[list] stage_names: Stages that the api need to be deployed. Valid value: RELEASE | PRE | TEST.
:param pulumi.Input[list] system_parameters: system_parameters defines the system parameters of the api.</p>
<p>The <strong>constant_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of Constant parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">in</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter location; values: ‘HEAD’ and ‘QUERY’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Constant parameter value.</p></li>
</ul>
<p>The <strong>fc_service_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arnRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - RAM role arn attached to the Function Compute service. This governs both who / what can invoke your Function, as well as what resources our Function has access to. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/52885.htm">User Permissions</a> for more details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">function_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The function name of function compute service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region that the function compute service belongs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service name of function compute service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Backend service time-out time; unit: millisecond.</p></li>
</ul>
<p>The <strong>http_service_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The address of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">aoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The http method of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Backend service time-out time; unit: millisecond.</p></li>
</ul>
<p>The <strong>http_vpc_service_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The http method of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Backend service time-out time; unit: millisecond.</p></li>
</ul>
<p>The <strong>mock_service_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">result</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The result of the mock service.</p></li>
</ul>
<p>The <strong>request_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bodyFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The body format of the api, which support the values of ‘STREAM’ and ‘FORM’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The http method of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mode of the parameters between request parameters and service parameters, which support the values of ‘MAPPING’ and ‘PASSTHROUGH’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol of api which supports values of ‘HTTP’,’HTTPS’ or ‘HTTP,HTTPS’</p></li>
</ul>
<p>The <strong>request_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value of the parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of Constant parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">in</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter location; values: ‘HEAD’ and ‘QUERY’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inService</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Backend service’s parameter location; values: BODY, HEAD, QUERY, and PATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameService</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Backend service’s parameter name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter required or not; values: REQUIRED and OPTIONAL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter type which supports values of ‘STRING’,’INT’,’BOOLEAN’,’LONG’,”FLOAT” and “DOUBLE”</p></li>
</ul>
<p>The <strong>system_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">in</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter location; values: ‘HEAD’ and ‘QUERY’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameService</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Backend service’s parameter name.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.api_id">
<code class="sig-name descname">api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the api of api gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.auth_type">
<code class="sig-name descname">auth_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.auth_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorization Type including APP and ANONYMOUS. Defaults to null.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.constant_parameters">
<code class="sig-name descname">constant_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.constant_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>constant_parameters defines the constant parameters of the api.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of Constant parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">in</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - System parameter location; values: ‘HEAD’ and ‘QUERY’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Constant parameter value.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of Constant parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.fc_service_config">
<code class="sig-name descname">fc_service_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.fc_service_config" title="Permalink to this definition">¶</a></dt>
<dd><p>fc_service_config defines the config when service_type selected ‘FunctionCompute’.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arnRole</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - RAM role arn attached to the Function Compute service. This governs both who / what can invoke your Function, as well as what resources our Function has access to. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/52885.htm">User Permissions</a> for more details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">function_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The function name of function compute service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region that the function compute service belongs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service name of function compute service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Backend service time-out time; unit: millisecond.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The api gateway that the api belongs to. Defaults to null.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.http_service_config">
<code class="sig-name descname">http_service_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.http_service_config" title="Permalink to this definition">¶</a></dt>
<dd><p>http_service_config defines the config when service_type selected ‘HTTP’.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The address of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">aoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The http method of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Backend service time-out time; unit: millisecond.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.http_vpc_service_config">
<code class="sig-name descname">http_vpc_service_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.http_vpc_service_config" title="Permalink to this definition">¶</a></dt>
<dd><p>http_vpc_service_config defines the config when service_type selected ‘HTTP-VPC’.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The http method of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Backend service time-out time; unit: millisecond.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.mock_service_config">
<code class="sig-name descname">mock_service_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.mock_service_config" title="Permalink to this definition">¶</a></dt>
<dd><p>http_service_config defines the config when service_type selected ‘MOCK’.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">result</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The result of the mock service.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.name" title="Permalink to this definition">¶</a></dt>
<dd><p>System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.request_config">
<code class="sig-name descname">request_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.request_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Request_config defines how users can send requests to your API.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bodyFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The body format of the api, which support the values of ‘STREAM’ and ‘FORM’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The http method of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The mode of the parameters between request parameters and service parameters, which support the values of ‘MAPPING’ and ‘PASSTHROUGH’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The protocol of api which supports values of ‘HTTP’,’HTTPS’ or ‘HTTP,HTTPS’</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.request_parameters">
<code class="sig-name descname">request_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.request_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>request_parameters defines the request parameters of the api.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default value of the parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of Constant parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">in</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - System parameter location; values: ‘HEAD’ and ‘QUERY’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inService</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Backend service’s parameter location; values: BODY, HEAD, QUERY, and PATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameService</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Backend service’s parameter name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Parameter required or not; values: REQUIRED and OPTIONAL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Parameter type which supports values of ‘STRING’,’INT’,’BOOLEAN’,’LONG’,”FLOAT” and “DOUBLE”</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.service_type">
<code class="sig-name descname">service_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of backend service. Type including HTTP,VPC and MOCK. Defaults to null.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.stage_names">
<code class="sig-name descname">stage_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.stage_names" title="Permalink to this definition">¶</a></dt>
<dd><p>Stages that the api need to be deployed. Valid value: RELEASE | PRE | TEST.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Api.system_parameters">
<code class="sig-name descname">system_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.system_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>system_parameters defines the system parameters of the api.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">in</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - System parameter location; values: ‘HEAD’ and ‘QUERY’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameService</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Backend service’s parameter name.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.apigateway.Api.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">auth_type=None</em>, <em class="sig-param">constant_parameters=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">fc_service_config=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">http_service_config=None</em>, <em class="sig-param">http_vpc_service_config=None</em>, <em class="sig-param">mock_service_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">request_config=None</em>, <em class="sig-param">request_parameters=None</em>, <em class="sig-param">service_type=None</em>, <em class="sig-param">stage_names=None</em>, <em class="sig-param">system_parameters=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Api resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the api of api gateway.</p></li>
<li><p><strong>auth_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorization Type including APP and ANONYMOUS. Defaults to null.</p></li>
<li><p><strong>constant_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – constant_parameters defines the constant parameters of the api.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of Constant parameter.</p></li>
<li><p><strong>fc_service_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – fc_service_config defines the config when service_type selected ‘FunctionCompute’.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The api gateway that the api belongs to. Defaults to null.</p></li>
<li><p><strong>http_service_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – http_service_config defines the config when service_type selected ‘HTTP’.</p></li>
<li><p><strong>http_vpc_service_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – http_vpc_service_config defines the config when service_type selected ‘HTTP-VPC’.</p></li>
<li><p><strong>mock_service_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – http_service_config defines the config when service_type selected ‘MOCK’.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p>
</p></li>
<li><p><strong>request_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Request_config defines how users can send requests to your API.</p></li>
<li><p><strong>request_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – request_parameters defines the request parameters of the api.</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of backend service. Type including HTTP,VPC and MOCK. Defaults to null.</p></li>
<li><p><strong>stage_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Stages that the api need to be deployed. Valid value: RELEASE | PRE | TEST.</p></li>
<li><p><strong>system_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – system_parameters defines the system parameters of the api.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>constant_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of Constant parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">in</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter location; values: ‘HEAD’ and ‘QUERY’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Constant parameter value.</p></li>
</ul>
<p>The <strong>fc_service_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arnRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - RAM role arn attached to the Function Compute service. This governs both who / what can invoke your Function, as well as what resources our Function has access to. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/52885.htm">User Permissions</a> for more details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">function_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The function name of function compute service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region that the function compute service belongs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service name of function compute service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Backend service time-out time; unit: millisecond.</p></li>
</ul>
<p>The <strong>http_service_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The address of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">aoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The http method of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Backend service time-out time; unit: millisecond.</p></li>
</ul>
<p>The <strong>http_vpc_service_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The http method of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Backend service time-out time; unit: millisecond.</p></li>
</ul>
<p>The <strong>mock_service_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">result</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The result of the mock service.</p></li>
</ul>
<p>The <strong>request_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bodyFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The body format of the api, which support the values of ‘STREAM’ and ‘FORM’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The http method of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mode of the parameters between request parameters and service parameters, which support the values of ‘MAPPING’ and ‘PASSTHROUGH’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol of api which supports values of ‘HTTP’,’HTTPS’ or ‘HTTP,HTTPS’</p></li>
</ul>
<p>The <strong>request_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value of the parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of Constant parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">in</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter location; values: ‘HEAD’ and ‘QUERY’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inService</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Backend service’s parameter location; values: BODY, HEAD, QUERY, and PATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameService</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Backend service’s parameter name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter required or not; values: REQUIRED and OPTIONAL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter type which supports values of ‘STRING’,’INT’,’BOOLEAN’,’LONG’,”FLOAT” and “DOUBLE”</p></li>
</ul>
<p>The <strong>system_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">in</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter location; values: ‘HEAD’ and ‘QUERY’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System parameter name which supports values including in <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/43677.html">system parameter list</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameService</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Backend service’s parameter name.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.apigateway.Api.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.apigateway.Api.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.Api.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_alicloud.apigateway.App">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">App</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.App" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a App resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: The description of the app. Defaults to null.
:param pulumi.Input[str] name: The name of the app. 
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.App.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.App.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the app. Defaults to null.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.App.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.App.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.App.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.App.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.apigateway.App.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.App.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing App resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the app. Defaults to null.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the app.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.apigateway.App.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.App.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.apigateway.App.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.App.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_alicloud.apigateway.AppAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">AppAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">stage_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.AppAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AppAttachment resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] api_id: The api_id that app apply to access.
:param pulumi.Input[str] app_id: The app that apply to the authorization.
:param pulumi.Input[str] group_id: The group that the api belongs to.
:param pulumi.Input[str] stage_name: Stage that the app apply to access.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.AppAttachment.api_id">
<code class="sig-name descname">api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.AppAttachment.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The api_id that app apply to access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.AppAttachment.app_id">
<code class="sig-name descname">app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.AppAttachment.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The app that apply to the authorization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.AppAttachment.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.AppAttachment.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The group that the api belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.AppAttachment.stage_name">
<code class="sig-name descname">stage_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.AppAttachment.stage_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Stage that the app apply to access.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.apigateway.AppAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">stage_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.AppAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AppAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The api_id that app apply to access.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The app that apply to the authorization.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group that the api belongs to.</p></li>
<li><p><strong>stage_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Stage that the app apply to access.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.apigateway.AppAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.AppAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.apigateway.AppAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.AppAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_alicloud.apigateway.AwaitableGetApisResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">AwaitableGetApisResult</code><span class="sig-paren">(</span><em class="sig-param">api_id=None</em>, <em class="sig-param">apis=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.AwaitableGetApisResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.apigateway.AwaitableGetAppsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">AwaitableGetAppsResult</code><span class="sig-paren">(</span><em class="sig-param">apps=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.AwaitableGetAppsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.apigateway.AwaitableGetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">AwaitableGetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param">groups=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.AwaitableGetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.apigateway.GetApisResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">GetApisResult</code><span class="sig-paren">(</span><em class="sig-param">api_id=None</em>, <em class="sig-param">apis=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.GetApisResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApis.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.GetApisResult.apis">
<code class="sig-name descname">apis</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.GetApisResult.apis" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of apis. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.GetApisResult.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.GetApisResult.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The group id that the apis belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.GetApisResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.GetApisResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.GetApisResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.GetApisResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of api IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.GetApisResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.GetApisResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of api names.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.apigateway.GetAppsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">GetAppsResult</code><span class="sig-paren">(</span><em class="sig-param">apps=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.GetAppsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApps.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.GetAppsResult.apps">
<code class="sig-name descname">apps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.GetAppsResult.apps" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of apps. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.GetAppsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.GetAppsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.GetAppsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.GetAppsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of app IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.GetAppsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.GetAppsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of app names.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.apigateway.GetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">GetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param">groups=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.GetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroups.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.GetGroupsResult.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.GetGroupsResult.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of api groups. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.GetGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.GetGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.GetGroupsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.GetGroupsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of api group IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.GetGroupsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.GetGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of api group names.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.apigateway.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Group resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: The description of the api gateway group. Defaults to null.
:param pulumi.Input[str] name: The name of the api gateway group. Defaults to null.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Group.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the api gateway group. Defaults to null.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Group.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the api gateway group. Defaults to null.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Group.sub_domain">
<code class="sig-name descname">sub_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Group.sub_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>(Available in 1.69.0+)      Second-level domain name automatically assigned to the API group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.Group.vpc_domain">
<code class="sig-name descname">vpc_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.Group.vpc_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>(Available in 1.69.0+)      Second-level VPC domain name automatically assigned to the API group.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.apigateway.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">sub_domain=None</em>, <em class="sig-param">vpc_domain=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the api gateway group. Defaults to null.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the api gateway group. Defaults to null.</p></li>
<li><p><strong>sub_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Available in 1.69.0+)     Second-level domain name automatically assigned to the API group.</p></li>
<li><p><strong>vpc_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Available in 1.69.0+)     Second-level VPC domain name automatically assigned to the API group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.apigateway.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.apigateway.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_alicloud.apigateway.VpcAccess">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">VpcAccess</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.VpcAccess" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VpcAccess resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] instance_id: ID of the instance in VPC (ECS/Server Load Balance).
:param pulumi.Input[str] name: The name of the vpc authorization. 
:param pulumi.Input[float] port: ID of the port corresponding to the instance.
:param pulumi.Input[str] vpc_id: The vpc id of the vpc authorization.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.VpcAccess.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.VpcAccess.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the instance in VPC (ECS/Server Load Balance).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.VpcAccess.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.VpcAccess.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the vpc authorization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.VpcAccess.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.VpcAccess.port" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the port corresponding to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.apigateway.VpcAccess.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.apigateway.VpcAccess.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The vpc id of the vpc authorization.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.apigateway.VpcAccess.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.VpcAccess.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VpcAccess resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the instance in VPC (ECS/Server Load Balance).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vpc authorization.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the port corresponding to the instance.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vpc id of the vpc authorization.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.apigateway.VpcAccess.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.VpcAccess.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.apigateway.VpcAccess.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.VpcAccess.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_alicloud.apigateway.get_apis">
<code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">get_apis</code><span class="sig-paren">(</span><em class="sig-param">api_id=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.get_apis" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the apis of the current Alibaba Cloud user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>api_id</strong> (<em>str</em>) – (It has been deprecated from version 1.52.2, and use field ‘ids’ to replace.) ID of the specified API.</p></li>
<li><p><strong>group_id</strong> (<em>str</em>) – ID of the specified group.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of api IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter api gateway apis by name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.apigateway.get_apps">
<code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">get_apps</code><span class="sig-paren">(</span><em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.get_apps" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the apps of the current Alibaba Cloud user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of app IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter apps by name.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.apigateway.get_groups">
<code class="sig-prename descclassname">pulumi_alicloud.apigateway.</code><code class="sig-name descname">get_groups</code><span class="sig-paren">(</span><em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.apigateway.get_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the api groups of the current Alibaba Cloud user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of api group IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter api gateway groups by name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
