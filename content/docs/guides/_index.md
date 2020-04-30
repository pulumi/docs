---
title: User Guides
meta_desc: Pulumi’s approach to infrastructure as code is great for continuous delivery,
           secure collaboration, and easy management of common cloud services and operations.
menu:
  userguides:
    name: Overview
    weight: 1
---

Pulumi’s approach to infrastructure as code is great for continuous delivery, secure collaboration, and easy management of common cloud services and operations.

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><i class="fab fa-connectdevelop pr-2"><a href="{{< prelref "continuous-delivery" >}}"></i> Continuous Delivery</a></h3>
        <p>
            Integrate Pulumi with your current continuous delivery pipeline.
        </p>
        <ul class="p2">
            <li><a href="{{< prelref "continuous-delivery/aws-code-services" >}}">AWS Code Services</a></li>
            <li><a href="{{< prelref "continuous-delivery/azure-devops" >}}">Azure Devops</a></li>
            <li><a href="{{< prelref "continuous-delivery/github-actions" >}}">GitHub Actions</a></li>
        </ul>
            <p class="mt-6">
                <a class="btn btn-secondary" href="{{< prelref "continuous-delivery" >}}">View More</a>
            </p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< prelref "saml" >}}"><i class="fas fa-user-lock pr-2"></i> SAML Integrations</a></h3>
        <p>
            Learn about <a href="{{< prelref "saml/sso" >}}">key SAML SSO configuration properties</a>, and link your Pulumi organization with your SAML 2.0 identity provider. Have members of your organization sign in via SSO.
        </p>
        <ul class="p2">
            <li><a href="{{< prelref "saml/aad" >}}">Azure AD</a></li>
            <li><a href="{{< prelref "saml/gsuite" >}}">Google Suite</a></li>
            <li><a href="{{< prelref "saml/okta" >}}">Okta</a></li>
        </ul>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <a href="{{< prelref "crosswalk/aws" >}}"><img class="h-auto w-32 center pt-6" src="/images/docs/reference/crosswalk/aws/logo.svg" alt="Pulumi Crosswalk for AWS"></a>
        <p>
            Use Pulumi's automatic well-architected best practices for common infrastructure-as-code tasks in AWS.
        </p>
        <ul class="p2">
            <li><a href="{{< prelref "crosswalk/aws/api-gateway" >}}">API Gateway</a></li>
            <li><a href="{{< prelref "crosswalk/aws/autoscaling" >}}">Autoscaling</a></li>
            <li><a href="{{< prelref "crosswalk/aws/cloudwatch" >}}">Cloudwatch</a></li>
        </ul>
            <p class="mt-6">
                <a class="btn btn-secondary" href="{{< prelref "crosswalk/aws" >}}">View More</a>
            </p>
    </div>
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <a href="{{< prelref "crosswalk/kubernetes" >}}"><img class="h-auto w-32 center pt-6" src="/images/docs/reference/crosswalk/kubernetes/crosswalk-for-k8s.svg" alt="Pulumi Crosswalk for Kubernetes"></a>
        <p>
        <p>
            Kubernetes for Everyone. Pulumi encapsulates best practices for common infrastructure-as-code tasks in Kubernetes, and its underyling infrastructure.
        </p>
        <ul class="p2">
            <li><a href="{{< prelref "crosswalk/kubernetes/control-plane" >}}">Managed Kubernetes Clusters</a></li>
            <li><a href="{{< prelref "crosswalk/kubernetes/cluster-services" >}}">Cluster</a> and <a href="{{< prelref "crosswalk/kubernetes/app-services" >}}">App</a> services.</li>
            <li><a href="{{< prelref "crosswalk/kubernetes/apps" >}}">Deploy Workloads</a></li>
        </ul>
            <p class="mt-6">
                <a class="btn btn-secondary" href="{{< prelref "crosswalk/kubernetes" >}}">View More</a>
            </p>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><i class="fas fa-shield-alt pr-2"><a href="{{< prelref "crossguard" >}}"></i>CrossGuard</a></h3>
        <p>
            Use Pulumi's CrossGuard to to enable cloud resource compliance using code.
        </p>
        <ul class="p2">
            <li><a href="{{< prelref "crossguard/core-concepts" >}}">Core Concepts</a></li>
            <li><a href="{{< prelref "crossguard/best-practices" >}}">Best Practices</a></li>
            <li><a href="{{< prelref "crossguard/configuration" >}}">Configuration</a></li>
            <li><a href="{{< prelref "crossguard/faq" >}}">Frequently Asked Questions</a></li>
        </ul>
            <p class="mt-6">
                <a class="btn btn-secondary" href="{{< prelref "crossguard" >}}">View More</a>
            </p>
    </div>
</div>
<div>
    <p>
        If you’d like to see additional guides, please <a href="https://github.com/pulumi/docs/issues/new?title=New Guide Request">request one</a>. Pull requests are also welcome!
    </p>
</div>
