
---
title: "Mfa"
block_external_search_index: true
---



Creates an MFA Policy.

This resource allows you to create and configure an MFA Policy.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as okta from "@pulumi/okta";

const example = new okta.policy.Mfa("example", {
    description: "Example",
    groupsIncludeds: [okta_group_everyone.id],
    oktaOtp: {
        enroll: "REQUIRED",
    },
    status: "ACTIVE",
});
```

> This content is derived from https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/policy_mfa.html.markdown.



## Create a Mfa Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/policy/#Mfa">Mfa</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/policy/#MfaArgs">MfaArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Mfa</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>duo=None<span class="p">, </span>fido_u2f=None<span class="p">, </span>fido_webauthn=None<span class="p">, </span>google_otp=None<span class="p">, </span>groups_includeds=None<span class="p">, </span>name=None<span class="p">, </span>okta_call=None<span class="p">, </span>okta_otp=None<span class="p">, </span>okta_password=None<span class="p">, </span>okta_push=None<span class="p">, </span>okta_question=None<span class="p">, </span>okta_sms=None<span class="p">, </span>priority=None<span class="p">, </span>rsa_token=None<span class="p">, </span>status=None<span class="p">, </span>symantec_vip=None<span class="p">, </span>yubikey_token=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewMfa<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaArgs">MfaArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#Mfa">Mfa</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Policy.Mfa.html">Mfa</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Policy.MfaArgs.html">MfaArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Duo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaduo">Mfa<wbr>Duo<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}DUO MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fido<wbr>U2f</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidou2f">Mfa<wbr>Fido<wbr>U2f<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Fido U2F MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fido<wbr>Webauthn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidowebauthn">Mfa<wbr>Fido<wbr>Webauthn<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Fido Web Authn MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Google<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfagoogleotp">Mfa<wbr>Google<wbr>Otp<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Google OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Groups<wbr>Includeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of Group IDs to Include.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Call</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktacall">Mfa<wbr>Okta<wbr>Call<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Okta Call MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaotp">Mfa<wbr>Okta<wbr>Otp<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Okta OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapassword">Mfa<wbr>Okta<wbr>Password<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Okta Password MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Push</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapush">Mfa<wbr>Okta<wbr>Push<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Okta Push MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Question</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaquestion">Mfa<wbr>Okta<wbr>Question<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Okta Question MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Sms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktasms">Mfa<wbr>Okta<wbr>Sms<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Okta SMS MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Priority of the policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rsa<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfarsatoken">Mfa<wbr>Rsa<wbr>Token<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}RSA Token MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Status: `"ACTIVE"` or `"INACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Symantec<wbr>Vip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfasymantecvip">Mfa<wbr>Symantec<wbr>Vip<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Symantec VIP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Yubikey<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfayubikeytoken">Mfa<wbr>Yubikey<wbr>Token<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Yubikey Token MFA policy settings.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Policy Description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Duo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaduo">*Mfa<wbr>Duo</a></span>
    </dt>
    <dd>{{% md %}}DUO MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fido<wbr>U2f</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidou2f">*Mfa<wbr>Fido<wbr>U2f</a></span>
    </dt>
    <dd>{{% md %}}Fido U2F MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fido<wbr>Webauthn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidowebauthn">*Mfa<wbr>Fido<wbr>Webauthn</a></span>
    </dt>
    <dd>{{% md %}}Fido Web Authn MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Google<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfagoogleotp">*Mfa<wbr>Google<wbr>Otp</a></span>
    </dt>
    <dd>{{% md %}}Google OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Groups<wbr>Includeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of Group IDs to Include.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Policy Name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Call</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktacall">*Mfa<wbr>Okta<wbr>Call</a></span>
    </dt>
    <dd>{{% md %}}Okta Call MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaotp">*Mfa<wbr>Okta<wbr>Otp</a></span>
    </dt>
    <dd>{{% md %}}Okta OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapassword">*Mfa<wbr>Okta<wbr>Password</a></span>
    </dt>
    <dd>{{% md %}}Okta Password MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Push</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapush">*Mfa<wbr>Okta<wbr>Push</a></span>
    </dt>
    <dd>{{% md %}}Okta Push MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Question</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaquestion">*Mfa<wbr>Okta<wbr>Question</a></span>
    </dt>
    <dd>{{% md %}}Okta Question MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Sms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktasms">*Mfa<wbr>Okta<wbr>Sms</a></span>
    </dt>
    <dd>{{% md %}}Okta SMS MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Priority of the policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rsa<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfarsatoken">*Mfa<wbr>Rsa<wbr>Token</a></span>
    </dt>
    <dd>{{% md %}}RSA Token MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Policy Status: `"ACTIVE"` or `"INACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Symantec<wbr>Vip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfasymantecvip">*Mfa<wbr>Symantec<wbr>Vip</a></span>
    </dt>
    <dd>{{% md %}}Symantec VIP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Yubikey<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfayubikeytoken">*Mfa<wbr>Yubikey<wbr>Token</a></span>
    </dt>
    <dd>{{% md %}}Yubikey Token MFA policy settings.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>duo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaduo">Mfa<wbr>Duo?</a></span>
    </dt>
    <dd>{{% md %}}DUO MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fido<wbr>U2f</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidou2f">Mfa<wbr>Fido<wbr>U2f?</a></span>
    </dt>
    <dd>{{% md %}}Fido U2F MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fido<wbr>Webauthn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidowebauthn">Mfa<wbr>Fido<wbr>Webauthn?</a></span>
    </dt>
    <dd>{{% md %}}Fido Web Authn MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>google<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfagoogleotp">Mfa<wbr>Google<wbr>Otp?</a></span>
    </dt>
    <dd>{{% md %}}Google OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>groups<wbr>Includeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of Group IDs to Include.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta<wbr>Call</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktacall">Mfa<wbr>Okta<wbr>Call?</a></span>
    </dt>
    <dd>{{% md %}}Okta Call MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaotp">Mfa<wbr>Okta<wbr>Otp?</a></span>
    </dt>
    <dd>{{% md %}}Okta OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapassword">Mfa<wbr>Okta<wbr>Password?</a></span>
    </dt>
    <dd>{{% md %}}Okta Password MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta<wbr>Push</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapush">Mfa<wbr>Okta<wbr>Push?</a></span>
    </dt>
    <dd>{{% md %}}Okta Push MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta<wbr>Question</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaquestion">Mfa<wbr>Okta<wbr>Question?</a></span>
    </dt>
    <dd>{{% md %}}Okta Question MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta<wbr>Sms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktasms">Mfa<wbr>Okta<wbr>Sms?</a></span>
    </dt>
    <dd>{{% md %}}Okta SMS MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Priority of the policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rsa<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfarsatoken">Mfa<wbr>Rsa<wbr>Token?</a></span>
    </dt>
    <dd>{{% md %}}RSA Token MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Status: `"ACTIVE"` or `"INACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>symantec<wbr>Vip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfasymantecvip">Mfa<wbr>Symantec<wbr>Vip?</a></span>
    </dt>
    <dd>{{% md %}}Symantec VIP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>yubikey<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfayubikeytoken">Mfa<wbr>Yubikey<wbr>Token?</a></span>
    </dt>
    <dd>{{% md %}}Yubikey Token MFA policy settings.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Policy Description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>duo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaduo">Dict[Mfa<wbr>Duo]</a></span>
    </dt>
    <dd>{{% md %}}DUO MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fido_<wbr>u2f</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidou2f">Dict[Mfa<wbr>Fido<wbr>U2f]</a></span>
    </dt>
    <dd>{{% md %}}Fido U2F MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fido_<wbr>webauthn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidowebauthn">Dict[Mfa<wbr>Fido<wbr>Webauthn]</a></span>
    </dt>
    <dd>{{% md %}}Fido Web Authn MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>google_<wbr>otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfagoogleotp">Dict[Mfa<wbr>Google<wbr>Otp]</a></span>
    </dt>
    <dd>{{% md %}}Google OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>groups_<wbr>includeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of Group IDs to Include.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Policy Name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta_<wbr>call</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktacall">Dict[Mfa<wbr>Okta<wbr>Call]</a></span>
    </dt>
    <dd>{{% md %}}Okta Call MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta_<wbr>otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaotp">Dict[Mfa<wbr>Okta<wbr>Otp]</a></span>
    </dt>
    <dd>{{% md %}}Okta OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta_<wbr>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapassword">Dict[Mfa<wbr>Okta<wbr>Password]</a></span>
    </dt>
    <dd>{{% md %}}Okta Password MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta_<wbr>push</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapush">Dict[Mfa<wbr>Okta<wbr>Push]</a></span>
    </dt>
    <dd>{{% md %}}Okta Push MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta_<wbr>question</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaquestion">Dict[Mfa<wbr>Okta<wbr>Question]</a></span>
    </dt>
    <dd>{{% md %}}Okta Question MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta_<wbr>sms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktasms">Dict[Mfa<wbr>Okta<wbr>Sms]</a></span>
    </dt>
    <dd>{{% md %}}Okta SMS MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Priority of the policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rsa_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfarsatoken">Dict[Mfa<wbr>Rsa<wbr>Token]</a></span>
    </dt>
    <dd>{{% md %}}RSA Token MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Policy Status: `"ACTIVE"` or `"INACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>symantec_<wbr>vip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfasymantecvip">Dict[Mfa<wbr>Symantec<wbr>Vip]</a></span>
    </dt>
    <dd>{{% md %}}Symantec VIP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>yubikey_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfayubikeytoken">Dict[Mfa<wbr>Yubikey<wbr>Token]</a></span>
    </dt>
    <dd>{{% md %}}Yubikey Token MFA policy settings.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Mfa Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Description.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Duo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaduo">Mfa<wbr>Duo?</a></span>
    </dt>
    <dd>{{% md %}}DUO MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fido<wbr>U2f</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidou2f">Mfa<wbr>Fido<wbr>U2f?</a></span>
    </dt>
    <dd>{{% md %}}Fido U2F MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fido<wbr>Webauthn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidowebauthn">Mfa<wbr>Fido<wbr>Webauthn?</a></span>
    </dt>
    <dd>{{% md %}}Fido Web Authn MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Google<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfagoogleotp">Mfa<wbr>Google<wbr>Otp?</a></span>
    </dt>
    <dd>{{% md %}}Google OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Groups<wbr>Includeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of Group IDs to Include.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Policy Name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Okta<wbr>Call</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktacall">Mfa<wbr>Okta<wbr>Call?</a></span>
    </dt>
    <dd>{{% md %}}Okta Call MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Okta<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaotp">Mfa<wbr>Okta<wbr>Otp?</a></span>
    </dt>
    <dd>{{% md %}}Okta OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Okta<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapassword">Mfa<wbr>Okta<wbr>Password?</a></span>
    </dt>
    <dd>{{% md %}}Okta Password MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Okta<wbr>Push</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapush">Mfa<wbr>Okta<wbr>Push?</a></span>
    </dt>
    <dd>{{% md %}}Okta Push MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Okta<wbr>Question</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaquestion">Mfa<wbr>Okta<wbr>Question?</a></span>
    </dt>
    <dd>{{% md %}}Okta Question MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Okta<wbr>Sms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktasms">Mfa<wbr>Okta<wbr>Sms?</a></span>
    </dt>
    <dd>{{% md %}}Okta SMS MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Priority of the policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Rsa<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfarsatoken">Mfa<wbr>Rsa<wbr>Token?</a></span>
    </dt>
    <dd>{{% md %}}RSA Token MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Status: `"ACTIVE"` or `"INACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Symantec<wbr>Vip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfasymantecvip">Mfa<wbr>Symantec<wbr>Vip?</a></span>
    </dt>
    <dd>{{% md %}}Symantec VIP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Yubikey<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfayubikeytoken">Mfa<wbr>Yubikey<wbr>Token?</a></span>
    </dt>
    <dd>{{% md %}}Yubikey Token MFA policy settings.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Policy Description.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Duo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaduo">*Mfa<wbr>Duo</a></span>
    </dt>
    <dd>{{% md %}}DUO MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fido<wbr>U2f</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidou2f">*Mfa<wbr>Fido<wbr>U2f</a></span>
    </dt>
    <dd>{{% md %}}Fido U2F MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fido<wbr>Webauthn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidowebauthn">*Mfa<wbr>Fido<wbr>Webauthn</a></span>
    </dt>
    <dd>{{% md %}}Fido Web Authn MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Google<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfagoogleotp">*Mfa<wbr>Google<wbr>Otp</a></span>
    </dt>
    <dd>{{% md %}}Google OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Groups<wbr>Includeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of Group IDs to Include.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Policy Name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Okta<wbr>Call</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktacall">*Mfa<wbr>Okta<wbr>Call</a></span>
    </dt>
    <dd>{{% md %}}Okta Call MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Okta<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaotp">*Mfa<wbr>Okta<wbr>Otp</a></span>
    </dt>
    <dd>{{% md %}}Okta OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Okta<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapassword">*Mfa<wbr>Okta<wbr>Password</a></span>
    </dt>
    <dd>{{% md %}}Okta Password MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Okta<wbr>Push</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapush">*Mfa<wbr>Okta<wbr>Push</a></span>
    </dt>
    <dd>{{% md %}}Okta Push MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Okta<wbr>Question</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaquestion">*Mfa<wbr>Okta<wbr>Question</a></span>
    </dt>
    <dd>{{% md %}}Okta Question MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Okta<wbr>Sms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktasms">*Mfa<wbr>Okta<wbr>Sms</a></span>
    </dt>
    <dd>{{% md %}}Okta SMS MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Priority of the policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Rsa<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfarsatoken">*Mfa<wbr>Rsa<wbr>Token</a></span>
    </dt>
    <dd>{{% md %}}RSA Token MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Policy Status: `"ACTIVE"` or `"INACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Symantec<wbr>Vip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfasymantecvip">*Mfa<wbr>Symantec<wbr>Vip</a></span>
    </dt>
    <dd>{{% md %}}Symantec VIP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Yubikey<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfayubikeytoken">*Mfa<wbr>Yubikey<wbr>Token</a></span>
    </dt>
    <dd>{{% md %}}Yubikey Token MFA policy settings.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Description.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>duo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaduo">Mfa<wbr>Duo?</a></span>
    </dt>
    <dd>{{% md %}}DUO MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fido<wbr>U2f</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidou2f">Mfa<wbr>Fido<wbr>U2f?</a></span>
    </dt>
    <dd>{{% md %}}Fido U2F MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fido<wbr>Webauthn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidowebauthn">Mfa<wbr>Fido<wbr>Webauthn?</a></span>
    </dt>
    <dd>{{% md %}}Fido Web Authn MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>google<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfagoogleotp">Mfa<wbr>Google<wbr>Otp?</a></span>
    </dt>
    <dd>{{% md %}}Google OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>groups<wbr>Includeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of Group IDs to Include.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Policy Name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>okta<wbr>Call</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktacall">Mfa<wbr>Okta<wbr>Call?</a></span>
    </dt>
    <dd>{{% md %}}Okta Call MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>okta<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaotp">Mfa<wbr>Okta<wbr>Otp?</a></span>
    </dt>
    <dd>{{% md %}}Okta OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>okta<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapassword">Mfa<wbr>Okta<wbr>Password?</a></span>
    </dt>
    <dd>{{% md %}}Okta Password MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>okta<wbr>Push</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapush">Mfa<wbr>Okta<wbr>Push?</a></span>
    </dt>
    <dd>{{% md %}}Okta Push MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>okta<wbr>Question</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaquestion">Mfa<wbr>Okta<wbr>Question?</a></span>
    </dt>
    <dd>{{% md %}}Okta Question MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>okta<wbr>Sms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktasms">Mfa<wbr>Okta<wbr>Sms?</a></span>
    </dt>
    <dd>{{% md %}}Okta SMS MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Priority of the policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>rsa<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfarsatoken">Mfa<wbr>Rsa<wbr>Token?</a></span>
    </dt>
    <dd>{{% md %}}RSA Token MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Status: `"ACTIVE"` or `"INACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>symantec<wbr>Vip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfasymantecvip">Mfa<wbr>Symantec<wbr>Vip?</a></span>
    </dt>
    <dd>{{% md %}}Symantec VIP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>yubikey<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfayubikeytoken">Mfa<wbr>Yubikey<wbr>Token?</a></span>
    </dt>
    <dd>{{% md %}}Yubikey Token MFA policy settings.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Policy Description.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>duo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaduo">Dict[Mfa<wbr>Duo]</a></span>
    </dt>
    <dd>{{% md %}}DUO MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fido_<wbr>u2f</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidou2f">Dict[Mfa<wbr>Fido<wbr>U2f]</a></span>
    </dt>
    <dd>{{% md %}}Fido U2F MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fido_<wbr>webauthn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidowebauthn">Dict[Mfa<wbr>Fido<wbr>Webauthn]</a></span>
    </dt>
    <dd>{{% md %}}Fido Web Authn MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>google_<wbr>otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfagoogleotp">Dict[Mfa<wbr>Google<wbr>Otp]</a></span>
    </dt>
    <dd>{{% md %}}Google OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>groups_<wbr>includeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of Group IDs to Include.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Policy Name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>okta_<wbr>call</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktacall">Dict[Mfa<wbr>Okta<wbr>Call]</a></span>
    </dt>
    <dd>{{% md %}}Okta Call MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>okta_<wbr>otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaotp">Dict[Mfa<wbr>Okta<wbr>Otp]</a></span>
    </dt>
    <dd>{{% md %}}Okta OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>okta_<wbr>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapassword">Dict[Mfa<wbr>Okta<wbr>Password]</a></span>
    </dt>
    <dd>{{% md %}}Okta Password MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>okta_<wbr>push</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapush">Dict[Mfa<wbr>Okta<wbr>Push]</a></span>
    </dt>
    <dd>{{% md %}}Okta Push MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>okta_<wbr>question</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaquestion">Dict[Mfa<wbr>Okta<wbr>Question]</a></span>
    </dt>
    <dd>{{% md %}}Okta Question MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>okta_<wbr>sms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktasms">Dict[Mfa<wbr>Okta<wbr>Sms]</a></span>
    </dt>
    <dd>{{% md %}}Okta SMS MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Priority of the policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>rsa_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfarsatoken">Dict[Mfa<wbr>Rsa<wbr>Token]</a></span>
    </dt>
    <dd>{{% md %}}RSA Token MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Policy Status: `"ACTIVE"` or `"INACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>symantec_<wbr>vip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfasymantecvip">Dict[Mfa<wbr>Symantec<wbr>Vip]</a></span>
    </dt>
    <dd>{{% md %}}Symantec VIP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>yubikey_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfayubikeytoken">Dict[Mfa<wbr>Yubikey<wbr>Token]</a></span>
    </dt>
    <dd>{{% md %}}Yubikey Token MFA policy settings.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Mfa Resource

Get an existing Mfa resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/policy/#MfaState">MfaState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/policy/#Mfa">Mfa</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>description=None<span class="p">, </span>duo=None<span class="p">, </span>fido_u2f=None<span class="p">, </span>fido_webauthn=None<span class="p">, </span>google_otp=None<span class="p">, </span>groups_includeds=None<span class="p">, </span>name=None<span class="p">, </span>okta_call=None<span class="p">, </span>okta_otp=None<span class="p">, </span>okta_password=None<span class="p">, </span>okta_push=None<span class="p">, </span>okta_question=None<span class="p">, </span>okta_sms=None<span class="p">, </span>priority=None<span class="p">, </span>rsa_token=None<span class="p">, </span>status=None<span class="p">, </span>symantec_vip=None<span class="p">, </span>yubikey_token=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetMfa<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaState">MfaState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#Mfa">Mfa</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Policy.Mfa.html">Mfa</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Policy.MfaState.html">MfaState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Duo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaduo">Mfa<wbr>Duo<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}DUO MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fido<wbr>U2f</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidou2f">Mfa<wbr>Fido<wbr>U2f<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Fido U2F MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fido<wbr>Webauthn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidowebauthn">Mfa<wbr>Fido<wbr>Webauthn<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Fido Web Authn MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Google<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfagoogleotp">Mfa<wbr>Google<wbr>Otp<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Google OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Groups<wbr>Includeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of Group IDs to Include.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Call</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktacall">Mfa<wbr>Okta<wbr>Call<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Okta Call MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaotp">Mfa<wbr>Okta<wbr>Otp<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Okta OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapassword">Mfa<wbr>Okta<wbr>Password<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Okta Password MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Push</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapush">Mfa<wbr>Okta<wbr>Push<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Okta Push MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Question</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaquestion">Mfa<wbr>Okta<wbr>Question<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Okta Question MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Sms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktasms">Mfa<wbr>Okta<wbr>Sms<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Okta SMS MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Priority of the policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rsa<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfarsatoken">Mfa<wbr>Rsa<wbr>Token<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}RSA Token MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Status: `"ACTIVE"` or `"INACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Symantec<wbr>Vip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfasymantecvip">Mfa<wbr>Symantec<wbr>Vip<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Symantec VIP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Yubikey<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfayubikeytoken">Mfa<wbr>Yubikey<wbr>Token<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Yubikey Token MFA policy settings.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Policy Description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Duo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaduo">*Mfa<wbr>Duo</a></span>
    </dt>
    <dd>{{% md %}}DUO MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fido<wbr>U2f</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidou2f">*Mfa<wbr>Fido<wbr>U2f</a></span>
    </dt>
    <dd>{{% md %}}Fido U2F MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fido<wbr>Webauthn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidowebauthn">*Mfa<wbr>Fido<wbr>Webauthn</a></span>
    </dt>
    <dd>{{% md %}}Fido Web Authn MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Google<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfagoogleotp">*Mfa<wbr>Google<wbr>Otp</a></span>
    </dt>
    <dd>{{% md %}}Google OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Groups<wbr>Includeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of Group IDs to Include.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Policy Name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Call</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktacall">*Mfa<wbr>Okta<wbr>Call</a></span>
    </dt>
    <dd>{{% md %}}Okta Call MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaotp">*Mfa<wbr>Okta<wbr>Otp</a></span>
    </dt>
    <dd>{{% md %}}Okta OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapassword">*Mfa<wbr>Okta<wbr>Password</a></span>
    </dt>
    <dd>{{% md %}}Okta Password MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Push</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapush">*Mfa<wbr>Okta<wbr>Push</a></span>
    </dt>
    <dd>{{% md %}}Okta Push MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Question</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaquestion">*Mfa<wbr>Okta<wbr>Question</a></span>
    </dt>
    <dd>{{% md %}}Okta Question MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Okta<wbr>Sms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktasms">*Mfa<wbr>Okta<wbr>Sms</a></span>
    </dt>
    <dd>{{% md %}}Okta SMS MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Priority of the policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rsa<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfarsatoken">*Mfa<wbr>Rsa<wbr>Token</a></span>
    </dt>
    <dd>{{% md %}}RSA Token MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Policy Status: `"ACTIVE"` or `"INACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Symantec<wbr>Vip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfasymantecvip">*Mfa<wbr>Symantec<wbr>Vip</a></span>
    </dt>
    <dd>{{% md %}}Symantec VIP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Yubikey<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfayubikeytoken">*Mfa<wbr>Yubikey<wbr>Token</a></span>
    </dt>
    <dd>{{% md %}}Yubikey Token MFA policy settings.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>duo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaduo">Mfa<wbr>Duo?</a></span>
    </dt>
    <dd>{{% md %}}DUO MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fido<wbr>U2f</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidou2f">Mfa<wbr>Fido<wbr>U2f?</a></span>
    </dt>
    <dd>{{% md %}}Fido U2F MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fido<wbr>Webauthn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidowebauthn">Mfa<wbr>Fido<wbr>Webauthn?</a></span>
    </dt>
    <dd>{{% md %}}Fido Web Authn MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>google<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfagoogleotp">Mfa<wbr>Google<wbr>Otp?</a></span>
    </dt>
    <dd>{{% md %}}Google OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>groups<wbr>Includeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of Group IDs to Include.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta<wbr>Call</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktacall">Mfa<wbr>Okta<wbr>Call?</a></span>
    </dt>
    <dd>{{% md %}}Okta Call MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta<wbr>Otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaotp">Mfa<wbr>Okta<wbr>Otp?</a></span>
    </dt>
    <dd>{{% md %}}Okta OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapassword">Mfa<wbr>Okta<wbr>Password?</a></span>
    </dt>
    <dd>{{% md %}}Okta Password MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta<wbr>Push</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapush">Mfa<wbr>Okta<wbr>Push?</a></span>
    </dt>
    <dd>{{% md %}}Okta Push MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta<wbr>Question</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaquestion">Mfa<wbr>Okta<wbr>Question?</a></span>
    </dt>
    <dd>{{% md %}}Okta Question MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta<wbr>Sms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktasms">Mfa<wbr>Okta<wbr>Sms?</a></span>
    </dt>
    <dd>{{% md %}}Okta SMS MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Priority of the policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rsa<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfarsatoken">Mfa<wbr>Rsa<wbr>Token?</a></span>
    </dt>
    <dd>{{% md %}}RSA Token MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Policy Status: `"ACTIVE"` or `"INACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>symantec<wbr>Vip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfasymantecvip">Mfa<wbr>Symantec<wbr>Vip?</a></span>
    </dt>
    <dd>{{% md %}}Symantec VIP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>yubikey<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfayubikeytoken">Mfa<wbr>Yubikey<wbr>Token?</a></span>
    </dt>
    <dd>{{% md %}}Yubikey Token MFA policy settings.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Policy Description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>duo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaduo">Dict[Mfa<wbr>Duo]</a></span>
    </dt>
    <dd>{{% md %}}DUO MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fido_<wbr>u2f</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidou2f">Dict[Mfa<wbr>Fido<wbr>U2f]</a></span>
    </dt>
    <dd>{{% md %}}Fido U2F MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fido_<wbr>webauthn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfafidowebauthn">Dict[Mfa<wbr>Fido<wbr>Webauthn]</a></span>
    </dt>
    <dd>{{% md %}}Fido Web Authn MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>google_<wbr>otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfagoogleotp">Dict[Mfa<wbr>Google<wbr>Otp]</a></span>
    </dt>
    <dd>{{% md %}}Google OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>groups_<wbr>includeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of Group IDs to Include.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Policy Name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta_<wbr>call</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktacall">Dict[Mfa<wbr>Okta<wbr>Call]</a></span>
    </dt>
    <dd>{{% md %}}Okta Call MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta_<wbr>otp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaotp">Dict[Mfa<wbr>Okta<wbr>Otp]</a></span>
    </dt>
    <dd>{{% md %}}Okta OTP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta_<wbr>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapassword">Dict[Mfa<wbr>Okta<wbr>Password]</a></span>
    </dt>
    <dd>{{% md %}}Okta Password MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta_<wbr>push</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktapush">Dict[Mfa<wbr>Okta<wbr>Push]</a></span>
    </dt>
    <dd>{{% md %}}Okta Push MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta_<wbr>question</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktaquestion">Dict[Mfa<wbr>Okta<wbr>Question]</a></span>
    </dt>
    <dd>{{% md %}}Okta Question MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>okta_<wbr>sms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfaoktasms">Dict[Mfa<wbr>Okta<wbr>Sms]</a></span>
    </dt>
    <dd>{{% md %}}Okta SMS MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Priority of the policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rsa_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfarsatoken">Dict[Mfa<wbr>Rsa<wbr>Token]</a></span>
    </dt>
    <dd>{{% md %}}RSA Token MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Policy Status: `"ACTIVE"` or `"INACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>symantec_<wbr>vip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfasymantecvip">Dict[Mfa<wbr>Symantec<wbr>Vip]</a></span>
    </dt>
    <dd>{{% md %}}Symantec VIP MFA policy settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>yubikey_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#mfayubikeytoken">Dict[Mfa<wbr>Yubikey<wbr>Token]</a></span>
    </dt>
    <dd>{{% md %}}Yubikey Token MFA policy settings.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Mfa<wbr>Duo</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#MfaDuo">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#MfaDuo">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaDuoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaDuoOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Mfa<wbr>Fido<wbr>U2f</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#MfaFidoU2f">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#MfaFidoU2f">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaFidoU2fArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaFidoU2fOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Mfa<wbr>Fido<wbr>Webauthn</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#MfaFidoWebauthn">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#MfaFidoWebauthn">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaFidoWebauthnArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaFidoWebauthnOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Mfa<wbr>Google<wbr>Otp</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#MfaGoogleOtp">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#MfaGoogleOtp">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaGoogleOtpArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaGoogleOtpOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Mfa<wbr>Okta<wbr>Call</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#MfaOktaCall">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#MfaOktaCall">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaOktaCallArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaOktaCallOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Mfa<wbr>Okta<wbr>Otp</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#MfaOktaOtp">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#MfaOktaOtp">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaOktaOtpArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaOktaOtpOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Mfa<wbr>Okta<wbr>Password</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#MfaOktaPassword">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#MfaOktaPassword">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaOktaPasswordArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaOktaPasswordOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Mfa<wbr>Okta<wbr>Push</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#MfaOktaPush">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#MfaOktaPush">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaOktaPushArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaOktaPushOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Mfa<wbr>Okta<wbr>Question</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#MfaOktaQuestion">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#MfaOktaQuestion">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaOktaQuestionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaOktaQuestionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Mfa<wbr>Okta<wbr>Sms</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#MfaOktaSms">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#MfaOktaSms">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaOktaSmsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaOktaSmsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Mfa<wbr>Rsa<wbr>Token</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#MfaRsaToken">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#MfaRsaToken">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaRsaTokenArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaRsaTokenOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Mfa<wbr>Symantec<wbr>Vip</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#MfaSymantecVip">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#MfaSymantecVip">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaSymantecVipArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaSymantecVipOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Mfa<wbr>Yubikey<wbr>Token</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#MfaYubikeyToken">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#MfaYubikeyToken">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaYubikeyTokenArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/policy?tab=doc#MfaYubikeyTokenOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>consent_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enroll</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-okta">https://github.com/pulumi/pulumi-okta</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

