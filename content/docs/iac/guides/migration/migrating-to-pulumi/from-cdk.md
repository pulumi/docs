---
title_tag: "Migrating from AWS CDK"
meta_desc: Migrate your existing AWS CDK TypeScript application
title: AWS CDK
h1: "Migrating from AWS CDK to Pulumi"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: AWS CDK
        parent: iac-guides-migration-from
        identifier: iac-guides-migration-from-cdk
        weight: 2
aliases:
    - /docs/iac/adopting-pulumi/migrating-to-pulumi/from-cdk/
---

If your team has already provisioned infrastructure using AWS CDK, and you'd like to adopt Pulumi, you have three primary strategies you can take:

* **[Neo](/product/neo/) automated migration (Recommended)**: Use Neo to automatically convert your CDK code and import existing resources with zero downtime
* Coexist with resources provisioned by CDK by referencing stack outputs
* Convert your CDK application to Pulumi, either by using the Pulumi CDK adapter or by migrating to a Pulumi program that imports existing resources

## Choosing a CDK migration path

### Neo automated migration (Recommended)

For most teams, Neo provides the fastest and safest migration path from CDK to Pulumi. Neo automates the entire migration process: converting your CDK code, importing existing CloudFormation resources, and verifying zero changes, all without downtime. This approach eliminates manual work and migration risks while preserving your existing infrastructure exactly as it is.

To migrate your CDK application with Neo, see [Migrating existing AWS CDK applications to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/migrating-from-cdk/migrating-existing-cdk-app/) or read about the [technical details of Neo's CDK migration capabilities](/blog/neo-cdk-migration/).

### Alternative migration paths

If Neo doesn't support your specific use case, or if you prefer manual control, you have two alternative paths:

**Keep using CDK constructs**: Pick the adapter path if you want minimal code change and to keep using CDK libraries and patterns while gaining Pulumi's engine, state, and policy features. See [Using Pulumi with AWS CDK](/docs/iac/guides/migration/migrating-to-pulumi/migrating-from-cdk/using-pulumi-cdk/).

**Manual migration**: Pick the manual migration path if you want full control over the conversion process or need to handle edge cases not yet supported by Neo. See the manual migration sections in [Migrating existing AWS CDK applications to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/migrating-from-cdk/migrating-existing-cdk-app/).
