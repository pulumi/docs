---
title_tag: "Pre-built Policy Packs"
meta_desc: Pulumi-authored pre-built policy packs for CIS, NIST, PCI DSS, HITRUST, AWS Organizations tag policies, and Pulumi best practices.
title: "Pre-built Policy Packs"
h1: "Pre-built Policy Packs"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    reference:
        name: Pre-built Policy Packs
        parent: reference-home
        weight: 8
        identifier: reference-pre-built-policy-packs
---

[Pulumi Policies](/docs/insights/policy/) lets you enforce rules on infrastructure at preview and update time, rejecting stacks that violate security, cost, or compliance standards. Pulumi maintains a set of pre-built policy packs that cover common regulatory and best-practice frameworks so you can adopt them without authoring each rule yourself.

## Available policy packs

### Pulumi best practices

Pulumi-authored policies that flag common misconfigurations across major cloud providers.

- [AWS](/docs/reference/pre-built-policy-packs/pulumi-best-practices/aws/)
- [Azure](/docs/reference/pre-built-policy-packs/pulumi-best-practices/azure/)
- [Google Cloud](/docs/reference/pre-built-policy-packs/pulumi-best-practices/google-cloud/)

### CIS Benchmarks

Policies that correspond to the Center for Internet Security (CIS) Foundations Benchmarks.

- [CIS AWS Foundations Benchmark](/docs/reference/pre-built-policy-packs/cis/aws/)
- [CIS Microsoft Azure Foundations Benchmark](/docs/reference/pre-built-policy-packs/cis/azure/)
- [CIS Google Cloud Platform Foundations Benchmark](/docs/reference/pre-built-policy-packs/cis/google-cloud/)

### CIS Kubernetes Benchmarks

Kubernetes-focused CIS benchmarks for managed Kubernetes services on each major cloud.

- [CIS Kubernetes Benchmark on AWS (EKS)](/docs/reference/pre-built-policy-packs/cis-kubernetes/aws/)
- [CIS Kubernetes Benchmark on Azure (AKS)](/docs/reference/pre-built-policy-packs/cis-kubernetes/azure/)
- [CIS Kubernetes Benchmark on Google Cloud (GKE)](/docs/reference/pre-built-policy-packs/cis-kubernetes/google-cloud/)

### NIST 800-53

Policies aligned to the NIST 800-53 control catalog.

- [NIST 800-53 for AWS](/docs/reference/pre-built-policy-packs/nist/aws/)

### PCI DSS

Policies aligned to the Payment Card Industry Data Security Standard.

- [PCI DSS for AWS](/docs/reference/pre-built-policy-packs/pci-dss/aws/)

### HITRUST CSF

Policies aligned to the HITRUST Common Security Framework.

- [HITRUST CSF for AWS](/docs/reference/pre-built-policy-packs/hitrust/aws/)
- [HITRUST CSF for Azure](/docs/reference/pre-built-policy-packs/hitrust/azure/)
- [HITRUST CSF for Google Cloud](/docs/reference/pre-built-policy-packs/hitrust/google-cloud/)

### AWS Organizations Tag Policies

Enforce AWS Organizations tagging standards on Pulumi-managed resources.

- [AWS Organizations Tag Policies for AWS](/docs/reference/pre-built-policy-packs/aws-organizations-tag-policies/aws/)

## Learn more

- [Pulumi Policies](/docs/insights/policy/) — the Pulumi Policy as Code framework.
- [Write your own policy pack](/docs/insights/policy/policy-packs/) — author custom policies in TypeScript or Python.
