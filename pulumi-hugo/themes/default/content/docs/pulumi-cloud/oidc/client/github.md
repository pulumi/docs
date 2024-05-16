---
title_tag: Configure OpenID Connect for Github | OIDC
meta_desc: This page describes how to configure Pulumi to accept Github OIDC tokens
title: Github
h1: Configuring OpenID Connect for Github
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: openid-connect-client
        weight: 1
---

This document outlines the steps required to configure Pulumi to accept Github id_tokens to be exchanged by Organization access tokens.

## Prerequisites

* You must be an admin of your Pulumi organization.

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the [official Github documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).
{{< /notes >}}

## Register the OIDC issuer

1. Navigate to **OIDC Issuers** under your Organization's **Settings** and click on **Register a new issuer**.
1. Name the issuer and complete the url: `https://token.actions.githubusercontent.com`
   ![Register Github](../register-github.png)
1. Submit the form

## Configure the Authorization Policies

1. Click on the issuer name
2. Change the policy decision to `Allow`
3. Change the token type to `Organization`
4. Add a policy to allow OIDC and configure the sub and audience for your organization and repositories:

<!-- markdownlint-disable no-bare-urls -->
* **Aud**: https://github.com/***organization***

* **Sub**: repo:***organization***/***repo***:*
<!-- markdownlint-enable no-bare-urls -->
For further information about Github token claims refer to the [official Github documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#understanding-the-oidc-token).
   ![Github policy example](../github-policies.png)
5. Click on update

## Set up the Github Actions step to fetch the OIDC token

```yaml
- name: Fetch OIDC token
  run: |
    OIDC_GH_TOKEN=$(curl -H "Authorization: bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" "$ACTIONS_ID_TOKEN_REQUEST_URL"  | jq -r '.value')
    echo "OIDC_GH_TOKEN=$OIDC_GH_TOKEN" >> $GITHUB_ENV
```

## Set up the Github Actions step to exchange it for a Pulumi access token

```yaml
- name: Fetch Pulumi access token
  run: |
    PULUMI_ACCESS_TOKEN=$(curl -X POST  \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'audience=urn:pulumi:org:ORG_NAME \
    -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
    -d 'subject_token_type=urn:ietf:params:oauth:token-type:id_token' \
    -d 'requested_token_type=urn:pulumi:token-type:access_token:organization' \
    -d 'subject_token=${{ env.OIDC_GH_TOKEN }}' \
    https://api.pulumi.com/oauth/token | jq -r '.access_token')
    echo "::add-mask::$PULUMI_ACCESS_TOKEN"
    echo "PULUMI_ACCESS_TOKEN=$PULUMI_ACCESS_TOKEN" >> $GITHUB_ENV
```

Replace ORG_NAME with the right Pulumi organization

## Sample Github Actions workflow

```yaml
name: Pulumi UP
on:
  workflow_dispatch:

permissions:
  id-token: write
  contents: read

jobs:
  run_cron_job:
    runs-on: ubuntu-20.04
    timeout-minutes: 30

    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Install pulumi
        uses: pulumi/actions@v4

      - name: Install deps
        run: yarn

      - name: Fetch OIDC token
        run: |
          OIDC_GH_TOKEN=$(curl -H "Authorization: bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" "$ACTIONS_ID_TOKEN_REQUEST_URL"  | jq -r '.value')
          echo "OIDC_GH_TOKEN=$OIDC_GH_TOKEN" >> $GITHUB_ENV

      - name: Fetch Pulumi access token
        run: |
          PULUMI_ACCESS_TOKEN=$(curl -X POST  \
            -H 'Content-Type: application/x-www-form-urlencoded' \
            -d 'audience=urn:pulumi:org:ORG_NAME' \
            -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
            -d 'subject_token_type=urn:ietf:params:oauth:token-type:id_token' \
            -d 'requested_token_type=urn:pulumi:token-type:access_token:organization' \
            -d 'subject_token=${{ env.OIDC_GH_TOKEN }}' \
            https://api.pulumi.com/api/oauth/token | jq -r '.access_token')
          echo "::add-mask::$PULUMI_ACCESS_TOKEN"
          echo "PULUMI_ACCESS_TOKEN=$PULUMI_ACCESS_TOKEN" >> $GITHUB_ENV

      - uses: pulumi/actions@v4
        with:
          command: up
          stack-name: ...
```
