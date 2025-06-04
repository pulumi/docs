---
title: "Announcing Pulumi Identity and Access Management (IAM)"
allow_long_title: true
date: 2025-06-05
draft: false
meta_desc: "Introducing Pulumi IAM: A new era of granular access control across Pulumi Cloud, starting with Custom Roles and scoped Access Tokens for enhanced security and automation."
meta_image: "meta.png" 
authors:
  - german-lena
  - devon-grove
  - arun-loganathan
tags:
  - iam
  - rbac
  - security
  - features
  - pulumi-cloud
  - access-tokens
  - oidc
---

Cloud development is accelerating at an unprecedented pace, fueled by AI and the relentless drive for innovation. But this incredible speed demands unwavering trust in your security posture. How do you empower teams to deploy rapidly and frequently without opening doors to risk or violating compliance mandates? Today, we're thrilled to answer that critical challenge by introducing **Pulumi Identity and Access Management** (IAM) – a foundational new capability designed to embed robust, granular security directly into your cloud development lifecycle, enabling you to innovate both quickly and safely with Pulumi. Pulumi IAM provides the unified framework for fine-grained authorization needed to confidently manage modern cloud infrastructure and applications across the entire Pulumi Cloud platform.

<!--more-->

## Our Vision for Pulumi IAM

Pulumi IAM is a foundational investment, delivering enterprise-grade access management through a phased approach. Today's release marks the beginning, with much more planned:

*   **Phase 1: Granular Access Tokens & Custom Roles (Available Today)**
    *   Define custom, reusable **Permissions** with fine-grained actions (e.g., `stack:delete` only).
    *   Create **Custom Roles** by combining Permissions with specific Pulumi Entities (Stacks, Environments, etc.).
    *   Generate **Organization Access Tokens** scoped precisely to these Custom Roles, perfect for secure automation.

*   **Phase 2: User & Team Role Assignment (Coming Soon)**
    *   Leverage **OIDC configuration** to dynamically assume Custom Roles for secure, tokenless authentication from CI/CD systems like GitHub Actions, GitLab, and more.
    *   Assign these powerful Custom Roles directly to **individual users and teams** within your Pulumi organization.
    *   Implement a complete overhaul of user and team access management, moving beyond the basic `Admin`/`Member` distinctions, and enabling reusability of custom building blocks permissions and roles that work for your organization
 
*   **Phase 3: Advanced Authorization & Scalability (Future Release)**
    *   Introduce **Attribute-Based Access Control (ABAC)**, allowing policies based on tags or other attributes of Pulumi Entities (e.g., "grant 'dev-role' access to all stacks tagged 'env:dev'").
    *   Enable the creation of **Custom RBAC Policies** with conditional logic for highly specific access scenarios and reuse them
    *   Provide mechanisms to manage permissions across hundreds or thousands of Pulumi Entities efficiently.

## A Foundation for Zero Trust & Unified Security

Pulumi IAM isn't just another feature; it's a foundational pillar underpinning security across the entire Pulumi Cloud ecosystem, enabling organizations to implement **Zero Trust** principles for their infrastructure management. Modern security models assume breaches will happen and demand rigorous verification for every access request. Static, organization-wide roles no longer suffice where separation of duties, least privilege, and compliance are paramount.

Pulumi IAM addresses these challenges by providing:

*   **Least Privilege Enforcement:** Define precisely *who* can do *what* on *which* specific resources, minimizing the potential impact if credentials or accounts are compromised. This is core to Zero Trust – grant only the minimum necessary access, verified at the point of action.
*   **Granular Control Across Pulumi:**
    *   **Infrastructure as Code (IaC):** Apply fine-grained controls over Pulumi Stacks 
    *   **Secrets Management:** Define specific access levels for Pulumi ESC Environments.
    *   **Insights:** Manage permissions for Pulumi Insights account settings.
*   **Secure Automation:** Provide secure, least-privilege tokens and OIDC integration for CI/CD pipelines and automation, drastically reducing the risk associated with over-privileged service accounts.
*   **Unified, Scalable Governance:** Establish a consistent authorization model that simplifies administration and scales from small teams to complex enterprise environments, ensuring security doesn't hinder velocity.

## Launching Today: Granular Access Tokens via Custom Roles

This vision begins today with the initial phase of Pulumi IAM, enabling you to define **Custom Roles** built from **fine-grained Permissions** and apply them specifically to **Organization Access Tokens** and **OIDC configurations**. This initial step provides immediate, significant security benefits, particularly for automation:

*   **True Least Privilege for CI/CD:** Scope pipeline tokens to *only* the actions (e.g., `pulumi up`) and Entities (e.g., `stack: myapp-prod`) they absolutely need.
*   **Reduced Blast Radius:** If a scoped token is compromised, the potential damage is limited strictly to the permissions defined in its associated role.
*   **Enhanced Compliance:** Demonstrate precise control over programmatic access to auditors.
*   **Secure OIDC Integration:** Implement tokenless workflows where CI/CD runners or other services dynamically assume specific Pulumi Roles with narrowly defined permissions.

## How to Get Started with Granular Access Tokens

Configuring and using Custom Roles for scoped tokens is done via the Pulumi Cloud console:

#### 1. Define a Custom Permission Set (Optional)

* Create reusable sets of fine-grained permissions. Navigate to Organization Settings -> Roles & Permissions -> Permissions.*

*Click "Create", name it (e.g., "Stack Update Only"), select Resource Type (e.g., Stack), check specific permissions (`stack:read`, `stack:update`), and save.

#### 2. Create a Custom Role

* Combine permissions with specific resources. Navigate to Organization Settings -> Roles & Permissions -> Roles.*

* Click "Create", name it (e.g., "CICD-ProdApp-Deployer"). Add policies: select Resource Type (e.g., Stacks), choose a Permission Set (standard or custom), specify target Stacks, and save. Add more policies for different resource types (Environments, etc.) as needed.

#### 3. Generate a Scoped Organization Access Token

* Navigate to User Settings -> Access Tokens -> Organization Access Tokens.*
* Click "Create token". Provide a description. **Select your Custom Role** from the "Role" dropdown. Generate the token.

#### 4. Configure OIDC Role Assumption (Optional)

*Navigate to Organization Settings -> Integrations -> OIDC.*
When configuring your OIDC provider, map claims to **assume a specific Custom Role**.


## New Scenarios Unlocked Today

This release immediately enables more secure and compliant workflows:

*   **Secure Multi-Environment CI/CD:** A single pipeline can use different OIDC configurations or tokens based on the target environment (dev, staging, prod), each assuming a role with appropriately restricted permissions (e.g., read-only for prod dependencies, write for the target stack).
*   **Restricted Operational Scripts:** An automation script designed only to read audit logs can use a token tied to a role granting *only* `audit_log:read` permission, preventing accidental or malicious modifications.
*   **Safer ChatOps & Tooling:** Integrations like ChatOps bots can operate with tokens scoped down to only necessary actions (e.g., triggering a `pulumi preview` on specific stacks).

{{% notes type="info" %}}
**Available Today:** Custom Permissions, Custom Roles, and the ability to scope Organization Access Tokens and OIDC configurations using these roles, is **available now** for customers on the **Pulumi Enterprise** and **Pulumi Business Critical** tiers. Explore these features in your Pulumi Cloud organization settings!
{{% /notes %}}

## Conclusion: Building a More Secure Future

Pulumi Identity and Access Management (IAM) represents a fundamental advancement in securing cloud development lifecycles managed by Pulumi, providing the controls needed to confidently embrace speed and scale. Today’s launch of Granular Access Tokens via Custom Roles provides immediate security improvements for automation and programmatic access, laying the vital groundwork for our comprehensive IAM vision rooted in Zero Trust principles.

This empowers platform and security teams with the fine-grained control needed to implement least privilege, enhance compliance, and scale Pulumi usage securely without sacrificing velocity.

We encourage our Enterprise and Business Critical customers to explore Custom Roles and Granular Access Tokens today. Dive into the [documentation]() (link placeholder) and start building roles tailored to your security requirements. We welcome your feedback and feature requests in our [GitHub repository](https://github.com/pulumi/pulumi-service/issues) (link placeholder). Join us as we build a more secure foundation for cloud engineering!