---
title: "Improve Image Build Efficiency with the Pulumi Docker Provider 4.0"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2023-02-28T09:00:00-05:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: Announcing the Pulumi Docker Provider 4.0, with improved image build efficiency, Docker BuildKit support, and availability by Pulumi Yaml and Pulumi Java programs.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - monica-rodriguez

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - containers
    - docker   
    - providers

---

The Pulumi Docker Provider has been a top Pulumi provider since it launched in 2018. It can be used to provision any of the resources available in Docker, including managing containers, images, networks, volumes and more.  

One of the most heavily used features of this provider is the `docker.Image` resource, which enables Pulumi users to build and (optionally) push a local Docker context (like an application folder), to a registry as part of a Pulumi deployment. Today we are excited to announce a set of improvements to the Pulumi Docker Provider Image Resource driven by the feedback we have received from our community. This set of improvements includes:

* Improved image build efficiency
* BuildKit support with cross-platform builds
* Pulumi YAML and Pulumi Java support

<!-- add more in why docker provider is a top provider and what can be done with it-->

<!--more-->

### Improved image build efficiency

In order to improve efficiency we have changed the default behavior to rebuild only on context change. This reduces build time and overall runtime in your Pulumi program. This functionality as well as other improvements we are announcing today is a [highly requested feature](https://github.com/pulumi/pulumi-docker/issues/132) from our community.

<!-- Add image/gif showing output during build -->

### BuildKit support

The enhanced functionality and performance provided by the [Docker BuildKit](https://docs.docker.com/build/buildkit/) is now fully available to be leveraged in your Pulumi programs. BuildKit comes with functionality for improving your builds’ performance and the reusability of your Dockerfiles. Cross-platform builds are now supported so that images can be built to target a container runtime that is different from the build environment.

<!-- Add image or code snippet for buildkit options or cross platform builds-->

### Pulumi YAML and Pulumi Java support

We announced [Pulumi YAML and Pulumi Java](https://www.pulumi.com/blog/pulumi-universal-iac/) last year and are excited to have extended support to the Pulumi Docker Provider. Previously the Pulumi Docker Provider Image Resource was a [Component Resource](https://www.pulumi.com/docs/intro/concepts/resources/components/), a logical grouping of resources, and now we have made it a [Custom Resource](https://www.pulumi.com/docs/intro/concepts/resources/#resources), a provider managed resource. This change enabled auto-support of all Pulumi languages. In addition, as a Custom Resource the resource can participate in the CRUD (create, replace, update, delete) lifecycle.

### Migrating to 4.0

```typescript

...
```

The Docker Provider Image Resource has everything you need to build, run, and push Docker images for any container registry. Try it out today!
