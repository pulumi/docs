---
title: Google Cloud Build
---

## Prerequisites

### Google Cloud Platform

- A Google Cloud Platform account with the following APIs enabled:
  - Cloud Build API
  - Cloud Functions API (and/or any other relevant resource that will be deployed).
- Add `Cloud Functions Developer` role (and/or any other relevant resource that will be deployed) and the `Service Account User` role to the Cloud Build's service account. You can do this by navigating to the IAM tab in the GCP Console.

![Cloud Build service account](/images/reference/google-cloud-build/cloud-build-service-account.png)

  - If you do not grant the necessary permissions to the Cloud Build service account, you may see an error like this while deploying Cloud Functions (or whichever resource you are deploying).
  ```
  error: Plan apply failed: googleapi: Error 403: Missing necessary permission iam.serviceAccounts.actAs for  on resource cloud-build-samples@appspot.gserviceaccount.com. Please grant  the roles/iam.serviceAccountUser role. You can do that by running 'gcloud iam service-accounts add-iam-policy-binding cloud-build-samples@appspot.gserviceaccount.com --member= --role=roles/iam.serviceAccountUser', forbidden
  ```

### Pulumi

- A Pulumi account. Don't have one? [Signup](https://app.pulumi.com/signup) now.
- An existing stack or create one based off a template.
- This page uses the [GCP Functions example](https://github.com/pulumi/examples/tree/master/gcp-ts-functions) from the Pulumi examples repo.
  - The choice of example has no bearing on the information presented on this page. You may choose any example. However, the Cloud Functions example is the easiest and quickest to get up and running with Cloud Build.

## Deploying from a Cloud Source repo

### Hosted on Cloud Source

Don't have a repo on Cloud Source yet? See this page for a [quickstart](https://cloud.google.com/source-repositories/docs/quickstart) tutorial.

### External repos

Have an existing repo already? Cloud Source supports [mirroring repositories](https://cloud.google.com/source-repositories/docs/mirroring-a-github-repository) that are on GitHub or Bitbucket.

## Pulumi Config

Set the appropriate `gcp:project` and `gcp:region` values. For example, if your GCP project ID is `awesome-project` and you would like to deploy resources to `us-central1`, then you should run:

`pulumi config set gcp:project awesome-project` and `pulumi config set gcp:region us-central`

**Note**: Not all resources are available in all regions. Please check that GCP supports the region and resource combination [here](https://cloud.google.com/about/locations/).

## `cloudbuild.yaml`

The Cloud Build configuration file below is a sample, to show you how to install the Pulumi CLI and run pulumi commands such as `pulumi preview` or `pulumi up` as part of your CI/CD workflow.

```yaml
steps:
- name: 'gcr.io/cloud-builders/yarn'
  entrypoint: /bin/sh
  args:
  - '-c'
  - 'chmod +x *.sh && ./pulumi.sh'
  env:
  - 'PULUMI_ACCESS_TOKEN=$_PULUMI_ACCESS_TOKEN'
  - 'BUILD_TYPE=$_BUILD_TYPE'
```

## Next Steps

### Substitutions

In the configuration above, we used custom substitutions. Cloud Build also has [default substitutions](https://cloud.google.com/cloud-build/docs/configuring-builds/substitute-variable-values). Using the default substitutions, you can make decisions in your CI or CD workflow.

### Encrypted Variables

If you have sensitive variables that may require encryption, you should create an encryption on Google KMS, then use that to encrypt your sensitive values. You may then use the encrypted strings in your cloud build configuration safely. Cloud Build can automatically decrypt sensitive strings at build time. See [this](https://cloud.google.com/cloud-build/docs/securing-builds/use-encrypted-secrets-credentials#using_the_encrypted_variable_in_build_requests) page to learn more.

### Pulumi Cloud Build builder

> The Pulumi builder is awaiting acceptance from the community repo maintainers. You can download the branch containing the builder while it is reviewed and merged.

Cloud Build supports custom [builders](https://cloud.google.com/cloud-build/docs/cloud-builders), as well as those that are built by the [community](https://github.com/GoogleCloudPlatform/cloud-builders-community).

The Pulumi builder is available for you to use in a cloud build step. Follow the steps in the repo to use it.

**Got questions or feedback about this page?** Checkout our community [Slack](https://slack.pulumi.io).
