---
title_tag: Deploying into Air-Gapped Environments | Self-Hosting Pulumi
meta_desc: Learn how to deploy Pulumi Self-Hosted into an air-gapped environment, from setting up artifact mirrors to configuring the Pulumi CLI.
title: Air-Gapped
h1: Deploying Pulumi Self-Hosted into air-gapped environments
menu:
  administration:
        name: Air-gapped
        parent: administration-self-hosting
        weight: 5
        identifier: administration-security-compliance-self-hosted-airgapped
aliases:
- /docs/administration/self-hosting/airgapped/
- /docs/pulumi-cloud/admin/self-hosted/airgapped/
pulumi_cloud_feature: self-hosting
---

{{< self-hosting-trial-note />}}

For organizations operating in highly regulated industries or environments with strict security requirements, deploying cloud infrastructure in an air-gapped environment is often a requirement. Such environments do not have network connectivity with the outside world, which many of Pulumi's default workflows assume.

Pulumi can be configured to run in air-gapped environments through [self-hosting](/docs/administration/self-hosting/), enabling enterprises to manage infrastructure as code securely within their private networks, remaining compliant while gaining the benefits of modern infrastructure automation.

This guide explains how to deploy Pulumi Self-Hosted in an air-gapped environment, covering the key requirements, setup process, and best practices.

## Why deploy Pulumi in an air-gapped environment?

Pulumi Cloud is a secure service with compliance built in. The default mode is to use Pulumi as a multi-tenanted software-as-a-service (SaaS) over the internet. Pulumi also offers a Self-Hosted edition for those who want more control over their configuration, often for advanced security and compliance reasons. Air-gapped Self-Host builds upon this even further to use Pulumi in the most rigorous and secure configuration possible.

{{% notes type="info" %}}
For more information about Pulumi Cloud's security and compliance posture, [read our security whitepaper](/security/pulumi-cloud-security-whitepaper/).
{{% /notes %}}

Air-gapped environments are completely isolated from the public internet, for scenarios with heightened data security and compliance. Common air-gapped scenarios include:

* **Financial Services**: Ensuring sensitive transaction data remains within internal networks.
* **Healthcare**: Complying with HIPAA and other patient data protection regulations.
* **Government and Defense**: Meeting strict operational security (OPSEC) and classified data handling requirements.
* **Industrial and Manufacturing**: Protecting critical infrastructure from cyber threats.

Once its dependencies are mirrored internally, Pulumi Self-Hosted lets you run infrastructure automation in these environments without reaching the public internet.

## Preparing for an air-gapped deployment

Here are the general areas to consider when preparing to use Pulumi in an air-gapped environment:

* Get a Pulumi Self-Hosted license key and images
* Provision internal infrastructure and install Pulumi Cloud
* Create and configure artifact mirrors

### Get a Pulumi Self-Hosted license key and images

Ensure you have access to Pulumi Self-Hosted which requires a license key as well as the
[Pulumi Cloud Docker images](/docs/administration/self-hosting/components/) for the various backend services. If you
don't have these, [contact us](/contact/) or [request a Proof of Concept](/product/self-hosted/#self-hosted-trial).

### Provision internal infrastructure and install Pulumi Cloud

You must set up internal servers for running Pulumi Self-Hosted, such as Kubernetes or virtual machines, as well as the necessary data stores.

The complete infrastructure required typically includes:

* **Isolated compute environment**: A virtual machine (VM) or Kubernetes cluster within the air-gapped network.
* **Pulumi Self-Hosted installation artifacts**: These can be retrieved from a network-accessible environment and transferred to the air-gapped system.
* **Private container registry**: Stores the Pulumi Self-Hosted container images inside the air-gapped network so your compute environment can pull them.
* **Database and storage backend**: MySQL and object storage (such as MinIO or an on-premises S3-compatible storage system) for state management.
* **Internal package management**: To host Pulumi SDKs and required language runtimes, as external package managers (npm, PyPI, etc.) won't be accessible.
* **Automation and CI/CD setup**: Configured to run within the air-gapped network for secure infrastructure deployments.

Pulumi supports many [deployment options](/docs/administration/self-hosting/deployment-options/), so consult your Pulumi representative about which approach best meets your needs.

### Create and configure artifact mirrors

Since the environment lacks internet access, you must provide local mirrors for certain artifacts typically downloaded over the internet:

* Pulumi CLI and SDK packages (Node.js, Python, Go, .NET, etc.).
* Pulumi provider binaries.
* Container registries for Pulumi Cloud Docker images.

You must configure all tools, scripts, and automation to use these mirrors instead of the default public internet URLs.

## Step-by-step deployment instructions

After you prepare your air-gapped environment, follow these steps to install Pulumi Self-Hosted:

### Step 1: Deploy the Pulumi Self-Hosted backend

Pulumi Self-Hosted can be installed using Kubernetes, Docker, or virtual machines. In an air-gapped setup, follow these steps:

1. Set up storage services.
    * MySQL 8.0+ for application data storage.
    * Object storage for state management, for instance, MinIO or an internal S3-compatible service.
2. Download the [Pulumi Self-Hosted images](/docs/administration/self-hosting/components/).
    * Retrieve the necessary installation files and images from a networked machine.
    * Transfer them to your air-gapped environment using an offline medium (USB drive, offline repository, etc.).
3. Install Pulumi Self-Hosted (for instance, on Kubernetes) by following the guide for your chosen [deployment option](/docs/administration/self-hosting/deployment-options/).
    * Pull the Pulumi Self-Hosted images from your private container registry instead of a public registry.
4. Configure authentication and access control.
    * Integrate with your organization's internal identity provider using [SAML SSO](/docs/administration/self-hosting/saml-sso/).
    * Define role-based access controls (RBAC) to ensure proper permissions.
    * For more detailed organization configuration options, refer to [this onboarding guide](/docs/administration/get-started/).

### Step 2: Configure the Pulumi CLI and SDKs

To enable developers to use Pulumi within the air-gapped environment:

1. Distribute the Pulumi CLI.
    * Host Pulumi CLI binaries internally for offline installation.
    * Ensure team members install the CLI from the internal repository.
2. Set up package mirrors.
    * Mirror necessary SDKs and package registries for Node.js (npm), Python (PyPI), Go (Go Modules), and .NET (NuGet).
    * Ensure developers can pull Pulumi SDK packages from an internal mirror.
3. Configure Pulumi to use the self-hosted backend.
    * Set the Pulumi backend URL:

        ```bash
        $ pulumi login https://pulumi.corpnet.acmecorp.com
        ```

    * Use an internally hosted Pulumi provider mirror. Set [`PULUMI_PLUGIN_DOWNLOAD_URL_OVERRIDES`](/docs/iac/cli/environment-variables/) to redirect provider plugin downloads to it, or install plugins from transferred files with [`pulumi plugin install --file`](/docs/iac/cli/commands/pulumi_plugin_install/).
    * Set `PULUMI_SKIP_UPDATE_CHECK=true`. Otherwise, the CLI tries to contact `api.pulumi.com` to check for a newer version, even when you're logged in to Pulumi Self-Hosted.

### Step 3: Run Pulumi in air-gapped mode

Once Pulumi Self-Hosted is installed and the CLI is configured, teams can:

* Deploy infrastructure using `pulumi up` while storing state internally.
* Automate deployments via internal CI/CD systems like Jenkins, GitLab CI, or an internal GitHub Actions runner.
* Enforce policies using Pulumi Policy as Code, installing policy pack dependencies from your internal package mirrors.

## Best practices for air-gapped Pulumi deployments

Because air-gapped is not the default mode Pulumi Cloud uses, there are some best practices for running Pulumi in air-gapped environments:

* **Automate dependency updates**: Establish a periodic process to update Pulumi CLI, SDKs, and providers by syncing with an external, controlled environment.
* **Monitor and audit usage**: Implement internal logging and monitoring to track Pulumi operations.
* **Secure your secrets management**: Use a secure secrets management solution, such as [Pulumi ESC](/docs/esc/) which is included in Self-Hosted, to manage sensitive data.

## Next steps

Pulumi Self-Hosted enables organizations to deploy and manage infrastructure within secure, air-gapped environments. By mirroring dependencies, configuring internal storage, and leveraging self-hosted Pulumi services, teams can maintain modern infrastructure automation workflows while meeting strict security and compliance requirements.

Interested in deploying Pulumi in your air-gapped environment? [Contact us](/contact/) to learn more about Pulumi Self-Hosted and enterprise support options.
