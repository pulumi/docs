---
title: "Products"
date: 2018-06-01T15:10:06-07:00
layout: "product"
identifier: "Products"
type: "page"
menu:
    main:
        weight: 1
    footer1:
        weight: 1

hero_title: "The Pulumi Platform"
hero_description: "Create, deploy, and manage cloud apps and infrastructure, for any cloud, in your favorite language. From infrastructure to containers to Kubernetes to serverless. Solutions for teams of all sizes, Dev and DevOps alike."
hero_buttons: "<a href='https://pulumi.io' class='button orange'>Read the Docs</a>"
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
<pre><code class=" hljs">$ pulumi up

<br>Previewing update of stack `mystack-dev`

<br>     Type
<br> +   pulumi:pulumi:Stack
<br> +   ├─ aws-infra:network:Network
<br> +   ├─ cloud:global:infrastructure
<br> +   │  ├─ aws:iam:Role
<br> +   │  ├─ aws:iam:RolePolicyAttachment
<br> +   ├─ cloud:bucket:Bucket
<br> +   │  ├─ cloud:function:Function
<br> +   │  │  └─ aws:serverless:Function
<br> +   │  │     ├─ aws:iam:Role
<br> +   │  │     ├─ aws:iam:RolePolicyAttachment
<br> +   │  │     └─ aws:lambda:Function
<br> +   │  ├─ aws:s3:Bucket
<br> +   ...

<br>info: 33 changes previewed:
<br>    + 33 resources to create</code></pre>
        </div>
    </div>
</div>'
---
