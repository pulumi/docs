---
title_tag: "Least Privilege Security for Pulumi IaC and ESC"
meta_desc: An overview of best practices to use Pulumi IaC and ESC in a least privilege environment
title: Least Privilege Security for Pulumi IaC and ESC
h1: Least privilege security for Pulumi IaC and ESC
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Least privilege security
        parent: iac-using-pulumi
        weight: 2
---

When using Pulumi Infrastructure as Code (IaC) alongside Pulumi ESC (Environments, Secrets, and Config), adopting a **least privilege security posture** ensures infrastructure security and compliance while enabling efficient developer workflows.

## Understanding the Security Implications of IaC Execution

Pulumi IaC programs are full-fledged applications capable of performing any action the developer can code, including accessing sensitive secrets. This capability is inherent to IaC tools in general, as they execute with the full privileges of their runtime environment.

Given this capability, developers with direct access to execute IaC code inherently have access to secrets that the program uses. For production or sensitive environments, it’s therefore essential to ensure deployments run in isolated, secure environments.

## Balancing Developer Access Across Environments

To balance security with developer productivity, clearly differentiate access between environments:

### Development and Test Environments:

Allow developers direct access to execute Pulumi IaC (`pulumi up`) and access ESC environments. This direct access is necessary to:

- Rapidly iterate on infrastructure code.
- Efficiently test changes and debug infrastructure issues.
- Quickly troubleshoot and fix configuration errors.

### Production or Sensitive Environments:

For production or similarly sensitive environments:

- Restrict developers from directly executing IaC.
- Require infrastructure changes to go through a structured pull request (PR) approval process.
- Execute deployments exclusively through secure, isolated CI/CD systems.

## Implementing Least Privilege with Pulumi

### 1. Configure Stack and ESC Permissions

Use Pulumi's [role-based access control (RBAC)](/docs/pulumi-cloud/access-management/teams/) to enforce least privilege effectively:

- **Organization-level defaults:**
  - Set conservative default permissions (`None` or `Read`) for both stacks and ESC environments.
  - Explicitly grant elevated permissions (`Write` or `Admin`) only when necessary.

- **Team-based permissions:**
  - Organize users into teams in the Pulumi Cloud console (`Settings > Teams`).
  - Assign stack and ESC permissions explicitly to teams, aligning access to organizational roles.

### 2. Setting Up Team-Based Permissions

- **Create teams** in the Pulumi Cloud console (`Settings > Teams`).
- **Assign stack permissions:** Grant teams permissions such as `Read`, `Write`, or `Admin` for specific stacks.
- **Assign ESC permissions:** Grant teams roles like `Environment reader`, `opener`, `editor`, or `admin`.

You can also set team access directly when initializing a stack via the CLI:

```bash
pulumi stack init --teams YourTeamName
```

This grants the specified team immediate read/write access to the new stack.

### 3. Secure Deployment Approaches for Production

Choose one of these secure deployment approaches in your sensitive environments:

### Option A: Pulumi Deployments (with GitHub and Other Integrations)

[Pulumi Deployments](/docs/pulumi-cloud/deployments/) provides automated, managed, and secure infrastructure deployments:

- **Automated GitHub integration:**  
  Automatically run `pulumi preview` on PRs and `pulumi up` upon PR merge.
- **REST API:**  
  Trigger deployments programmatically from your custom workflows or third-party CI/CD systems using the Pulumi Deployments REST API.

**Setup steps for GitHub integration:**

1. **Install the Pulumi GitHub App:**
   - Navigate to Pulumi Cloud Console → `Settings > Integrations`.
   - Install the app and authorize it for your GitHub repository.

2. **Configure deployment triggers:**
   - Navigate to your stack in Pulumi Cloud Console → `Stack Settings > Deploy`.
   - Set deployment triggers (e.g., PR merges to `main` branch).

**Learn more:** [Pulumi Deployments GitHub Integration](https://www.pulumi.com/docs/iac/using-pulumi/continuous-delivery/github-app/)

**REST API documentation:** [Pulumi Deployments REST API](https://www.pulumi.com/docs/pulumi-cloud/deployments/rest-api/)

---

### Option B: CI/CD with GitHub Actions and OIDC Authentication

Use GitHub Actions with Pulumi’s OIDC integration for secure, token-less deployments:

- Configure Pulumi Cloud to trust GitHub’s OIDC provider.
- Obtain a Pulumi access token scoped specifically to a team rather than the entire organization.

**Full Example Workflow (Team-Scoped):**

```yaml
name: Pulumi Deployment

on:
  push:
    branches:
      - main

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Authenticate with Pulumi (Team-scoped)
        uses: pulumi/auth-actions@v1
        with:
          organization: your-org-name
          requested-token-type: urn:pulumi:token-type:access_token:team
          team: your-team-name

      - name: Deploy Infrastructure
        uses: pulumi/actions@v6
        with:
          command: up
          stack-name: your-org-name/your-stack-name
```

- `pulumi/auth-actions` exchanges an OIDC token for a team-scoped Pulumi access token.
- `pulumi/actions` executes `pulumi up` adhering to the assigned team permissions.

**Detailed documentation:**
[GitHub OIDC Setup](https://www.pulumi.com/docs/pulumi-cloud/access-management/oidc/client/github/)
[Pulumi GitHub Actions](https://www.pulumi.com/docs/iac/using-pulumi/continuous-delivery/github-actions/)

---

### Option C: CI/CD with Other Providers

Pulumi integrates seamlessly with many other popular CI/CD platforms beyond GitHub Actions, such as:

- **GitLab CI/CD**
- **Azure DevOps Pipelines**
- **Jenkins**
- **CircleCI**

These platforms can also leverage secure OIDC authentication or token-based workflows tailored to your security needs.

You can [lock down access to specific pipelines](https://www.pulumi.com/docs/pulumi-cloud/access-management/oidc/client/#configure-the-authorization-policies) using the `sub`, `aud`, and custom claims coming from your CI/CD provider.

Explore integrations and detailed setup guides here in our [Continuous Delivery documentation.](https://www.pulumi.com/docs/iac/using-pulumi/continuous-delivery/)

---

## Auditing and Monitoring

Ensure your security posture remains robust by:

- Regularly reviewing access and deployment logs.
- Monitoring ESC logs for secret access patterns.
- Auditing team-based permissions regularly to ensure compliance.

## Summary of Best Practices

- **Development/Test:** Provide developers direct IaC execution for productivity.
- **Production/Sensitive:** Restrict direct IaC execution; enforce structured approvals and secure, isolated deployments.
- **Permissions Management:** Use Pulumi’s RBAC for fine-grained, team-based access controls.
- **Secure CI/CD:** Prefer token-less OIDC authentication or controlled Pulumi Deployments integrations.
- **Continuous Auditing:** Regularly audit infrastructure and secret access logs.

Adopting these best practices ensures secure management of infrastructure and secrets while maintaining developer efficiency and agility.
