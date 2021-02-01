---
title: Package pulumi_auth0
title_tag: Package pulumi_auth0 | Python SDK
linktitle: pulumi_auth0
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "auth0" >}}

<div class="section" id="pulumi-auth0">
<h1>Pulumi Auth0<a class="headerlink" href="#pulumi-auth0" title="Permalink to this headline"></a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-auth0">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-auth0/issues">pulumi/pulumi-auth0 repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-auth0/issues">terraform-providers/terraform-provider-auth0 repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_auth0"></span><dl class="py class">
<dt id="pulumi_auth0.Client">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Client</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ClientAddonsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ClientAddonsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_logout_urls</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_origins</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">callbacks</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_metadata</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret_rotation_trigger</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_auth</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_loc</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_on</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_preview</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">form_template</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grant_types</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initiate_login_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_first_party</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_token_endpoint_ip_header_trusted</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_configuration</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ClientJwtConfigurationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ClientJwtConfigurationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ClientMobileArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ClientMobileArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_conformant</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_token</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ClientRefreshTokenArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ClientRefreshTokenArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_endpoint_auth_method</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_origins</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Client" title="Permalink to this definition"></a></dt>
<dd><p>With this resource, you can set up applications that use Auth0 for authentication and configure allowed callback URLs and secrets for these applications. Depending on your plan, you may also configure add-ons to allow your application to call another application’s API (such as Firebase and AWS) on behalf of an authenticated user.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_client</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;myClient&quot;</span><span class="p">,</span>
    <span class="n">addons</span><span class="o">=</span><span class="n">auth0</span><span class="o">.</span><span class="n">ClientAddonsArgs</span><span class="p">(</span>
        <span class="n">firebase</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">&quot;clientEmail&quot;</span><span class="p">:</span> <span class="s2">&quot;john.doe@example.com&quot;</span><span class="p">,</span>
            <span class="s2">&quot;lifetimeInSeconds&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
            <span class="s2">&quot;privateKey&quot;</span><span class="p">:</span> <span class="s2">&quot;wer&quot;</span><span class="p">,</span>
            <span class="s2">&quot;privateKeyId&quot;</span><span class="p">:</span> <span class="s2">&quot;qwreerwerwe&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="n">samlp</span><span class="o">=</span><span class="n">auth0</span><span class="o">.</span><span class="n">ClientAddonsSamlpArgs</span><span class="p">(</span>
            <span class="n">audience</span><span class="o">=</span><span class="s2">&quot;https://example.com/saml&quot;</span><span class="p">,</span>
            <span class="n">create_upn_claim</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="n">map_identities</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="n">map_unknown_claims_as_is</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="n">mappings</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;email&quot;</span><span class="p">:</span> <span class="s2">&quot;http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress&quot;</span><span class="p">,</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="n">name_identifier_format</span><span class="o">=</span><span class="s2">&quot;urn:oasis:names:tc:SAML:2.0:nameid-format:persistent&quot;</span><span class="p">,</span>
            <span class="n">name_identifier_probes</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress&quot;</span><span class="p">],</span>
            <span class="n">passthrough_claims_with_no_mapping</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">),</span>
    <span class="n">allowed_logout_urls</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;https://example.com&quot;</span><span class="p">],</span>
    <span class="n">allowed_origins</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;https://example.com&quot;</span><span class="p">],</span>
    <span class="n">app_type</span><span class="o">=</span><span class="s2">&quot;non_interactive&quot;</span><span class="p">,</span>
    <span class="n">callbacks</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;https://example.com/callback&quot;</span><span class="p">],</span>
    <span class="n">client_metadata</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;zoo&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">custom_login_page_on</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Test Applications Long Description&quot;</span><span class="p">,</span>
    <span class="n">grant_types</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;authorization_code&quot;</span><span class="p">,</span>
        <span class="s2">&quot;http://auth0.com/oauth/grant-type/password-realm&quot;</span><span class="p">,</span>
        <span class="s2">&quot;implicit&quot;</span><span class="p">,</span>
        <span class="s2">&quot;password&quot;</span><span class="p">,</span>
        <span class="s2">&quot;refresh_token&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">is_first_party</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">is_token_endpoint_ip_header_trusted</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">jwt_configuration</span><span class="o">=</span><span class="n">auth0</span><span class="o">.</span><span class="n">ClientJwtConfigurationArgs</span><span class="p">(</span>
        <span class="n">alg</span><span class="o">=</span><span class="s2">&quot;RS256&quot;</span><span class="p">,</span>
        <span class="n">lifetime_in_seconds</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span>
        <span class="n">scopes</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="n">secret_encoded</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">mobile</span><span class="o">=</span><span class="n">auth0</span><span class="o">.</span><span class="n">ClientMobileArgs</span><span class="p">(</span>
        <span class="n">ios</span><span class="o">=</span><span class="n">auth0</span><span class="o">.</span><span class="n">ClientMobileIosArgs</span><span class="p">(</span>
            <span class="n">app_bundle_identifier</span><span class="o">=</span><span class="s2">&quot;com.my.bundle.id&quot;</span><span class="p">,</span>
            <span class="n">team_id</span><span class="o">=</span><span class="s2">&quot;9JA89QQLNQ&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">),</span>
    <span class="n">oidc_conformant</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">token_endpoint_auth_method</span><span class="o">=</span><span class="s2">&quot;client_secret_post&quot;</span><span class="p">,</span>
    <span class="n">web_origins</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;https://example.com&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>addons</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ClientAddonsArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for add-ons for this client. For details, see Add-ons.</p></li>
<li><p><strong>allowed_logout_urls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). URLs that Auth0 may redirect to after logout.</p></li>
<li><p><strong>allowed_origins</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). URLs that represent valid origins for cross-origin resource sharing. By default, all your callback URLs will be allowed.</p></li>
<li><p><strong>app_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Type of application the client represents. Options include <code class="docutils literal notranslate"><span class="pre">native</span></code>, <code class="docutils literal notranslate"><span class="pre">spa</span></code>, <code class="docutils literal notranslate"><span class="pre">regular_web</span></code>, <code class="docutils literal notranslate"><span class="pre">non_interactive</span></code>, <code class="docutils literal notranslate"><span class="pre">rms</span></code>, <code class="docutils literal notranslate"><span class="pre">box</span></code>, <code class="docutils literal notranslate"><span class="pre">cloudbees</span></code>, <code class="docutils literal notranslate"><span class="pre">concur</span></code>, <code class="docutils literal notranslate"><span class="pre">dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">mscrm</span></code>, <code class="docutils literal notranslate"><span class="pre">echosign</span></code>, <code class="docutils literal notranslate"><span class="pre">egnyte</span></code>, <code class="docutils literal notranslate"><span class="pre">newrelic</span></code>, <code class="docutils literal notranslate"><span class="pre">office365</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce</span></code>, <code class="docutils literal notranslate"><span class="pre">sentry</span></code>, <code class="docutils literal notranslate"><span class="pre">sharepoint</span></code>, <code class="docutils literal notranslate"><span class="pre">slack</span></code>, <code class="docutils literal notranslate"><span class="pre">springcm</span></code>, <code class="docutils literal notranslate"><span class="pre">zendesk</span></code>, <code class="docutils literal notranslate"><span class="pre">zoom</span></code>.</p></li>
<li><p><strong>callbacks</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). URLs that Auth0 may call back to after a user authenticates for the client. Make sure to specify the protocol (<a class="reference external" href="https://">https://</a>) otherwise the callback may fail in some cases. With the exception of custom URI schemes for native clients, all callbacks should use protocol <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>client_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Map(String)</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>client_secret_rotation_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Map.</p></li>
<li><p><strong>cross_origin_auth</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the client can be used to make cross-origin authentication requests.</p></li>
<li><p><strong>cross_origin_loc</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. URL for the location on your site where the cross-origin verification takes place for the cross-origin auth flow. Used when performing auth in your own domain instead of through the Auth0-hosted login page.</p></li>
<li><p><strong>custom_login_page</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Content of the custom login page.</p></li>
<li><p><strong>custom_login_page_on</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not a custom login page is to be used.</p></li>
<li><p><strong>custom_login_page_preview</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, (Max length = 140 characters). Description of the purpose of the client.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>encryption_key</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Map(String).</p></li>
<li><p><strong>form_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Form template for WS-Federation protocol.</p></li>
<li><p><strong>grant_types</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). Types of grants that this client is authorized to use.</p></li>
<li><p><strong>is_first_party</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not this client is a first-party client.</p></li>
<li><p><strong>is_token_endpoint_ip_header_trusted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the token endpoint IP header is trusted.</p></li>
<li><p><strong>jwt_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ClientJwtConfigurationArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for the JWTs issued for this client. For details, see JWT Configuration.</p></li>
<li><p><strong>logo_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. URL of the logo for the client. Recommended size is 150px x 150px. If none is set, the default badge for the application type will be shown.</p></li>
<li><p><strong>mobile</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ClientMobileArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for mobile native applications. For details, see Mobile.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the client.</p></li>
<li><p><strong>oidc_conformant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not this client will conform to strict OIDC specifications.</p></li>
<li><p><strong>sso</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the client should use Auth0 rather than the IdP to perform Single Sign-On (SSO). True = Use Auth0.</p></li>
<li><p><strong>sso_disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not SSO is disabled.</p></li>
<li><p><strong>token_endpoint_auth_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Defines the requested authentication method for the token endpoint. Options include <code class="docutils literal notranslate"><span class="pre">none</span></code> (public client without a client secret), <code class="docutils literal notranslate"><span class="pre">client_secret_post</span></code> (client uses HTTP POST parameters), <code class="docutils literal notranslate"><span class="pre">client_secret_basic</span></code> (client uses HTTP Basic).</p></li>
<li><p><strong>web_origins</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). URLs that represent valid web origins for use with web message response mode.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.Client.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ClientAddonsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ClientAddonsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_logout_urls</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_origins</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">callbacks</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_metadata</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret_rotation_trigger</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_auth</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_loc</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_on</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_preview</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">form_template</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grant_types</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initiate_login_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_first_party</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_token_endpoint_ip_header_trusted</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_configuration</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ClientJwtConfigurationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ClientJwtConfigurationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ClientMobileArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ClientMobileArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_conformant</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_token</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ClientRefreshTokenArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ClientRefreshTokenArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_endpoint_auth_method</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_origins</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.Client" title="pulumi_auth0.Client">Client</a><a class="headerlink" href="#pulumi_auth0.Client.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Client resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>addons</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ClientAddonsArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for add-ons for this client. For details, see Add-ons.</p></li>
<li><p><strong>allowed_logout_urls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). URLs that Auth0 may redirect to after logout.</p></li>
<li><p><strong>allowed_origins</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). URLs that represent valid origins for cross-origin resource sharing. By default, all your callback URLs will be allowed.</p></li>
<li><p><strong>app_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Type of application the client represents. Options include <code class="docutils literal notranslate"><span class="pre">native</span></code>, <code class="docutils literal notranslate"><span class="pre">spa</span></code>, <code class="docutils literal notranslate"><span class="pre">regular_web</span></code>, <code class="docutils literal notranslate"><span class="pre">non_interactive</span></code>, <code class="docutils literal notranslate"><span class="pre">rms</span></code>, <code class="docutils literal notranslate"><span class="pre">box</span></code>, <code class="docutils literal notranslate"><span class="pre">cloudbees</span></code>, <code class="docutils literal notranslate"><span class="pre">concur</span></code>, <code class="docutils literal notranslate"><span class="pre">dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">mscrm</span></code>, <code class="docutils literal notranslate"><span class="pre">echosign</span></code>, <code class="docutils literal notranslate"><span class="pre">egnyte</span></code>, <code class="docutils literal notranslate"><span class="pre">newrelic</span></code>, <code class="docutils literal notranslate"><span class="pre">office365</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce</span></code>, <code class="docutils literal notranslate"><span class="pre">sentry</span></code>, <code class="docutils literal notranslate"><span class="pre">sharepoint</span></code>, <code class="docutils literal notranslate"><span class="pre">slack</span></code>, <code class="docutils literal notranslate"><span class="pre">springcm</span></code>, <code class="docutils literal notranslate"><span class="pre">zendesk</span></code>, <code class="docutils literal notranslate"><span class="pre">zoom</span></code>.</p></li>
<li><p><strong>callbacks</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). URLs that Auth0 may call back to after a user authenticates for the client. Make sure to specify the protocol (<a class="reference external" href="https://">https://</a>) otherwise the callback may fail in some cases. With the exception of custom URI schemes for native clients, all callbacks should use protocol <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. ID of the client.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>client_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Map(String)</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Secret for the client; keep this private.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>client_secret_rotation_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Map.</p></li>
<li><p><strong>cross_origin_auth</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the client can be used to make cross-origin authentication requests.</p></li>
<li><p><strong>cross_origin_loc</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. URL for the location on your site where the cross-origin verification takes place for the cross-origin auth flow. Used when performing auth in your own domain instead of through the Auth0-hosted login page.</p></li>
<li><p><strong>custom_login_page</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Content of the custom login page.</p></li>
<li><p><strong>custom_login_page_on</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not a custom login page is to be used.</p></li>
<li><p><strong>custom_login_page_preview</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, (Max length = 140 characters). Description of the purpose of the client.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>encryption_key</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Map(String).</p></li>
<li><p><strong>form_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Form template for WS-Federation protocol.</p></li>
<li><p><strong>grant_types</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). Types of grants that this client is authorized to use.</p></li>
<li><p><strong>is_first_party</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not this client is a first-party client.</p></li>
<li><p><strong>is_token_endpoint_ip_header_trusted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the token endpoint IP header is trusted.</p></li>
<li><p><strong>jwt_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ClientJwtConfigurationArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for the JWTs issued for this client. For details, see JWT Configuration.</p></li>
<li><p><strong>logo_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. URL of the logo for the client. Recommended size is 150px x 150px. If none is set, the default badge for the application type will be shown.</p></li>
<li><p><strong>mobile</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ClientMobileArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for mobile native applications. For details, see Mobile.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the client.</p></li>
<li><p><strong>oidc_conformant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not this client will conform to strict OIDC specifications.</p></li>
<li><p><strong>sso</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the client should use Auth0 rather than the IdP to perform Single Sign-On (SSO). True = Use Auth0.</p></li>
<li><p><strong>sso_disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not SSO is disabled.</p></li>
<li><p><strong>token_endpoint_auth_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Defines the requested authentication method for the token endpoint. Options include <code class="docutils literal notranslate"><span class="pre">none</span></code> (public client without a client secret), <code class="docutils literal notranslate"><span class="pre">client_secret_post</span></code> (client uses HTTP POST parameters), <code class="docutils literal notranslate"><span class="pre">client_secret_basic</span></code> (client uses HTTP Basic).</p></li>
<li><p><strong>web_origins</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). URLs that represent valid web origins for use with web message response mode.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.addons">
<em class="property">property </em><code class="sig-name descname">addons</code><a class="headerlink" href="#pulumi_auth0.Client.addons" title="Permalink to this definition"></a></dt>
<dd><p>List(Resource). Configuration settings for add-ons for this client. For details, see Add-ons.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.allowed_logout_urls">
<em class="property">property </em><code class="sig-name descname">allowed_logout_urls</code><a class="headerlink" href="#pulumi_auth0.Client.allowed_logout_urls" title="Permalink to this definition"></a></dt>
<dd><p>List(String). URLs that Auth0 may redirect to after logout.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.allowed_origins">
<em class="property">property </em><code class="sig-name descname">allowed_origins</code><a class="headerlink" href="#pulumi_auth0.Client.allowed_origins" title="Permalink to this definition"></a></dt>
<dd><p>List(String). URLs that represent valid origins for cross-origin resource sharing. By default, all your callback URLs will be allowed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.app_type">
<em class="property">property </em><code class="sig-name descname">app_type</code><a class="headerlink" href="#pulumi_auth0.Client.app_type" title="Permalink to this definition"></a></dt>
<dd><p>String. Type of application the client represents. Options include <code class="docutils literal notranslate"><span class="pre">native</span></code>, <code class="docutils literal notranslate"><span class="pre">spa</span></code>, <code class="docutils literal notranslate"><span class="pre">regular_web</span></code>, <code class="docutils literal notranslate"><span class="pre">non_interactive</span></code>, <code class="docutils literal notranslate"><span class="pre">rms</span></code>, <code class="docutils literal notranslate"><span class="pre">box</span></code>, <code class="docutils literal notranslate"><span class="pre">cloudbees</span></code>, <code class="docutils literal notranslate"><span class="pre">concur</span></code>, <code class="docutils literal notranslate"><span class="pre">dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">mscrm</span></code>, <code class="docutils literal notranslate"><span class="pre">echosign</span></code>, <code class="docutils literal notranslate"><span class="pre">egnyte</span></code>, <code class="docutils literal notranslate"><span class="pre">newrelic</span></code>, <code class="docutils literal notranslate"><span class="pre">office365</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce</span></code>, <code class="docutils literal notranslate"><span class="pre">sentry</span></code>, <code class="docutils literal notranslate"><span class="pre">sharepoint</span></code>, <code class="docutils literal notranslate"><span class="pre">slack</span></code>, <code class="docutils literal notranslate"><span class="pre">springcm</span></code>, <code class="docutils literal notranslate"><span class="pre">zendesk</span></code>, <code class="docutils literal notranslate"><span class="pre">zoom</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.callbacks">
<em class="property">property </em><code class="sig-name descname">callbacks</code><a class="headerlink" href="#pulumi_auth0.Client.callbacks" title="Permalink to this definition"></a></dt>
<dd><p>List(String). URLs that Auth0 may call back to after a user authenticates for the client. Make sure to specify the protocol (<a class="reference external" href="https://">https://</a>) otherwise the callback may fail in some cases. With the exception of custom URI schemes for native clients, all callbacks should use protocol <a class="reference external" href="https://">https://</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.client_id">
<em class="property">property </em><code class="sig-name descname">client_id</code><a class="headerlink" href="#pulumi_auth0.Client.client_id" title="Permalink to this definition"></a></dt>
<dd><p>String. ID of the client.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.client_metadata">
<em class="property">property </em><code class="sig-name descname">client_metadata</code><a class="headerlink" href="#pulumi_auth0.Client.client_metadata" title="Permalink to this definition"></a></dt>
<dd><p>Map(String)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.client_secret">
<em class="property">property </em><code class="sig-name descname">client_secret</code><a class="headerlink" href="#pulumi_auth0.Client.client_secret" title="Permalink to this definition"></a></dt>
<dd><p>String. Secret for the client; keep this private.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.client_secret_rotation_trigger">
<em class="property">property </em><code class="sig-name descname">client_secret_rotation_trigger</code><a class="headerlink" href="#pulumi_auth0.Client.client_secret_rotation_trigger" title="Permalink to this definition"></a></dt>
<dd><p>Map.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.cross_origin_auth">
<em class="property">property </em><code class="sig-name descname">cross_origin_auth</code><a class="headerlink" href="#pulumi_auth0.Client.cross_origin_auth" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not the client can be used to make cross-origin authentication requests.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.cross_origin_loc">
<em class="property">property </em><code class="sig-name descname">cross_origin_loc</code><a class="headerlink" href="#pulumi_auth0.Client.cross_origin_loc" title="Permalink to this definition"></a></dt>
<dd><p>String. URL for the location on your site where the cross-origin verification takes place for the cross-origin auth flow. Used when performing auth in your own domain instead of through the Auth0-hosted login page.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.custom_login_page">
<em class="property">property </em><code class="sig-name descname">custom_login_page</code><a class="headerlink" href="#pulumi_auth0.Client.custom_login_page" title="Permalink to this definition"></a></dt>
<dd><p>String. Content of the custom login page.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.custom_login_page_on">
<em class="property">property </em><code class="sig-name descname">custom_login_page_on</code><a class="headerlink" href="#pulumi_auth0.Client.custom_login_page_on" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not a custom login page is to be used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.custom_login_page_preview">
<em class="property">property </em><code class="sig-name descname">custom_login_page_preview</code><a class="headerlink" href="#pulumi_auth0.Client.custom_login_page_preview" title="Permalink to this definition"></a></dt>
<dd><p>String.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_auth0.Client.description" title="Permalink to this definition"></a></dt>
<dd><p>String, (Max length = 140 characters). Description of the purpose of the client.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.encryption_key">
<em class="property">property </em><code class="sig-name descname">encryption_key</code><a class="headerlink" href="#pulumi_auth0.Client.encryption_key" title="Permalink to this definition"></a></dt>
<dd><p>Map(String).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.form_template">
<em class="property">property </em><code class="sig-name descname">form_template</code><a class="headerlink" href="#pulumi_auth0.Client.form_template" title="Permalink to this definition"></a></dt>
<dd><p>String. Form template for WS-Federation protocol.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.grant_types">
<em class="property">property </em><code class="sig-name descname">grant_types</code><a class="headerlink" href="#pulumi_auth0.Client.grant_types" title="Permalink to this definition"></a></dt>
<dd><p>List(String). Types of grants that this client is authorized to use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.is_first_party">
<em class="property">property </em><code class="sig-name descname">is_first_party</code><a class="headerlink" href="#pulumi_auth0.Client.is_first_party" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not this client is a first-party client.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.is_token_endpoint_ip_header_trusted">
<em class="property">property </em><code class="sig-name descname">is_token_endpoint_ip_header_trusted</code><a class="headerlink" href="#pulumi_auth0.Client.is_token_endpoint_ip_header_trusted" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not the token endpoint IP header is trusted.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.jwt_configuration">
<em class="property">property </em><code class="sig-name descname">jwt_configuration</code><a class="headerlink" href="#pulumi_auth0.Client.jwt_configuration" title="Permalink to this definition"></a></dt>
<dd><p>List(Resource). Configuration settings for the JWTs issued for this client. For details, see JWT Configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.logo_uri">
<em class="property">property </em><code class="sig-name descname">logo_uri</code><a class="headerlink" href="#pulumi_auth0.Client.logo_uri" title="Permalink to this definition"></a></dt>
<dd><p>String. URL of the logo for the client. Recommended size is 150px x 150px. If none is set, the default badge for the application type will be shown.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.mobile">
<em class="property">property </em><code class="sig-name descname">mobile</code><a class="headerlink" href="#pulumi_auth0.Client.mobile" title="Permalink to this definition"></a></dt>
<dd><p>List(Resource). Configuration settings for mobile native applications. For details, see Mobile.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_auth0.Client.name" title="Permalink to this definition"></a></dt>
<dd><p>String. Name of the client.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.oidc_conformant">
<em class="property">property </em><code class="sig-name descname">oidc_conformant</code><a class="headerlink" href="#pulumi_auth0.Client.oidc_conformant" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not this client will conform to strict OIDC specifications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.sso">
<em class="property">property </em><code class="sig-name descname">sso</code><a class="headerlink" href="#pulumi_auth0.Client.sso" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not the client should use Auth0 rather than the IdP to perform Single Sign-On (SSO). True = Use Auth0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.sso_disabled">
<em class="property">property </em><code class="sig-name descname">sso_disabled</code><a class="headerlink" href="#pulumi_auth0.Client.sso_disabled" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not SSO is disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.token_endpoint_auth_method">
<em class="property">property </em><code class="sig-name descname">token_endpoint_auth_method</code><a class="headerlink" href="#pulumi_auth0.Client.token_endpoint_auth_method" title="Permalink to this definition"></a></dt>
<dd><p>String. Defines the requested authentication method for the token endpoint. Options include <code class="docutils literal notranslate"><span class="pre">none</span></code> (public client without a client secret), <code class="docutils literal notranslate"><span class="pre">client_secret_post</span></code> (client uses HTTP POST parameters), <code class="docutils literal notranslate"><span class="pre">client_secret_basic</span></code> (client uses HTTP Basic).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.web_origins">
<em class="property">property </em><code class="sig-name descname">web_origins</code><a class="headerlink" href="#pulumi_auth0.Client.web_origins" title="Permalink to this definition"></a></dt>
<dd><p>List(String). URLs that represent valid web origins for use with web message response mode.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Client.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Client.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Client.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.ClientGrant">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">ClientGrant</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audience</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ClientGrant" title="Permalink to this definition"></a></dt>
<dd><p>Auth0 uses various grant types, or methods by which you grant limited access to your resources to another entity without exposing credentials. The OAuth 2.0 protocol supports several types of grants, which allow different types of access. This resource allows you to create and manage client grants used with configured Auth0 clients.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_client</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;myClient&quot;</span><span class="p">)</span>
<span class="n">my_resource_server</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">ResourceServer</span><span class="p">(</span><span class="s2">&quot;myResourceServer&quot;</span><span class="p">,</span>
    <span class="n">identifier</span><span class="o">=</span><span class="s2">&quot;https://api.example.com/client-grant&quot;</span><span class="p">,</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[</span>
        <span class="n">auth0</span><span class="o">.</span><span class="n">ResourceServerScopeArgs</span><span class="p">(</span>
            <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Create foos&quot;</span><span class="p">,</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;create:foo&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">auth0</span><span class="o">.</span><span class="n">ResourceServerScopeArgs</span><span class="p">(</span>
            <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Create bars&quot;</span><span class="p">,</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;create:bar&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">])</span>
<span class="n">my_client_grant</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">ClientGrant</span><span class="p">(</span><span class="s2">&quot;myClientGrant&quot;</span><span class="p">,</span>
    <span class="n">audience</span><span class="o">=</span><span class="n">my_resource_server</span><span class="o">.</span><span class="n">identifier</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="n">my_client</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;create:foo&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Audience or API Identifier for this grant.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. ID of the client for this grant.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). Permissions (scopes) included in this grant.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.ClientGrant.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audience</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.ClientGrant" title="pulumi_auth0.ClientGrant">ClientGrant</a><a class="headerlink" href="#pulumi_auth0.ClientGrant.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing ClientGrant resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Audience or API Identifier for this grant.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. ID of the client for this grant.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). Permissions (scopes) included in this grant.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ClientGrant.audience">
<em class="property">property </em><code class="sig-name descname">audience</code><a class="headerlink" href="#pulumi_auth0.ClientGrant.audience" title="Permalink to this definition"></a></dt>
<dd><p>String. Audience or API Identifier for this grant.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ClientGrant.client_id">
<em class="property">property </em><code class="sig-name descname">client_id</code><a class="headerlink" href="#pulumi_auth0.ClientGrant.client_id" title="Permalink to this definition"></a></dt>
<dd><p>String. ID of the client for this grant.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ClientGrant.scopes">
<em class="property">property </em><code class="sig-name descname">scopes</code><a class="headerlink" href="#pulumi_auth0.ClientGrant.scopes" title="Permalink to this definition"></a></dt>
<dd><p>List(String). Permissions (scopes) included in this grant.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ClientGrant.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ClientGrant.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.ClientGrant.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ClientGrant.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Connection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Connection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_clients</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_domain_connection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ConnectionOptionsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ConnectionOptionsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realms</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy_version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validation</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Connection" title="Permalink to this definition"></a></dt>
<dd><p>With Auth0, you can define sources of users, otherwise known as connections, which may include identity providers (such as Google or LinkedIn), databases, or passwordless authentication methods. This resource allows you to configure and manage connections to be used with your clients and users.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_connection</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Connection</span><span class="p">(</span><span class="s2">&quot;myConnection&quot;</span><span class="p">,</span>
    <span class="n">options</span><span class="o">=</span><span class="n">auth0</span><span class="o">.</span><span class="n">ConnectionOptionsArgs</span><span class="p">(</span>
        <span class="n">brute_force_protection</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">configuration</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">&quot;bar&quot;</span><span class="p">:</span> <span class="s2">&quot;baz&quot;</span><span class="p">,</span>
            <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="n">custom_scripts</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">&quot;getUser&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;&quot;function getByEmail (email, callback) {</span>
<span class="s2">  return callback(new Error(&quot;Whoops!&quot;))</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="n">enabled_database_customization</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">password_histories</span><span class="o">=</span><span class="p">[</span><span class="n">auth0</span><span class="o">.</span><span class="n">ConnectionOptionsPasswordHistoryArgs</span><span class="p">(</span>
            <span class="n">enable</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">size</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
        <span class="p">)],</span>
        <span class="n">password_policy</span><span class="o">=</span><span class="s2">&quot;excellent&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">strategy</span><span class="o">=</span><span class="s2">&quot;auth0&quot;</span><span class="p">)</span>
</pre></div>
</div>
<blockquote>
<div><p>The Auth0 dashboard displays only one connection per social provider. Although the Auth0 Management API allowes the creation of multiple connections per strategy, the additional connections may not be visible in the Auth0 dashboard.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name used in login screen</p></li>
<li><p><strong>enabled_clients</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – IDs of the clients for which the connection is enabled. If not specified, no clients are enabled.</p></li>
<li><p><strong>is_domain_connection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether or not the connection is domain level.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the connection.</p></li>
<li><p><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ConnectionOptionsArgs'</em><em>]</em><em>]</em>) – Configuration settings for connection options. For details, see Options.</p></li>
<li><p><strong>realms</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Defines the realms for which the connection will be used (i.e., email domains). If not specified, the connection name is added as the realm.</p></li>
<li><p><strong>strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the connection, which indicates the identity provider. Options include <code class="docutils literal notranslate"><span class="pre">ad</span></code>, <code class="docutils literal notranslate"><span class="pre">adfs</span></code>, <code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aol</span></code>, <code class="docutils literal notranslate"><span class="pre">apple</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0-adldap</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0-oidc</span></code>, <code class="docutils literal notranslate"><span class="pre">baidu</span></code>, <code class="docutils literal notranslate"><span class="pre">bitbucket</span></code>, <code class="docutils literal notranslate"><span class="pre">bitly</span></code>, <code class="docutils literal notranslate"><span class="pre">box</span></code>, <code class="docutils literal notranslate"><span class="pre">custom</span></code>, <code class="docutils literal notranslate"><span class="pre">daccount</span></code>, <code class="docutils literal notranslate"><span class="pre">dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">dwolla</span></code>, <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">evernote</span></code>, <code class="docutils literal notranslate"><span class="pre">evernote-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">exact</span></code>, <code class="docutils literal notranslate"><span class="pre">facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">fitbit</span></code>, <code class="docutils literal notranslate"><span class="pre">flickr</span></code>, <code class="docutils literal notranslate"><span class="pre">github</span></code>, <code class="docutils literal notranslate"><span class="pre">google-apps</span></code>, <code class="docutils literal notranslate"><span class="pre">google-oauth2</span></code>, <code class="docutils literal notranslate"><span class="pre">guardian</span></code>, <code class="docutils literal notranslate"><span class="pre">instagram</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code>, <code class="docutils literal notranslate"><span class="pre">line</span></code>, <code class="docutils literal notranslate"><span class="pre">linkedin</span></code>, <code class="docutils literal notranslate"><span class="pre">miicard</span></code>, <code class="docutils literal notranslate"><span class="pre">oauth1</span></code>, <code class="docutils literal notranslate"><span class="pre">oauth2</span></code>, <code class="docutils literal notranslate"><span class="pre">office365</span></code>, <code class="docutils literal notranslate"><span class="pre">oidc</span></code>, <code class="docutils literal notranslate"><span class="pre">paypal</span></code>, <code class="docutils literal notranslate"><span class="pre">paypal-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">pingfederate</span></code>, <code class="docutils literal notranslate"><span class="pre">planningcenter</span></code>, <code class="docutils literal notranslate"><span class="pre">renren</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce-community</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce-sandbox</span></code> <code class="docutils literal notranslate"><span class="pre">samlp</span></code>, <code class="docutils literal notranslate"><span class="pre">sharepoint</span></code>, <code class="docutils literal notranslate"><span class="pre">shopify</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">soundcloud</span></code>, <code class="docutils literal notranslate"><span class="pre">thecity</span></code>, <code class="docutils literal notranslate"><span class="pre">thecity-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">thirtysevensignals</span></code>, <code class="docutils literal notranslate"><span class="pre">twitter</span></code>, <code class="docutils literal notranslate"><span class="pre">untappd</span></code>, <code class="docutils literal notranslate"><span class="pre">vkontakte</span></code>, <code class="docutils literal notranslate"><span class="pre">waad</span></code>, <code class="docutils literal notranslate"><span class="pre">weibo</span></code>, <code class="docutils literal notranslate"><span class="pre">windowslive</span></code>, <code class="docutils literal notranslate"><span class="pre">wordpress</span></code>, <code class="docutils literal notranslate"><span class="pre">yahoo</span></code>, <code class="docutils literal notranslate"><span class="pre">yammer</span></code>, <code class="docutils literal notranslate"><span class="pre">yandex</span></code>.</p></li>
<li><p><strong>strategy_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version 1 is deprecated, use version 2.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>validation</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Validation of the minimum and maximum values allowed for a user to have as username. For details, see Validation.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.Connection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_clients</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_domain_connection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ConnectionOptionsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ConnectionOptionsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realms</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy_version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validation</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.Connection" title="pulumi_auth0.Connection">Connection</a><a class="headerlink" href="#pulumi_auth0.Connection.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Connection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name used in login screen</p></li>
<li><p><strong>enabled_clients</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – IDs of the clients for which the connection is enabled. If not specified, no clients are enabled.</p></li>
<li><p><strong>is_domain_connection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether or not the connection is domain level.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the connection.</p></li>
<li><p><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ConnectionOptionsArgs'</em><em>]</em><em>]</em>) – Configuration settings for connection options. For details, see Options.</p></li>
<li><p><strong>realms</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Defines the realms for which the connection will be used (i.e., email domains). If not specified, the connection name is added as the realm.</p></li>
<li><p><strong>strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the connection, which indicates the identity provider. Options include <code class="docutils literal notranslate"><span class="pre">ad</span></code>, <code class="docutils literal notranslate"><span class="pre">adfs</span></code>, <code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aol</span></code>, <code class="docutils literal notranslate"><span class="pre">apple</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0-adldap</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0-oidc</span></code>, <code class="docutils literal notranslate"><span class="pre">baidu</span></code>, <code class="docutils literal notranslate"><span class="pre">bitbucket</span></code>, <code class="docutils literal notranslate"><span class="pre">bitly</span></code>, <code class="docutils literal notranslate"><span class="pre">box</span></code>, <code class="docutils literal notranslate"><span class="pre">custom</span></code>, <code class="docutils literal notranslate"><span class="pre">daccount</span></code>, <code class="docutils literal notranslate"><span class="pre">dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">dwolla</span></code>, <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">evernote</span></code>, <code class="docutils literal notranslate"><span class="pre">evernote-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">exact</span></code>, <code class="docutils literal notranslate"><span class="pre">facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">fitbit</span></code>, <code class="docutils literal notranslate"><span class="pre">flickr</span></code>, <code class="docutils literal notranslate"><span class="pre">github</span></code>, <code class="docutils literal notranslate"><span class="pre">google-apps</span></code>, <code class="docutils literal notranslate"><span class="pre">google-oauth2</span></code>, <code class="docutils literal notranslate"><span class="pre">guardian</span></code>, <code class="docutils literal notranslate"><span class="pre">instagram</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code>, <code class="docutils literal notranslate"><span class="pre">line</span></code>, <code class="docutils literal notranslate"><span class="pre">linkedin</span></code>, <code class="docutils literal notranslate"><span class="pre">miicard</span></code>, <code class="docutils literal notranslate"><span class="pre">oauth1</span></code>, <code class="docutils literal notranslate"><span class="pre">oauth2</span></code>, <code class="docutils literal notranslate"><span class="pre">office365</span></code>, <code class="docutils literal notranslate"><span class="pre">oidc</span></code>, <code class="docutils literal notranslate"><span class="pre">paypal</span></code>, <code class="docutils literal notranslate"><span class="pre">paypal-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">pingfederate</span></code>, <code class="docutils literal notranslate"><span class="pre">planningcenter</span></code>, <code class="docutils literal notranslate"><span class="pre">renren</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce-community</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce-sandbox</span></code> <code class="docutils literal notranslate"><span class="pre">samlp</span></code>, <code class="docutils literal notranslate"><span class="pre">sharepoint</span></code>, <code class="docutils literal notranslate"><span class="pre">shopify</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">soundcloud</span></code>, <code class="docutils literal notranslate"><span class="pre">thecity</span></code>, <code class="docutils literal notranslate"><span class="pre">thecity-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">thirtysevensignals</span></code>, <code class="docutils literal notranslate"><span class="pre">twitter</span></code>, <code class="docutils literal notranslate"><span class="pre">untappd</span></code>, <code class="docutils literal notranslate"><span class="pre">vkontakte</span></code>, <code class="docutils literal notranslate"><span class="pre">waad</span></code>, <code class="docutils literal notranslate"><span class="pre">weibo</span></code>, <code class="docutils literal notranslate"><span class="pre">windowslive</span></code>, <code class="docutils literal notranslate"><span class="pre">wordpress</span></code>, <code class="docutils literal notranslate"><span class="pre">yahoo</span></code>, <code class="docutils literal notranslate"><span class="pre">yammer</span></code>, <code class="docutils literal notranslate"><span class="pre">yandex</span></code>.</p></li>
<li><p><strong>strategy_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version 1 is deprecated, use version 2.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>validation</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Validation of the minimum and maximum values allowed for a user to have as username. For details, see Validation.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Connection.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_auth0.Connection.display_name" title="Permalink to this definition"></a></dt>
<dd><p>Name used in login screen</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Connection.enabled_clients">
<em class="property">property </em><code class="sig-name descname">enabled_clients</code><a class="headerlink" href="#pulumi_auth0.Connection.enabled_clients" title="Permalink to this definition"></a></dt>
<dd><p>IDs of the clients for which the connection is enabled. If not specified, no clients are enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Connection.is_domain_connection">
<em class="property">property </em><code class="sig-name descname">is_domain_connection</code><a class="headerlink" href="#pulumi_auth0.Connection.is_domain_connection" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether or not the connection is domain level.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Connection.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_auth0.Connection.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Connection.options">
<em class="property">property </em><code class="sig-name descname">options</code><a class="headerlink" href="#pulumi_auth0.Connection.options" title="Permalink to this definition"></a></dt>
<dd><p>Configuration settings for connection options. For details, see Options.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Connection.realms">
<em class="property">property </em><code class="sig-name descname">realms</code><a class="headerlink" href="#pulumi_auth0.Connection.realms" title="Permalink to this definition"></a></dt>
<dd><p>Defines the realms for which the connection will be used (i.e., email domains). If not specified, the connection name is added as the realm.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Connection.strategy">
<em class="property">property </em><code class="sig-name descname">strategy</code><a class="headerlink" href="#pulumi_auth0.Connection.strategy" title="Permalink to this definition"></a></dt>
<dd><p>Type of the connection, which indicates the identity provider. Options include <code class="docutils literal notranslate"><span class="pre">ad</span></code>, <code class="docutils literal notranslate"><span class="pre">adfs</span></code>, <code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aol</span></code>, <code class="docutils literal notranslate"><span class="pre">apple</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0-adldap</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0-oidc</span></code>, <code class="docutils literal notranslate"><span class="pre">baidu</span></code>, <code class="docutils literal notranslate"><span class="pre">bitbucket</span></code>, <code class="docutils literal notranslate"><span class="pre">bitly</span></code>, <code class="docutils literal notranslate"><span class="pre">box</span></code>, <code class="docutils literal notranslate"><span class="pre">custom</span></code>, <code class="docutils literal notranslate"><span class="pre">daccount</span></code>, <code class="docutils literal notranslate"><span class="pre">dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">dwolla</span></code>, <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">evernote</span></code>, <code class="docutils literal notranslate"><span class="pre">evernote-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">exact</span></code>, <code class="docutils literal notranslate"><span class="pre">facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">fitbit</span></code>, <code class="docutils literal notranslate"><span class="pre">flickr</span></code>, <code class="docutils literal notranslate"><span class="pre">github</span></code>, <code class="docutils literal notranslate"><span class="pre">google-apps</span></code>, <code class="docutils literal notranslate"><span class="pre">google-oauth2</span></code>, <code class="docutils literal notranslate"><span class="pre">guardian</span></code>, <code class="docutils literal notranslate"><span class="pre">instagram</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code>, <code class="docutils literal notranslate"><span class="pre">line</span></code>, <code class="docutils literal notranslate"><span class="pre">linkedin</span></code>, <code class="docutils literal notranslate"><span class="pre">miicard</span></code>, <code class="docutils literal notranslate"><span class="pre">oauth1</span></code>, <code class="docutils literal notranslate"><span class="pre">oauth2</span></code>, <code class="docutils literal notranslate"><span class="pre">office365</span></code>, <code class="docutils literal notranslate"><span class="pre">oidc</span></code>, <code class="docutils literal notranslate"><span class="pre">paypal</span></code>, <code class="docutils literal notranslate"><span class="pre">paypal-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">pingfederate</span></code>, <code class="docutils literal notranslate"><span class="pre">planningcenter</span></code>, <code class="docutils literal notranslate"><span class="pre">renren</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce-community</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce-sandbox</span></code> <code class="docutils literal notranslate"><span class="pre">samlp</span></code>, <code class="docutils literal notranslate"><span class="pre">sharepoint</span></code>, <code class="docutils literal notranslate"><span class="pre">shopify</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">soundcloud</span></code>, <code class="docutils literal notranslate"><span class="pre">thecity</span></code>, <code class="docutils literal notranslate"><span class="pre">thecity-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">thirtysevensignals</span></code>, <code class="docutils literal notranslate"><span class="pre">twitter</span></code>, <code class="docutils literal notranslate"><span class="pre">untappd</span></code>, <code class="docutils literal notranslate"><span class="pre">vkontakte</span></code>, <code class="docutils literal notranslate"><span class="pre">waad</span></code>, <code class="docutils literal notranslate"><span class="pre">weibo</span></code>, <code class="docutils literal notranslate"><span class="pre">windowslive</span></code>, <code class="docutils literal notranslate"><span class="pre">wordpress</span></code>, <code class="docutils literal notranslate"><span class="pre">yahoo</span></code>, <code class="docutils literal notranslate"><span class="pre">yammer</span></code>, <code class="docutils literal notranslate"><span class="pre">yandex</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Connection.strategy_version">
<em class="property">property </em><code class="sig-name descname">strategy_version</code><a class="headerlink" href="#pulumi_auth0.Connection.strategy_version" title="Permalink to this definition"></a></dt>
<dd><p>Version 1 is deprecated, use version 2.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Connection.validation">
<em class="property">property </em><code class="sig-name descname">validation</code><a class="headerlink" href="#pulumi_auth0.Connection.validation" title="Permalink to this definition"></a></dt>
<dd><p>Validation of the minimum and maximum values allowed for a user to have as username. For details, see Validation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Connection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Connection.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Connection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Connection.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.CustomDomain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">CustomDomain</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification_method</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.CustomDomain" title="Permalink to this definition"></a></dt>
<dd><p>With Auth0, you can use a custom domain to maintain a consistent user experience. This resource allows you to create and manage a custom domain within your Auth0 tenant.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_custom_domain</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">CustomDomain</span><span class="p">(</span><span class="s2">&quot;myCustomDomain&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;auth.example.com&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;auth0_managed_certs&quot;</span><span class="p">,</span>
    <span class="n">verification_method</span><span class="o">=</span><span class="s2">&quot;txt&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the custom domain.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Provisioning type for the custom domain. Options include <code class="docutils literal notranslate"><span class="pre">auth0_managed_certs</span></code> and <code class="docutils literal notranslate"><span class="pre">self_managed_certs</span></code>.</p></li>
<li><p><strong>verification_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Domain verification method. Options include <code class="docutils literal notranslate"><span class="pre">txt</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.CustomDomain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>CustomDomainVerificationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>CustomDomainVerificationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification_method</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.CustomDomain" title="pulumi_auth0.CustomDomain">CustomDomain</a><a class="headerlink" href="#pulumi_auth0.CustomDomain.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing CustomDomain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the custom domain.</p></li>
<li><p><strong>primary</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not this is a primary domain.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Configuration status for the custom domain. Options include <code class="docutils literal notranslate"><span class="pre">disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">pending</span></code>, <code class="docutils literal notranslate"><span class="pre">pending_verification</span></code>, and <code class="docutils literal notranslate"><span class="pre">ready</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Provisioning type for the custom domain. Options include <code class="docutils literal notranslate"><span class="pre">auth0_managed_certs</span></code> and <code class="docutils literal notranslate"><span class="pre">self_managed_certs</span></code>.</p></li>
<li><p><strong>verification</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CustomDomainVerificationArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for verification. For details, see Verification.</p></li>
<li><p><strong>verification_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Domain verification method. Options include <code class="docutils literal notranslate"><span class="pre">txt</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.CustomDomain.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_auth0.CustomDomain.domain" title="Permalink to this definition"></a></dt>
<dd><p>String. Name of the custom domain.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.CustomDomain.primary">
<em class="property">property </em><code class="sig-name descname">primary</code><a class="headerlink" href="#pulumi_auth0.CustomDomain.primary" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not this is a primary domain.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.CustomDomain.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_auth0.CustomDomain.status" title="Permalink to this definition"></a></dt>
<dd><p>String. Configuration status for the custom domain. Options include <code class="docutils literal notranslate"><span class="pre">disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">pending</span></code>, <code class="docutils literal notranslate"><span class="pre">pending_verification</span></code>, and <code class="docutils literal notranslate"><span class="pre">ready</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.CustomDomain.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_auth0.CustomDomain.type" title="Permalink to this definition"></a></dt>
<dd><p>String. Provisioning type for the custom domain. Options include <code class="docutils literal notranslate"><span class="pre">auth0_managed_certs</span></code> and <code class="docutils literal notranslate"><span class="pre">self_managed_certs</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.CustomDomain.verification">
<em class="property">property </em><code class="sig-name descname">verification</code><a class="headerlink" href="#pulumi_auth0.CustomDomain.verification" title="Permalink to this definition"></a></dt>
<dd><p>List(Resource). Configuration settings for verification. For details, see Verification.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.CustomDomain.verification_method">
<em class="property">property </em><code class="sig-name descname">verification_method</code><a class="headerlink" href="#pulumi_auth0.CustomDomain.verification_method" title="Permalink to this definition"></a></dt>
<dd><p>String. Domain verification method. Options include <code class="docutils literal notranslate"><span class="pre">txt</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.CustomDomain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.CustomDomain.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.CustomDomain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.CustomDomain.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Email">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Email</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>EmailCredentialsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EmailCredentialsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_from_address</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Email" title="Permalink to this definition"></a></dt>
<dd><p>With Auth0, you can have standard welcome, password reset, and account verification email-based workflows built right into Auth0. This resource allows you to configure email providers so you can route all emails that are part of Auth0’s authentication workflows through the supported high-volume email service of your choice.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_email_provider</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Email</span><span class="p">(</span><span class="s2">&quot;myEmailProvider&quot;</span><span class="p">,</span>
    <span class="n">credentials</span><span class="o">=</span><span class="n">auth0</span><span class="o">.</span><span class="n">EmailCredentialsArgs</span><span class="p">(</span>
        <span class="n">access_key_id</span><span class="o">=</span><span class="s2">&quot;AKIAXXXXXXXXXXXXXXXX&quot;</span><span class="p">,</span>
        <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">,</span>
        <span class="n">secret_access_key</span><span class="o">=</span><span class="s2">&quot;7e8c2148xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">default_from_address</span><span class="o">=</span><span class="s2">&quot;accounts@example.com&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EmailCredentialsArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for the credentials for the email provider. For details, see Credentials.</p></li>
<li><p><strong>default_from_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Email address to use as the sender when no other “from” address is specified.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the email provider is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the email provider. Options include <code class="docutils literal notranslate"><span class="pre">mailgun</span></code>, <code class="docutils literal notranslate"><span class="pre">mandrill</span></code>, <code class="docutils literal notranslate"><span class="pre">sendgrid</span></code>, <code class="docutils literal notranslate"><span class="pre">ses</span></code>, <code class="docutils literal notranslate"><span class="pre">smtp</span></code>, and <code class="docutils literal notranslate"><span class="pre">sparkpost</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.Email.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>EmailCredentialsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EmailCredentialsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_from_address</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.Email" title="pulumi_auth0.Email">Email</a><a class="headerlink" href="#pulumi_auth0.Email.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Email resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EmailCredentialsArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for the credentials for the email provider. For details, see Credentials.</p></li>
<li><p><strong>default_from_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Email address to use as the sender when no other “from” address is specified.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the email provider is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the email provider. Options include <code class="docutils literal notranslate"><span class="pre">mailgun</span></code>, <code class="docutils literal notranslate"><span class="pre">mandrill</span></code>, <code class="docutils literal notranslate"><span class="pre">sendgrid</span></code>, <code class="docutils literal notranslate"><span class="pre">ses</span></code>, <code class="docutils literal notranslate"><span class="pre">smtp</span></code>, and <code class="docutils literal notranslate"><span class="pre">sparkpost</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Email.credentials">
<em class="property">property </em><code class="sig-name descname">credentials</code><a class="headerlink" href="#pulumi_auth0.Email.credentials" title="Permalink to this definition"></a></dt>
<dd><p>List(Resource). Configuration settings for the credentials for the email provider. For details, see Credentials.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Email.default_from_address">
<em class="property">property </em><code class="sig-name descname">default_from_address</code><a class="headerlink" href="#pulumi_auth0.Email.default_from_address" title="Permalink to this definition"></a></dt>
<dd><p>String. Email address to use as the sender when no other “from” address is specified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Email.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_auth0.Email.enabled" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not the email provider is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Email.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_auth0.Email.name" title="Permalink to this definition"></a></dt>
<dd><p>String. Name of the email provider. Options include <code class="docutils literal notranslate"><span class="pre">mailgun</span></code>, <code class="docutils literal notranslate"><span class="pre">mandrill</span></code>, <code class="docutils literal notranslate"><span class="pre">sendgrid</span></code>, <code class="docutils literal notranslate"><span class="pre">ses</span></code>, <code class="docutils literal notranslate"><span class="pre">smtp</span></code>, and <code class="docutils literal notranslate"><span class="pre">sparkpost</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Email.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Email.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Email.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Email.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.EmailTemplate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">EmailTemplate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">from_</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">result_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">syntax</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_lifetime_in_seconds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.EmailTemplate" title="Permalink to this definition"></a></dt>
<dd><p>With Auth0, you can have standard welcome, password reset, and account verification email-based workflows built right into Auth0. This resource allows you to configure email templates to customize the look, feel, and sender identities of emails sent by Auth0. Used in conjunction with configured email providers.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_email_provider</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Email</span><span class="p">(</span><span class="s2">&quot;myEmailProvider&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">default_from_address</span><span class="o">=</span><span class="s2">&quot;accounts@example.com&quot;</span><span class="p">,</span>
    <span class="n">credentials</span><span class="o">=</span><span class="n">auth0</span><span class="o">.</span><span class="n">EmailCredentialsArgs</span><span class="p">(</span>
        <span class="n">access_key_id</span><span class="o">=</span><span class="s2">&quot;AKIAXXXXXXXXXXXXXXXX&quot;</span><span class="p">,</span>
        <span class="n">secret_access_key</span><span class="o">=</span><span class="s2">&quot;7e8c2148xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&quot;</span><span class="p">,</span>
        <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">my_email_template</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">EmailTemplate</span><span class="p">(</span><span class="s2">&quot;myEmailTemplate&quot;</span><span class="p">,</span>
    <span class="n">template</span><span class="o">=</span><span class="s2">&quot;welcome_email&quot;</span><span class="p">,</span>
    <span class="n">body</span><span class="o">=</span><span class="s2">&quot;&lt;html&gt;&lt;body&gt;&lt;h1&gt;Welcome!&lt;/h1&gt;&lt;/body&gt;&lt;/html&gt;&quot;</span><span class="p">,</span>
    <span class="n">from_</span><span class="o">=</span><span class="s2">&quot;welcome@example.com&quot;</span><span class="p">,</span>
    <span class="n">result_url</span><span class="o">=</span><span class="s2">&quot;https://example.com/welcome&quot;</span><span class="p">,</span>
    <span class="n">subject</span><span class="o">=</span><span class="s2">&quot;Welcome&quot;</span><span class="p">,</span>
    <span class="n">syntax</span><span class="o">=</span><span class="s2">&quot;liquid&quot;</span><span class="p">,</span>
    <span class="n">url_lifetime_in_seconds</span><span class="o">=</span><span class="mi">3600</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span><span class="n">my_email_provider</span><span class="p">]))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The name of the resource.</p>
</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Body of the email template. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the template is enabled.</p></li>
</ul>
</dd>
</dl>
<p>:param pulumi.Input[str] from*: String. Email address to use as the sender. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.
:param pulumi.Input[str] result_url: String. URL to redirect the user to after a successful action. <a class="reference external" href="https://auth0.com/docs/email/templates#configuring-the-redirect-to-url">Learn more</a>.
:param pulumi.Input[str] subject: String. Subject line of the email. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.
:param pulumi.Input[str] syntax: String. Syntax of the template body. You can use either text or HTML + Liquid syntax.
:param pulumi.Input[str] template: String. Template name. Options include <code class="docutils literal notranslate"><span class="pre">verify_email</span></code>, <code class="docutils literal notranslate"><span class="pre">reset_email</span></code>, <code class="docutils literal notranslate"><span class="pre">welcome_email</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked_account</span></code>, <code class="docutils literal notranslate"><span class="pre">stolen_credentials</span></code>, <code class="docutils literal notranslate"><span class="pre">enrollment_email</span></code>, <code class="docutils literal notranslate"><span class="pre">mfa_oob_code</span></code>, <code class="docutils literal notranslate"><span class="pre">change_password</span></code> (legacy), and <code class="docutils literal notranslate"><span class="pre">password_reset</span></code> (legacy).
:param pulumi.Input[int] url_lifetime_in_seconds: Integer. Number of seconds during which the link within the email will be valid.</p>
<dl class="py method">
<dt id="pulumi_auth0.EmailTemplate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">from_</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">result_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">syntax</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_lifetime_in_seconds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.EmailTemplate" title="pulumi_auth0.EmailTemplate">EmailTemplate</a><a class="headerlink" href="#pulumi_auth0.EmailTemplate.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing EmailTemplate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The unique name of the resulting resource.</p>
</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>String. Body of the email template. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.</p>
</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the template is enabled.</p></li>
</ul>
</dd>
</dl>
<p>:param pulumi.Input[str] from*: String. Email address to use as the sender. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.
:param pulumi.Input[str] result_url: String. URL to redirect the user to after a successful action. <a class="reference external" href="https://auth0.com/docs/email/templates#configuring-the-redirect-to-url">Learn more</a>.
:param pulumi.Input[str] subject: String. Subject line of the email. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.
:param pulumi.Input[str] syntax: String. Syntax of the template body. You can use either text or HTML + Liquid syntax.
:param pulumi.Input[str] template: String. Template name. Options include <code class="docutils literal notranslate"><span class="pre">verify_email</span></code>, <code class="docutils literal notranslate"><span class="pre">reset_email</span></code>, <code class="docutils literal notranslate"><span class="pre">welcome_email</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked_account</span></code>, <code class="docutils literal notranslate"><span class="pre">stolen_credentials</span></code>, <code class="docutils literal notranslate"><span class="pre">enrollment_email</span></code>, <code class="docutils literal notranslate"><span class="pre">mfa_oob_code</span></code>, <code class="docutils literal notranslate"><span class="pre">change_password</span></code> (legacy), and <code class="docutils literal notranslate"><span class="pre">password_reset</span></code> (legacy).
:param pulumi.Input[int] url_lifetime_in_seconds: Integer. Number of seconds during which the link within the email will be valid.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.EmailTemplate.body">
<em class="property">property </em><code class="sig-name descname">body</code><a class="headerlink" href="#pulumi_auth0.EmailTemplate.body" title="Permalink to this definition"></a></dt>
<dd><p>String. Body of the email template. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.EmailTemplate.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_auth0.EmailTemplate.enabled" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not the template is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.EmailTemplate.from_">
<em class="property">property </em><code class="sig-name descname">from_</code><a class="headerlink" href="#pulumi_auth0.EmailTemplate.from_" title="Permalink to this definition"></a></dt>
<dd><p>String. Email address to use as the sender. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.EmailTemplate.result_url">
<em class="property">property </em><code class="sig-name descname">result_url</code><a class="headerlink" href="#pulumi_auth0.EmailTemplate.result_url" title="Permalink to this definition"></a></dt>
<dd><p>String. URL to redirect the user to after a successful action. <a class="reference external" href="https://auth0.com/docs/email/templates#configuring-the-redirect-to-url">Learn more</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.EmailTemplate.subject">
<em class="property">property </em><code class="sig-name descname">subject</code><a class="headerlink" href="#pulumi_auth0.EmailTemplate.subject" title="Permalink to this definition"></a></dt>
<dd><p>String. Subject line of the email. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.EmailTemplate.syntax">
<em class="property">property </em><code class="sig-name descname">syntax</code><a class="headerlink" href="#pulumi_auth0.EmailTemplate.syntax" title="Permalink to this definition"></a></dt>
<dd><p>String. Syntax of the template body. You can use either text or HTML + Liquid syntax.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.EmailTemplate.template">
<em class="property">property </em><code class="sig-name descname">template</code><a class="headerlink" href="#pulumi_auth0.EmailTemplate.template" title="Permalink to this definition"></a></dt>
<dd><p>String. Template name. Options include <code class="docutils literal notranslate"><span class="pre">verify_email</span></code>, <code class="docutils literal notranslate"><span class="pre">reset_email</span></code>, <code class="docutils literal notranslate"><span class="pre">welcome_email</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked_account</span></code>, <code class="docutils literal notranslate"><span class="pre">stolen_credentials</span></code>, <code class="docutils literal notranslate"><span class="pre">enrollment_email</span></code>, <code class="docutils literal notranslate"><span class="pre">mfa_oob_code</span></code>, <code class="docutils literal notranslate"><span class="pre">change_password</span></code> (legacy), and <code class="docutils literal notranslate"><span class="pre">password_reset</span></code> (legacy).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.EmailTemplate.url_lifetime_in_seconds">
<em class="property">property </em><code class="sig-name descname">url_lifetime_in_seconds</code><a class="headerlink" href="#pulumi_auth0.EmailTemplate.url_lifetime_in_seconds" title="Permalink to this definition"></a></dt>
<dd><p>Integer. Number of seconds during which the link within the email will be valid.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.EmailTemplate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.EmailTemplate.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.EmailTemplate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.EmailTemplate.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.GlobalClient">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">GlobalClient</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>GlobalClientAddonsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>GlobalClientAddonsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_logout_urls</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_origins</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">callbacks</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_metadata</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret_rotation_trigger</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_auth</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_loc</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_on</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_preview</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">form_template</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grant_types</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initiate_login_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_first_party</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_token_endpoint_ip_header_trusted</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_configuration</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>GlobalClientJwtConfigurationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>GlobalClientJwtConfigurationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>GlobalClientMobileArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>GlobalClientMobileArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_conformant</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_token</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>GlobalClientRefreshTokenArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>GlobalClientRefreshTokenArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_endpoint_auth_method</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_origins</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.GlobalClient" title="Permalink to this definition"></a></dt>
<dd><p>Create a GlobalClient resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_auth0.GlobalClient.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>GlobalClientAddonsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>GlobalClientAddonsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_logout_urls</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_origins</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">callbacks</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_metadata</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret_rotation_trigger</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_auth</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_loc</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_on</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_preview</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">form_template</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grant_types</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initiate_login_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_first_party</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_token_endpoint_ip_header_trusted</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_configuration</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>GlobalClientJwtConfigurationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>GlobalClientJwtConfigurationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>GlobalClientMobileArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>GlobalClientMobileArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_conformant</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_token</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>GlobalClientRefreshTokenArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>GlobalClientRefreshTokenArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_endpoint_auth_method</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_origins</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.GlobalClient" title="pulumi_auth0.GlobalClient">GlobalClient</a><a class="headerlink" href="#pulumi_auth0.GlobalClient.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing GlobalClient resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.GlobalClient.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.GlobalClient.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.GlobalClient.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.GlobalClient.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Hook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Hook</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">trigger_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Hook" title="Permalink to this definition"></a></dt>
<dd><p>Hooks are secure, self-contained functions that allow you to customize the behavior of Auth0 when executed for selected extensibility points of the Auth0 platform. Auth0 invokes Hooks during runtime to execute your custom Node.js code.</p>
<p>Depending on the extensibility point, you can use Hooks with Database Connections and/or Passwordless Connections.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_hook</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Hook</span><span class="p">(</span><span class="s2">&quot;myHook&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">script</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;function (user, context, callback) { </span>
<span class="s2">  callback(null, { user }); </span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">trigger_id</span><span class="o">=</span><span class="s2">&quot;pre-user-registration&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the hook is enabled, or disabled</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of this hook</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Code to be executed when this hook runs</p></li>
<li><p><strong>trigger_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Execution stage of this rule. Can be credentials-exchange, pre-user-registration, post-user-registration, post-change-password, or send-phone-message</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.Hook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">trigger_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.Hook" title="pulumi_auth0.Hook">Hook</a><a class="headerlink" href="#pulumi_auth0.Hook.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Hook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the hook is enabled, or disabled</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of this hook</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Code to be executed when this hook runs</p></li>
<li><p><strong>trigger_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Execution stage of this rule. Can be credentials-exchange, pre-user-registration, post-user-registration, post-change-password, or send-phone-message</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Hook.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_auth0.Hook.enabled" title="Permalink to this definition"></a></dt>
<dd><p>Whether the hook is enabled, or disabled</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Hook.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_auth0.Hook.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of this hook</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Hook.script">
<em class="property">property </em><code class="sig-name descname">script</code><a class="headerlink" href="#pulumi_auth0.Hook.script" title="Permalink to this definition"></a></dt>
<dd><p>Code to be executed when this hook runs</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Hook.trigger_id">
<em class="property">property </em><code class="sig-name descname">trigger_id</code><a class="headerlink" href="#pulumi_auth0.Hook.trigger_id" title="Permalink to this definition"></a></dt>
<dd><p>Execution stage of this rule. Can be credentials-exchange, pre-user-registration, post-user-registration, post-change-password, or send-phone-message</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Hook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Hook.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Hook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Hook.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.LogStream">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">LogStream</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sink</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>LogStreamSinkArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>LogStreamSinkArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.LogStream" title="Permalink to this definition"></a></dt>
<dd><p>Create a LogStream resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] status: Status of the LogStream
:param pulumi.Input[str] type: Type of the log stream, which indicates the sink provider</p>
<dl class="py method">
<dt id="pulumi_auth0.LogStream.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sink</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>LogStreamSinkArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>LogStreamSinkArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.LogStream" title="pulumi_auth0.LogStream">LogStream</a><a class="headerlink" href="#pulumi_auth0.LogStream.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing LogStream resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the LogStream</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the log stream, which indicates the sink provider</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.LogStream.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_auth0.LogStream.status" title="Permalink to this definition"></a></dt>
<dd><p>Status of the LogStream</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.LogStream.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_auth0.LogStream.type" title="Permalink to this definition"></a></dt>
<dd><p>Type of the log stream, which indicates the sink provider</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.LogStream.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.LogStream.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.LogStream.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.LogStream.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Prompt">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Prompt</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">universal_login_experience</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Prompt" title="Permalink to this definition"></a></dt>
<dd><p>With this resource, you can manage your Auth0 prompts, including choosing the login experience version.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Prompt</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">universal_login_experience</span><span class="o">=</span><span class="s2">&quot;classic&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>universal_login_experience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which login experience to use. Options include <code class="docutils literal notranslate"><span class="pre">classic</span></code> and <code class="docutils literal notranslate"><span class="pre">new</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.Prompt.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">universal_login_experience</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.Prompt" title="pulumi_auth0.Prompt">Prompt</a><a class="headerlink" href="#pulumi_auth0.Prompt.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Prompt resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>universal_login_experience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which login experience to use. Options include <code class="docutils literal notranslate"><span class="pre">classic</span></code> and <code class="docutils literal notranslate"><span class="pre">new</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Prompt.universal_login_experience">
<em class="property">property </em><code class="sig-name descname">universal_login_experience</code><a class="headerlink" href="#pulumi_auth0.Prompt.universal_login_experience" title="Permalink to this definition"></a></dt>
<dd><p>Which login experience to use. Options include <code class="docutils literal notranslate"><span class="pre">classic</span></code> and <code class="docutils literal notranslate"><span class="pre">new</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Prompt.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Prompt.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Prompt.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Prompt.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">debug</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Provider" title="Permalink to this definition"></a></dt>
<dd><p>The provider type for the auth0 package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Provider.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Provider.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.ResourceServer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">ResourceServer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_offline_access</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforce_policies</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ResourceServerScopeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ResourceServerScopeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ResourceServerScopeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ResourceServerScopeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signing_alg</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signing_secret</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_consent_for_verifiable_first_party_clients</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_dialect</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_lifetime</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_lifetime_for_web</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification_location</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ResourceServer" title="Permalink to this definition"></a></dt>
<dd><p>With this resource, you can set up APIs that can be consumed from your authorized applications.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_resource_server</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">ResourceServer</span><span class="p">(</span><span class="s2">&quot;myResourceServer&quot;</span><span class="p">,</span>
    <span class="n">allow_offline_access</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">identifier</span><span class="o">=</span><span class="s2">&quot;https://api.example.com&quot;</span><span class="p">,</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[</span>
        <span class="n">auth0</span><span class="o">.</span><span class="n">ResourceServerScopeArgs</span><span class="p">(</span>
            <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Create foos&quot;</span><span class="p">,</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;create:foo&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">auth0</span><span class="o">.</span><span class="n">ResourceServerScopeArgs</span><span class="p">(</span>
            <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Create bars&quot;</span><span class="p">,</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;create:bar&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">signing_alg</span><span class="o">=</span><span class="s2">&quot;RS256&quot;</span><span class="p">,</span>
    <span class="n">skip_consent_for_verifiable_first_party_clients</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">token_lifetime</span><span class="o">=</span><span class="mi">8600</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_offline_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not refresh tokens can be issued for this resource server.</p></li>
<li><p><strong>enforce_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not authorization polices are enforced.</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Unique identifier for the resource server. Used as the audience parameter for authorization calls. Can not be changed once set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Friendly name for the resource server. Cannot include <code class="docutils literal notranslate"><span class="pre">&lt;</span></code> or <code class="docutils literal notranslate"><span class="pre">&gt;</span></code> characters.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Map(String). Used to store additional metadata</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ResourceServerScopeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Set(Resource).  List of permissions (scopes) used by this resource server. For details, see Scopes.</p></li>
<li><p><strong>signing_alg</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Algorithm used to sign JWTs. Options include <code class="docutils literal notranslate"><span class="pre">HS256</span></code> and <code class="docutils literal notranslate"><span class="pre">RS256</span></code>.</p></li>
<li><p><strong>signing_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Secret used to sign tokens when using symmetric algorithms (HS256).</p></li>
<li><p><strong>skip_consent_for_verifiable_first_party_clients</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not to skip user consent for applications flagged as first party.</p></li>
<li><p><strong>token_dialect</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Dialect of access tokens that should be issued for this resource server. Options include <code class="docutils literal notranslate"><span class="pre">access_token</span></code> or <code class="docutils literal notranslate"><span class="pre">access_token_authz</span></code> (includes permissions).</p></li>
<li><p><strong>token_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Integer. Number of seconds during which access tokens issued for this resource server from the token endpoint remain valid.</p></li>
<li><p><strong>token_lifetime_for_web</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Integer. Number of seconds during which access tokens issued for this resource server via implicit or hybrid flows remain valid. Cannot be greater than the <code class="docutils literal notranslate"><span class="pre">token_lifetime</span></code> value.</p></li>
<li><p><strong>verification_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_offline_access</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforce_policies</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ResourceServerScopeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ResourceServerScopeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ResourceServerScopeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ResourceServerScopeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signing_alg</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signing_secret</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_consent_for_verifiable_first_party_clients</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_dialect</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_lifetime</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_lifetime_for_web</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification_location</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.ResourceServer" title="pulumi_auth0.ResourceServer">ResourceServer</a><a class="headerlink" href="#pulumi_auth0.ResourceServer.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing ResourceServer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_offline_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not refresh tokens can be issued for this resource server.</p></li>
<li><p><strong>enforce_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not authorization polices are enforced.</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Unique identifier for the resource server. Used as the audience parameter for authorization calls. Can not be changed once set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Friendly name for the resource server. Cannot include <code class="docutils literal notranslate"><span class="pre">&lt;</span></code> or <code class="docutils literal notranslate"><span class="pre">&gt;</span></code> characters.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Map(String). Used to store additional metadata</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ResourceServerScopeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Set(Resource).  List of permissions (scopes) used by this resource server. For details, see Scopes.</p></li>
<li><p><strong>signing_alg</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Algorithm used to sign JWTs. Options include <code class="docutils literal notranslate"><span class="pre">HS256</span></code> and <code class="docutils literal notranslate"><span class="pre">RS256</span></code>.</p></li>
<li><p><strong>signing_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Secret used to sign tokens when using symmetric algorithms (HS256).</p></li>
<li><p><strong>skip_consent_for_verifiable_first_party_clients</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not to skip user consent for applications flagged as first party.</p></li>
<li><p><strong>token_dialect</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Dialect of access tokens that should be issued for this resource server. Options include <code class="docutils literal notranslate"><span class="pre">access_token</span></code> or <code class="docutils literal notranslate"><span class="pre">access_token_authz</span></code> (includes permissions).</p></li>
<li><p><strong>token_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Integer. Number of seconds during which access tokens issued for this resource server from the token endpoint remain valid.</p></li>
<li><p><strong>token_lifetime_for_web</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Integer. Number of seconds during which access tokens issued for this resource server via implicit or hybrid flows remain valid. Cannot be greater than the <code class="docutils literal notranslate"><span class="pre">token_lifetime</span></code> value.</p></li>
<li><p><strong>verification_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.allow_offline_access">
<em class="property">property </em><code class="sig-name descname">allow_offline_access</code><a class="headerlink" href="#pulumi_auth0.ResourceServer.allow_offline_access" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not refresh tokens can be issued for this resource server.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.enforce_policies">
<em class="property">property </em><code class="sig-name descname">enforce_policies</code><a class="headerlink" href="#pulumi_auth0.ResourceServer.enforce_policies" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not authorization polices are enforced.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.identifier">
<em class="property">property </em><code class="sig-name descname">identifier</code><a class="headerlink" href="#pulumi_auth0.ResourceServer.identifier" title="Permalink to this definition"></a></dt>
<dd><p>String. Unique identifier for the resource server. Used as the audience parameter for authorization calls. Can not be changed once set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_auth0.ResourceServer.name" title="Permalink to this definition"></a></dt>
<dd><p>String. Friendly name for the resource server. Cannot include <code class="docutils literal notranslate"><span class="pre">&lt;</span></code> or <code class="docutils literal notranslate"><span class="pre">&gt;</span></code> characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.options">
<em class="property">property </em><code class="sig-name descname">options</code><a class="headerlink" href="#pulumi_auth0.ResourceServer.options" title="Permalink to this definition"></a></dt>
<dd><p>Map(String). Used to store additional metadata</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.scopes">
<em class="property">property </em><code class="sig-name descname">scopes</code><a class="headerlink" href="#pulumi_auth0.ResourceServer.scopes" title="Permalink to this definition"></a></dt>
<dd><p>Set(Resource).  List of permissions (scopes) used by this resource server. For details, see Scopes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.signing_alg">
<em class="property">property </em><code class="sig-name descname">signing_alg</code><a class="headerlink" href="#pulumi_auth0.ResourceServer.signing_alg" title="Permalink to this definition"></a></dt>
<dd><p>String. Algorithm used to sign JWTs. Options include <code class="docutils literal notranslate"><span class="pre">HS256</span></code> and <code class="docutils literal notranslate"><span class="pre">RS256</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.signing_secret">
<em class="property">property </em><code class="sig-name descname">signing_secret</code><a class="headerlink" href="#pulumi_auth0.ResourceServer.signing_secret" title="Permalink to this definition"></a></dt>
<dd><p>String. Secret used to sign tokens when using symmetric algorithms (HS256).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.skip_consent_for_verifiable_first_party_clients">
<em class="property">property </em><code class="sig-name descname">skip_consent_for_verifiable_first_party_clients</code><a class="headerlink" href="#pulumi_auth0.ResourceServer.skip_consent_for_verifiable_first_party_clients" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not to skip user consent for applications flagged as first party.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.token_dialect">
<em class="property">property </em><code class="sig-name descname">token_dialect</code><a class="headerlink" href="#pulumi_auth0.ResourceServer.token_dialect" title="Permalink to this definition"></a></dt>
<dd><p>String. Dialect of access tokens that should be issued for this resource server. Options include <code class="docutils literal notranslate"><span class="pre">access_token</span></code> or <code class="docutils literal notranslate"><span class="pre">access_token_authz</span></code> (includes permissions).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.token_lifetime">
<em class="property">property </em><code class="sig-name descname">token_lifetime</code><a class="headerlink" href="#pulumi_auth0.ResourceServer.token_lifetime" title="Permalink to this definition"></a></dt>
<dd><p>Integer. Number of seconds during which access tokens issued for this resource server from the token endpoint remain valid.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.token_lifetime_for_web">
<em class="property">property </em><code class="sig-name descname">token_lifetime_for_web</code><a class="headerlink" href="#pulumi_auth0.ResourceServer.token_lifetime_for_web" title="Permalink to this definition"></a></dt>
<dd><p>Integer. Number of seconds during which access tokens issued for this resource server via implicit or hybrid flows remain valid. Cannot be greater than the <code class="docutils literal notranslate"><span class="pre">token_lifetime</span></code> value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.verification_location">
<em class="property">property </em><code class="sig-name descname">verification_location</code><a class="headerlink" href="#pulumi_auth0.ResourceServer.verification_location" title="Permalink to this definition"></a></dt>
<dd><p>String</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ResourceServer.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.ResourceServer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ResourceServer.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Role">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RolePermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RolePermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RolePermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RolePermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Role" title="Permalink to this definition"></a></dt>
<dd><p>With this resource, you can created and manage collections of permissions that can be assigned to users, which are otherwise known as roles. Permissions (scopes) are created on auth0_resource_server, then associated with roles and optionally, users using this resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_resource_server</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">ResourceServer</span><span class="p">(</span><span class="s2">&quot;myResourceServer&quot;</span><span class="p">,</span>
    <span class="n">enforce_policies</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">identifier</span><span class="o">=</span><span class="s2">&quot;my-resource-server-identifier&quot;</span><span class="p">,</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[</span><span class="n">auth0</span><span class="o">.</span><span class="n">ResourceServerScopeArgs</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">&quot;read something&quot;</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="s2">&quot;read:something&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">signing_alg</span><span class="o">=</span><span class="s2">&quot;RS256&quot;</span><span class="p">,</span>
    <span class="n">skip_consent_for_verifiable_first_party_clients</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">token_lifetime</span><span class="o">=</span><span class="mi">86400</span><span class="p">)</span>
<span class="n">my_role</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;myRole&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Role Description...&quot;</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">[</span><span class="n">auth0</span><span class="o">.</span><span class="n">RolePermissionArgs</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;read:something&quot;</span><span class="p">,</span>
        <span class="n">resource_server_identifier</span><span class="o">=</span><span class="n">my_resource_server</span><span class="o">.</span><span class="n">identifier</span><span class="p">,</span>
    <span class="p">)])</span>
<span class="n">my_user</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;myUser&quot;</span><span class="p">,</span>
    <span class="n">connection_name</span><span class="o">=</span><span class="s2">&quot;Username-Password-Authentication&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;test@test.com&quot;</span><span class="p">,</span>
    <span class="n">nickname</span><span class="o">=</span><span class="s2">&quot;testnick&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;passpass$12$12&quot;</span><span class="p">,</span>
    <span class="n">roles</span><span class="o">=</span><span class="p">[</span><span class="n">my_role</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">user_id</span><span class="o">=</span><span class="s2">&quot;auth0|1234567890&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;testnick&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Description of the role.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name for this role.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RolePermissionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Set(Resource). Configuration settings for permissions (scopes) attached to the role. For details, see Permissions.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RolePermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RolePermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RolePermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RolePermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.Role" title="pulumi_auth0.Role">Role</a><a class="headerlink" href="#pulumi_auth0.Role.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Description of the role.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name for this role.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RolePermissionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Set(Resource). Configuration settings for permissions (scopes) attached to the role. For details, see Permissions.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Role.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_auth0.Role.description" title="Permalink to this definition"></a></dt>
<dd><p>String. Description of the role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Role.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_auth0.Role.name" title="Permalink to this definition"></a></dt>
<dd><p>String. Name for this role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Role.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_auth0.Role.permissions" title="Permalink to this definition"></a></dt>
<dd><p>Set(Resource). Configuration settings for permissions (scopes) attached to the role. For details, see Permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Role.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Role.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Role.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Role.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Rule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Rule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Rule" title="Permalink to this definition"></a></dt>
<dd><p>With Auth0, you can create custom Javascript snippets that run in a secure, isolated sandbox as part of your authentication pipeline, which are otherwise known as rules. This resource allows you to create and manage rules. You can create global variable for use with rules by using the RuleConfig resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_rule</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Rule</span><span class="p">(</span><span class="s2">&quot;myRule&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">script</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;function (user, context, callback) {</span>
<span class="s2">  callback(null, user, context);</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">my_rule_config</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">RuleConfig</span><span class="p">(</span><span class="s2">&quot;myRuleConfig&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;bar&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether the rule is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the rule. May only contain alphanumeric characters, spaces, and hyphens. May neither start nor end with hyphens or spaces.</p></li>
<li><p><strong>order</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Integer. Order in which the rule executes relative to other rules. Lower-valued rules execute first.</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Code to be executed when the rule runs.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.Rule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.Rule" title="pulumi_auth0.Rule">Rule</a><a class="headerlink" href="#pulumi_auth0.Rule.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Rule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether the rule is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the rule. May only contain alphanumeric characters, spaces, and hyphens. May neither start nor end with hyphens or spaces.</p></li>
<li><p><strong>order</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Integer. Order in which the rule executes relative to other rules. Lower-valued rules execute first.</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Code to be executed when the rule runs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Rule.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_auth0.Rule.enabled" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether the rule is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Rule.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_auth0.Rule.name" title="Permalink to this definition"></a></dt>
<dd><p>String. Name of the rule. May only contain alphanumeric characters, spaces, and hyphens. May neither start nor end with hyphens or spaces.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Rule.order">
<em class="property">property </em><code class="sig-name descname">order</code><a class="headerlink" href="#pulumi_auth0.Rule.order" title="Permalink to this definition"></a></dt>
<dd><p>Integer. Order in which the rule executes relative to other rules. Lower-valued rules execute first.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Rule.script">
<em class="property">property </em><code class="sig-name descname">script</code><a class="headerlink" href="#pulumi_auth0.Rule.script" title="Permalink to this definition"></a></dt>
<dd><p>String. Code to be executed when the rule runs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Rule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Rule.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Rule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Rule.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.RuleConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">RuleConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.RuleConfig" title="Permalink to this definition"></a></dt>
<dd><p>With Auth0, you can create custom Javascript snippets that run in a secure, isolated sandbox as part of your authentication pipeline, which are otherwise known as rules. This resource allows you to create and manage variables that are available to all rules via Auth0’s global configuration object. Used in conjunction with configured rules.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_rule</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Rule</span><span class="p">(</span><span class="s2">&quot;myRule&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">script</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;function (user, context, callback) {</span>
<span class="s2">  callback(null, user, context);</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">my_rule_config</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">RuleConfig</span><span class="p">(</span><span class="s2">&quot;myRuleConfig&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;bar&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Key for a rules configuration variable.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, Case-sensitive. Value for a rules configuration variable.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.RuleConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.RuleConfig" title="pulumi_auth0.RuleConfig">RuleConfig</a><a class="headerlink" href="#pulumi_auth0.RuleConfig.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing RuleConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Key for a rules configuration variable.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, Case-sensitive. Value for a rules configuration variable.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.RuleConfig.key">
<em class="property">property </em><code class="sig-name descname">key</code><a class="headerlink" href="#pulumi_auth0.RuleConfig.key" title="Permalink to this definition"></a></dt>
<dd><p>String. Key for a rules configuration variable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.RuleConfig.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_auth0.RuleConfig.value" title="Permalink to this definition"></a></dt>
<dd><p>String, Case-sensitive. Value for a rules configuration variable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.RuleConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.RuleConfig.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.RuleConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.RuleConfig.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Tenant">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Tenant</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_logout_urls</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">change_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>TenantChangePasswordArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TenantChangePasswordArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_audience</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_directory</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_redirection_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_locales</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_page</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>TenantErrorPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TenantErrorPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>TenantFlagsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TenantFlagsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">friendly_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guardian_mfa_page</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>TenantGuardianMfaPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TenantGuardianMfaPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idle_session_lifetime</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>float<span class="p">, </span>Awaitable<span class="p">[</span>float<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">picture_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sandbox_version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_lifetime</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>float<span class="p">, </span>Awaitable<span class="p">[</span>float<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">universal_login</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>TenantUniversalLoginArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TenantUniversalLoginArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Tenant" title="Permalink to this definition"></a></dt>
<dd><p>With this resource, you can manage Auth0 tenants, including setting logos and support contact information, setting error pages, and configuring default tenant behaviors.</p>
<blockquote>
<div><p>Auth0 does not currently support creating tenants through the Management API. Therefore this resource can only manage an existing tenant created through the Auth0 dashboard.</p>
</div></blockquote>
<p>Auth0 does not currently support adding/removing extensions on tenants through their API. The Auth0 dashboard must be used to add/remove extensions.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">tenant</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Tenant</span><span class="p">(</span><span class="s2">&quot;tenant&quot;</span><span class="p">,</span>
    <span class="n">allowed_logout_urls</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;http://mysite/logout&quot;</span><span class="p">],</span>
    <span class="n">change_password</span><span class="o">=</span><span class="n">auth0</span><span class="o">.</span><span class="n">TenantChangePasswordArgs</span><span class="p">(</span>
        <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">html</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;./password_reset.html&quot;</span><span class="p">),</span>
    <span class="p">),</span>
    <span class="n">default_audience</span><span class="o">=</span><span class="s2">&quot;&lt;client_id&gt;&quot;</span><span class="p">,</span>
    <span class="n">default_directory</span><span class="o">=</span><span class="s2">&quot;Connection-Name&quot;</span><span class="p">,</span>
    <span class="n">error_page</span><span class="o">=</span><span class="n">auth0</span><span class="o">.</span><span class="n">TenantErrorPageArgs</span><span class="p">(</span>
        <span class="n">html</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;./error.html&quot;</span><span class="p">),</span>
        <span class="n">show_log_link</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">url</span><span class="o">=</span><span class="s2">&quot;http://mysite/errors&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">friendly_name</span><span class="o">=</span><span class="s2">&quot;Tenant Name&quot;</span><span class="p">,</span>
    <span class="n">guardian_mfa_page</span><span class="o">=</span><span class="n">auth0</span><span class="o">.</span><span class="n">TenantGuardianMfaPageArgs</span><span class="p">(</span>
        <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">html</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;./guardian_multifactor.html&quot;</span><span class="p">),</span>
    <span class="p">),</span>
    <span class="n">picture_url</span><span class="o">=</span><span class="s2">&quot;http://mysite/logo.png&quot;</span><span class="p">,</span>
    <span class="n">sandbox_version</span><span class="o">=</span><span class="s2">&quot;8&quot;</span><span class="p">,</span>
    <span class="n">session_lifetime</span><span class="o">=</span><span class="mi">46000</span><span class="p">,</span>
    <span class="n">support_email</span><span class="o">=</span><span class="s2">&quot;support@mysite&quot;</span><span class="p">,</span>
    <span class="n">support_url</span><span class="o">=</span><span class="s2">&quot;http://mysite/support&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_logout_urls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). URLs that Auth0 may redirect to after logout.</p></li>
<li><p><strong>change_password</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TenantChangePasswordArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for change passsword page. For details, see Change Password Page.</p></li>
<li><p><strong>default_audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. API Audience to use by default for API Authorization flows. This setting is equivalent to appending the audience to every authorization request made to the tenant for every application.</p></li>
<li><p><strong>default_directory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the connection to be used for Password Grant exchanges. Options include <code class="docutils literal notranslate"><span class="pre">auth0-adldap</span></code>, <code class="docutils literal notranslate"><span class="pre">ad</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0</span></code>, <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">waad</span></code>, and <code class="docutils literal notranslate"><span class="pre">adfs</span></code>.</p></li>
<li><p><strong>default_redirection_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. The default absolute redirection uri, must be https and cannot contain a fragment.</p></li>
<li><p><strong>error_page</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TenantErrorPageArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for error pages. For details, see Error Page.</p></li>
<li><p><strong>flags</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TenantFlagsArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for tenant flags. For details, see Flags.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Friendly name for the tenant.</p></li>
<li><p><strong>guardian_mfa_page</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TenantGuardianMfaPageArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for the Guardian MFA page. For details, see Guardian MFA Page.</p></li>
<li><p><strong>idle_session_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Number of hours during which a session can be inactive before the user must log in again.</p></li>
<li><p><strong>picture_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – . String URL of logo to be shown for the tenant. Recommended size is 150px x 150px. If no URL is provided, the Auth0 logo will be used.</p></li>
<li><p><strong>sandbox_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Selected sandbox version for the extensibility environment, which allows you to use custom scripts to extend parts of Auth0’s functionality.</p></li>
<li><p><strong>session_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Number of hours during which a session will stay valid.</p></li>
<li><p><strong>support_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Support email address for authenticating users.</p></li>
<li><p><strong>support_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Support URL for authenticating users.</p></li>
<li><p><strong>universal_login</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TenantUniversalLoginArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for Universal Login. For details, see Universal Login.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.Tenant.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_logout_urls</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">change_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>TenantChangePasswordArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TenantChangePasswordArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_audience</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_directory</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_redirection_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_locales</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_page</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>TenantErrorPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TenantErrorPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>TenantFlagsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TenantFlagsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">friendly_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guardian_mfa_page</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>TenantGuardianMfaPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TenantGuardianMfaPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idle_session_lifetime</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>float<span class="p">, </span>Awaitable<span class="p">[</span>float<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">picture_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sandbox_version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_lifetime</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>float<span class="p">, </span>Awaitable<span class="p">[</span>float<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">universal_login</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>TenantUniversalLoginArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TenantUniversalLoginArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.Tenant" title="pulumi_auth0.Tenant">Tenant</a><a class="headerlink" href="#pulumi_auth0.Tenant.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Tenant resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_logout_urls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List(String). URLs that Auth0 may redirect to after logout.</p></li>
<li><p><strong>change_password</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TenantChangePasswordArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for change passsword page. For details, see Change Password Page.</p></li>
<li><p><strong>default_audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. API Audience to use by default for API Authorization flows. This setting is equivalent to appending the audience to every authorization request made to the tenant for every application.</p></li>
<li><p><strong>default_directory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the connection to be used for Password Grant exchanges. Options include <code class="docutils literal notranslate"><span class="pre">auth0-adldap</span></code>, <code class="docutils literal notranslate"><span class="pre">ad</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0</span></code>, <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">waad</span></code>, and <code class="docutils literal notranslate"><span class="pre">adfs</span></code>.</p></li>
<li><p><strong>default_redirection_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. The default absolute redirection uri, must be https and cannot contain a fragment.</p></li>
<li><p><strong>error_page</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TenantErrorPageArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for error pages. For details, see Error Page.</p></li>
<li><p><strong>flags</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TenantFlagsArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for tenant flags. For details, see Flags.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Friendly name for the tenant.</p></li>
<li><p><strong>guardian_mfa_page</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TenantGuardianMfaPageArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for the Guardian MFA page. For details, see Guardian MFA Page.</p></li>
<li><p><strong>idle_session_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Number of hours during which a session can be inactive before the user must log in again.</p></li>
<li><p><strong>picture_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – . String URL of logo to be shown for the tenant. Recommended size is 150px x 150px. If no URL is provided, the Auth0 logo will be used.</p></li>
<li><p><strong>sandbox_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Selected sandbox version for the extensibility environment, which allows you to use custom scripts to extend parts of Auth0’s functionality.</p></li>
<li><p><strong>session_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Number of hours during which a session will stay valid.</p></li>
<li><p><strong>support_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Support email address for authenticating users.</p></li>
<li><p><strong>support_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Support URL for authenticating users.</p></li>
<li><p><strong>universal_login</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TenantUniversalLoginArgs'</em><em>]</em><em>]</em>) – List(Resource). Configuration settings for Universal Login. For details, see Universal Login.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.allowed_logout_urls">
<em class="property">property </em><code class="sig-name descname">allowed_logout_urls</code><a class="headerlink" href="#pulumi_auth0.Tenant.allowed_logout_urls" title="Permalink to this definition"></a></dt>
<dd><p>List(String). URLs that Auth0 may redirect to after logout.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.change_password">
<em class="property">property </em><code class="sig-name descname">change_password</code><a class="headerlink" href="#pulumi_auth0.Tenant.change_password" title="Permalink to this definition"></a></dt>
<dd><p>List(Resource). Configuration settings for change passsword page. For details, see Change Password Page.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.default_audience">
<em class="property">property </em><code class="sig-name descname">default_audience</code><a class="headerlink" href="#pulumi_auth0.Tenant.default_audience" title="Permalink to this definition"></a></dt>
<dd><p>String. API Audience to use by default for API Authorization flows. This setting is equivalent to appending the audience to every authorization request made to the tenant for every application.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.default_directory">
<em class="property">property </em><code class="sig-name descname">default_directory</code><a class="headerlink" href="#pulumi_auth0.Tenant.default_directory" title="Permalink to this definition"></a></dt>
<dd><p>String. Name of the connection to be used for Password Grant exchanges. Options include <code class="docutils literal notranslate"><span class="pre">auth0-adldap</span></code>, <code class="docutils literal notranslate"><span class="pre">ad</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0</span></code>, <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">waad</span></code>, and <code class="docutils literal notranslate"><span class="pre">adfs</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.default_redirection_uri">
<em class="property">property </em><code class="sig-name descname">default_redirection_uri</code><a class="headerlink" href="#pulumi_auth0.Tenant.default_redirection_uri" title="Permalink to this definition"></a></dt>
<dd><p>String. The default absolute redirection uri, must be https and cannot contain a fragment.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.error_page">
<em class="property">property </em><code class="sig-name descname">error_page</code><a class="headerlink" href="#pulumi_auth0.Tenant.error_page" title="Permalink to this definition"></a></dt>
<dd><p>List(Resource). Configuration settings for error pages. For details, see Error Page.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.flags">
<em class="property">property </em><code class="sig-name descname">flags</code><a class="headerlink" href="#pulumi_auth0.Tenant.flags" title="Permalink to this definition"></a></dt>
<dd><p>List(Resource). Configuration settings for tenant flags. For details, see Flags.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.friendly_name">
<em class="property">property </em><code class="sig-name descname">friendly_name</code><a class="headerlink" href="#pulumi_auth0.Tenant.friendly_name" title="Permalink to this definition"></a></dt>
<dd><p>String. Friendly name for the tenant.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.guardian_mfa_page">
<em class="property">property </em><code class="sig-name descname">guardian_mfa_page</code><a class="headerlink" href="#pulumi_auth0.Tenant.guardian_mfa_page" title="Permalink to this definition"></a></dt>
<dd><p>List(Resource). Configuration settings for the Guardian MFA page. For details, see Guardian MFA Page.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.idle_session_lifetime">
<em class="property">property </em><code class="sig-name descname">idle_session_lifetime</code><a class="headerlink" href="#pulumi_auth0.Tenant.idle_session_lifetime" title="Permalink to this definition"></a></dt>
<dd><p>Integer. Number of hours during which a session can be inactive before the user must log in again.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.picture_url">
<em class="property">property </em><code class="sig-name descname">picture_url</code><a class="headerlink" href="#pulumi_auth0.Tenant.picture_url" title="Permalink to this definition"></a></dt>
<dd><p>. String URL of logo to be shown for the tenant. Recommended size is 150px x 150px. If no URL is provided, the Auth0 logo will be used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.sandbox_version">
<em class="property">property </em><code class="sig-name descname">sandbox_version</code><a class="headerlink" href="#pulumi_auth0.Tenant.sandbox_version" title="Permalink to this definition"></a></dt>
<dd><p>String. Selected sandbox version for the extensibility environment, which allows you to use custom scripts to extend parts of Auth0’s functionality.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.session_lifetime">
<em class="property">property </em><code class="sig-name descname">session_lifetime</code><a class="headerlink" href="#pulumi_auth0.Tenant.session_lifetime" title="Permalink to this definition"></a></dt>
<dd><p>Integer. Number of hours during which a session will stay valid.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.support_email">
<em class="property">property </em><code class="sig-name descname">support_email</code><a class="headerlink" href="#pulumi_auth0.Tenant.support_email" title="Permalink to this definition"></a></dt>
<dd><p>String. Support email address for authenticating users.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.support_url">
<em class="property">property </em><code class="sig-name descname">support_url</code><a class="headerlink" href="#pulumi_auth0.Tenant.support_url" title="Permalink to this definition"></a></dt>
<dd><p>String. Support URL for authenticating users.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.universal_login">
<em class="property">property </em><code class="sig-name descname">universal_login</code><a class="headerlink" href="#pulumi_auth0.Tenant.universal_login" title="Permalink to this definition"></a></dt>
<dd><p>List(Resource). Configuration settings for Universal Login. For details, see Universal Login.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Tenant.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.Tenant.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Tenant.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_metadata</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocked</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_verified</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">family_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">given_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nickname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">phone_number</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">phone_verified</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">picture</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_metadata</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verify_email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.User" title="Permalink to this definition"></a></dt>
<dd><p>With this resource, you can manage user identities, including resetting passwords, and creating, provisioning, blocking, and deleting users.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">admin</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Administrator&quot;</span><span class="p">)</span>
<span class="n">user</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
    <span class="n">connection_name</span><span class="o">=</span><span class="s2">&quot;Username-Password-Authentication&quot;</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;unique_username&quot;</span><span class="p">,</span>
    <span class="n">given_name</span><span class="o">=</span><span class="s2">&quot;Firstname&quot;</span><span class="p">,</span>
    <span class="n">family_name</span><span class="o">=</span><span class="s2">&quot;Lastname&quot;</span><span class="p">,</span>
    <span class="n">nickname</span><span class="o">=</span><span class="s2">&quot;some.nickname&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;test@test.com&quot;</span><span class="p">,</span>
    <span class="n">email_verified</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;passpass$12$12&quot;</span><span class="p">,</span>
    <span class="n">roles</span><span class="o">=</span><span class="p">[</span><span class="n">admin</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, JSON format. Custom fields that store info about the user that impact the user’s core functionality, such as how an application functions or what the user can access. Examples include support plans and IDs for external accounts.</p></li>
<li><p><strong>connection_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the connection from which the user information was sourced.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Email address of the user.</p></li>
<li><p><strong>email_verified</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the email address has been verified.</p></li>
<li><p><strong>nickname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Preferred nickname or alias of the user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, Case-sensitive. Initial password for this user. Used for non-SMS connections.</p></li>
<li><p><strong>phone_number</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Phone number for the user; follows the E.164 recommendation. Used for SMS connections.</p></li>
<li><p><strong>phone_verified</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the phone number has been verified.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Set(String). Set of IDs of roles assigned to the user.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. ID of the user.</p></li>
<li><p><strong>user_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, JSON format. Custom fields that store info about the user that does not impact a user’s core functionality. Examples include work address, home address, and user preferences.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Username of the user. Only valid if the connection requires a username.</p></li>
<li><p><strong>verify_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the user will receive a verification email after creation. Overrides behavior of <code class="docutils literal notranslate"><span class="pre">email_verified</span></code> parameter.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_metadata</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocked</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_verified</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">family_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">given_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nickname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">phone_number</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">phone_verified</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">picture</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_metadata</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verify_email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_auth0.User" title="pulumi_auth0.User">User</a><a class="headerlink" href="#pulumi_auth0.User.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, JSON format. Custom fields that store info about the user that impact the user’s core functionality, such as how an application functions or what the user can access. Examples include support plans and IDs for external accounts.</p></li>
<li><p><strong>connection_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the connection from which the user information was sourced.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Email address of the user.</p></li>
<li><p><strong>email_verified</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the email address has been verified.</p></li>
<li><p><strong>nickname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Preferred nickname or alias of the user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, Case-sensitive. Initial password for this user. Used for non-SMS connections.</p></li>
<li><p><strong>phone_number</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Phone number for the user; follows the E.164 recommendation. Used for SMS connections.</p></li>
<li><p><strong>phone_verified</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the phone number has been verified.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Set(String). Set of IDs of roles assigned to the user.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. ID of the user.</p></li>
<li><p><strong>user_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, JSON format. Custom fields that store info about the user that does not impact a user’s core functionality. Examples include work address, home address, and user preferences.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Username of the user. Only valid if the connection requires a username.</p></li>
<li><p><strong>verify_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the user will receive a verification email after creation. Overrides behavior of <code class="docutils literal notranslate"><span class="pre">email_verified</span></code> parameter.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.app_metadata">
<em class="property">property </em><code class="sig-name descname">app_metadata</code><a class="headerlink" href="#pulumi_auth0.User.app_metadata" title="Permalink to this definition"></a></dt>
<dd><p>String, JSON format. Custom fields that store info about the user that impact the user’s core functionality, such as how an application functions or what the user can access. Examples include support plans and IDs for external accounts.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.connection_name">
<em class="property">property </em><code class="sig-name descname">connection_name</code><a class="headerlink" href="#pulumi_auth0.User.connection_name" title="Permalink to this definition"></a></dt>
<dd><p>String. Name of the connection from which the user information was sourced.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_auth0.User.email" title="Permalink to this definition"></a></dt>
<dd><p>String. Email address of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.email_verified">
<em class="property">property </em><code class="sig-name descname">email_verified</code><a class="headerlink" href="#pulumi_auth0.User.email_verified" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not the email address has been verified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.nickname">
<em class="property">property </em><code class="sig-name descname">nickname</code><a class="headerlink" href="#pulumi_auth0.User.nickname" title="Permalink to this definition"></a></dt>
<dd><p>String. Preferred nickname or alias of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.password">
<em class="property">property </em><code class="sig-name descname">password</code><a class="headerlink" href="#pulumi_auth0.User.password" title="Permalink to this definition"></a></dt>
<dd><p>String, Case-sensitive. Initial password for this user. Used for non-SMS connections.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.phone_number">
<em class="property">property </em><code class="sig-name descname">phone_number</code><a class="headerlink" href="#pulumi_auth0.User.phone_number" title="Permalink to this definition"></a></dt>
<dd><p>String. Phone number for the user; follows the E.164 recommendation. Used for SMS connections.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.phone_verified">
<em class="property">property </em><code class="sig-name descname">phone_verified</code><a class="headerlink" href="#pulumi_auth0.User.phone_verified" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not the phone number has been verified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.roles">
<em class="property">property </em><code class="sig-name descname">roles</code><a class="headerlink" href="#pulumi_auth0.User.roles" title="Permalink to this definition"></a></dt>
<dd><p>Set(String). Set of IDs of roles assigned to the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.user_id">
<em class="property">property </em><code class="sig-name descname">user_id</code><a class="headerlink" href="#pulumi_auth0.User.user_id" title="Permalink to this definition"></a></dt>
<dd><p>String. ID of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.user_metadata">
<em class="property">property </em><code class="sig-name descname">user_metadata</code><a class="headerlink" href="#pulumi_auth0.User.user_metadata" title="Permalink to this definition"></a></dt>
<dd><p>String, JSON format. Custom fields that store info about the user that does not impact a user’s core functionality. Examples include work address, home address, and user preferences.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_auth0.User.username" title="Permalink to this definition"></a></dt>
<dd><p>String. Username of the user. Only valid if the connection requires a username.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.verify_email">
<em class="property">property </em><code class="sig-name descname">verify_email</code><a class="headerlink" href="#pulumi_auth0.User.verify_email" title="Permalink to this definition"></a></dt>
<dd><p>Boolean. Indicates whether or not the user will receive a verification email after creation. Overrides behavior of <code class="docutils literal notranslate"><span class="pre">email_verified</span></code> parameter.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.User.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_auth0.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.User.translate_input_property" title="Permalink to this definition"></a></dt>
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
