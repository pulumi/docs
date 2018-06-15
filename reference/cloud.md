---
title: "Cloud Framework"
---

The `@pulumi/cloud` package lets you program infrastructure and application logic, side by side in harmony, using
simple, high-level cloud building blocks.  This package has three key defining attributes:

- **Easy Cloud Development**: Build robust and scalable cloud applications with just a few lines of code.
- **Cloud Agnostic**: Not specific to any one particular cloud (AWS, Azure, Google Cloud, Kubernetes, and various on-premises clouds). Applications built using the high-level `@pulumi/cloud` components like [Service], [Table], [Topic] and [API] can be deployed to a variety of cloud platforms. Although Pulumi only support AWS today in this framework, our plan is to offer an implementation of this on all major clouds.
* **Serverless**: The `@pulumi/cloud` makes it easy to build applications with minimal fixed infrastructure, event-driven application logic, and using resources that are charged based on actual consumption.

This library is open source and available in the [pulumi/pulumi-cloud](https://github.com/pulumi/pulumi-cloud)
repo.  Full API documentation is available [here](./pkg/nodejs/@pulumi/cloud/index.html).

## Examples

See the following examples of programs that use the Pulumi Cloud library:

- [URL Shortener](https://github.com/pulumi/examples/tree/master/cloud-ts-url-shortener/). A complete URL shortener web application using high-level `cloud.Table` and `cloud.API` components.
- [Video Thumnailer](https://github.com/pulumi/examples/tree/master/cloud-js-thumbnailer/). An end-to-end pipeline for generating keyframe thumbnails from videos uploaded to a bucket using containerized [FFmpeg](https://www.ffmpeg.org/).  
- [Voting App](https://github.com/pulumi/examples/tree/master/cloud-ts-voting-app). A simple voting app example that uses two containers: Redis for the data store and Python Flask app for the frontend.

<!-- LINKS -->

[Service]: pkg/nodejs/@pulumi/cloud/index.html#Service
[Table]: pkg/nodejs/@pulumi/cloud/index.html#Table
[Topic]: pkg/nodejs/@pulumi/cloud/index.html#Topic
[API]: pkg/nodejs/@pulumi/cloud/index.html#API
