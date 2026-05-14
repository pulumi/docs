---
title: "Snowflake Warehouses, Roles, and Short-Lived Credentials with Pulumi"
date: 2026-06-16
draft: false
meta_desc: "Provision Snowflake warehouses, databases, role hierarchies, and grants with Pulumi while using Pulumi ESC to avoid long-lived static credentials."
meta_image: meta.png
feature_image: feature.png
authors:
    - pablo-seibelt
tags:
    - snowflake
    - data-platform
    - esc
social:
    twitter: |
        Snowflake IaC should cover more than warehouses.

        Model roles, grants, databases, and short-lived credentials with Pulumi and ESC.
    linkedin: |
        Snowflake governance depends on both infrastructure and access.

        This guide shows how to provision warehouses, databases, role hierarchies, and grants with Pulumi while using Pulumi ESC to avoid long-lived static credentials.
    bluesky: |
        Snowflake IaC needs warehouses, roles, grants, databases, and better credential handling.

        Use Pulumi and ESC to manage Snowflake access without long-lived secrets.
---

Managing a modern data platform requires more than just creating a few tables. As data teams scale, the complexity of managing compute resources, access controls, and secure credentials grows quickly. Manual governance becomes impractical once warehouses, roles, and grants span multiple environments.

Pulumi ESC can provide short-lived Snowflake credentials so your Pulumi programs can manage warehouses, databases, and RBAC roles without storing long-lived private keys or passwords in CI/CD.

When data teams manage Snowflake through the web UI or ad hoc SQL scripts, they often hit three walls. First, "warehouse sprawl" occurs when compute resources are created without clear ownership or auto-suspend policies, leading to unexpected costs. Second, manual RBAC management makes it nearly impossible to audit who has access to what as the role hierarchy grows. Finally, static credentials stored in CI/CD pipelines create a persistent security risk.

Operational risk and audit pressure increase as data platforms become central to business operations. Waiting to automate Snowflake governance leads to technical debt that is difficult to unwind once object sprawl takes hold. Platform teams need a way to enforce consistency and security from the first warehouse onward.

By the end of this post, you will build a complete Snowflake environment using Pulumi. This includes provisioning virtual warehouses with auto-suspend policies, creating databases, and establishing a secure, hierarchical RBAC model. You will also learn how to inject the necessary credentials using [Pulumi ESC](/docs/esc/) to eliminate static secrets.

<!--more-->

## Define warehouses, roles, and grants as code

Snowflake's architecture separates compute (warehouses) from storage (databases), providing incredible flexibility. However, this flexibility can lead to inconsistent security policies if managed manually. By using Pulumi, you can:

1. Define your entire data environment in TypeScript, Python, or Go.
2. Version control your role hierarchy and permission grants.
3. Automate the creation of isolated environments for development and testing.
4. Use Pulumi ESC to eliminate long-lived static credentials in CI/CD.

## The Snowflake RBAC model

Snowflake uses Role-Based Access Control (RBAC). Privileges are granted to roles, and roles are granted to users or other roles to create a hierarchy. A common pattern is to create "functional roles" for users and "access roles" for specific resources.

## Walkthrough: warehouses, databases, and roles

Let's look at how to define a standard Snowflake environment using the Pulumi Snowflake provider.

### 1. Define compute and storage

First, we'll create a virtual warehouse and a database.

```typescript
import * as snowflake from "@pulumi/snowflake";

const warehouse = new snowflake.Warehouse("my-warehouse", {
    name: "MY_WAREHOUSE",
    warehouseSize: "X-SMALL",
    autoSuspend: 60,
    autoResume: "true",
});

const database = new snowflake.Database("my-database", {
    name: "MY_DATABASE",
});
```

### 2. Create a role hierarchy

Next, we'll define roles and establish a parent-child relationship. This allows a "writer" role to inherit all permissions from a "reader" role.

```typescript
const readerRole = new snowflake.AccountRole("reader-role", {
    name: "MY_READER_ROLE",
});

const writerRole = new snowflake.AccountRole("writer-role", {
    name: "MY_WRITER_ROLE",
});

const roleGrants = new snowflake.GrantAccountRole("role-grants", {
    roleName: readerRole.name,
    parentRoleName: writerRole.name,
});
```

### 3. Grant privileges

Finally, we grant specific privileges to these roles.

```typescript
const readerDbGrant = new snowflake.GrantPrivilegesToAccountRole("reader-db-grant", {
    privileges: ["USAGE"],
    accountRoleName: readerRole.name,
    onAccountObject: {
        objectType: "DATABASE",
        objectName: database.name,
    },
});

const writerWhGrant = new snowflake.GrantPrivilegesToAccountRole("writer-wh-grant", {
    privileges: ["USAGE"],
    accountRoleName: writerRole.name,
    onAccountObject: {
        objectType: "WAREHOUSE",
        objectName: warehouse.name,
    },
});
```

## Secure credentials and governance

Storing Snowflake passwords or private keys in CI/CD variables is a security risk. Pulumi ESC (Environments, Secrets, and Configuration) provides a better way. You can use `snowflake-login` for dynamic OIDC-based authentication or `snowflake-user` to automatically rotate RSA keypairs.

Here is an example ESC environment configuration for Snowflake:

```yaml
values:
  snowflake:
    login:
      fn::open::snowflake-login:
        oidc:
          account: my-org-account
          user: PULUMI_ESC_USER
          role: ACCOUNTADMIN
```

This configuration allows Pulumi to authenticate to Snowflake using a short-lived OIDC token, meaning no static secrets are ever stored in your environment.

For large organizations, Pulumi Insights allows you to query your entire infrastructure using [Resource Search](/docs/insights/discovery/search/) syntax or natural language. You can easily find "ungoverned" warehouses that don't follow naming conventions:

```text
type:snowflake:index/warehouse:Warehouse -name:PROD_
```

## Conclusion

By combining Pulumi's infrastructure as code with Pulumi ESC's secret management, you can build a secure, scalable, and governed Snowflake environment. Whether you're managing one warehouse or many environments, the patterns remain the same: define, version, and secure.
