---
title_tag: "Using Pulumi Deployments"
meta_desc: Reference documentation for configuring and using Pulumi Deployments
title: "Using deployments"
h1: "Using Pulumi Deployments"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    parent: deployments
    weight: 2
aliases:
  - /docs/intro/deployments/reference/
---

This page highlights some common patterns and workflows using Pulumi Deployments.

## Deployment Settings

Deployment settings refer to the full set of configuration required to run a Pulumi Deployment, defined on a per-stack basis. These settings may be defined once for the stack, via the UI, Pulumi Service provider, or the REST API and can be consumed using any of the triggers, i.e., push-to-deploy, click-to-deploy, or via the REST API.

### From the Pulumi Cloud UI

From the Pulumi Console, a stack's deployment settings can be accessed via the `Settings > Deploy` tab. Once the settings are defined via the UI, they apply to all Deployment triggers, including push-to-deploy (if you have the GitHub app installed), click-to-deploy and the REST API.

![Pulumi UI - Deployment Settings](../ui-settings.png)

### From the API

Alternatively, a stack's deployment settings may be defined and subsequently modified using the REST API.

```POST https://api.pulumi.com/{org}/{project}/{stack}/deployment/settings```

```json
{
    "sourceContext": {
        "git": {
            "repoURL": "https://github.com/pulumi/deploy-demos.git",
            "branch": "main",
            "repoDir": "pulumi-programs/simple-resource"
        }
    },
    "operationContext": {
        "environmentVariables": {
            "TEST_VAR": "foo",
            "SECRET_VAR": {
                "secret": "my-secret"
            }
        }
    }
}
```

To modify an environment variable in the deployment settings, you only need to specify the changed settings:

```POST https://api.pulumi.com/api/preview/{org}/{project}/{stack}/deployment/settings```

```json
{
    "operationContext": {
        "environmentVariables": {
            "TEST_VAR": "new_value"
        }
    }
}
```

The [REST API documentation](../api) contains much more thorough information about individual API properties.

### Defined as Code with the Pulumi Service Provider

Finally, a stack's deployment settings may be defined as a resource within the stack itself using the Pulumi Service provider. This lets you securely store your settings in source control alongside your code.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as service from "@pulumi/pulumiservice";

const config = new pulumi.Config();

const settings = new service.DeploymentSettings("deployment_settings", {
    organization: "service-provider-test-org",
    project: "test-deployment-settings-project",
    stack: "dev",
    operationContext: {
        environmentVariables: {
            TEST_VAR: "foo",
            SECRET_VAR: config.requireSecret("my_secret"),
        }
    },
    sourceContext: {
        git: {
            repoUrl: "https://github.com/pulumi/deploy-demos.git",
            branch: "refs/heads/main",
            repoDir: "pulumi-programs/simple-resource"
        }
    }
});
```

## Deployment Triggers

A deployment trigger refers to a method of initializing a deployment. Currently, a deployment may be triggered using the REST API, by clicking a button in the Pulumi Console, or via a `git push` if the GitHub application is installed.

### REST API

Once deployment settings are defined for a stack, triggering a deployment is as simple as a two-line request.

```POST https://api.pulumi.com/api/preview/{org}/{project}/{stack}/deployments```

```json
{
    "inheritSettings": true,
    "operation": "update/preview/refresh/destroy"
}
```

The `inheritSettings` property allows you to make use of the predefined deployment settings for the stack. If you would rather not use the predefined settings, set `inheritSettings` to `false`. If you need to override some specific settings, specify them in the request body.

```POST https://api.pulumi.com/api/preview/{org}/{project}/{stack}/deployments```

```json
{
    "inheritSettings": true,
    "operation": "update/preview/refresh/destroy",
    "operationContext": {
        "environmentVariables": {
            "EXTRA_VAR": {
                "secret": "my-super-secret-value"
            }
        }
    }
}
```

The merge behavior of deployment settings are further explained in the [REST API documentation](../api).

### Click to Deploy

A deployment may be triggered at the simple click of a button in the Pulumi Console. Useful to test if your deployment settings are configured correctly or to execute one-off deployments.

![Pulumi UI - Click to Deploy](../ui-deploy-button.png)

### GitHub Push to Deploy

Once you have the GitHub application installed in your Pulumi organization, you can choose to have deployments run a `pulumi preview` when Pull Requests are opened against a target branch, or `pulumi up` when a commit is pushed to a branch.

{{% notes type="info" %}}

The `pulumi preview` on Pull Request capability requires that the Github user creating the Pull Request has their Github Organization Visibility set to `Public`.

{{% /notes %}}

![Pulumi UI - Push to Deploy](../ui-push-to-deploy.png)

## Configuring push-to-deploy from GitHub

### GitHub App Installation

You'll need to install and configure the [Pulumi GitHub App](/docs/using-pulumi/continuous-delivery/github-app/#installation-and-configuration) to use push-to-deploy functionality. The app requires read access to your repos so it can clone your Pulumi programs and listen to merge commits to automatically trigger deployments on `git push`.

{{% notes type="warning" %}}

While the app can be installed via GitHub, it **must be installed through the Pulumi Cloud** using the steps below to ensure correct setup. Installing through the Pulumi Cloud ensures we have a connection from Pulumi to your GitHub user or organization.

{{% /notes %}}

Follow these steps:

1. Ensure you have selected the Pulumi organization you wish to use with Pulumi Deployments in the Organization drop-down.
2. Navigate to Settings > Integrations.
3. Select the "Install the Pulumi GitHub App" button.

   If this page says you already have the app installed, you can stop here. If the page asks you to accept additional permissions for the app, please accept the permissions and stop here.

4. After clicking "Install" you will be directed to GitHub. Select the GitHub organization you wish to use with Pulumi Deployments.
5. Select which repos (or all repos) Pulumi Deployments can have access to, and then Install.
6. You will be redirected to the Pulumi Cloud (app.pulumi.com). Return to **Settings** > **Integrations** to confirm the GitHub App is installed.

If you installed the GitHub app in the past and the steps above aren't showing it as installed for your desired organization, please try the following:

- Ensure you're a GitHub admin of the GitHub organization where you're installing the app.
- Uninstall the app (via GitHub) and re-install it following the steps above. **Note:** Uninstalling the app will delete any push-to-deploy configurations you may have already setup.

### Configuring settings

Once the GitHub app has been installed, the deployment settings for a stack can be defined using the methods defined in the `Deployment Settings` section.

### Limitations

- Configuring deployment settings for a stack currently requires admin privileges in the Pulumi organization.
- The GitHub app may only be installed by a GitHub *and* Pulumi admin.
- Currently, there is a 1 to 1 mapping between GitHub organizations and Pulumi organizations.

## Common Scenarios

### Path Filtering

When using the GitHub app and push-to-deploy, you may want to filter deployment events to only target file changes in specific directories. You can easily do this using path filtering, so a deployment is only triggered if there is a change in files that match the path filters. This is especially useful for monorepos where you may have multiple Pulumi programs within the same repository.

![Pulumi UI - Path Filters](../ui-path-filters.png)

As with any other deployment setting, the path filters may be set via the Pulumi Console, using the REST API or defined in code using the Service provider.

### Customizing the Deployment Environment

By default, the deployment is executed using the [pulumi/pulumi](https://hub.docker.com/r/pulumi/pulumi) image. However, there may be scenarios where you might want to customize the image used for the execution, e.g. if you want to use a different version of python or need to include additional dependencies.

This is possible by specifying a custom executor image for your deployment.

![Pulumi UI - Custom Executor](../ui-custom-executor.png)

Image requirements:

- It must be a unix-based image which includes `curl`.
- It must include the `pulumi` CLI in its `$PATH`.
- It must include the required SDK runtime(s) for your Pulumi program.

{{% notes "info" %}}

Using a custom image may result in slower execution due to time spent pulling the image.

{{% /notes %}}

### Customizing the dependency installation step

By default, the deployment executor will attempt to install dependencies for your project by using the default dependency manager for the language (i.e. `npm` for nodejs or `virtualenv` for python). However, there may be scenarios where you may want to have more control over the dependency installation step (e.g. you are using `yarn` and/or a different version of `node` than the one that is installed by default).

This is enabled by skipping the default dependency installation step (under Advanced Settings in the UI), and setting a few pre-run commands and environment variables.

![Pulumi UI - Node Version](../ui-node-version.png)
