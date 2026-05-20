---
title: What is a GitHub Actions Secret?
meta_desc: "GitHub Actions secrets are encrypted environment variables for CI/CD workflows. Learn scopes (repo, environment, organization), libsodium encryption, and OIDC alternatives."
meta_image: /images/what-is/what-is-a-github-action-secret-meta.png
type: what-is
page_title: "What is a GitHub Actions Secret?"
authors: ["diana-esteves"]
---

**A GitHub Actions secret is an encrypted variable scoped to a repository, environment, or organization that GitHub injects into workflow runs as an environment variable or step input, with automatic redaction in logs and no exposure to forked pull requests by default.** Secrets let you keep API tokens, deployment credentials, and signing keys out of your workflow YAML while still using them in CI/CD steps.

Secrets are encrypted using a [libsodium sealed box](https://docs.github.com/en/rest/actions/secrets) before they ever leave your browser or the GitHub REST client, and decrypted only on the runner that's executing a job that references them. Logs are scanned for secret values and automatically redacted, but the protection is real-time text matching — `echo $MY_SECRET | base64` or `set -x` can still expose values in ways the redactor can't reliably catch. For credentials that require fine-grained access or short-lived issuance, modern GitHub Actions workflows often skip stored secrets entirely and use [OIDC federation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect) to mint cloud credentials per run.

In this article, we'll cover the key questions about GitHub Actions secrets:

* What is a GitHub Actions secret used for?
* What are the secret scopes (repo, environment, organization)?
* How are GitHub Actions secrets encrypted?
* How do workflows access secrets?
* What are the limits of GitHub Actions secrets?
* What is OIDC and how does it compare to stored secrets?
* What are best practices for GitHub Actions secrets?
* How does Pulumi use GitHub Actions secrets?
* Frequently asked questions about GitHub Actions secrets

## What is a GitHub Actions secret used for?

A secret is the right place for any sensitive value a workflow needs at runtime. Typical uses:

* Cloud credentials (AWS access keys, Azure service principal secrets, GCP service-account JSON).
* Container registry tokens for `docker login`.
* Deployment tokens for hosting platforms (Vercel, Netlify, Cloudflare).
* Third-party API tokens (Slack, PagerDuty, monitoring tools).
* Signing keys for code signing, package publishing, or commit signing.
* Pulumi access tokens for IaC workflows.

For non-sensitive data (build flags, environment names, log levels), use repository, environment, or organization **variables** instead. Variables aren't encrypted but also aren't redacted — they're meant for things that can safely appear in logs.

## What are the secret scopes (repo, environment, organization)?

GitHub Actions secrets live at three scopes that determine where they can be referenced and which workflows can read them.

| Scope | Where defined | Available to | Best for |
|---|---|---|---|
| **Repository** | Repository → Settings → Secrets and variables → Actions | Every workflow in the repository | Single-repo deploys, build tokens |
| **Environment** | Repository → Settings → Environments → \<env\> | Jobs that `environment:` into that environment, with optional approval gates | Per-stage credentials (dev/staging/prod) |
| **Organization** | Organization → Settings → Secrets and variables → Actions | Selected (or all) repositories in the org | Shared credentials across many repos |

Environment-scoped secrets are the most powerful tier because they let you require manual approval, wait timers, and deployment-branch policies before a job can read production credentials. A common production pattern: organization-scoped credentials for shared services, environment-scoped secrets for per-stage deploy keys, repository secrets for repo-specific tokens.

## How are GitHub Actions secrets encrypted?

Secrets are encrypted with a [libsodium sealed box](https://doc.libsodium.org/public-key_cryptography/sealed_boxes) before they're transmitted to GitHub. The repository or organization holds a public key; the secret is encrypted with that key client-side; only GitHub holds the corresponding private key to decrypt it on the runner.

| Stage | Protection |
|---|---|
| Submission | Sealed-box encryption (NaCl `crypto_box_seal`) before transit |
| Storage | Encrypted at rest in GitHub's storage |
| Delivery to runner | Decrypted only when a job that references the secret runs |
| In the runner | Available to the running job as an env var or step input |
| In logs | Automatic redaction of matching values |
| After job ends | Discarded with the ephemeral runner |

GitHub itself can decrypt your secrets to deliver them to runners, so the trust boundary is GitHub plus your runner. For higher-assurance setups, self-hosted runners or hardware security modules in the cloud provider you're deploying to (via OIDC, see below) can shrink that boundary further.

## How do workflows access secrets?

Inside a workflow YAML file, secrets are referenced through the `secrets` context:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - name: Deploy
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        run: ./deploy.sh
```

Notes that catch teams out:

* **Secrets aren't passed to forked PRs by default.** Workflows triggered by `pull_request` from a fork get an empty `secrets` context unless you explicitly opt in with `pull_request_target` (which has its own security considerations).
* **Composite and reusable actions don't inherit secrets automatically.** You have to pass them in as `inputs:` or use `secrets: inherit` when calling a reusable workflow.
* **`GITHUB_TOKEN` is a special, auto-issued, short-lived secret** scoped to the current repository. Prefer it to a personal access token whenever you can.

## What are the limits of GitHub Actions secrets?

Per GitHub's [documentation](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

* **64 KB maximum size** per secret. Large credential bundles (full service-account JSON files, multi-line certs) may need to be base64-encoded to fit, or stored externally.
* **Up to 1,000 secrets** per repository, **100** per environment, and **1,000** per organization.
* **No native rotation.** GitHub doesn't expire or rotate values for you; you have to update them out of band (or use OIDC to avoid storing them at all).
* **No fine-grained access within a repo.** Any workflow in the repository can read any repo-scoped secret. Environments are the only way to gate access to a subset.
* **Limited audit detail.** The audit log records secret-management events (create/update/delete) but not which workflow runs read a given secret.
* **No first-class versioning.** Updating a secret overwrites the previous value.

## What is OIDC and how does it compare to stored secrets?

[GitHub Actions OIDC](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect) lets workflows request a short-lived OIDC token that the cloud provider exchanges for temporary credentials. Nothing has to be stored as a secret.

| Approach | Credential lifetime | Rotation | Surface area |
|---|---|---|---|
| **Stored secret** | Until you rotate it (often months) | Manual | Anything that can read the secret |
| **OIDC + cloud role** | Minutes (provider-controlled) | Automatic per run | Only the specific job's identity |

For AWS, Azure, GCP, HashiCorp Vault, [Pulumi ESC](/product/esc/), and most modern cloud providers, OIDC is the recommended path. Workflows assume a role scoped to "GitHub Actions in this repo on this branch" and receive temporary credentials directly. Stored secrets remain useful for SaaS APIs that don't support OIDC.

## What are best practices for GitHub Actions secrets?

* **Prefer OIDC to stored secrets.** For any cloud that supports it (AWS, Azure, GCP, Vault, [Pulumi ESC](/product/esc/)), federate identity instead of storing long-lived credentials.
* **Scope secrets to environments, not repos.** Environment secrets unlock deploy gates, branch policies, and approval workflows that repo-scoped secrets don't.
* **Use the smallest scope that works.** Repo > environment > org isn't a hierarchy of "more powerful" — it's a hierarchy of blast radius. Pick the tightest one.
* **Use `GITHUB_TOKEN` over PATs.** It's auto-issued, short-lived, and scoped to the current repository.
* **Don't `echo` secrets.** GitHub's log redactor catches direct prints, but transformations (`echo $SECRET | base64`, `set -x`, logging child process output) can leak values past the redactor. Pass secrets as env vars and let the tools that need them read them directly.
* **Block secrets in forked PRs.** The default is already to not pass them; resist any workflow design that requires `pull_request_target` with secrets unless you've thought hard about the threat model.
* **Rotate periodically.** Even with OIDC, anything still stored as a secret should have a documented rotation cadence. Pair this with secret-scanning to catch accidental commits.

## How does Pulumi use GitHub Actions secrets?

Pulumi's [GitHub Actions integration](/docs/iac/packages-and-automation/continuous-delivery/github-actions/) uses secrets for the same things any other CI tool does: a `PULUMI_ACCESS_TOKEN` for talking to the Pulumi Cloud backend, and cloud-provider credentials (or, ideally, OIDC) for the actual `pulumi up`.

A typical workflow with OIDC and [Pulumi ESC](/product/esc/):

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
    environment: production
    steps:
      - uses: actions/checkout@v4
      - uses: pulumi/auth-actions@v1
        with:
          organization: my-org
          requested-token-type: urn:pulumi:token-type:access_token:organization
      - uses: pulumi/actions@v6
        with:
          command: up
          stack-name: prod
```

What this gives you:

* No `PULUMI_ACCESS_TOKEN` stored in GitHub. The OIDC flow exchanges the workflow's identity for a short-lived Pulumi Cloud token.
* No cloud-provider credentials stored in GitHub. [Pulumi ESC](/product/esc/) brokers AWS/Azure/GCP credentials and rotates them on every run.
* The `environment: production` gate gives you approval workflows and branch policies on top.

[Get started with Pulumi and GitHub Actions](/docs/iac/packages-and-automation/continuous-delivery/github-actions/) to wire up IaC pipelines in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about GitHub Actions secrets

### Are GitHub Actions secrets encrypted?

Yes. Secrets are encrypted with a libsodium sealed box before they're transmitted to GitHub, stored encrypted at rest, and decrypted only on the runner executing a job that references them. The trust boundary is GitHub plus the runner that decrypts the value.

### Where do I add a GitHub Actions secret?

For a repository: **Settings → Secrets and variables → Actions → New repository secret**. For an environment: **Settings → Environments → \<env\> → Add secret**. For an organization (admin-only): **Organization Settings → Secrets and variables → Actions**.

### What is the maximum size of a GitHub Actions secret?

64 KB. For larger payloads (full service-account JSON, multi-line certificates), base64-encode the value before storing it, or store the payload in an external secrets manager and use a smaller secret to authenticate to that store.

### How many secrets can I have?

Up to 1,000 per repository, 100 per environment, and 1,000 per organization. Hitting these limits usually means the secrets should live in a centralized store like [Pulumi ESC](/product/esc/) or [HashiCorp Vault](/what-is/what-is-hashicorp-vault/) instead.

### Can a forked pull request access my secrets?

No, by default. Workflows triggered by `pull_request` from a fork run with an empty `secrets` context. `pull_request_target` does pass secrets but executes against the base branch's workflow definition; use it carefully and never check out forked code before secrets are needed.

### How are secrets redacted from logs?

GitHub scans log output for known secret values and replaces matches with `***`. This works for direct prints (`echo $MY_SECRET`) but not for transformations (`echo $MY_SECRET | base64`, partial outputs, or values written to files that are later cat'd). Treat the redactor as defense-in-depth, not the primary control.

### Should I use OIDC instead of storing secrets?

For any cloud provider that supports it (AWS, Azure, GCP, Vault, [Pulumi ESC](/product/esc/)), yes. OIDC issues short-lived credentials per workflow run, eliminating long-lived stored secrets and dramatically reducing rotation overhead. Stored secrets stay useful for SaaS APIs that don't support OIDC.

### Can I share secrets between repositories?

Yes — use organization-level secrets and select which repositories can access them. Avoid the older pattern of duplicating the same secret into every repo; it's a rotation nightmare.

### Does `GITHUB_TOKEN` count as a secret?

It behaves like one (encrypted, redacted in logs, scoped to the job) but you don't manage it — GitHub issues a fresh `GITHUB_TOKEN` for every workflow run and discards it at the end. Prefer it to a personal access token wherever possible.

### Can I rotate secrets automatically?

Not natively. GitHub doesn't refresh stored values on a schedule. The closest options: rotate the upstream credential and update the secret via the GitHub REST/GraphQL API from another workflow, or skip stored secrets entirely with OIDC.

## Learn more

Pulumi pairs with GitHub Actions through OIDC and [Pulumi ESC](/product/esc/) so cloud credentials never live in your repository. Workflows authenticate by identity, ESC brokers per-run credentials, and the Pulumi GitHub Actions integration handles the rest. [Get started today](/docs/get-started/).

Related reading:

* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is a CircleCI Secret?](/what-is/what-is-a-circleci-secret/)
* [What is a Cloudflare Secret?](/what-is/what-is-a-cloudflare-secret/)
* [What is HashiCorp Vault?](/what-is/what-is-hashicorp-vault/)
* [What is AWS Secrets Manager?](/what-is/what-is-aws-secrets-manager/)
* [What is Azure Key Vault?](/what-is/what-is-azure-key-vault/)
