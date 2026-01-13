---
title_tag: "Using Pulumi GitLab Integration | CI/CD"
meta_desc: Integrate the results of Pulumi stack previews to GitLab Merge Requests. It
           will show you any potential infrastructure changes on Merge Requests.
title: GitLab Integration
h1: Pulumi CI/CD & GitLab Integration
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: GitLab Integration
        parent: iac-using-pulumi-cicd
        weight: 8
aliases:
- /docs/iac/using-pulumi/continuous-delivery/gitlab-app/
- /docs/guides/continuous-delivery/gitlab-app/
- /docs/using-pulumi/continuous-delivery/gitlab-app/
- /docs/iac/packages-and-automation/continuous-delivery/gitlab-app/
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

### In Pulumi Cloud

1. Navigate to **Settings** > **Integrations** in the Pulumi Cloud dashboard.
1. In the GitLab integration card, select **Authorize GitLab**.

### In GitLab

1. You will be redirected to GitLab, where you will be asked to approve the integration. Authenticate with your GitLab identity. This authorization is temporary and can be removed later.

### Back in Pulumi Cloud

1. After approving the integration and being redirected back to Pulumi Cloud, use the dropdown to select the GitLab organization you would like to integrate with and select **Save**.
1. The authorization between the GitLab organization and Pulumi is now complete. Optionally, you can disassociate your personal GitLab identity from Pulumi by selecting your identity in the top right corner of the integration card, then selecting **Remove Identity**.

### Configuring the GitLab pipeline

For the Pulumi preview command to run, you need to add a GitLab pipeline file to your project. If you are already using pipelines, you just need to update your pipeline file.

#### In Pulumi Cloud

1. [Generate a Pulumi access token](/docs/administration/access-identity/access-tokens/) using the account that you would like to post the merge request notes. Save this token for use in the next step.

#### In GitLab

1. Set the newly generated token as a CI Variable for your project. Name it `PULUMI_ACCESS_TOKEN`.
1. In your GitLab project, create a `.gitlab-ci.yml` file if one doesn't already exist.
1. Add the following content to the `.gitlab-ci.yml` file, updating `pulumi/gitlab-demo/dev` to be the path to your stack:

    ```yaml
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

1. Commit the file.

## Configuring the GitLab webhook

{{% notes type="warning" %}}
This step is only required for users whose GitLab plan does not include Group Access Tokens.
{{% /notes %}}

### In Pulumi Cloud

1. [Create a Pulumi access token](/docs/pulumi-cloud/accounts#access-tokens) using the account that you would like the merge request notes to be posted as. Save this token for use in the next step.

### In GitLab

You can configure a Group Hook or a Project Hook. The configuration values are the same regardless of where the webhook is registered. Configuring a webhook at the Group level means you don't have to configure it for every project manually.

1. Navigate to **Settings** > **Webhooks** in your GitLab Group or Project.
1. Fill out the form as follows:
    * **URL**: `https://api.pulumi.com/workflow/gitlab`
    * **Secret Token**: The Pulumi access token you created above
    * Uncheck all trigger boxes and check only **Merge request events**

    ![GitLab webhook configuration - triggers](/images/docs/guides/continuous-delivery/gitlab-app/group_hook_1.png)

1. Ensure the checkbox under **SSL verification** is checked.
1. Click **Add webhook**.

    ![GitLab webhook configuration - SSL verification](/images/docs/guides/continuous-delivery/gitlab-app/group_hook_2.png)

That's it! Now when you create a merge request and run Pulumi in a merge request pipeline, you should see notes in the MR that show a summary of the Pulumi preview. Learn how to run [Pulumi in GitLab CI/CD](/docs/using-pulumi/continuous-delivery/gitlab-ci/).

Here's a preview of what the merge request note looks like in GitLab:

![GitLab merge request showing Pulumi preview note](/images/docs/guides/continuous-delivery/gitlab-app/merge_request_note.png)

## Disabling the Integration

If would like to disable the integration for a specific execution of Pulumi,
you can always set the `PULUMI_DISABLE_CI_DETECTION` env var to `false` without having to remove
the integration configuration itself.
