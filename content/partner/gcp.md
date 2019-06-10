---
title: "Cloud Native Infrastructure as Code for Google Cloud with Pulumi"
date: 2018-09-01T09:37:50-07:00
layout: "gcp"
page_class: "partner"

url: "/gcp"

meta_title: "Cloud Native Infrastructure as Code for Google Cloud with Pulumi"
meta_desc: "Programming Google Cloud with Pulumi for huge productivity gains, and a unified programming model for Devs and DevOps."
meta_image: "/images/pulumi.png"

topic: "Cloud Native Infrastructure as Code"
hero_title: "Program the cloud with Pulumi and Google Cloud"
hero_description: "Pulumi provides a cloud native programming model for Google Cloud to create containers, serverless functions, and infrastructure, enabling the delivery of Cloud Native Infrastructure as Code, using real programming languages. <br><br>Find out how to program the cloud with Pulumi and Google Cloud."
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
<pre><code class="javascript hljs">import * as k8s from "@pulumi/kubernetes";
<br>import * as pulumi from "@pulumi/pulumi";
<br>import { k8sProvider, k8sConfig } from "./cluster";

<br>const name = `${pulumi.getProject()}-${pulumi.getStack()}`;
<br>const canaryLabels = { app: `canary-${name}` };
<br>const canary = new k8s.apps.v1beta1.Deployment("canary", {
    <br>&nbsp;&nbsp;spec: {
        <br>&nbsp;&nbsp;&nbsp;&nbsp;selector: { matchLabels: canaryLabels },
        <br>&nbsp;&nbsp;&nbsp;&nbsp;replicas: 1,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;template: {
            <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metadata: { labels: canaryLabels },
            <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spec: { containers: [{ name, image: "nginx" }] },
        <br>&nbsp;&nbsp;&nbsp;&nbsp;},
    <br>&nbsp;&nbsp;},
<br>}, { provider: k8sProvider });

<br>export let kubeConfig = k8sConfig;<br/><br/></code></pre>
        </div>
    </div>
</div>'
---
