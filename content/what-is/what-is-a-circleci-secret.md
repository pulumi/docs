---
title: What is a CircleCI Secret?
meta_desc: "CircleCI secrets are encrypted environment variables for CI/CD jobs. Learn project env vars, contexts, restricted contexts, OIDC, and rotation best practices."
meta_image: /images/what-is/what-is-a-circleci-secret-meta.png
type: what-is
page_title: "What is a CircleCI Secret?"
authors: ["diana-esteves"]
---

**A CircleCI secret is an encrypted environment variable that CircleCI injects into a job's execution environment as a regular env var, scoped either to a single project or to an organization-level context that selected projects can opt into.** Secrets cover the credentials a pipeline needs at runtime — cloud access keys, deploy tokens, container registry credentials, and the like — without putting them in `.circleci/config.yml`.

CircleCI provides three primary scopes (project environment variables, organization contexts, and restricted contexts), encrypts values at rest, and masks them in job output by default. For long-lived cloud credentials, modern CircleCI pipelines often skip stored secrets entirely and use [OIDC federation](https://circleci.com/docs/openid-connect-tokens/) to mint short-lived credentials per run — the same pattern recommended for GitHub Actions and other CI systems. Pulumi ESC integrates with CircleCI's OIDC issuer so [Pulumi ESC environments](/product/esc/) can broker AWS, GCP, and other cloud credentials into pipelines without storing them on either side.

In this article, we'll cover the key questions about CircleCI secrets:

* What is a CircleCI secret used for?
* What are the CircleCI secret scopes (project, context, restricted context)?
* How are CircleCI secrets stored and protected?
* How do jobs access secrets?
* What is OIDC and how does it compare to stored secrets?
* What are the limits of CircleCI secrets?
* What are best practices for CircleCI secrets?
* How does Pulumi work with CircleCI secrets?
* Frequently asked questions about CircleCI secrets

## What is a CircleCI secret used for?

A CircleCI secret is the right place for anything sensitive a pipeline needs at runtime. Typical uses:

* Cloud credentials (AWS access keys, GCP service-account JSON, Azure client secrets).
* Container registry tokens for `docker login` and image pushes.
* Deployment tokens for hosting platforms (Heroku, Vercel, Netlify).
* Third-party API tokens for monitoring, error reporting, or Slack notifications.
* Signing keys for package publishing, code signing, or release artifacts.
* `PULUMI_ACCESS_TOKEN` and other IaC backend credentials.

Non-sensitive values that vary per project (region, log level, application name) are usually better placed in project env vars too, but they're best kept as plain text that's also safe to log.

## What are the CircleCI secret scopes (project, context, restricted context)?

CircleCI offers three secret scopes that determine which jobs can read which values.

| Scope | Where defined | Available to | Best for |
|---|---|---|---|
| **Project environment variable** | Project Settings → Environment Variables | Every job in the project | Project-specific tokens |
| **Context** | Organization Settings → Contexts | Jobs in any project that opt into the context | Shared credentials across projects |
| **Restricted context** | Organization Settings → Contexts (with security groups) | Only jobs that match branch, tag, or security-group rules | Production credentials, signing keys |

[Contexts](https://circleci.com/docs/contexts/) are the more powerful tier: secrets live at the organization level, projects opt in by listing the context in their workflow, and **restricted contexts** can be further locked down by branch, tag, or organization security group. The standard pattern: project env vars for repo-specific tokens, contexts for shared services, restricted contexts for production-only credentials.

## How are CircleCI secrets stored and protected?

CircleCI encrypts secret values at rest using a [HashiCorp Vault](/what-is/what-is-hashicorp-vault/) backend on its platform, and TLS protects values in transit. Once a secret is written, the value can no longer be read from the UI or API — only updated or removed.

| Stage | Protection |
|---|---|
| Submission | TLS to the CircleCI API |
| Storage | Encrypted at rest in CircleCI's secrets backend |
| Delivery to executor | Injected as env vars into the job's execution environment |
| In the job | Available as standard env vars; not readable from the UI or API after creation |
| In logs | Values are masked from job output by default |
| After job ends | Discarded with the ephemeral executor |

The trust boundary is CircleCI plus the executor that runs your job. For higher-assurance setups, self-hosted runners shrink that boundary and OIDC federation (next section) removes the stored-secret requirement entirely for cloud credentials.

## How do jobs access secrets?

Inside a `.circleci/config.yml`, secrets are referenced as standard shell environment variables. Project env vars are available automatically; context-scoped secrets require the workflow to opt into the context.

```yaml
version: 2.1

jobs:
  deploy:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - run:
          name: Deploy
          command: |
            aws s3 sync ./dist s3://my-bucket
          environment:
            AWS_DEFAULT_REGION: us-west-2

workflows:
  build_and_deploy:
    jobs:
      - deploy:
          context:
            - aws-prod
          filters:
            branches:
              only: main
```

Two patterns that catch teams out:

* **Secrets are env vars.** Don't `echo` them. CircleCI masks known values from output, but transformations (`echo $TOKEN | base64`, `set -x`) can leak values past the masker.
* **Context membership is what unlocks org-level secrets.** A project not listed in a context can't see its env vars, even if jobs in that project reference the names.

## What is OIDC and how does it compare to stored secrets?

CircleCI issues an [OpenID Connect token](https://circleci.com/docs/openid-connect-tokens/) for every job, signed by CircleCI and verifiable by any cloud provider that accepts OIDC. The job can exchange that token for short-lived cloud credentials without ever holding a long-lived access key.

| Approach | Credential lifetime | Rotation | Surface area |
|---|---|---|---|
| **Stored secret** | Until you rotate it (often months) | Manual | Anything that can read the env var |
| **OIDC + cloud role** | Minutes (provider-controlled) | Automatic per run | Only the specific job's identity |

For AWS, Azure, GCP, [HashiCorp Vault](/what-is/what-is-hashicorp-vault/), and [Pulumi ESC](/product/esc/), OIDC is the recommended path. The job presents the OIDC token, the provider validates the issuer and claims, and short-lived credentials come back for that run only. Stored secrets remain useful for SaaS APIs that don't accept OIDC.

## What are the limits of CircleCI secrets?

* **No native rotation.** CircleCI doesn't expire or refresh values for you; you have to update them out of band (or use OIDC to avoid storing them at all).
* **No first-class versioning.** Updating a secret overwrites the previous value; the only history is in your team's records.
* **Write-only after creation.** A stored value can be updated or removed but not read back through the UI or API. That's a feature for security but can be frustrating during debugging.
* **Limited audit detail.** The audit log captures create/update/delete events on secrets and contexts, but not per-job reads.
* **Context-level access is binary.** A project either opts into a context or it doesn't; there's no sub-context filtering inside a project beyond restricted-context branch/tag rules.
* **No built-in size cap published**, but treat large credential blobs (full service-account JSON, multi-megabyte certs) as a smell and store them in an external vault instead.

## What are best practices for CircleCI secrets?

* **Prefer OIDC to stored secrets.** For any cloud that supports it (AWS, Azure, GCP, [HashiCorp Vault](/what-is/what-is-hashicorp-vault/), [Pulumi ESC](/product/esc/)), federate identity instead of storing long-lived credentials.
* **Use restricted contexts for production.** Pair production-only credentials with branch/tag filters and security-group restrictions so a feature branch can't deploy to prod.
* **Don't echo secrets.** CircleCI masks known values, but transformations defeat the masker. Pass secrets as env vars and let the tools that need them read them directly.
* **Scope to contexts, not project env vars, for anything shared.** A token used by three repos belongs in a context, not duplicated three times. Rotation is the difference between updating one value and updating three.
* **Rotate stored secrets on a schedule.** Document a cadence and use the [CircleCI API](https://circleci.com/docs/api/v2/index.html) or a small script to push new values, rather than relying on console clicks.
* **Pair secrets with policy.** [CircleCI runtime policies](https://circleci.com/docs/runtime-policies/) and config validation can block jobs that try to consume contexts they shouldn't.

## How does Pulumi work with CircleCI secrets?

Pulumi runs in CircleCI through the [Pulumi Orb](https://circleci.com/developer/orbs/orb/pulumi/pulumi). The orb expects a `PULUMI_ACCESS_TOKEN` (and any provider credentials) to be available as env vars; the recommended source is OIDC into [Pulumi ESC](/product/esc/), with ESC then brokering AWS, Azure, GCP, or other credentials into the same run.

```yaml
version: 2.1

orbs:
  pulumi: pulumi/pulumi@2

jobs:
  preview:
    docker:
      - image: cimg/node:lts
    steps:
      - checkout
      - pulumi/login
      - pulumi/preview:
          stack: my-org/my-project/prod

workflows:
  pulumi:
    jobs:
      - preview:
          context:
            - pulumi-prod
```

What you get from this pattern:

* Cloud credentials never live in CircleCI as long-lived secrets — ESC issues per-run AWS/Azure/GCP credentials based on the OIDC token CircleCI presents.
* `PULUMI_ACCESS_TOKEN` itself can be issued from the OIDC token (via `pulumi/auth-actions`-equivalent flows), eliminating the only static secret the pipeline used to need.
* Contexts give you the org-level scoping; restricted contexts give you the prod-only gates.

[Get started with Pulumi on CircleCI](/docs/iac/packages-and-automation/continuous-delivery/circleci/) to wire up IaC pipelines in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about CircleCI secrets

### Are CircleCI secrets encrypted?

Yes. Values are stored encrypted at rest in CircleCI's secrets backend, transmitted over TLS, and injected into a job's execution environment only when the job runs. Once a secret is written, the value can no longer be read through the UI or API; only updated or removed.

### What is the difference between a CircleCI context and a project environment variable?

A **project environment variable** lives in one project and is available to every job in that project. A **context** lives at the organization level and is available to any project that explicitly opts into it. Contexts are the right answer for credentials shared across multiple projects; project env vars are for repo-specific values.

### What is a restricted context?

A [restricted context](https://circleci.com/docs/contexts/) layers branch, tag, or security-group rules on top of a regular context. Only jobs that match the rules can read the context's secrets. The canonical use case is production credentials that should only be readable from jobs running on the `main` branch or release tags.

### How do I rotate a CircleCI secret?

Update the value through the UI (Project Settings → Environment Variables, or Organization Settings → Contexts) or the CircleCI API. Old jobs in flight finish with the previous value; new jobs pick up the new value. For automated rotation, use the API together with the upstream credential's own rotation mechanism.

### Can I read a CircleCI secret value from the UI?

No. Once written, a secret's value is masked in the UI and not returned by the API. You can update or delete it but not retrieve it. This is intentional; for debugging, log into the upstream system to verify the value.

### How do I share a secret across multiple projects?

Use a context. Define the secret in **Organization Settings → Contexts**, then list the context in each project's workflow under `context:`. The same value flows into every project that opts in, and rotating it is a single update.

### Should I use OIDC instead of storing secrets?

For any cloud provider that supports it (AWS, Azure, GCP, [HashiCorp Vault](/what-is/what-is-hashicorp-vault/), [Pulumi ESC](/product/esc/)), yes. OIDC issues short-lived credentials per job run, eliminates long-lived stored values, and dramatically reduces rotation overhead. Stored secrets remain useful for SaaS APIs that don't accept OIDC.

### Are CircleCI secrets visible in job logs?

CircleCI masks known secret values from job output by default, replacing matches with asterisks. The masker works for direct prints but not for transformations (`echo $TOKEN | base64`, partial outputs, files later cat'd). Treat masking as defense-in-depth, not the primary control.

### Can I limit which jobs in a project can read a context?

Indirectly, via restricted contexts with branch, tag, or security-group rules. There isn't a per-job ACL within a regular context; if a project opts into a context, every job in that project's workflow can declare it.

### How do I audit who used a CircleCI secret?

CircleCI's audit log records secret-management events (create, update, delete, context membership changes). It does not record per-job reads of a stored value. For tighter audit, use OIDC and rely on the cloud provider's audit log (CloudTrail, etc.) to see what the issued credential did.

## Learn more

Pulumi pairs with CircleCI through the Pulumi Orb and [Pulumi ESC](/product/esc/): cloud credentials are minted per run via OIDC, ESC brokers access, and the orb runs `pulumi up` or `pulumi preview` against your stacks. [Get started today](/docs/get-started/).

Related reading:

* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is a GitHub Actions Secret?](/what-is/what-is-a-github-action-secret/)
* [What is a Cloudflare Secret?](/what-is/what-is-a-cloudflare-secret/)
* [What is HashiCorp Vault?](/what-is/what-is-hashicorp-vault/)
* [What is AWS Secrets Manager?](/what-is/what-is-aws-secrets-manager/)
* [What is CI/CD?](/what-is/what-is-ci-cd/)
