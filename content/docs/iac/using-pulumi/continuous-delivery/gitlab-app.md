---
title_tag: "Using Pulumi GitLab Integration | CI/CD"
meta_desc: Integrate the results of Pulumi stack previews to GitLab Merge Requests.
  It will show you any potential infrastructure changes on Merge Requests.
title: GitLab Integration
h1: Pulumi CI/CD & GitLab Integration
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    name: GitLab Integration
    parent: iac-using-pulumi-cicd
    weight: 8
aliases:
  - /docs/guides/continuous-delivery/gitlab-app/
  - /docs/using-pulumi/continuous-delivery/gitlab-app/
  - /docs/iac/packages-and-automation/continuous-delivery/gitlab-app/
search:
  keywords:
    - gitlab
    - integration
    - merge
    - requests
    - potential
    - previews
    - integrate
---

With this GitLab integration, Pulumi is able to add Pulumi Previews to a GitLab Merge Request.

## Integration Methods

There are two ways to integrate Pulumi and GitLab.

* If you are a Premium or Ultimate GitLab customer, you will use a GitLab Group Access Token. This integration type is simpler to setup and is not tied to a specific user. The user configuring the integration will need to be a GitLab Organization Owner.
* If you are not a paying GitLab customer, you will use a User OAuth Token. You will also need to configure a webhook, as described below.

{{% notes type="info" %}}
This feature is currently not compatible with GitLab's [pipelines for merged results](https://docs.gitlab.com/ee/ci/pipelines/merged_results_pipelines.html).
See the [GitLab issue](https://gitlab.com/gitlab-org/gitlab/-/issues/350086) for details as to why.
{{% /notes %}}

## Integrating via GitLab Group Access Token

If you are a Premium or Ultimate GitLab customer, you have access to GitLab Group Access Tokens, which Pulumi will use to add Pulumi Previews to your merge requests.

1. In the Pulumi dashboard, navigate to Integrations, found under the Settings menu.
2. In the GitLab integration card, select Authorize GitLab.
3. You will be redirected to GitLab, where you will be asked to approve the integration. For this step, you will authenticate with your GitLab identity. This is temporary and can be removed later.
4. After approving the integration and redirecting back to Pulumi, use the dropdown to select the GitLab organization you would like to integrate with and select save.
5. The authorization between the GitLab organization and Pulumi is now complete. Optionally, you can now disassociate your personal GitLab identity from Pulumi by selecting your identity in top right corner of the integration card, and then selecting Remove Identity.

### Configuring the GitLab Pipeline

For the Pulumi preview command to run, you need to add a GitLab pipeline file to your project. If you are already using pipelines, you just need to update your pipeline file.

1. [Generate a Pulumi](https://www.pulumi.com/docs/pulumi-cloud/access-management/access-tokens/) token using the account that you would like to post the merge request notes. Save this token as we will use this momentarily in a following step.
2. In GitLab, set the newly generated token as a CI Variable for your project. Name it `PULUMI_ACCESS_TOKEN`.
3. In your GitLab project, create a `.gitlab-ci.yml` if one doesn't already exist.
4. Add the following content to the `.gitlab-ci.yml` file, updating `pulumi/gitlab-demo/dev` to be the path to your stack

    ```bash
      image: pulumi/pulumi-go:latest

      stages:
          - pulumi

      preview:
        stage: pulumi
        script:
          - pulumi preview -s pulumi/gitlab-demo/dev
        only:
          - merge_request

    ```
  
5. Commit the file

## Configuring the GitLab Webhook

{{% notes type="warning" %}}
This step is only required for users whose GitLab plan does not include Group Access Tokens.
{{% /notes %}}

* [Create a Pulumi access token](/docs/pulumi-cloud/accounts#access-tokens) using the account that you would like the merge request notes to be posted as. Save this token as we will use this momentarily in a following step.
* You can configure a Group Hook or a Project Hook. The configuration values you use are the same regardless of where the webhook is registered on GitLab.
* Configuring a webhook at the Group-level means that you don't have to configure the webhook for every project manually.
If you only want to configure a webhook for a certain project, then you may do that as well.
* Head-over to the Settings > Webhooks page of your Group or Project and fill out the form as follows:
  * URL: `https://api.pulumi.com/workflow/gitlab`
  * Secret Token: `<The Pulumi access token from above.>`
  * Uncheck all boxes and check just the **Merge request events** checkbox

![Group Hook Setup 1](/images/docs/guides/continuous-delivery/gitlab-app/group_hook_1.png)

* Ensure the checkbox under **SSL verification** is checked as shown below
* Click the **Add webhook** button.

![Group Hook Setup 2](/images/docs/guides/continuous-delivery/gitlab-app/group_hook_2.png)

That's it! Now when you create a merge request and run Pulumi in a merge request pipeline, you should see notes in the MR that show a summary of the Pulumi preview. Learn how to run [Pulumi in GitLab CI/CD](/docs/using-pulumi/continuous-delivery/gitlab-ci/).

Here's a preview of what it looks like.

![Merge Request Note](/images/docs/guides/continuous-delivery/gitlab-app/merge_request_note.png)

## Disabling the Integration

If would like to disable the integration for a specific execution of Pulumi,
you can always set the `PULUMI_DISABLE_CI_DETECTION` env var to `false` without having to remove
the integration configuration itself.
