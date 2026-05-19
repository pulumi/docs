---
title: "Replace PATs and Rotate Cloud Credentials with Pulumi ESC"
date: 2026-06-30
meta_desc: "Use Pulumi ESC to replace static GitHub PATs with installation tokens and rotate cloud keys with short-lived credentials and CI-friendly configuration."
meta_image: meta.png
feature_image: feature.png
authors:
  - pablo-seibelt
tags:
  - esc
  - secrets
  - security
social:
    twitter: |
        Static PATs and cloud keys are easy to forget.

        Use Pulumi ESC to move CI toward GitHub App installation tokens, short-lived cloud credentials, and scheduled rotation.
    linkedin: |
        Long-lived PATs and cloud keys create operational risk in CI.

        This guide shows how Pulumi ESC can issue short-lived credentials, support scheduled rotation, and reduce static secrets in automation workflows.
    bluesky: |
        Static PATs and cloud keys linger too long.

        Use ESC for installation tokens, short-lived cloud credentials, and scheduled rotation in CI.
---

Static, long-lived credentials are a major security vulnerability, especially when they are copied into CI systems. For teams that manage GitHub Personal Access Tokens (PATs) and cloud credentials across many repositories and accounts, 90-day rotation needs to become an automated operating model, not a calendar reminder. Whether the credential is a GitHub PAT or an AWS IAM access key, leaving it unchanged increases compromise risk over time.

This post focuses on rotating GitHub and cloud provider credentials that power your entire CI/CD ecosystem. Most platform teams still manage rotation through calendar reminders and manual updates, which makes cutovers fragile when a PAT or cloud key expires during deployment.

## Why it matters now

Compliance frameworks like SOC 2 and PCI DSS increasingly drive teams toward automated rotation for administrative credentials. PCI DSS v4.0 §8.6.3 requires periodic rotation of service account credentials on an entity-defined schedule, and SOC 2 Type II auditors frequently look for system-enforced controls as evidence of consistent access management. Beyond compliance, the risk of a long-lived credential leak is a top-tier operational threat. If a secret is leaked, an attacker has a 90-day window to exploit it if you only rotate quarterly. Automating this process reduces the window of exposure and eliminates the human error inherent in manual rotation.

## Reader outcome

By the end of this post, you will replace static GitHub PATs with short-lived GitHub App installation tokens and automate cloud credential rotation using [Pulumi ESC](/docs/esc/). You will learn how to protect the GitHub App private key, implement a "two-secret" rotation strategy for AWS IAM keys to reduce downtime risk, and configure GitHub Actions to fetch credentials on demand.

<!--more-->

## The 90-day security challenge

Many security frameworks require rotating administrative credentials every 90 days. Manually tracking these dates across developers and CI/CD pipelines is a recipe for failure. Pulumi ESC solves this by moving from static secrets to a model where credentials are either generated on-demand or rotated automatically on a schedule.

## GitHub: from PATs to short-lived tokens

GitHub Personal Access Tokens (PATs) are notoriously difficult to manage. They are often over-privileged and rarely rotated. Pulumi ESC replaces static PATs in CI/CD by using the `gh-login` provider. The GitHub App private key still needs to be stored securely in ESC and rotated or revoked through your GitHub App process.

Instead of storing a PAT as a GitHub Secret, you register a GitHub App and use ESC to issue an installation access token. These tokens are:

1. **Short-lived**: They expire automatically after 1 hour.
1. **Scoped**: They only have the permissions granted to the GitHub App.
1. **On-demand**: They are generated only when a workflow needs them.

### ESC environment for GitHub

```yaml
values:
  github:
    fn::open::gh-login:
      appId: 123456
      privateKey:
        fn::secret: |
          -----BEGIN RSA PRIVATE KEY-----
          ...
          -----END RSA PRIVATE KEY-----
      owner: my-org
      repositories:
        - infrastructure
      permissions:
        contents: read
        pull_requests: write
  environmentVariables:
    GH_TOKEN: ${github.accessToken}
```

## AWS: dynamic vs. rotated credentials

For cloud providers like AWS, Pulumi ESC offers two distinct strategies depending on your application's needs.

### 1. Dynamic credentials (OIDC)

This pattern works best for CI/CD. GitHub Actions authenticates to Pulumi Cloud with OIDC (OpenID Connect), then ESC exchanges its own OIDC token for temporary AWS credentials. No long-lived cloud secrets are stored in GitHub.

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::123456789012:role/esc-oidc
          sessionName: github-actions-session
          subjectAttributes:
            - currentEnvironment.name
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
```

### 2. Rotated secrets

Some legacy applications or third-party integrations cannot use OIDC and require a static access key. For these cases, ESC's Rotated Secrets automate periodic rotation on a schedule you configure.

ESC uses a "two-secret" strategy, keeping both the current and previous keys valid during the rotation window to reduce downtime risk while consumers move to the new key.

```yaml
values:
  iam:
    fn::rotate::aws-iam:
      inputs:
        region: us-west-2
        login: ${environments.logins.production.aws.login}
        userArn: arn:aws:iam::123456789012:user/ci-user
```

## No long-lived secrets in GitHub Actions

By combining these features, you can build a CI/CD pipeline that contains no long-lived secrets in GitHub Actions. The [`pulumi/auth-actions`](https://github.com/pulumi/auth-actions) and [`pulumi/esc-action`](https://github.com/pulumi/esc-action) work together to fetch exactly what is needed for each run.

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - name: Authenticate with Pulumi Cloud
        uses: pulumi/auth-actions@v1
        with:
          organization: my-org
          requested-token-type: urn:pulumi:token-type:access_token:organization
      - name: Fetch ESC environment
        uses: pulumi/esc-action@v1
        with:
          environment: my-org/platform/production
      - name: Deploy
        run: pulumi up --yes
```

## Audit trail and compliance

When an environment is opened, read, or rotated, Pulumi ESC can log the event. This provides an audit trail for environment opens and rotations, including the identity and timing of access events. For security teams, this turns a "black box" of static secrets into a more transparent, governed system that can support evidence for rotation controls. To try this pattern, start with the [Pulumi ESC getting started guide](/docs/esc/get-started/) and the [GitHub dynamic login credentials guide](/docs/esc/integrations/dynamic-login-credentials/gh-login/).
