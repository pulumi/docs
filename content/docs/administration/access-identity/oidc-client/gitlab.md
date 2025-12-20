---
title_tag: Configure OpenID Connect for Gitlab | OIDC
meta_desc: This page describes how to configure Pulumi to accept Gitlab OIDC tokens
title: Gitlab
h1: Configuring OpenID Connect for Gitlab
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Gitlab
    parent: administration-access-identity-oidc-client
    weight: 1
    identifier: pulumi-cloud-access-management-oidc-client-gitlab
aliases:
- /docs/pulumi-cloud/oidc/client/gitlab/
- /docs/pulumi-cloud/access-management/oidc-client/gitlab/
---

This document outlines the steps required to configure Pulumi to accept Gitlab id_tokens to be exchanged by Organization access tokens.

{{< notes type="info" >}}
This guide demonstrates using `organization` tokens. Depending on your [Pulumi edition](/docs/administration/access-identity/oidc-client/#token-types-by-edition), you may also use `personal` or `team` tokens by adjusting the token type in the authorization policies and the `requested-token-type` parameter.
{{< /notes >}}

## Prerequisites

* You must be an admin of your Pulumi organization.

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the [official Gitlab documentation](https://docs.gitlab.com/integration/openid_connect_provider/).
{{< /notes >}}

## Register the OIDC issuer

1. Navigate to **OIDC Issuers** under your Organization's **Settings** and click on **Register a new issuer**.
1. Name the issuer and complete the url: `https://gitlab.com/` (or your gitlab self managed url)
   ![Register Gitlab](../register-gitlab.png)
1. Submit the form

## Configure the Authorization Policies

1. Click on the issuer name
2. Change the policy decision to `Allow`
3. Change the token type to `Organization`
4. Add a policy to allow OIDC and configure the sub and audience for your organization and repositories:

<!-- markdownlint-disable no-bare-urls -->
* **Aud**: urn:pulumi:org:***org-name***

**Sub**: project_path:***namespace***/***project***:ref_type:branch:ref:***branch-name***
<!-- markdownlint-enable no-bare-urls -->
<!-- markdownlint-enable no-bare-urls -->
For further information about GitLab token claims, refer to the [official GitLab documentation](https://docs.gitlab.com/ci/secrets/id_token_authentication/).
5. Click on update

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

Replace `org-name` with the right Pulumi organization.

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
