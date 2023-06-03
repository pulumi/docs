---
title_tag: "Convert Code to Pulumi"
meta_desc: Pulumi converters allow you to convert ARM, CloudFormation, Kubernetes CustomResources, Kubernetes YAML, and Terraform to Pulumi.
title: Convert code
h1: Convert code to Pulumi
menu:
  usingpulumi:
    identifier: converters
    parent: adopting-pulumi
    weight: 4
aliases:
- /docs/converters/
---

Pulumi converters allow you to convert ARM, CloudFormation, Kubernetes CustomResources, Kubernetes YAML, and Terraform to Pulumi.

<ul class="">
    <li class="pt-4">
        <a class="" href="/arm2pulumi">
        ARM to Pulumi:
        </a>
        This conversion tool will do the magic of translating your ARM templates into modern code using Pulumi.
    </li>
    <li class="pt-4">
        <a class="" href="/cf2pulumi">
        CloudFormation to Pulumi:
        </a>
        This conversion tool will do the magic of translating your CloudFormation templates into TypeScript/JavaScript, Python, Go and C# using Pulumi.
    </li>
    <li class="pt-4">
        <a class="" href="/blog/introducing-crd2pulumi">
        Kubernetes CustomResources to Pulumi:
        </a>
        CustomResources in Kubernetes allow users to extend the API with their types. These types are defined using CustomResourceDefinitions (CRDs), which include an OpenAPI schema.
        Our new crd2pulumi tool takes the pain out of managing CustomResources by generating types in the Pulumi-supported language of your choice!
    </li>
    <li class="pt-4">
        <a class="" href="/kube2pulumi">
        Kubernetes YAML to Pulumi:
        </a>
        This conversion tool will do the magic of translating your YAML into modern code using Pulumi.
    </li>
    <li class="pt-4">
        <a class="" href="/tf2pulumi">
        Terraform to Pulumi:
        </a>
        This conversion tool will do the magic of translating your HCL into modern code using Pulumi.
    </li>
</ul>
