---
title: "Serverless Programming with Pulumi"
date: 2018-07-23T09:37:50-07:00
layout: "serverless"
page_class: "topic"

url: "/serverless"

meta_title: "Serverless Programming with Pulumi"
meta_desc: "Pulumi provides a cloud native programming model for serverless applications. Any code, any cloud, any app."
meta_image: "/images/pulumi.png"

topic: "Cloud Native Infrastructure as Code"
hero_title: "Serverless Programming with Pulumi"
hero_description: "Pulumi provides a cloud native programming model for serverless applications: from high-level multi-cloud, to fine-grained cloud-specific libraries.<br><br>Any code, any cloud, any language."
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
<pre><code class="javascript hljs">// Create a serverless REST API

import * as cloud from "@pulumi/cloud";<br/>

let app = new cloud.API("my-app");<br/>
app.static("/", "www");<br/>

// Serve a simple REST API on `GET /hello`:

app.get("/hello", (req, res) =><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;res.json({ hello: "World!" }));</br>

export let url = app.publish().url;<br/><br/><br/></code></pre>
        </div>
    </div>
</div>'
---
