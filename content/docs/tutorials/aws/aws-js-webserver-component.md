---
title: "AWS Web Server component example"
---

<a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/aws-js-webserver-component" target="_blank">
    <img src="https://get.pulumi.com/new/button.svg" alt="Deploy" style="float: right; padding: 8px; margin-top: -65px; margin-right: 8px">
</a>

> <a class="btn btn-secondary" href="https://github.com/pulumi/examples/tree/master/aws-js-webserver-component" target="_blank" style="float: right"><i class="fab fa-github pr-2"></i> VIEW CODE</a>
> The source code for this tutorial is available [on GitHub](https://github.com/pulumi/examples/tree/master/aws-js-webserver-component). Ensure you have
> a copy locally and have changed into its directory before starting the tutorial's steps.


Deploy an EC2 instance using `@pulumi/aws`, using a common module for creating an instance. A function `createInstance` is defined in [webserver.js](webserver.js) which is then used in main program.

For a walkthrough of the main example, [Infrastructure on AWS](https://www.pulumi.com/docs/reference/tutorials/aws/tutorial-ec2-webserver/).

