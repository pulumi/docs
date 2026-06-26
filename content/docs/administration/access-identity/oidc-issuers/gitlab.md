---
title_tag: Configure OpenID Connect for GitLab | OIDC
meta_desc: This page describes how to configure Pulumi Cloud to accept GitLab OIDC tokens.
title: GitLab
h1: Configuring OpenID Connect for GitLab
menu:
  administration:
    name: GitLab
    parent: administration-access-identity-oidc-issuers
    weight: 1
    identifier: pulumi-cloud-access-management-oidc-issuers-gitlab
aliases:
- /docs/administration/access-identity/oidc-client/gitlab/
- /docs/pulumi-cloud/oidc/client/gitlab/
- /docs/pulumi-cloud/access-management/oidc-client/gitlab/
---

This document outlines the steps required to configure Pulumi Cloud to accept GitLab id_tokens and exchange them for organization access tokens.

{{< notes type="info" >}}
This guide walks through the Pulumi Cloud UI. You can also configure OIDC Issuers via the [REST API](/docs/reference/cloud-rest-api/oidc-issuers/) or the [`OidcIssuer`](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/oidcissuer/) resource in the Pulumi Service provider.
{{< /notes >}}

{{< notes type="info" >}}
This guide demonstrates using `organization` tokens. Depending on your [Pulumi edition](/docs/administration/access-identity/oidc-issuers/#token-types-by-edition), you can also use `personal` or `team` tokens by adjusting the token type in the authorization policies and the `requested-token-type` parameter.
{{< /notes >}}

## Prerequisites

- You must be an admin of your Pulumi organization.

{{< notes type="warning" >}}
This guide provides step-by-step instructions based on the official provider documentation, which is subject to change. For the most current information, refer to the [official GitLab documentation](https://docs.gitlab.com/integration/openid_connect_provider/).
{{< /notes >}}

## Register the OIDC Issuer

1. Navigate to **Settings → Access Management → OIDC Issuers** and select **Register issuer**.
1. Name the issuer and set the issuer URL to `https://gitlab.com/` (or your GitLab self-managed URL).
1. Submit the form.

## Configure the authorization policies

1. Select the issuer name.
1. Set **Decision** to **Allow**.
1. Set **Token type** to **Organization**.
1. Add a policy to allow OIDC and configure the audience and subject claims for your organization and repositories:

   <!-- markdownlint-disable no-bare-urls -->
   - **Aud**: `urn:pulumi:org:<org-name>`
   - **Sub**: `project_path:<namespace>/<project>:ref_type:branch:ref:<branch-name>`
   <!-- markdownlint-enable no-bare-urls -->

   For more information about GitLab token claims, see the [official GitLab documentation](https://docs.gitlab.com/ci/secrets/id_token_authentication/).
1. Select **Save policies**.

## Set up GitLab CI to use Pulumi OIDC authentication

In your `.gitlab-ci.yml`, configure the job to request an ID token and use it with the Pulumi CLI:

```yaml
variables:
  PULUMI_ORG: "org-name"

.pulumi-oidc:
  image:
    name: pulumi/pulumi:latest
    entrypoint: [""]
  id_tokens:
    GITLAB_OIDC_TOKEN:
      aud: "urn:pulumi:org:${PULUMI_ORG}"
  before_script:
    - pulumi login --oidc-token "$GITLAB_OIDC_TOKEN" --oidc-org "$PULUMI_ORG" --cloud-url https://api.pulumi.com
```

Replace `org-name` with your Pulumi organization name.

## Sample GitLab CI pipeline

```yaml
variables:
  PULUMI_ORG: "org-name"
  STACK_NAME: "org-name/project-name/stack-name"

stages:
  - preview
  - deploy

.pulumi-oidc:
  image:
    name: pulumi/pulumi:latest
    entrypoint: [""]
  id_tokens:
    GITLAB_OIDC_TOKEN:
      aud: "urn:pulumi:org:${PULUMI_ORG}"
  before_script:
    - pulumi login --oidc-token "$GITLAB_OIDC_TOKEN" --oidc-org "$PULUMI_ORG" --cloud-url https://api.pulumi.com

pulumi-preview:
  extends: .pulumi-oidc
  stage: preview
  script:
    - cd infrastructure
    - npm ci
    - pulumi preview --stack "$STACK_NAME"
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

pulumi-up:
  extends: .pulumi-oidc
  stage: deploy
  script:
    - cd infrastructure
    - npm ci
    - pulumi up --stack "$STACK_NAME" --yes
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
  environment:
    name: production

```
