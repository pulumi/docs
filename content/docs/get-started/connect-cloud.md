---
title_tag: Connect Pulumi to Your Cloud Account
meta_desc: Pulumi uses your existing AWS, Azure, Google Cloud, or Kubernetes credentials — no separate credential system. Learn how to check and configure cloud access.
title: Connect Your Cloud Account
h1: Connect Your Cloud Account
menu:
    get-started:
        name: Connect Your Cloud Account
        parent: get-started-home
        weight: 2
        identifier: get-started-connect-cloud
---

Pulumi has no credential system of its own. It authenticates to your cloud the same way your cloud provider's own CLI and SDKs do — using the same environment variables, configuration files, and identity mechanisms. If your cloud provider's CLI already works on your machine, Pulumi already has everything it needs.

## How Pulumi authenticates

Each Pulumi provider uses the cloud vendor's official SDK and its standard credential chain, so any authentication method your cloud supports — CLI login, environment variables, instance profiles, workload identity — works with Pulumi unchanged. You can also set credentials explicitly for an individual [stack](/docs/iac/concepts/stacks/) using [provider configuration](/docs/iac/concepts/config/).

For the full range of options per provider, see the setup pages for [AWS](/registry/packages/aws/installation-configuration/), [Azure](/registry/packages/azure-native/installation-configuration/), [Google Cloud](/registry/packages/gcp/installation-configuration/), and [Kubernetes](/registry/packages/kubernetes/installation-configuration/).

## Check whether you're already connected

Run your cloud's identity check. If it prints your account, identity, or cluster details, Pulumi can already manage resources there and you can continue straight to writing your program.

| Cloud | Command | Success looks like |
| --- | --- | --- |
| AWS | `aws sts get-caller-identity` | Your user ID, account, and ARN are printed |
| Azure | `az account show` | Your subscription and tenant details are printed |
| Google Cloud | `gcloud config list` | Your active account and project are printed |
| Kubernetes | `kubectl cluster-info` | Your cluster's control plane address is printed |

## Set up access for your cloud

If the check above didn't succeed — or you'd like to review the details — each getting started guide has a configuration page for its cloud. These pages are part of the full tutorial flow, so the Previous and Next buttons on each page take you back to installing Pulumi or onward to creating and deploying your first project.

<section class="docs-home mt-4 mb-12">
    <div class="docs-home-section">
        <div class="cards-logo-label-link clouds">
            <a data-track="connect-aws-configure" href="/docs/iac/get-started/aws/configure/">
                <div class="card-icon">
                    <div class="icon aws-40"></div>
                </div>
                <div class="label">
                    <span class="text-sm text-gray-800 dark:text-gray-300">Configure access to AWS &rarr;</span>
                </div>
            </a>
            <a data-track="connect-azure-configure" href="/docs/iac/get-started/azure/configure/">
                <div class="card-icon">
                    <div class="icon azure-40"></div>
                </div>
                <div class="label">
                    <span class="text-sm text-gray-800 dark:text-gray-300">Configure access to Azure &rarr;</span>
                </div>
            </a>
            <a data-track="connect-google-configure" href="/docs/iac/get-started/gcp/configure/">
                <div class="card-icon">
                    <div class="icon google-cloud-40"></div>
                </div>
                <div class="label">
                    <span class="text-sm text-gray-800 dark:text-gray-300">Configure access to Google Cloud &rarr;</span>
                </div>
            </a>
            <a data-track="connect-kubernetes-configure" href="/docs/iac/get-started/kubernetes/configure/">
                <div class="card-icon">
                    <div class="icon kubernetes-40"></div>
                </div>
                <div class="label">
                    <span class="text-sm text-gray-800 dark:text-gray-300">Configure access to Kubernetes &rarr;</span>
                </div>
            </a>
        </div>
    </div>
</section>

## Best practice: short-lived credentials with Pulumi ESC

Long-lived static keys are the most common source of credential leaks. [Pulumi ESC](/docs/esc/) can mint short-lived cloud credentials on demand via OpenID Connect (OIDC), so nothing sensitive lives on your workstation or in CI. See the ESC login providers for [AWS](/docs/esc/providers/login/aws-login/), [Azure](/docs/esc/providers/login/azure-login/), and [Google Cloud](/docs/esc/providers/login/gcp-login/).

## Next steps

1. Pick your cloud above and continue its getting started flow — configuration is step 3 of the tutorial.
1. New to Pulumi entirely? Start from the [getting started overview](/docs/get-started/).
