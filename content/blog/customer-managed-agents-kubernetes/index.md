---
title: "Kubernetes-native Option for Pulumi Deployments Customer-Managed Agents"
allow_long_title: true
date: 2024-07-29T09:08:31-07:00
draft: false
meta_desc: Introducing Kubernetes-native support for Customer Managed Agents in Pulumi Cloud for enhanced flexibility and control over your infrastructure deployments.
meta_image: meta.png
authors:
    - levi-blackstone
    - meagan-cojocar
tags:
    - releases
---

We are excited to announce the availability of Kubernetes-native support for Customer-Managed Agents for Pulumi Deployments, further enhancing the flexibility and control over your infrastructure deployments. This new feature allows you to self-host deployment agents within your Kubernetes environment, bringing the same power and flexibility of Pulumi-hosted deployments to isolated environments.

## Customer Managed Agents: Flexibility and Control

Customer Managed Agents, [announced earlier this year](/blog/customer-managed-deployment-agents-launch), allow you to self-host deployment agents, delivering the power and flexibility of Pulumi Deployments within your own infrastructure. Here’s how you can benefit:

- **Host Anywhere**: Deploy Customer Managed Agents on any hardware or environment of your choice, including fully private VPCs.
- **Compliance and Security**: Keep your cloud provider credentials within your private network, meeting stringent compliance requirements.
- **Scalability**: Set up multiple agent pools and scale dynamically, supporting up to 150 concurrent deployments.
- **Versatility**: Mix and match Pulumi-hosted and self-hosted deployments to suit different infrastructure needs.

### Key Features

1. **Multiple Deployment Triggers**: Supports all Pulumi deployment triggers such as Drift Detection, Scheduled Deployments, click to deploy, REST API, Git push, Review Stacks, and remote Automation API.
2. **OpenID Authentication**: Fetch tokens dynamically for increased security.
3. **Flexible Configuration**: Configure through YAML files or environment variables, adaptable to various deployment environments.

### Docker and Kubernetes Support

By default, Customer-Managed Agents are deployed using Docker. However, with this new release, you can now leverage Kubernetes for running these agents, enabling you to deploy it  within your existing infrastructure.

### Getting Started with Kubernetes

To use Kubernetes for running Customer-Managed Agents:

1. **Install the Pulumi GitHub App**: Ensure it's integrated with your source control.
2. **Set Up Deployment Pools**:
   - Navigate to Deployment Runners under Organization Settings in the left hand navigation bar.
   - Create a new pool by clicking 'Add new pool'
   - You will get a new access token, copy and save the token.
3. **Install Agents**:
   - Follow the provided instructions to install agents within your Kubernetes environment.
4. **Configure Agents**:
   - Use `pulumi-deployment-agent.yaml` for configuration.
   - Set environment variables directly in your Kubernetes Deployment.
5. **Configure Stack**:
   - Go to Deploy settings, found under the Settings tab on a stack. Scroll down and select the pool you created under the Deployment Runner pool drop-down.

### Verification

After setting up, verify the agent by doing a `pulumi refresh` through the Deploy Actions drop-down on your stack page.

To increase deployment concurrency, use the same token to set up multiple agents and they will be assigned to the same pool.

## Wrapping It Up

Customer-Managed Agents with Kubernetes support empower you to manage deployments according to your specific needs. Whether it’s for security, compliance, or operational efficiency, this feature provides the flexibility and control necessary for modern infrastructure management.

For more details, check out our [documentation](https://www.pulumi.com/docs/guides/continuous-delivery/customer-managed-agents/) or contact our sales team to get started with Customer-Managed Agents today.

Feel free to reach out with feedback or questions. We’re here to support you every step of the way.
