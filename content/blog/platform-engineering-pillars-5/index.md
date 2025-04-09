---
title: "Security as an Enabler: Building Trust into Your Platform"
date: 2025-04-09T12:16:29-04:00
draft: false
meta_desc:
meta_image: meta.png
authors:
    - adam-gordon-bell
tags:
    - platform-engineering
    - platform-engineering-pillars
social:
    twitter:
    linkedin:

---
In previous articles in this series, we explored how [platform engineering](/blog/tag/platform-engineering-pillars/) transforms infrastructure chaos into consistent provisioning, enables self-service capabilities, and streamlines developer workflows. Each pillar builds upon the previous ones to create a foundation for developer productivity and organizational agility.

But there's still one critical element that can either accelerate or derail all this progress: security.

Traditional approaches to security often create friction. Security reviews happen at the end of development cycles, causing costly delays and rework. Security teams are seen as "the department of no," enforcing policies that feel arbitrary and restrictive. Developers face unclear requirements, manual processes, and bottlenecks that slow innovation—ultimately pushing teams to find workarounds that create even greater risks.

<!--more-->

Integrating security into your internal developer platform transforms security from a frustrating gatekeeper into a built-in enabler, helping developers move faster, safer, and with greater confidence.

Done right developers gain autonomy without compromising security, security teams become partners rather than blockers, and your organization builds a foundation of trust that accelerates innovation.

## The Problem: Security as a Gatekeeper

Traditional security practices often create friction rather than enable innovation. Developers frequently encounter last-minute security reviews that delay deployments, unclear or overly restrictive policies that feel arbitrary, and security teams perceived as blockers rather than collaborative partners.

This friction has real consequences. When security becomes a bottleneck, developers may resort to bypassing established processes, leading to shadow IT and increased risk from manual, inconsistent security practices. Ultimately, this slows innovation, reduces developer autonomy, and undermines the very agility your platform aims to achieve.

A common reaction to these traditional bottlenecks is to "shift security left," pushing security checks and responsibilities earlier into the development lifecycle. While incorporating security feedback early is crucial, simply shifting the entire burden onto developers isn't the ideal solution either. It risks overwhelming developers and can still lead to inconsistencies if not managed correctly. True enablement comes not just from shifting when security happens, but how it's integrated.

{{% notes type="info" %}}

### Security Responsibilities: Key Roles and Activities

Security responsibilities can be organized in different ways depending on your organization's size, structure, and maturity. Regardless of how these responsibilities are distributed, it's important to clearly understand the roles and activities involved:

- **Security Policy and Architecture (Security Teams)**:  
  - Define security policies, standards, and best practices.  
  - Provide guidance, education, and support to developers and infrastructure/platform roles.  
  - Conduct threat modeling, security architecture reviews, and proactive security assessments.

- **Security Operations (SecOps or SRE)**:  
  - Monitor, detect, and respond to security incidents in real-time.  
  - Manage security tooling, incident response workflows, and security automation.  
  - Collaborate closely with developers and infrastructure/platform roles to integrate security monitoring and response into daily workflows.

- **Infrastructure and Application Security (Platform Teams, DevOps, Developers)**:  
  - Embed security directly into infrastructure and application workflows.  
  - Implement secure defaults, policy-as-code, and automated security checks.  
  - Collaborate proactively with security policy and operations roles to ensure security is built-in, not bolted-on.

{{% /notes %}}

### The Solution: Embedding Security into Developer Workflows

The key to truly solving security friction, therefore, isn't just adding earlier checkpoints—it's embedding security directly into the platform and the daily workflows of your developers. Instead of treating security as a final hurdle or a complex new responsibility solely for developers, platform engineering integrates security early and continuously through secure-by-default components and automated guardrails. Let's explore how this looks in practice.

Let's explore how this looks in practice.

## Foundational Security Checks: Necessary but Not Sufficient

Integrating automated security scanning early in the CI/CD pipeline (using tools like Dependabot, Snyk, Trivy for vulnerability scanning, SAST, etc.) is a fundamental and necessary practice. Providing developers with this rapid feedback helps catch issues early.

However these "shift-left" checks are only part of the solution. Relying solely on these tools can still place a significant burden on developers to interpret and act on findings without adequate platform support.

### Policy-as-Code for Security: Automating Trust

If you've adopted the [two-level intent-based approach](/blog/platform-engineering-pillars-3/) we discussed earlier, your developers already benefit from secure-by-default infrastructure modules. In that model, developers specify their intent ("I need a Java service with Kafka and PostgreSQL"), and the platform team ensures that underlying modules automatically handle security details like IAM roles, encryption, and bucket permissions.

However, even with these secure defaults, it's critical to have automated guardrails in place. Policy-as-Code provides this additional layer of automated enforcement, ensuring security standards are consistently applied—even if someone attempts to bypass or modify the provided modules. Think of this as a "belt and suspenders" approach: secure defaults in modules are your first line of defense, and Policy-as-Code is your second, ensuring nothing slips through.

For Example:

- **IAM Roles with Least Privilege:**  
  - **Secure Default (Module):** The platform team's IAM module automatically generates roles with least-privilege permissions. Developers don't specify IAM roles directly.  
  - **Policy-as-Code (Additional Guardrail):** A policy explicitly checks all IAM roles provisioned by the platform, ensuring no role grants overly broad permissions (e.g., no wildcard permissions). If a module is accidentally modified or misconfigured, the policy catches it immediately.

- **Mandatory Encryption at Rest:**  
  - **Secure Default (Module):** The platform team's database module automatically provisions databases with encryption at rest enabled. Developers don't specify encryption settings directly.  
  - **Policy-as-Code (Additional Guardrail):** A policy explicitly checks all storage resources to ensure encryption at rest is always enabled. If a developer or platform engineer accidentally modifies the module or bypasses it, the policy immediately flags the issue.

Integrating Policy-as-Code into your platform makes security automated, transparent, and unobtrusive. Developers gain clarity and confidence through immediate feedback, while security teams achieve consistency and control—allowing your organization to move swiftly without compromising security.

## 🚨 Security Anti-Patterns: Common Mistakes and How to Avoid Them

Even with good intentions, teams often fall into common security traps. These anti-patterns create friction, increase risk, and undermine your platform's security posture. Let's explore four frequent security mistakes—and how your platform can help teams avoid them.

{{% notes %}}

### 1. 📂 **Secrets in Developer `.env` Files**

**What it looks like:**  
Developers store sensitive credentials (API keys, passwords, tokens) in local `.env` files, risking accidental commits to version control or leaks.

**Why it's risky:**  
Exposed secrets can lead to unauthorized access, data breaches, and compliance violations.

**How to avoid it:**  
- Use centralized secrets management.
- Automatically inject secrets at runtime, never storing them locally or in code.
- Add `.env` files to `.gitignore` and use pre-commit hooks to detect accidental commits.

{{% /notes %}}

{{% notes type="tip" %}}

### 2. 🌐 **Overly Permissive IAM Roles**

**What it looks like:**  
Developers grant overly broad permissions (e.g., `AdministratorAccess`, `*:*`) due to confusion or frustration with restrictive policies.

**Why it's risky:**  
Excessive permissions increase the blast radius of security incidents.

**How to avoid it:**  
- Provide reusable IAM role modules with least-privilege defaults.
- Enforce least-privilege IAM policies automatically with policy-as-code (Pulumi CrossGuard).
- Regularly audit IAM permissions and remove unused or overly broad permissions.

{{% /notes %}}

{{% notes type="info" %}}

### 3. 📦 **Ignoring Software Supply Chain Security**

**What it looks like:**  
Teams blindly trust third-party dependencies, container images, or build artifacts without verifying integrity or scanning for vulnerabilities.

**Why it's risky:**  
Supply chain attacks introduce vulnerabilities or backdoors into your applications.

**How to avoid it:**  
- Generate and verify Software Bill of Materials (SBOM).
- Implement automated vulnerability scanning (Dependabot, Snyk, Trivy).
- Sign and verify container images and build artifacts (Cosign, Sigstore).

{{% /notes %}}

{{% notes type="tip" %}}

### 4. 🖥️ **Security as "Someone Else's Job"**

**What it looks like:**  
Developers assume security is solely the responsibility of dedicated security teams, ignoring security implications during development.

**Why it's risky:**  
Security becomes reactive rather than proactive, missing opportunities to prevent vulnerabilities early.

**How to avoid it:**  
- Provide lightweight, developer-friendly security training and resources.
- Foster collaboration between developers, platform teams, and security teams through shared responsibility.

{{% /notes %}}

### Protecting Sensitive Credentials by Default

Developers frequently handle sensitive credentials manually—copying database passwords, API keys, or tokens into local configuration files or environment variables. This manual approach creates significant security risks, complexity, and friction.

Consider a common scenario: A developer setting up a new microservice manually copies sensitive credentials into a local `.env` file. Later, this file is accidentally committed to version control, exposing credentials publicly. Or perhaps the credentials are unintentionally included in a Docker image during a build step, making them accessible to anyone who can pull the image. Even worse, if the developer's machine is compromised, attackers can leverage these exposed credentials to move laterally into production systems. Each scenario triggers urgent security responses—credential rotations, incident investigations, and potential downtime—causing delays, frustration, and risk.

Centralized secrets management solves this problem by securely storing sensitive credentials and automatically injecting them into applications at runtime. Developers no longer handle secrets manually, eliminating complexity and significantly reducing the risk of accidental exposure. Platform teams integrate secrets management directly into reusable service templates, ensuring new services automatically retrieve and inject credentials securely—without developer intervention.

By embedding centralized secrets management into your platform, you eliminate manual handling of sensitive credentials, reduce security risks, and accelerate secure deployments. Developers gain simplicity and confidence, while security teams gain peace of mind—enabling your organization to deploy faster and safer.

### Identity and Access Management: Frictionless Security through Identity

Developers frequently struggle with managing multiple static credentials—such as cloud provider keys, passwords, or tokens. These credentials can expire, get lost, or accidentally leak, creating friction, frustration, and security risks.

Consider a common scenario: A developer urgently troubleshooting a production issue attempts to access critical cloud resources, only to discover their static credentials have expired or been rotated. They waste valuable time tracking down new credentials, interrupting colleagues, or filing support tickets—delaying resolution and increasing frustration.

Identity-based authentication solves this problem by tying permissions directly to user identities. Instead of juggling static keys or passwords, developers authenticate seamlessly through familiar identity providers. For example, when a developer logs into their corporate identity provider, they automatically gain secure, temporary access to cloud resources through integrations like OpenID Connect (OIDC) or SAML-based single sign-on (SSO). No manual credential management is required, and access is always up-to-date and secure.

This approach dramatically simplifies access management, reduces complexity, and eliminates credential-related friction. Developers gain immediate, secure access to the resources they need, exactly when they need them—accelerating productivity without compromising security.

## Real-World Example: Security Enablement from Build to Incident Response

Imagine a developer deploying a new microservice. They select a secure-by-default template from the platform's service catalog. Immediately, policy-as-code validates security compliance, ensuring encryption settings and IAM roles are correctly configured. Secrets management automatically injects credentials securely, eliminating manual handling. Identity-based access ensures the developer can securely access resources without friction.

As the service builds, automated vulnerability scanning proactively checks dependencies and container images for known vulnerabilities. A Software Bill of Materials (SBOM) is automatically generated, transparently tracking all dependencies. Secure build pipelines sign and verify artifacts, ensuring only trusted, verified code reaches production.

Once deployed, automated security monitoring is immediately enabled, providing real-time visibility into the service's security posture. Later, a new vulnerability is discovered in a third-party library used by the microservice. Because the platform automatically generated an SBOM, the security operations team quickly identifies exactly which services are affected. Integrated monitoring detects unusual activity related to this vulnerability in production, triggering clear, actionable alerts directly within observability dashboards.

Incident response workflows guide developers and SecOps teams through rapid containment and remediation. The team quickly deploys a patched version of the affected dependency, leveraging the secure software supply chain practices—automated scanning, artifact signing, and secure deployments—to confidently and rapidly roll out the fix.

In this scenario, security isn't a blocker—it's seamlessly integrated into every stage of the software lifecycle. From secure builds and deployments to rapid incident detection and response, your platform empowers developers and security teams to confidently deliver secure software at speed.

But how do you know if your security practices are truly enabling your teams? To answer that, you need clear, actionable metrics.

## Metrics: Measuring Security Enablement

To ensure your platform's security practices truly enable developers, track two complementary metrics:

- **Security Incident Rate:**  
  Measure the frequency and severity of security incidents or vulnerabilities discovered in production. A decreasing incident rate indicates your security practices effectively reduce risk.

- **Developer Security Friction Score:**  
  Regularly survey developers to gauge how much security processes slow them down or cause frustration. A low friction score indicates security is integrated smoothly into developer workflows, enabling rather than hindering innovation.

By consistently tracking these two metrics, you ensure your platform's security practices effectively reduce risk without becoming a frustrating bottleneck—enabling your organization to innovate quickly, safely, and confidently.

## Pulumi and Security Enablement

Pulumi provides built-in capabilities that embed security directly into your platform, enabling frictionless developer workflows:

- **[Policy as Code (CrossGuard)](https://www.pulumi.com/product/crossguard/):** Automatically enforce security and compliance standards before deployment.
- **[Secure Secrets Management (Pulumi ESC)](https://www.pulumi.com/product/esc/):** Centralize and securely inject secrets without manual handling.
- **[Identity-Based Authentication (OIDC & SAML)](https://www.pulumi.com/docs/pulumi-cloud/oidc/):** Simplify secure access to cloud resources using existing identities.
- **[Secure Software Supply Chain Integrations](https://www.pulumi.com/docs/using-pulumi/continuous-delivery/):** Automate vulnerability scanning, SBOM generation, and artifact signing.
- **[Audit Logs and Visibility](https://www.pulumi.com/docs/pulumi-cloud/audit-logs/):** Provide comprehensive visibility into infrastructure changes for easy compliance and auditing.

With Pulumi, security becomes an integrated, frictionless part of your platform—accelerating innovation while building trust.

## Security as a Platform Feature

Security doesn't have to be a frustrating gatekeeper. By embedding security directly into your platform—through shift-left practices, automated policy enforcement, secure defaults, and integrated security operations—you empower developers to innovate quickly, safely, and confidently. Security becomes a built-in feature, enabling autonomy and trust rather than creating friction and delays.

Each pillar we've explored, [Provisioning](/blog/platform-engineering-pillars-2/), [Self-Service](/blog/platform-engineering-pillars-3/), [Developer Experience](/blog/platform-engineering-pillars-4/), and now Security, builds upon the previous ones, creating a cohesive internal developer platform that removes friction and accelerates innovation.

But even with security embedded, developers still need clear visibility into their systems to quickly identify, understand, and resolve issues. In the next article, we'll explore how Observability becomes a developer superpower, providing actionable insights and proactive visibility that further enhances developer confidence and productivity.