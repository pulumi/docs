---
title: "Rotate PATs and Cloud Credentials Without Static Secrets"
date: 2026-06-30
meta_desc: "Use Pulumi ESC to replace static GitHub PATs and cloud keys with short-lived credentials, scheduled rotation, and CI-friendly configuration."
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

        Use Pulumi ESC to move CI toward short-lived credentials and scheduled rotation.
    linkedin: |
        Long-lived PATs and cloud keys create operational risk in CI.

        This guide shows how Pulumi ESC can issue short-lived credentials, support scheduled rotation, and reduce static secrets in automation workflows.
    bluesky: |
        Static PATs and cloud keys linger too long.

        Use ESC for short-lived credentials and scheduled rotation in CI.
---

Static, long-lived credentials are a major security vulnerability. For teams that manage GitHub Personal Access Tokens (PATs) and cloud credentials across many repositories and accounts, 90-day rotation needs to become an automated operating model, not a calendar reminder. Whether it is a GitHub PAT or an AWS IAM access key, the longer a secret remains unchanged, the greater the risk of compromise.

This post focuses on rotating GitHub and cloud provider credentials that power your entire CI/CD ecosystem. Most platform teams still manage rotation through calendar reminders and manual updates, which makes cutovers fragile when a PAT or cloud key expires during deployment.

## Why it matters now

Compliance mandates like SOC 2 and PCI DSS increasingly require proof of automated rotation for administrative credentials. Beyond compliance, the risk of a long-lived credential leak is a top-tier operational threat. If a secret is leaked, an attacker has a 90-day window to exploit it if you only rotate quarterly. Automating this process reduces the window of exposure and eliminates the human error inherent in manual rotation.

## Reader outcome

By the end of this post, you will automate the rotation of GitHub PATs and cloud credentials using [Pulumi ESC](/docs/esc/). You will learn how to move from static PATs to short-lived installation tokens, implement a "two-secret" rotation strategy for AWS IAM keys to ensure zero downtime, and configure GitHub Actions to fetch these rotated credentials on-demand.

<!--more-->

## The 90-day security challenge

Many security frameworks require rotating administrative credentials every 90 days. Manually tracking these dates across developers and CI/CD pipelines is a recipe for failure. Pulumi ESC solves this by moving from static secrets to a model where credentials are either generated on-demand or rotated automatically on a schedule.

## GitHub: from PATs to short-lived tokens

GitHub Personal Access Tokens (PATs) are notoriously difficult to manage. They are often over-privileged and rarely rotated. Pulumi ESC replaces the need for static PATs in CI/CD by using the `gh-login` provider.

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
      installationId: 789012
      privateKey:
        fn::secret:
          ciphertext: <encrypted-key>
```

## AWS: dynamic vs. rotated credentials

For cloud providers like AWS, Pulumi ESC offers two distinct strategies depending on your application's needs.

### 1. Dynamic credentials (OIDC)

This is the gold standard for CI/CD. Using OpenID Connect (OIDC), your GitHub Actions workflow exchanges a short-lived identity token for temporary AWS credentials. There are zero static secrets stored in GitHub.

```yaml
values:
  aws:
    fn::open::aws-login:
      oidc:
        roleArn: arn:aws:iam::123456789012:role/esc-oidc
        sessionName: github-actions-session
```

### 2. Rotated secrets

Some legacy applications or third-party integrations cannot use OIDC and require a static access key. For these cases, ESC's Rotated Secrets automate the 90-day rotation requirement.

ESC uses a "two-secret" strategy, keeping both the current and previous keys valid during the rotation window to prevent downtime.

```yaml
values:
  iam:
    fn::rotate::aws-iam:
      inputs:
        region: us-west-2
        login: ${environments.logins.production.aws.login}
        userArn: arn:aws:iam::123456789012:user/ci-user
```

## Zero static secrets in GitHub Actions

By combining these features, you can build a CI/CD pipeline that contains no long-lived secrets. The `pulumi/auth-actions` and `pulumi/esc-action` work together to fetch exactly what is needed for each run.

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v6
      - name: Authenticate with Pulumi Cloud
        uses: pulumi/auth-actions@v1
        with:
          organization: my-org
      - name: Fetch Secrets
        uses: pulumi/esc-action@v1
        with:
          environment: production
      - name: Deploy
        run: pulumi up
```

## Audit trail and compliance

Every time a secret is opened or rotated, Pulumi ESC logs the event. This provides a granular audit trail showing exactly which identity accessed which secret and when. For security teams, this turns a "black box" of static secrets into a transparent, governed system that satisfies even the strictest 90-day rotation requirements.
