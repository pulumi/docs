---
title: "PostgreSQL RBAC Without Grant Drift"
date: 2026-06-09
draft: false
meta_desc: "Manage PostgreSQL roles, grants, schemas, and default privileges with Pulumi so access rules stay consistent as databases evolve."
meta_image: meta.png
feature_image: feature.png
authors:
    - pablo-seibelt
tags:
    - postgresql
    - security
    - iac
social:
    twitter: |
        PostgreSQL access drift often hides in default privileges.

        Manage roles, grants, schemas, and future tables with Pulumi instead.
    linkedin: |
        PostgreSQL RBAC gets tricky when new schemas and future tables arrive after the initial grant.

        This guide shows how to manage roles, grants, schemas, and default privileges with Pulumi so access rules stay consistent.
    bluesky: |
        PostgreSQL grant drift hides in future tables and default privileges.

        Manage RBAC with Pulumi.
---

Database administrators often struggle with access drift as teams grow and schemas evolve. Manually running `GRANT` commands for every new table or schema is a recipe for onboarding failures and security holes. When a new developer joins or a service is decommissioned, the manual cleanup of roles and privileges often lags behind, leaving stale access that is difficult to audit and even harder to remediate without breaking production applications.

The risk of unauthorized data access or accidental data loss increases every time a manual database change is made. As your database schema grows, the complexity of managing permissions manually becomes an operational bottleneck. Modeling your PostgreSQL RBAC with Pulumi ensures that access control is versioned, reproducible, and automatically applied to new objects through default privileges, eliminating the "access gap" that occurs during rapid development.

<!--more-->

## What you'll build

In this post, you will learn how to manage PostgreSQL access control as code using Pulumi. You will build:

1. **Custom roles** for applications and developers.
2. **Database and schema grants** that follow the principle of least privilege.
3. **Default privileges** to ensure that new tables automatically inherit the correct permissions.

By the end, you will have a secure, automated database access model that survives schema changes and team rotations.

## Modeling Roles and Databases

The first step is to define the roles and databases. In PostgreSQL, a role can represent a user or a group.

```typescript
import * as postgresql from "@pulumi/postgresql";

const myDatabase = new postgresql.Database("my-database", {
    name: "app_db",
});

const appRole = new postgresql.Role("app-role", {
    name: "app_user",
    login: true,
    password: "very-secure-password",
});
```

## Managing Grants

Once you have roles and databases, you need to grant permissions. The `postgresql.Grant` resource allows you to specify exactly what a role can do.

```typescript
const dbGrant = new postgresql.Grant("db-grant", {
    database: myDatabase.name,
    objectType: "database",
    privileges: ["CONNECT"],
    role: appRole.name,
});

const schemaGrant = new postgresql.Grant("schema-grant", {
    database: myDatabase.name,
    objectType: "schema",
    privileges: ["USAGE"],
    role: appRole.name,
    schema: "public",
});
```

## Automating with Default Privileges

To avoid manual grants for every new table, use `postgresql.DefaultPrivileges`. This ensures that any new table created by a specific role automatically has the correct permissions.

```typescript
const defaultPrivs = new postgresql.DefaultPrivileges("read-only-defaults", {
    database: myDatabase.name,
    owner: "postgres",
    schema: "public",
    objectType: "table",
    privileges: ["SELECT"],
    role: appRole.name,
});
```

## Validation

After running `pulumi up`, you can validate your PostgreSQL RBAC model:

1. **Role Check**: Run `\du` in `psql` to verify that the `app_user` role exists with the correct attributes.
2. **Grant Verification**: Run `\z` to see the access control list for your tables and schemas.
3. **Default Privilege Test**: Create a new table as the `postgres` user and verify that the `app_user` automatically has `SELECT` permissions on it.

By managing your PostgreSQL roles and grants as code, you ensure that your security model is always in sync with your database schema, providing a clear audit trail and reducing the risk of stale or excessive permissions.
