---
title_tag: Deploying into Air-Gapped Environments | Self-Hosting Pulumi
meta_desc: Learn how to deploy Pulumi self-hosted into air-gapped environments.
title: Air-Gapped
h1: Deploying Pulumi Self-Hosted into Air-Gapped Environments
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    cloud:
        name: Air-Gapped
        parent: pulumi-cloud-admin-self-hosted
        weight: 5
        identifier: pulumi-cloud-admin-self-hosted-airgapped
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, sign up for the [30-day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).
{{% /notes %}}

For organizations operating in highly regulated industries or environments with strict security requirements, deploying cloud infrastructure in an air-gapped environment is often a requirement. Such environments do not have network connectivity with the outside world, which many of Pulumi's default workflows assume.

Pulumi can be configured to run in air-gapped environments through [self-hosting](/docs/pulumi-cloud/admin/self-hosted), enabling enterprises to manage infrastructure as code securely within their private networks, remaining compliant while gaining the benefits of modern infrastructure automation.

In this guide, we will explore how to deploy Pulumi Self-Hosted in an air-gapped environment, covering the key requirements, setup process, and best practices.

## Why Deploy Pulumi in an Air-Gapped Environment?

Air-gapped environments are completely isolated from the public internet, for scenarios where data security and compliance are paramount. Common use cases include:

* **Financial Services**: Ensuring sensitive transaction data remains within internal networks.
* **Healthcare**: Complying with HIPAA and other patient data protection regulations.
* **Government and Defense**: Meeting strict operational security (OPSEC) and classified data handling requirements.
* **Industrial and Manufacturing**: Protecting critical infrastructure from cyber threats.

Pulumi Self-Hosted offers a robust solution for these environments, enabling infrastructure automation without requiring external network dependencies.

## Preparing for an Air-Gapped Deployment

Here are the general areas to consider when preparing to use Pulumi in an air-gapped environment:

* Obtain Pulumi Self-Hosted
* Provision Internal Infrastructure and Install Pulumi Cloud
* Create and Configure Artifact Mirrors

### Obtain Pulumi Self-Hosted

Ensure you have access to Pulumi Self-Hosted, which includes the Pulumi API and backend services. If you don't have
access, you can either [contact us](/contact) or [request access here](/product/self-hosted/#self-hosted-trial).

### Provision Internal Infrastructure and Install Pulumi Cloud

You must set up internal servers for running Pulumi Self-Hosted, such as Kubernetes or virtual machines, as well as the necessary data stores.

The complete infrastructure required typically includes:

* *An Isolated Compute Environment*: A virtual machine (VM) or Kubernetes cluster within the air-gapped network.
* *Pulumi Self-Hosted Installation Artifacts*: These can be retrieved from a network-accessible environment and transferred to the air-gapped system.
* *A Private Container Registry*: Required to store Pulumi service images for deployment.
* *Database and Storage Backend*: PostgreSQL and object storage (such as MinIO or an on-premises S3-compatible storage system) for state management.
* *Internal Package Management*: To host Pulumi SDKs and required language runtimes, as external package managers (npm, PyPI, etc.) won't be accessible.
* *Automation and CI/CD Setup*: Configured to run within the air-gapped network for secure infrastructure deployments.

Pulumi supports many [deployment options](/docs/pulumi-cloud/admin/self-hosted/deployment-options) so it is a good idea to consult with your Pulumi representative on what approach will best meet your needs.

### Create and Configure Artifact Mirrors

Since the environment lacks internet access, you must provide local mirrors for certain artifacts typically downloaded over the internet:

* Pulumi CLI and SDK packages (Node.js, Python, Go, .NET, etc.).
* Pulumi provider binaries.
* Container registries for Pulumi Cloud Docker images.

You must configure all tools, scripts, and automation to use these mirrors instead of the default public internet URLs.

## Step-by-Step Deployment Instructions

Here are more detailed instructions on how to install Pulumi Self-Hosted to your air-gapped environment once it has been prepared:

### Step 1: Deploy the Pulumi Self-Hosted Backend

Pulumi Self-Hosted can be installed using Kubernetes, Docker, or virtual machines. In an air-gapped setup, follow these steps:

1. Download the Pulumi Self-Hosted release
    * Retrieve the necessary installation files and images from a networked machine.
    * Transfer them to your air-gapped environment using an offline medium (USB drive, offline repository, etc.).
2. Install Pulumi Self-Hosted (for instance, on Kubernetes)
    * Deploy the Pulumi API server, database, and storage backend using Helm or static manifests.
    * Configure internal object storage (e.g., MinIO or an internal S3-compatible service) for state management.
3. Configure Authentication and Access Control
    * Integrate with your organization's internal identity provider (OIDC, LDAP, SAML).
    * Define role-based access controls (RBAC) to ensure proper permissions.

### Step 2: Configure the Pulumi CLI and SDKs

To enable developers to use Pulumi within the air-gapped environment:

1. Distribute the Pulumi CLI
    * Host Pulumi CLI binaries internally for offline installation.
    * Ensure team members install the CLI from the internal repository.
2. Set Up Package Mirrors
    * Mirror necessary SDKs and package registries for Node.js (npm), Python (PyPI), Go (Go Modules), and .NET (NuGet).
    * Ensure developers can pull Pulumi SDK packages from an internal mirror.
3. Configure Pulumi to Use the Self-Hosted Backend
    * Set the Pulumi backend URL:

        ```bash
        $ pulumi login https://pulumi.corpnet.acmecorp.com
        ```

    * Use an internally hosted Pulumi provider mirror.

### Step 3: Running Pulumi in Air-Gapped Mode

Once Pulumi Self-Hosted is installed and the CLI is configured, teams can:

* Deploy infrastructure using `pulumi up` while storing state internally.
* Automate deployments via internal CI/CD systems like Jenkins, GitLab CI, or an internal GitHub Actions runner.
* Enforce policies using Pulumi Policy as Code (CrossGuard) without external dependencies.

## Best Practices for Air-Gapped Pulumi Deployments

Because air-gapped is not the default mode Pulumi Cloud uses, there are some best practices for running Pulumi in air-gapped environments:

* *Automate Dependency Updates*: Establish a periodic process to update Pulumi CLI, SDKs, and providers by syncing with an external, controlled environment.
* *Monitor and Audit Usage*: Implement internal logging and monitoring to track Pulumi operations.
* *Secure Your Secrets Management*: Use a secure secrets management solution, such as [Pulumi ESC](/docs/esc) which is included in Self-Hosted, to manage sensitive data.

## Next Steps

Pulumi Self-Hosted enables organizations to deploy and manage infrastructure within secure, air-gapped environments. By mirroring dependencies, configuring internal storage, and leveraging self-hosted Pulumi services, teams can maintain modern infrastructure automation workflows while meeting strict security and compliance requirements.

Interested in deploying Pulumi in your air-gapped environment? [Contact us](/contact) to learn more about Pulumi Self-Hosted and enterprise support options.
