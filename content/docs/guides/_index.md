---
title: Guides
menu:
  userguides:
    identifier: guides
---

Pulumi’s approach to infrastructure as code is great for continuous delivery, secure collaboration, and easy management of common cloud services and operations.

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><i class="fab fa-connectdevelop pr-2"><a href="{{< relref "continuous-delivery" >}}"></i> Continuous Delivery</a></h3>
        <p>
            Integrate Pulumi with your current continuous delivery pipeline.
        </p>
        <ul class="p2">
            <li><a href="{{< relref "continuous-delivery/aws-code-services" >}}">AWS Code Services</a></li>
            <li><a href="{{< relref "continuous-delivery/azure-devops" >}}">Azure Devops</a></li>
            <li><a href="{{< relref "continuous-delivery/github-actions" >}}">GitHub Actions</a></li>
        </ul>
            <p class="mt-6">
                <a class="btn btn-secondary" href="{{< relref "continuous-delivery" >}}">View More</a>
            </p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "saml" >}}"><i class="fas fa-user-lock pr-2"></i> SAML Integrations</a></h3>
        <p>
            Learn about <a href="{{< relref "saml/sso" >}}">key SAML SSO configuration properties</a>, and link your Pulumi organization with your SAML 2.0 identity provider. Have members of your organization sign in via SSO.
        </p>
        <ul class="p2">
            <li><a href="{{< relref "saml/aad" >}}">Azure AD</a></li>
            <li><a href="{{< relref "saml/gsuite" >}}">Google Suite</a></li>
            <li><a href="{{< relref "saml/okta" >}}">Okta</a></li>
        </ul>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <a href="{{< relref "crosswalk/aws" >}}"><img class="h-auto w-32 center pt-6" src="/images/docs/reference/crosswalk/aws/logo.svg" alt="Pulumi Crosswalk for AWS"></a>
        <p>
            Use Pulumi's automatic well-architected best practices for common infrastructure-as-code tasks in AWS.
        </p>
        <ul class="p2">
            <li><a href="{{< relref "crosswalk/aws/api-gateway" >}}">API Gateway</a></li>
            <li><a href="{{< relref "crosswalk/aws/autoscaling" >}}">Autoscaling</a></li>
            <li><a href="{{< relref "crosswalk/aws/cloudwatch" >}}">Cloudwatch</a></li>
        </ul>
            <p class="mt-6">
                <a class="btn btn-secondary" href="{{< relref "crosswalk/aws" >}}">View More</a>
            </p>
    </div>
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <a href="{{< relref "crosswalk/kubernetes" >}}"><img class="h-auto w-32 center pt-6" src="/images/docs/reference/crosswalk/kubernetes/crosswalk-for-k8s.svg" alt="Pulumi Crosswalk for Kubernetes"></a>
        <p>
        <p>
            Kubernetes for Humans. Pulumi encapsulates best practices for common infrastructure-as-code tasks in Kubernetes, and its underyling infrastructure.
        </p>
        <ul class="p2">
            <li><a href="{{< relref "crosswalk/kubernetes/control-plane" >}}">Managed Kubernetes Clusters</a></li>
            <li><a href="{{< relref "crosswalk/kubernetes/cluster-services" >}}">Cluster</a> and <a href="{{< relref "crosswalk/kubernetes/app-services" >}}">App</a> services.</li>
            <li><a href="{{< relref "crosswalk/kubernetes/apps" >}}">Deploy Workloads</a></li>
        </ul>
            <p class="mt-6">
                <a class="btn btn-secondary" href="{{< relref "crosswalk/kubernetes" >}}">View More</a>
            </p>
    </div>
</div>
<div>
    <p>
        If you’d like to see additional guides, please <a href="https://github.com/pulumi/docs/issues/new?title=New Guide Request">request one</a>. Pull requests are also welcome!
    </p>
</div>
