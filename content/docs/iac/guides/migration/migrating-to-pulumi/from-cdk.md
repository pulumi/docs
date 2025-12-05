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

If your team has already provisioned infrastructure using AWS CDK, and you'd like to adopt Pulumi, you have two primary strategies you can take:

* Coexist with resources provisioned by CDK by referencing stack outputs.
* Convert your CDK application to Pulumi, either by using the Pulumi CDK adapter or by migrating to a Pulumi program that imports existing resources.

## Choose a CDK migration path

To keep using AWS CDK constructs while adopting Pulumi as the engine, see [Using Pulumi with AWS CDK](/docs/iac/guides/migration/migrating-to-pulumi/migrating-from-cdk/using-pulumi-cdk/).

To migrate an existing AWS CDK application to a Pulumi program that manages your current infrastructure, see [Migrating existing AWS CDK applications to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/migrating-from-cdk/migrating-existing-cdk-app/).
