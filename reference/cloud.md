---
title: "Cloud Framework"
---

JavaScript and TypeScript API reference: [@pulumi/cloud](../packages/pulumi-cloud)

The `@pulumi/cloud` package lets you program infrastructure and application logic, side by side in harmony, using
simple, high-level cloud building blocks.  This package has three key defining attributes:

- **Easy Cloud Development**: Build robust and scalable cloud applications with just a few lines of code.
- **Cloud Agnostic**: Not specific to any one particular cloud (AWS, Azure, Google Cloud, Kubernetes, and various on-premises clouds). Applications built using the high-level `@pulumi/cloud` components like [Service], [Table], [Topic] and [HttpEndpoint] can be deployed to a variety of cloud platforms. Although Pulumi only support AWS today in this framework, our plan is to offer an implementation of this on all major clouds.
* **Serverless**: The `@pulumi/cloud` makes it easy to build applications with minimal fixed infrastructure, event-driven application logic, and using resources that are charged based on actual consumption.

## Examples

See the following examples of programs that use the Pulumi Cloud library:

- [URL Shortener](https://github.com/pulumi/examples/tree/master/cloud-ts-url-shortener/). A complete URL shortener web application using high-level `cloud.Table` and `cloud.HttpEndpoint` components.
- [Video Thumnailer](https://github.com/pulumi/examples/tree/master/cloud-js-thumbnailer/). An end-to-end pipeline for generating keyframe thumbnails from videos uploaded to a bucket using containerized [FFmpeg](https://www.ffmpeg.org/).  
- [Voting App](https://github.com/pulumi/examples/tree/master/cloud-ts-voting-app). A simple voting app example that uses two containers: Redis for the data store and Python Flask app for the frontend.

🚧 TODO:
* Example program
* Configuration
* Link to reference docs
* Relationship to Terraform provider

<!-- LINKS -->

[Service]: /packages/pulumi-cloud/interfaces/_service_.service.html
[Table]: /packages/pulumi-cloud/interfaces/_service_.service.html
[Topic]: /packages/pulumi-cloud/interfaces/_topic_.topic.html
[HttpEndpoint]: /packages/pulumi-cloud/interfaces/_httpendpoint_.httpendpoint.html