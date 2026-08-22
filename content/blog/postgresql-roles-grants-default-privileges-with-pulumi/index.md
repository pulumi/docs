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

The risk of unauthorized data access or accidental data loss increases every time a manual database change is made. As your database schema grows, the complexity of managing permissions manually becomes an operational bottleneck. Modeling your PostgreSQL RBAC with Pulumi makes access control versioned and reproducible, and default privileges help close the access gap that occurs when new objects are created during rapid development.

<!--more-->

## What you'll build

In this post, you will learn how to manage PostgreSQL access control as code using Pulumi. You will build:

1. **Custom roles** for applications and developers.
1. **Database and schema grants** that follow the principle of least privilege.
1. **Table, sequence, and default privileges** so existing and future objects receive the correct permissions.

By the end, you will have a secure, automated database access model that survives schema changes and team rotations.

## Modeling roles and databases

The first step is to define the roles and databases. In PostgreSQL, a role can represent a user or a group.

```typescript
import * as postgresql from "@pulumi/postgresql";
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const dbPassword = config.requireSecret("dbPassword");

const myDatabase = new postgresql.Database("my-database", {
    name: "app_db",
});

const appRole = new postgresql.Role("app-role", {
    name: "app_user",
    login: true,
    password: dbPassword,
});
```

## Managing grants

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

const tableGrant = new postgresql.Grant("table-grant", {
    database: myDatabase.name,
    objectType: "table",
    privileges: ["SELECT"],
    role: appRole.name,
    schema: "public",
});

const sequenceGrant = new postgresql.Grant("sequence-grant", {
    database: myDatabase.name,
    objectType: "sequence",
    privileges: ["USAGE", "SELECT"],
    role: appRole.name,
    schema: "public",
});
```

The table grant covers existing tables in the schema. Sequence grants matter for applications that call sequence functions such as `currval` or `nextval`, including inserts into tables that use `SERIAL` columns.

## Automating with default privileges

To avoid manual grants for every future table or sequence, use `postgresql.DefaultPrivileges`. Default privileges apply to objects created by a specific owner role, so align the `owner` value with the role your migrations use to create database objects.

```typescript
const defaultTablePrivs = new postgresql.DefaultPrivileges("read-only-table-defaults", {
    database: myDatabase.name,
    owner: "postgres",
    schema: "public",
    objectType: "table",
    privileges: ["SELECT"],
    role: appRole.name,
});

const defaultSequencePrivs = new postgresql.DefaultPrivileges("read-only-sequence-defaults", {
    database: myDatabase.name,
    owner: "postgres",
    schema: "public",
    objectType: "sequence",
    privileges: ["USAGE", "SELECT"],
    role: appRole.name,
});
```

Default privileges apply only to future objects created by the configured `owner` role. They do not retroactively grant access to existing tables or sequences, which is why the explicit grants in the previous section still matter.

## Validation

After running `pulumi up`, you can validate your PostgreSQL RBAC model:

1. **Role check**: Run `\du` in `psql` to verify that the `app_user` role exists with the correct attributes.
1. **Grant verification**: Run `\z` to see access control lists for tables and sequences, `\dn+` to inspect schema privileges, and `\l+` to confirm database access.
1. **Default privilege test**: Create a new table and sequence as the `postgres` user and verify that the `app_user` receives the expected permissions.

By managing your PostgreSQL roles and grants as code, you keep your security model closer to your database schema, provide a clear audit trail, and reduce the risk of stale or excessive permissions.
