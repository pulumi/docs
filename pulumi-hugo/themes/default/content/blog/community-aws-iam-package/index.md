---
title: "Introducing the Community AWS IAM Package"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-10-05T09:24:26-07:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: The Community AWS IAM Package helps users from all backgrounds quickly create IAM Roles, Policies, and Users.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - zack-chase

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - aws
    - iam

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---

Building on top of the cloud can be frustrating at times. You will likely run into resources that complicated to create, others that are very tedious to create, and worst of all resources that are complicated and tedious to create. As cloud engineers ourselves, we feel the same pain as our users and strive to build abstractions that make cloud engineering a more productive and pleasant experience.

Recently we released our [Community AWS IAM Package](/registry/packages/aws-iam/) to help deliver on the promise of making the cloud easier to use for every operator, engineer, and user. This package is based on the Terraform AWS IAM Module, so it allows our users to take advantage of battle-tested abstractions. The package also helps transitioning Terraform users by maintaining similar resource names and inputs so they can focus on taking advantage of features of their programming language of choice (TypeScript, JavaScript, Python, Go, .NET, and YAML).

## Examples

In the following sections, we will show a few examples of common use cases when using the Community AWS IAM Package.

### Assumable Role with SAML

The example code below shows how you can create an Assumable Role with SAML, which will create a single IAM role which can be assumed by users with a SAML Identity Provider.

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
export const assumableRoleWithSaml = new iam.AssumableRoleWithSAML("aws-iam-example-assumable-role-with-saml", {
    providerIds: [ "arn:aws:iam::235367859851:saml-provider/idp_saml" ],
    role: {
        name: "saml-role",
        policyArns: [ "arn:aws:iam::aws:policy/ReadOnlyAccess" ],
    },
    tags: {
        Role: "saml-role",
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
assumable_role_with_saml = iam.AssumableRoleWithSAML(
    'assumable_role_with_saml',
    role=iam.RoleArgs(
        name='saml-role',
        policy_arns=['arn:aws:iam::aws:policy/ReadOnlyAccess'],
    ),
    tags={
        'Role': 'saml-role',
    },
    provider_ids=['arn:aws:iam::235367859851:saml-provider/idp_saml']
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
assumableRoleWithSAML, err := iam.NewAssumableRoleWithSAML(ctx, "assumable-role-with-saml", &iam.AssumableRoleWithSAMLArgs{
    Role: iam.RoleArgs{
        Name:       pulumi.String("saml-role"),
        PolicyArns: pulumi.ToStringArray([]string{"arn:aws:iam::aws:policy/ReadOnlyAccess"}),
    },
    Tags: pulumi.ToStringMap(map[string]string{
        "Role": "saml-role",
    }),
    ProviderIds: pulumi.ToStringArray([]string{"arn:aws:iam::235367859851:saml-provider/idp_saml"}),
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var assumableRoleWithSaml = new AssumableRoleWithSAML("assumable-role-with-saml", new AssumableRoleWithSAMLArgs
{
    Role = new RoleArgs
    {
        Name = "saml-role",
        PolicyArns = {"arn:aws:iam::aws:policy/ReadOnlyAccess"},
    },
    Tags = new InputMap<string>
    {
        {"Role", "saml-role"},
    },
    ProviderIds = {"arn:aws:iam::235367859851:saml-provider/idp_saml"},
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
    assumableRoleWithSaml:
        type: "aws-iam:index:AssumableRoleWithSAML"
        properties:
            role:
                name: "saml-role"
                policyArns:
                    - "arn:aws:iam::aws:policy/ReadOnlyAccess"
            tags:
                Role: "saml-role"
            providerIds:
                - "arn:aws:iam::235367859851:saml-provider/idp_saml"
```

{{% /choosable %}}

### EKS Assumable Role

The example code below shows how you can create an EKS Assumable Role, which will create an IAM Role that can be assumed by multiple EKS Service Accounts.

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
export const eksRole = new iam.EKSRole("aws-iam-example-eks-role", {
    role: {
        name: "eks-role",
        policyArns: [ "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy" ],
    },
    tags: {
        Name: "eks-role",
    },
    clusterServiceAccounts: {
        "cluster1": [ "default:my-app" ],
        "cluster2": [ "default:my-app", "canary:my-app" ],
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
eks_role = iam.EKSRole(
    'eks_role',
    role=iam.RoleArgs(
        name='eks-role',
        policy_arns=['arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy'],
    ),
    tags={
        'Name': 'eks-role',
    },
    cluster_service_accounts={
        'cluster1': [ 'default:my-app' ],
        'cluster2': [ 'default:my-app', 'canary:my-app' ],
    },
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
eksRole, err := iam.NewEKSRole(ctx, "eks-role", &iam.EKSRoleArgs{
    Role: iam.RoleArgs{
        Name:       pulumi.String("eks-role"),
        PolicyArns: pulumi.ToStringArray([]string{"arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"}),
    },
    Tags: pulumi.ToStringMap(map[string]string{
        "Role": "eks-role",
    }),
    ClusterServiceAccounts: pulumi.ToStringArrayMap(map[string][]string{
    	"cluster1": {"default:my-app"},
    	"cluster2": {"default:my-app", "canary:my-app"},
    }),
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var eksRole = new EKSRole("eks-role", new EKSRoleArgs
{
    Role = new RoleArgs
    {
        Name = "eks-role",
        PolicyArns = {"arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"},
    },
    Tags = new InputMap<string>
    {
        {"Name", "eks-role"},
    },
    ClusterServiceAccounts = {
        {"cluster1", ImmutableArray.Create<string>(new string[] {"default:my-app"})},
        {"cluster2", ImmutableArray.Create<string>(new string[] {"default:my-app", "canary:my-app"})}
    },
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
    eksRole:
        type: "aws-iam:index:EKSRole"
        properties:
            role:
                name: "eks-role"
                policyArns:
                    - "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
            tags:
                Name: "eks-role"
            clusterServiceAccounts:
                cluster1:
                    - "default:my-app"
                cluster2:
                    - "default:my-app"
                    - "canary:my-app"
```

{{% /choosable %}}

### IAM Role for an EKS Service Account

The example code below shows how you can create an IAM Role for an EKS Service Account, which will create an IAM Role with various Policies attached that can be assumed by multiple EKS Service Accounts.

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
export const roleForServiceAccountsEks = new iam.RoleForServiceAccountsEks("aws-iam-example-role-for-service-accounts-eks", {
    role: {
        name: "vpc-cni"
    },
    tags: {
        Name: "vpc-cni-irsa",
    },
    oidcProviders: {
        main: {
            providerArn: "arn:aws:iam::012345678901:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/5C54DDF35ER19312844C7333374CC09D",
            namespaceServiceAccounts: ["default:my-app", "canary:my-app"],
        }
    },
    policies: {
        vpnCni: {
            attach: true,
            enableIpv4: true,
        },
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
role_for_service_account_eks = iam.RoleForServiceAccountsEks(
    'role_for_service_account_eks',
    role=iam.RoleArgs(
        name='vpc-cni'
    ),
    tags={
        'Name': 'vpc-cni-irsa',
    },
    oidc_providers={
        'main': iam.OIDCProviderArgs(
            provider_arn='arn:aws:iam::012345678901:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/5C54DDF35ER19312844C7333374CC09D',
            namespace_service_accounts=['default:my-app', 'canary:my-app'],
        ),
    },
    policies=iam.EKSRolePoliciesArgs(
        vpn_cni=iam.EKSVPNCNIPolicyArgs(
            attach=True,
            enable_ipv4=True,
        ),
    ),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
roleForServiceAccountsEKS, err := iam.NewRoleForServiceAccountsEks(ctx, "role-for-service-accounts-eks", &iam.RoleForServiceAccountsEksArgs{
    Role: iam.EKSServiceAccountRolePtr(&iam.EKSServiceAccountRoleArgs{
        Name: pulumi.String("vpc-cni"),
    }),
    Tags: pulumi.ToStringMap(map[string]string{
        "Name": "vpc-cni-irsa",
    }),
    OidcProviders: iam.OIDCProviderMap{
        "main": iam.OIDCProviderArgs{
            ProviderArn:              pulumi.String("arn:aws:iam::012345678901:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/5C54DDF35ER19312844C7333374CC09D"),
            NamespaceServiceAccounts: pulumi.ToStringArray([]string{"default:my-app", "canary:my-app"}),
        },
    },
    Policies: iam.EKSRolePoliciesPtr(&iam.EKSRolePoliciesArgs{
        VpnCni: iam.EKSVPNCNIPolicyPtr(&iam.EKSVPNCNIPolicyArgs{
            Attach:     pulumi.Bool(true),
            EnableIpv4: pulumi.BoolPtr(true),
        }),
    }),
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var roleForServiceAccountEks = new RoleForServiceAccountsEks("role-for-service-account-eks", new RoleForServiceAccountsEksArgs
{
    Role = new EKSServiceAccountRoleArgs
    {
        Name = "vpn-cni",
    },
    Tags = {
        {"Name", "vpc-cni-irsa"},
    },
    OidcProviders = {
        {"main", new OIDCProviderArgs
        {
            ProviderArn = "arn:aws:iam::012345678901:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/5C54DDF35ER19312844C7333374CC09D",
            NamespaceServiceAccounts = {"default:my-app", "canary:my-app"},
        }},
    },
    Policies = new EKSRolePoliciesArgs
    {
        VpnCni = new EKSVPNCNIPolicyArgs
        {
            Attach = true,
            EnableIpv4 = true,
        },
    },
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
    roleForServiceAccountsEks:
        type: "aws-iam:index:RoleForServiceAccountsEks"
        properties:
            role:
                name: "vpc-cni"
            tags:
                Name: "vpc-cni-irsa"
            oidcProviders:
                main:
                    providerArn: "arn:aws:iam::012345678901:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/5C54DDF35ER19312844C7333374CC09D"
                    namespaceServiceAccounts:
                        - "default:my-app"
                        - "canary:my-app"
            policies:
                vpnCni:
                    attach: true
                    enableIpv4: true
```

{{% /choosable %}}

You can find a complete list of supported EKS Policies within the [API Documentation](/registry/packages/aws-iam/api-docs/roleforserviceaccountseks/).

### More Use Cases

A few of the other use cases support by the Community AWS IAM package are:

- [Create individual IAM users](/registry/packages/aws-iam/api-docs/user/)
- [Use Groups to Assign Permissions to IAM Users](/registry/packages/aws-iam/api-docs/groupwithpolicies/)
- [Create IAM Policies](/registry/packages/aws-iam/api-docs/policy/)
- [View all supported resources](/registry/packages/aws-iam/api-docs/)

## Learn More

If you want to learn more about Pulumi and the Community AWS IAM package, here are a few links you might find interesting:

- Read the [AWS IAM documentation](/registry/packages/aws-iam/) to learn more about the package, how to [install and configure](/registry/packages/aws-iam/installation-configuration/) it and use its APIs.
- If you’re interested in learning more about Pulumi concepts, try the [Concepts](/docs/concepts/) page.
