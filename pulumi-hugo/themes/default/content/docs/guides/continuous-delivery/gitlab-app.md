---
title: Pulumi GitLab Integration
meta_desc: Integrate the results of Pulumi stack previews to GitLab Merge Requests. It
           will show you any potential infrastructure changes on Merge Requests.
menu:
    userguides:
        parent: cont_delivery
        weight: 1
---

With this new GitLab integration, Pulumi is able to add summary notes to a GitLab Merge Request by using the merge request information
posted to the Pulumi Service via [GitLab Webhooks](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html#merge-request-events).

To enable the integration with your GitLab project, you will need to ensure you have done the following two things:

* [Signup](https://app.pulumi.com/signup) for a Pulumi account with your GitLab identity (or link your GitLab identity with an existing account.)
* If your GitLab Project is under a GitLab Group, ensure that the group is added to Pulumi as an [organization](https://app.pulumi.com/site/trial)

## Prerequisites

* You must have a GitLab identity associated with your Pulumi account.
* If you are integrating a GitLab project that is under a group, [add an organization]({{< relref "/docs/intro/pulumi-service/organizations#creating-an-organization" >}})
  in Pulumi.
  * After you add the organization, ensure that it uses GitLab [as its identity provider]({{< relref "/docs/intro/pulumi-service/organizations#changing-identity-providers" >}}).

{{% notes type="warning" %}}
This feature is currently not compatible with GitLab's [pipelines for merged results](https://docs.gitlab.com/ee/ci/pipelines/pipelines_for_merged_results.html).
See the [GitLab issue](https://gitlab.com/gitlab-org/gitlab/-/issues/350086) for details as to why.
{{% /notes %}}

## Configuring the GitLab Webhook

* Create a [Pulumi access token](https://app.pulumi.com/account/tokens) using the account that you would like the merge request notes to be posted as. Save this token as we will use this momentarily in a following step.
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

That's it! Now when you create a merge request and run Pulumi in a merge request pipeline, you should see notes in the MR that show a summary of the Pulumi preview. Learn how to run [Pulumi in GitLab CI/CD](https://www.pulumi.com/docs/guides/continuous-delivery/gitlab-ci/).

Here's a preview of what it looks like.

![Merge Request Note](/images/docs/guides/continuous-delivery/gitlab-app/merge_request_note.png)

## Disabling the Integration

If would like to disable the integration for a specific execution of Pulumi,
you can always set the `PULUMI_DISABLE_CI_DETECTION` env var to `false` without having to remove
the integration configuration itself.
