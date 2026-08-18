---
title: "Announcing Experimental Rust Support for Pulumi"
date: 2026-08-18
draft: false
meta_desc: "An experimental, community-supported Rust SDK and language plugin for Pulumi, now in Pulumi Labs, with examples across AWS, Azure, Google Cloud, and Kubernetes."
feature_image: feature.png
authors:
    - luke-ward
tags:
    - rust
    - community
category: community
schema_type: auto

# Social media copy is auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Rust has been one of the most upvoted requests in Pulumi's history. It now exists: pulumi-rust is public in Pulumi Labs.

        Write an ordinary Rust crate, build it with Cargo, deploy it with pulumi up. Here's what works today.
    linkedin: |
        Rust has been one of the most upvoted requests in Pulumi's history. Until now the honest answer was "not yet".

        That changed today. pulumi-rust, an experimental Rust SDK and language plugin, is public in the Pulumi Labs organization.

        A Pulumi program in Rust is an ordinary crate. Cargo builds it, pulumi up deploys it, and there is nothing exotic in between.

        Labs means experimental and community-supported, with no stability promises yet. It also means the project graduates on community interest, so the most useful thing you can do is run it and tell us what breaks.

        The setup is one clone and one build.
    bluesky: |
        A Pulumi program in Rust is just a crate. Cargo builds it, pulumi up deploys it, and provider SDKs come from the real provider schemas.

        pulumi-rust is experimental and community-supported, now public in Pulumi Labs. Twenty-two examples are there to try.
---

Rust language support is one of the most upvoted requests in Pulumi's history: [pulumi/pulumi#3622](https://github.com/pulumi/pulumi/issues/3622).  Today there is something concrete to point at. [pulumi-rust](https://github.com/pulumi-labs/pulumi-rust) is an experimental Rust SDK and language plugin for Pulumi, now public in the Pulumi Labs organization. You write a Pulumi program as an ordinary Rust crate, build it with Cargo, and deploy it with `pulumi up`.

<!--more-->

## What Pulumi Labs means

Pulumi Labs is where we publish experimental, community-supported projects. Labs projects come with no promises of maintenance, stability, or security, and pulumi-rust is not an official Pulumi project. What Labs provides is a public home and a path: if a project earns real community interest, we can graduate it to full support. Community involvement is greatly encouraged.

## Pulumi programs in Rust

Here is a complete program that creates an S3 bucket and exports its name:

```rust
fn main() {
    pulumi::run(|ctx| async move {
        let bucket = pulumi_aws::s3::Bucket::new(
            &ctx,
            "my-bucket",
            pulumi_aws::s3::BucketArgs::default(),
            pulumi::ResourceOptions::default(),
        );

        ctx.export("bucketName", bucket.bucket().cast::<pulumi::PropertyValue>());

        Ok(())
    });
}
```

Provider SDKs are generated per project from the provider's schema with `pulumi package gen-sdk`. Every generated args struct derives `Default` and every field is an `Option`, so a program names only the inputs it sets and closes the literal with `..Default::default()`. A provider release that adds an optional input will not break your program.

## What works today

1. **The full language conformance suite.** All of Pulumi's language conformance tests pass.
1. **SDK generation at real-world scale.** AWS, Azure, GCP.
1. **Twenty-two examples that compile.** The repository ports the usual [example](https://github.com/pulumi-labs/pulumi-rust/tree/main/examples) scenarios to Rust across AWS, Azure, Google Cloud, Kubernetes, DigitalOcean, and Docker.

## How it works

The plugin is a language host: a gRPC server implementing the Pulumi engine's interface, which is the same architecture behind every Pulumi language. The CLI launches it to run programs with Cargo, to generate Rust SDKs from provider schemas, and to generate Rust projects from PCL programs.

Your program never sees any of that. A Pulumi Rust project is an ordinary crate with a `Pulumi.yaml` beside its `Cargo.toml`, and the runtime dependency is one entry in `[dependencies]`.

## Getting started

You need Rust 1.85+, Go 1.25+, and the Pulumi CLI. Nothing is published to crates.io yet and there are no prebuilt plugin binaries, so both the SDK and the plugin come from a checkout, and the project template wires the SDK in by relative path. That is why your project sits next to the checkout:

```sh
git clone https://github.com/pulumi-labs/pulumi-rust
(cd pulumi-rust/pulumi-language-rust && go build .)
export PATH="$PWD/pulumi-rust/pulumi-language-rust:$PATH"

cp -r pulumi-rust/templates/rust my-demo && cd my-demo
```

Fill in `${PROJECT}` in `Cargo.toml` and `Pulumi.yaml` and `${DESCRIPTION}` in `Pulumi.yaml`, then:

```sh
pulumi stack init dev
pulumi up
```

And that's it!

## Try it

1. The [pulumi-rust repository](https://github.com/pulumi-labs/pulumi-rust) has the SDK, the language plugin, and the project template.
1. The [examples directory](https://github.com/pulumi-labs/pulumi-rust/tree/main/examples) has all twenty-two programs, each with its own README and pinned provider version.

If you want Pulumi in Rust to become real, the strongest signal you can send is to use it. Run an example, port a small stack, and [file an issue](https://github.com/pulumi-labs/pulumi-rust/issues) when something breaks or something works. Community interest is what moves a Labs project toward full support.
