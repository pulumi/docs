---
title: "OIDC Connect Trust Relationships for Pulumi Cloud"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2024-04-19T21:45:13Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Introducing OIDC Connect Trust Relationships for Pulumi Cloud

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - cleve-littlefield
    - german-lena

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - oidc
    - oidc-connect
    - new-feature

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

We are excited to introduce a powerful addition to Pulumi's authentication capabilities: OIDC Connect Trust Relationships. This feature makes it easy to integrate Pulumi securely into any ecosystem that supports OIDC Connect. By incorporating OIDC Connect, Pulumi is not only extending its compatibility with a broader range of environments but also reinforcing its commitment to delivering top-tier, secure, and scalable solutions to developers and enterprises alike. Whether you are working within CI/CD pipelines or engaging directly with cloud services, this new feature ensures that your infrastructure management is more secure, efficient, and aligned with industry best practices.

<!--more-->

## Addressing the "Secret Zero" Challenge

A lot of platforms deal with the “secret zero” challenge, where they are very secure but to access them you often have to maintain a long-term access token. Managing long-term access tokens has always been a challenge for developers. Often those secrets are set and forgotten, leaving the team to have to do an inventory when it comes time to rotate them. This struggle often leads to those secrets not being rotated very often. This long-term access token becomes a weak point in the overall security posture as well as a hassle for developers.  With OIDC Trust Relationships, we're tackling the "secret zero" challenge head-on by introducing exchanging a secure platform token for a short-term Pulumi token. This enhances security and simplifies token management.

## Simplified Authentication

OIDC Trust Relationships simplify the authentication process by allowing you to securely request dynamic credentials for Pulumi using your preferred OIDC Connect provider. OIDC connect is supported across many popular CICD systems, such as GitHub, GitLab, Circle CI, and more. In addition, OIDC Connect can be used from within most cloud providers, such as AWS, Azure, GCP, and more. T

## Enhanced Security with Policy Controls

When you set up an OIDC Trust Relationship in Pulumi Cloud, you can set policies to deny or approve token exchanges based on issuer subject or additional claims. We support wildcard matching to create simple policies that support complex authorization scenarios. Based on your specific policy requirements, these policies can be used to issue a token scoped to an organization, team, or personal access.

## Demo

In this demo, we are going to use Github Actions to retrieve Pulumi credentials and use those credentials to list all the Pulumi ESC Environments in our organization.

<!-- markdownlint-disable ol-prefix -->
1. Go to the OIDC Issuers Page.
2. Register Issuer and give a name and (optional) max expiration. Enter the GitHub actions URL `https://token.actions.githubusercontent.com`.
3. Add a policy to allow OIDC and configure the sub and audience as needed, and save the policy. In the demo, we are using:

<!-- markdownlint-disable no-bare-urls -->
    * **Aud**: https://github.com/***organization***

    * **Sub**: repo:***organization***/***repo***:*
<!-- markdownlint-enable no-bare-urls -->
4. Create a GitHub action. Here is a sample code. Ensure to replace the organization name with your organization in the `fetch pulumi token` step.

<!-- markdownlint-disable code-block-style -->
```yaml
name: Pulumi ESC List Environments
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

      - name: fetch gh token
        run: |
          OIDC_GH_TOKEN=$(curl -H "Authorization: bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" "$ACTIONS_ID_TOKEN_REQUEST_URL"  | jq -r '.value')
          echo "OIDC_GH_TOKEN=$OIDC_GH_TOKEN" >> $GITHUB_ENV

      - name: fetch pulumi token
        run: |
          PULUMI_ACCESS_TOKEN=$(curl -X POST  \
            -H 'Content-Type: application/x-www-form-urlencoded' \
            -d 'audience=urn:pulumi:org:arun-test' \
            -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
            -d 'subject_token_type=urn:ietf:params:oauth:token-type:id_token' \
            -d 'requested_token_type=urn:pulumi:token-type:access_token:organization' \
            -d 'subject_token=${{ env.OIDC_GH_TOKEN }}' \
            https://api.pulumi.com/api/oauth/token | jq -r '.access_token')
          echo "::add-mask::$PULUMI_ACCESS_TOKEN"
          echo "PULUMI_ACCESS_TOKEN=$PULUMI_ACCESS_TOKEN" >> $GITHUB_ENV

      - name: Login to Pulumi
        run: pulumi login
        env:
          PULUMI_ACCESS_TOKEN: ${{ env.PULUMI_ACCESS_TOKEN }}

      - name: List all Pulumi ESC Environments
        run: pulumi env ls -o arun-test
```
<!-- markdownlint-enable code-block-style -->
5. Go to GitHub Actions page, and run the workflow you just created.
<!-- markdownlint-enable ol-prefix -->
{{< video title="GitHub Actions OIDC Trust Demo" src="./oidc-trust-demo.mp4" width=600 height=420 autoplay="true" loop="true" >}}

## Seamless Integration with Pulumi ESC

OIDC Trust Relationships seamlessly integrate with Pulumi ESC (Environments, Secrets, and Config), providing a comprehensive solution for managing infrastructure and secret/configuration needs. You can now use your native GitHub app token to exchange it for a short-lived Pulumi Token, and ESC will seamlessly exchange it for a cloud token through an ESC environment.

## Next steps

* [OIDC Connect Trust Relationships overview](/docs/pulumi-cloud/oidc/client/)
* [Configuring OIDC for Github](/docs/pulumi-cloud/oidc/client/github/)
