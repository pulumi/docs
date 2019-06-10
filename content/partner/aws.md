---
title: "Cloud Native Infrastructure as Code for AWS with Pulumi"
date: 2018-07-23T09:37:50-07:00
layout: "aws"
page_class: "partner"

url: "/aws"

meta_title: "Cloud Native Infrastructure as Code for AWS with Pulumi"
meta_desc: "Programming the AWS cloud with Pulumi for huge productivity gains, and a unified programming model for Devs and DevOps."
meta_image: "/images/pulumi.png"

topic: "Cloud Native Infrastructure as Code"
hero_title: "Program the cloud with Pulumi and AWS"
hero_description: "<img src='/images/partners/aws-apn.png' style='height:190px; float:left; padding-right:20px;'>Pulumi provides a cloud native programming model for AWS to create containers, serverless functions, and infrastructure, enabling the delivery of Cloud Native Infrastructure as Code, using real programming languages. <br><br>Find out how to program the cloud with Pulumi and AWS."
hero_classes: "bg-purple white-text"
hero_right_content: '<div class="code_container">
    <div class="anim_headbar">
        <div class="dot-container">
            <div class="window-dot dot-red"></div>
            <div class="window-dot dot-yellow"></div>
            <div class="window-dot dot-green"></div>
        </div>
    </div>
    <div class="anim_textbox code_display_textbox">
        <div class="code-display">
<pre><code class="javascript hljs">const aws = require("@pulumi/aws");

<br>let size = "t2.micro";
<br>let ami  = "ami-7172b611"

<br>let group = new aws.ec2.SecurityGroup("web-secgrp", {
    <br>&nbsp;&nbsp;ingress: [
        <br>&nbsp;&nbsp;&nbsp;&nbsp;{ protocol: "tcp", fromPort: 22,
            <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
        <br>&nbsp;&nbsp;&nbsp;&nbsp;{ protocol: "tcp", fromPort: 80,
            <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    <br>&nbsp;&nbsp;],
<br>});

<br>let server = new aws.ec2.Instance("web-server-www", {
    <br>&nbsp;&nbsp;tags: { "Name": "web-server-www" },
    <br>&nbsp;&nbsp;instanceType: size,
    <br>&nbsp;&nbsp;securityGroups: [ group.name ],
    <br>&nbsp;&nbsp;ami: ami,
    <br>&nbsp;&nbsp;userData: userData
<br>});<br/><br/></code></pre>
        </div>
    </div>
</div>'
---
