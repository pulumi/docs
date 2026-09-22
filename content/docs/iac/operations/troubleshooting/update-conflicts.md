---
title_tag: "Resolving Pulumi Update Conflicts"
meta_desc: "Learn how to resolve 409 conflict errors when another update is currently in progress."
title: Update conflicts
h1: "409 conflict: Another update is currently in progress"
menu:
    iac:
        name: Update Conflicts
        parent: iac-operations-troubleshooting
        weight: 10
aliases:
    - /docs/troubleshooting/#conflict
    - /docs/support/troubleshooting/common-issues/update-conflicts/
    - /docs/iac/troubleshooting/common-issues/update-conflicts/
---

Run `pulumi cancel` to cancel the update.

{{% notes type="warning" %}}
Warning! If you cancel another person's update, their update will fail immediately.
{{% /notes %}}

One of the services that the [Pulumi Cloud](/docs/administration/) provides is *concurrency control*. The service allows at most one user to update a particular stack at a time. This is accomplished by using "leases"; whenever a user requests an update, they request a "lease" on the stack that gives them the right to update the requested stack. The service makes sure that only one person has a lease active at a time.

If you get this error message, this means that the service believes that somebody else has requested and was granted a lease to the stack that you are attempting to update. There are two reasons why this could be:

1. Somebody else is currently updating the stack. If you are working on a stack with more than one collaborator, it could be that your collaborators have initiated an update without your knowledge. You can confirm this by visiting the Pulumi web console and seeing who initiated the most recent update.
1. You were updating the stack, but the Pulumi CLI crashed in the middle of the update.

If you are working on a stack with no other collaborators, it is common to encounter situation number 2 if you run into a bug in Pulumi. If this update was not triggered by someone else, you can use the `pulumi cancel` command to cancel the current update. This operation revokes the "lease" that the service has given to the person who initiated the stack update.

## Preventing conflicts in CI/CD

Cancelling and retrying fixes a single conflict, but if you're seeing this error repeatedly, the underlying cause is usually a pipeline that lets more than one `pulumi up` reach the same stack at once. Because only one lease can be held on a stack at a time, two runs racing for it always leave one to fail with this error — the durable fix is to serialize updates per stack, not to keep cancelling.

The same race can happen without a second automated run at all: a teammate running `pulumi up` from their own machine against a stack your pipeline also deploys will collide with it exactly the same way. Treat any stack a pipeline manages as pipeline-owned, and have collaborators go through the pipeline (or a [preview-only](/docs/iac/cli/commands/pulumi_preview/) local run) rather than updating it directly.

How you serialize updates depends on your CI/CD system:

- **GitHub Actions** — use a [concurrency group](/docs/iac/operations/continuous-delivery/github-actions/#control-concurrent-runs) keyed to the stack, without `cancel-in-progress`, so queued deployments wait rather than overlap.
- **GitLab CI/CD** — assign deployment jobs a [`resource_group`](/docs/iac/operations/continuous-delivery/gitlab-ci/#serialize-deployments) so GitLab runs them one at a time.
- **Travis CI** — set **Limit concurrent jobs** to `1` for deployment builds, as described in the [Travis CI guide](/docs/iac/operations/continuous-delivery/travis/#concurrency).
- **Jenkins** — wrap the deployment stage in a [`lock`](https://www.jenkins.io/doc/pipeline/steps/lockable-resources/) step from the Lockable Resources plugin, keyed to the stack, so the Jenkins queue holds a second run until the first finishes:

  ```groovy
  stage('Deploy') {
      steps {
          lock(resource: 'myproject-production-stack') {
              sh 'pulumi up --stack myorg/myproject/production --yes'
          }
      }
  }
  ```

- **Any other system** — look for its equivalent of a named lock or serial job queue (most CI/CD systems have one) and key it to the stack, the same way as above.

If you'd rather not wire this up yourself, [Pulumi Deployments](/docs/deployments/) queues updates per stack automatically — see [Deployment queue](/docs/deployments/operations/deployment-queue/) — so this class of conflict can't occur regardless of what triggers the update.
