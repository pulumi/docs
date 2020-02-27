---
title: Google Cloud Build
meta_desc: This page gives an overview of how to integration Google Cloud Build with a Pulumi program.
menu:
    userguides:
        parent: cont_delivery
        weight: 1

aliases:
- /docs/reference/cd-google-cloud-build/
- /docs/console/continuous-delivery/google-cloud-build/
---

## Prerequisites

### Google Cloud Platform

- A Google Cloud Platform account with the following APIs enabled:
    - Cloud Build API
    - Cloud Functions API (and/or any other relevant resource that will be deployed).
- Add `Cloud Functions Developer` role (and/or any other relevant resource that will be deployed) and the `Service Account User` role to the Cloud Build's service account. You can do this by navigating to the IAM tab in the GCP Console.

![Cloud Build service account](/images/docs/reference/google-cloud-build/cloud-build-service-account.png)

- If you do not grant the necessary permissions to the Cloud Build service account, you may see an error like this while deploying Cloud Functions (or whichever resource you are deploying.)

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

## Build Configuration

### `cloudbuild.yaml`

The Cloud Build configuration file below is a sample, to show you how to install the Pulumi CLI and run pulumi commands such as `pulumi preview` or `pulumi up` as part of your CI/CD workflow.

**Note:** The `_INSECURE_SUBSTITUTION_PULUMI_ACCESS_TOKEN` substitution is a simple way to specify the token, but you should consider using encrypted variables.

```yaml
steps:
- name: 'gcr.io/cloud-builders/yarn'
  entrypoint: /bin/sh
  args:
  - '-c'
  - 'chmod +x *.sh && ./pulumi.sh'
  env:
  # We use substitution for an example. Your Pulumi access token is sensitive and as such should be encrypted.
  # See the Encrypted Variables section below on how to do that.
  - 'PULUMI_ACCESS_TOKEN=$_INSECURE_SUBSTITUTION_PULUMI_ACCESS_TOKEN'
  - 'BUILD_TYPE=$_BUILD_TYPE'
```

In the above configuration, both `_BUILD_TYPE` and `_INSECURE_SUBSTITUTION_PULUMI_ACCESS_TOKEN` are substitutions configured in Cloud Build Triggers. You can read more about triggers [here](https://cloud.google.com/cloud-build/docs/running-builds/automate-builds).

- `_BUILD_TYPE` is used to indicate to the build environment about the type of build it is running. This allows us to run a `preview` or an `update` based on the build type. To configure the substitution, you need to setup build triggers for each type of branch builds you intend to support for your project.

- `_INSECURE_SUBSTITUTION_PULUMI_ACCESS_TOKEN` is used to supply the [Pulumi Access Token](https://app.pulumi.com/account/tokens) value.

For example, if you only want to support PR and merge builds, setup two triggers with the filter pattern `master` for all merge builds and `^master` for all other builds.

![Cloud Build Triggers](/images/docs/reference/google-cloud-build/cloud-build-triggers.png)

Here's the configuration of the "PR build" type trigger:

![Cloud Build Trigger configuration](/images/docs/reference/google-cloud-build/cloud-build-trigger-config.png)

### `pulumi.sh`

A basic bash script that does the following:

- Restore the Node dependencies for your Pulumi program.
- Perform a `pulumi login`.
- Select your stack.
- Run either `pulumi preview` or `pulumi up --yes` based on the `BUILD_TYPE` env var.

```bash
#!/bin/bash

# exit if a command returns a non-zero exit code and also print the commands and their args as they are executed.
set -e -x

# Download and install required tools.
# pulumi
curl -L https://get.pulumi.com/ | bash
export PATH=$PATH:$HOME/.pulumi/bin

# Restore npm dependencies for our infra app.
yarn install

# Login into pulumi. This will require the PULUMI_ACCESS_TOKEN environment variable.
pulumi login

# Select the appropriate stack.
pulumi stack select praneetloke/gcp-functions/dev

case $BUILD_TYPE in
  PullRequest)
      pulumi preview
    ;;
  *)
      pulumi up --yes
    ;;
esac
```

### Build Triggers

Cloud Build supports triggers that can start a new instance of your cloud build using the configuration defined in your repo.
To setup a build trigger, navigate to the Cloud Build service (or click [here](https://console.cloud.google.com/cloud-build/triggers) to go there now) in your GCP Console, making sure that you have the correct project selected.
Click on **Add Trigger** and follow the prompts to setup a trigger for your repo. In the final step **Trigger settings**, select the following settings:

- **Branch (regex)**: `[^master]`
    - This will match any branch _except_ `master`.
    - This means that this trigger will run for any branch other than `master`.
    - Alternatively, you can set this to `master` if you want this trigger to only run for `master` branches.
    - The default `.*` will match all branches, and therefore, the trigger will run for pushes against any branch.
- **Build configuration**: `Cloud Build configuration`.

## Next Steps

### Use the Pulumi community builder image for Google Cloud Build

We have created a builder image that will install the Pulumi CLI for you in a Node-based image. Since the builder is part of Google Cloud Build's community builders, you will need to make the builder available to your project by cloning the community builders' Git repo. See [this](https://github.com/GoogleCloudPlatform/cloud-builders-community/tree/master/pulumi) here for more information and an example for how to use the builder in your project.

### Encrypted Variables

If you have sensitive variables that may require encryption, you should create an encryption on Google KMS, then use that to encrypt your sensitive values. You may then use the encrypted strings in your cloud build configuration safely. Cloud Build can automatically decrypt sensitive strings at build time. See [this](https://cloud.google.com/cloud-build/docs/securing-builds/use-encrypted-secrets-credentials#using_the_encrypted_variable_in_build_requests) page to learn more.

### Substitutions

In the configuration above, we used custom substitutions. Cloud Build also has [default substitutions](https://cloud.google.com/cloud-build/docs/configuring-builds/substitute-variable-values). Using the default substitutions, you can make decisions in your CI or CD workflow.
