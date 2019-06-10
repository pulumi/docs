---
title: "Cloud Native Infrastructure as Code for Microsoft Azure with Pulumi"
date: 2018-09-01T09:37:50-07:00
layout: "azure"
page_class: "partner"

url: "/azure"

meta_title: "Cloud Native Infrastructure as Code for Microsoft Azure with Pulumi"
meta_desc: "Programming the Azure cloud with Pulumi for huge productivity gains, and a unified programming model for Devs and DevOps."
meta_image: "/images/pulumi.png"

topic: "Cloud Native Infrastructure as Code"
hero_title: "Program the cloud with Pulumi and Azure"
hero_description: "Pulumi provides a cloud native programming model for Azure to create containers, serverless functions, and infrastructure, enabling the delivery of Cloud Native Infrastructure as Code, using real programming languages. <br><br>Find out how to program the cloud with Pulumi and Azure."
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
<pre><code class="javascript hljs">import * as helm from "@pulumi/kubernetes/helm";
<br>import * as k8s from "@pulumi/kubernetes";
<br>import { k8sCluster, k8sProvider } from "./cluster";

<br>const apache = new helm.v2.Chart("apache", {
    <br>&nbsp;&nbsp;repo: "bitnami",
    <br>&nbsp;&nbsp;chart: "apache",
    <br>&nbsp;&nbsp;version: "1.0.0",
<br>}, { providers: { kubernetes: k8sProvider } });

<br>export let cluster = k8sCluster.name;
<br>export let kubeConfig = k8sCluster.kubeConfigRaw;
<br>export let serviceIP =
    <br>&nbsp;&nbsp;(apache.resources["v1/Service::default/apache-apache"]
    <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as k8s.core.v1.Service).
        <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spec.apply(s => s.clusterIP);<br/><br/></code></pre>
        </div>
    </div>
</div>'
---
