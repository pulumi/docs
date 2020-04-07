
---
title: "UserAttributeMapper"
block_external_search_index: true
---



## # keycloak.ldap.UserAttributeMapper

Allows for creating and managing user attribute mappers for Keycloak users
federated via LDAP.

The LDAP user attribute mapper can be used to map a single LDAP attribute
to an attribute on the Keycloak user model.

### Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as keycloak from "@pulumi/keycloak";

const realm = new keycloak.Realm("realm", {
    enabled: true,
    realm: "test",
});
const ldapUserFederation = new keycloak.ldap.UserFederation("ldap_user_federation", {
    bindCredential: "admin",
    bindDn: "cn=admin,dc=example,dc=org",
    connectionUrl: "ldap://openldap",
    rdnLdapAttribute: "cn",
    realmId: realm.id,
    userObjectClasses: [
        "simpleSecurityObject",
        "organizationalRole",
    ],
    usernameLdapAttribute: "cn",
    usersDn: "dc=example,dc=org",
    uuidLdapAttribute: "entryDN",
});
const ldapUserAttributeMapper = new keycloak.ldap.UserAttributeMapper("ldap_user_attribute_mapper", {
    ldapAttribute: "bar",
    ldapUserFederationId: ldapUserFederation.id,
    realmId: realm.id,
    userModelAttribute: "foo",
});
```

### Argument Reference

The following arguments are supported:

- `realm_id` - (Required) The realm that this LDAP mapper will exist in.
- `ldap_user_federation_id` - (Required) The ID of the LDAP user federation provider to attach this mapper to.
- `name` - (Required) Display name of this mapper when displayed in the console.
- `user_model_attribute` - (Required) Name of the user property or attribute you want to map the LDAP attribute into.
- `ldap_attribute` - (Required) Name of the mapped attribute on the LDAP object.
- `read_only` - (Optional) When `true`, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak. Defaults to `false`.
- `always_read_value_from_ldap` - (Optional) When `true`, the value fetched from LDAP will override the value stored in Keycloak. Defaults to `false`.
- `is_mandatory_in_ldap` - (Optional) When `true`, this attribute must exist in LDAP. Defaults to `false`.

> This content is derived from https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/keycloak_ldap_user_attribute_mapper.html.markdown.



## Create a UserAttributeMapper Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/keycloak/ldap/#UserAttributeMapper">UserAttributeMapper</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/keycloak/ldap/#UserAttributeMapperArgs">UserAttributeMapperArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">UserAttributeMapper</span><span class="p">(resource_name, opts=None, </span>always_read_value_from_ldap=None<span class="p">, </span>is_mandatory_in_ldap=None<span class="p">, </span>ldap_attribute=None<span class="p">, </span>ldap_user_federation_id=None<span class="p">, </span>name=None<span class="p">, </span>read_only=None<span class="p">, </span>realm_id=None<span class="p">, </span>user_model_attribute=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewUserAttributeMapper<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-keycloak/sdk/go/keycloak/ldap?tab=doc#UserAttributeMapperArgs">UserAttributeMapperArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-keycloak/sdk/go/keycloak/ldap?tab=doc#UserAttributeMapper">UserAttributeMapper</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Keycloak/Pulumi.Keycloak.Ldap.UserAttributeMapper.html">UserAttributeMapper</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Keycloak/Pulumi.Keycloak.Ldap.UserAttributeMapperArgs.html">UserAttributeMapperArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Always<wbr>Read<wbr>Value<wbr>From<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, the value fetched from LDAP will override the value stored in Keycloak.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Mandatory<wbr>In<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, this attribute must exist in LDAP.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ldap<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the mapped attribute on LDAP object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ldap<wbr>User<wbr>Federation<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ldap user federation provider to attach this mapper to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Display name of the mapper when displayed in the console.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Realm<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The realm in which the ldap user federation provider exists.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>User<wbr>Model<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the UserModel property or attribute you want to map the LDAP attribute into.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Always<wbr>Read<wbr>Value<wbr>From<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, the value fetched from LDAP will override the value stored in Keycloak.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Mandatory<wbr>In<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, this attribute must exist in LDAP.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ldap<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the mapped attribute on LDAP object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ldap<wbr>User<wbr>Federation<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ldap user federation provider to attach this mapper to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Display name of the mapper when displayed in the console.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Realm<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The realm in which the ldap user federation provider exists.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>User<wbr>Model<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the UserModel property or attribute you want to map the LDAP attribute into.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>always<wbr>Read<wbr>Value<wbr>From<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, the value fetched from LDAP will override the value stored in Keycloak.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is<wbr>Mandatory<wbr>In<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, this attribute must exist in LDAP.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ldap<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the mapped attribute on LDAP object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ldap<wbr>User<wbr>Federation<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ldap user federation provider to attach this mapper to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Display name of the mapper when displayed in the console.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>realm<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The realm in which the ldap user federation provider exists.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>user<wbr>Model<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the UserModel property or attribute you want to map the LDAP attribute into.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>always_<wbr>read_<wbr>value_<wbr>from_<wbr>ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, the value fetched from LDAP will override the value stored in Keycloak.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is_<wbr>mandatory_<wbr>in_<wbr>ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, this attribute must exist in LDAP.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ldap_<wbr>attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the mapped attribute on LDAP object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ldap_<wbr>user_<wbr>federation_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ldap user federation provider to attach this mapper to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Display name of the mapper when displayed in the console.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>realm_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The realm in which the ldap user federation provider exists.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>user_<wbr>model_<wbr>attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the UserModel property or attribute you want to map the LDAP attribute into.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## UserAttributeMapper Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Always<wbr>Read<wbr>Value<wbr>From<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, the value fetched from LDAP will override the value stored in Keycloak.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Is<wbr>Mandatory<wbr>In<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, this attribute must exist in LDAP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ldap<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the mapped attribute on LDAP object.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ldap<wbr>User<wbr>Federation<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ldap user federation provider to attach this mapper to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Display name of the mapper when displayed in the console.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Realm<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The realm in which the ldap user federation provider exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Model<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the UserModel property or attribute you want to map the LDAP attribute into.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Always<wbr>Read<wbr>Value<wbr>From<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, the value fetched from LDAP will override the value stored in Keycloak.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Is<wbr>Mandatory<wbr>In<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, this attribute must exist in LDAP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ldap<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the mapped attribute on LDAP object.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ldap<wbr>User<wbr>Federation<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ldap user federation provider to attach this mapper to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Display name of the mapper when displayed in the console.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Realm<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The realm in which the ldap user federation provider exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Model<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the UserModel property or attribute you want to map the LDAP attribute into.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>always<wbr>Read<wbr>Value<wbr>From<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, the value fetched from LDAP will override the value stored in Keycloak.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>is<wbr>Mandatory<wbr>In<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, this attribute must exist in LDAP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ldap<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the mapped attribute on LDAP object.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ldap<wbr>User<wbr>Federation<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ldap user federation provider to attach this mapper to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Display name of the mapper when displayed in the console.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>realm<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The realm in which the ldap user federation provider exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user<wbr>Model<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the UserModel property or attribute you want to map the LDAP attribute into.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>always_<wbr>read_<wbr>value_<wbr>from_<wbr>ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, the value fetched from LDAP will override the value stored in Keycloak.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>is_<wbr>mandatory_<wbr>in_<wbr>ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, this attribute must exist in LDAP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ldap_<wbr>attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the mapped attribute on LDAP object.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ldap_<wbr>user_<wbr>federation_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ldap user federation provider to attach this mapper to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Display name of the mapper when displayed in the console.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>realm_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The realm in which the ldap user federation provider exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user_<wbr>model_<wbr>attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the UserModel property or attribute you want to map the LDAP attribute into.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing UserAttributeMapper Resource

Get an existing UserAttributeMapper resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/keycloak/ldap/#UserAttributeMapperState">UserAttributeMapperState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/keycloak/ldap/#UserAttributeMapper">UserAttributeMapper</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>always_read_value_from_ldap=None<span class="p">, </span>is_mandatory_in_ldap=None<span class="p">, </span>ldap_attribute=None<span class="p">, </span>ldap_user_federation_id=None<span class="p">, </span>name=None<span class="p">, </span>read_only=None<span class="p">, </span>realm_id=None<span class="p">, </span>user_model_attribute=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetUserAttributeMapper<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-keycloak/sdk/go/keycloak/ldap?tab=doc#UserAttributeMapperState">UserAttributeMapperState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-keycloak/sdk/go/keycloak/ldap?tab=doc#UserAttributeMapper">UserAttributeMapper</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Keycloak/Pulumi.Keycloak.Ldap.UserAttributeMapper.html">UserAttributeMapper</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Keycloak/Pulumi.Keycloak.Ldap.UserAttributeMapperState.html">UserAttributeMapperState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Always<wbr>Read<wbr>Value<wbr>From<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, the value fetched from LDAP will override the value stored in Keycloak.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Mandatory<wbr>In<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, this attribute must exist in LDAP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ldap<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the mapped attribute on LDAP object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ldap<wbr>User<wbr>Federation<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ldap user federation provider to attach this mapper to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Display name of the mapper when displayed in the console.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Realm<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The realm in which the ldap user federation provider exists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Model<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the UserModel property or attribute you want to map the LDAP attribute into.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Always<wbr>Read<wbr>Value<wbr>From<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, the value fetched from LDAP will override the value stored in Keycloak.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Mandatory<wbr>In<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, this attribute must exist in LDAP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ldap<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the mapped attribute on LDAP object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ldap<wbr>User<wbr>Federation<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ldap user federation provider to attach this mapper to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Display name of the mapper when displayed in the console.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Realm<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The realm in which the ldap user federation provider exists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Model<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the UserModel property or attribute you want to map the LDAP attribute into.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>always<wbr>Read<wbr>Value<wbr>From<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, the value fetched from LDAP will override the value stored in Keycloak.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is<wbr>Mandatory<wbr>In<wbr>Ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, this attribute must exist in LDAP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ldap<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the mapped attribute on LDAP object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ldap<wbr>User<wbr>Federation<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ldap user federation provider to attach this mapper to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Display name of the mapper when displayed in the console.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>realm<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The realm in which the ldap user federation provider exists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>Model<wbr>Attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the UserModel property or attribute you want to map the LDAP attribute into.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>always_<wbr>read_<wbr>value_<wbr>from_<wbr>ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, the value fetched from LDAP will override the value stored in Keycloak.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is_<wbr>mandatory_<wbr>in_<wbr>ldap</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, this attribute must exist in LDAP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ldap_<wbr>attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the mapped attribute on LDAP object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ldap_<wbr>user_<wbr>federation_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ldap user federation provider to attach this mapper to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Display name of the mapper when displayed in the console.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>realm_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The realm in which the ldap user federation provider exists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user_<wbr>model_<wbr>attribute</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the UserModel property or attribute you want to map the LDAP attribute into.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-keycloak">https://github.com/pulumi/pulumi-keycloak</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

