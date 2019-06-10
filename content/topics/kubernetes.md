---
title: "Kubernetes with Pulumi"
date: 2018-07-23T09:37:50-07:00
layout: "kubernetes"
page_class: "topic"

url: "/kubernetes"

meta_title: "Kubernetes deployments with Pulumi"
meta_desc: "Pulumi provides a cloud native programming model for Kubernetes deployments and orchestration. Any code, any cloud, any app."
meta_image: "/images/pulumi.png"

topic: "Cloud Native Infrastructure as Code"
hero_title: "Kubernetes with Pulumi"
hero_description: "Pulumi provides a cloud native programming model for kubernetes deployments and orchestration: from on-premises to AWS EKS, Microsoft AKS, and Google GKE.<br><br>Any code, any cloud, any language."
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
<pre><code class="javascript hljs">import * as k8sjs from "./k8sjs";<br>

let redis = new k8sjs.ServiceDeployment("redis", {<br>
&nbsp;&nbsp;image: "k8s.gcr.io/redis:e2e",<br>
&nbsp;&nbsp;ports: [ 6379 ]<br>
});<br>

let web = new k8sjs.ServiceDeployment("web", {<br>
&nbsp;&nbsp;replicas: 3,<br>
&nbsp;&nbsp;image: "gcr.io/google-samples/gb-frontend:v4",<br>
&nbsp;&nbsp;ports: [ 80 ],<br>
&nbsp;&nbsp;loadBalancer: true,<br>
});<br>

export let frontendIp = web.ipAddress;<br/><br/></code></pre>
        </div>
    </div>
</div>'
---
