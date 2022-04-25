---
title: Converters
meta_desc: Pulumi converters allow you to convert ARM, CloudFormation, Kubernetes CustomResources, Kubernetes YAML, and Terraform to Pulumi.
no_on_this_page: true
menu:
  converters:
      name: Overview
      weight: 1
---

Pulumi converters allow you to convert ARM, CloudFormation, Kubernetes CustomResources, Kubernetes YAML, and Terraform to Pulumi.

<ul class="">
    <li class="pt-4">
        <a class="" href="{{< relref "/arm2pulumi" >}}">
        ARM to Pulumi:
        </a>
        This conversion tool will do the magic of translating your ARM templates into modern code using Pulumi.
    </li>
    <li class="pt-4">
        <a class="" href="{{< relref "/cf2pulumi" >}}">
        CloudFormation to Pulumi:
        </a>
        This conversion tool will do the magic of translating your CloudFormation templates into TypeScript/JavaScript, Python, Go and C# using Pulumi.
    </li>
    <li class="pt-4">
        <a class="" href="{{< relref "/blog/introducing-crd2pulumi" >}}">
        Kubernetes CustomResources to Pulumi:
        </a>
        CustomResources in Kubernetes allow users to extend the API with their types. These types are defined using CustomResourceDefinitions (CRDs), which include an OpenAPI schema.
        Our new crd2pulumi tool takes the pain out of managing CustomResources by generating types in the Pulumi-supported language of your choice!
    </li>
    <li class="pt-4">
        <a class="" href="{{< relref "/kube2pulumi" >}}">
        Kubernetes YAML to Pulumi:
        </a>
        This conversion tool will do the magic of translating your YAML into modern code using Pulumi.
    </li>
    <li class="pt-4">
        <a class="" href="{{< relref "/tf2pulumi" >}}">
        Terraform to Pulumi:
        </a>
        This conversion tool will do the magic of translating your HCL into modern code using Pulumi.
    </li>
</ul>
