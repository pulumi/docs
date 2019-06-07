---
title: "Container Management with Pulumi"
date: 2018-07-23T09:37:50-07:00
layout: "containers"
page_class: "topic"

url: "/containers"

meta_title: "Container Management with Pulumi"
meta_desc: "Pulumi provides a cloud native programming model for container management. Any code, any cloud, any app."
meta_image: "assets/images/pulumi.png"

topic: "Cloud Native Infrastructure as Code"
hero_title: "Container Management with Pulumi"
hero_description: "Pulumi provides a cloud native programming model for container management: deploy Docker to AWS Fargate, Microsoft ACI, and Kubernetes.<br><br>Any code, any cloud, any language."
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
<pre><code class="javascript hljs">// Deploy Nginx to AWS Fargate

import * as cloud from "@pulumi/cloud";


let nginx = new cloud.Service("nginx", {<br>
    image: "nginx",<br>
    ports: [{ port: 80 }],<br>
    replicas: 2,<br>
});


export let url = nginx.defaultEndpoint;<br/><br><br/><br/></code></pre>
        </div>
    </div>
</div>'
---
