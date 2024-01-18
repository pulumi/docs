---
title_tag: Import Environments | Pulumi ESC
title: Import environments
h1: "Pulumi ESC: Import Environments"
meta_desc: This page provides an overview on how to import environments in Pulumi ESC.
weight: 5
menu:
  pulumiesc:
    parent: esc-get-started
    identifier: esc-get-started-import-environments
---

## Overview

There may be scenarios where the value you need to retrieve is stored in a different environment file. For example, imagine you are building a system that integrates with a third-party service such as:

- a payment provider
- weather data provider
- a content-management system

In the development environment, you might be integrating with the sandbox or development endpoint of the third-party service, while in the testing environment, you might be integrating with the production endpoint. Both endpoints may share the same base URL.

![Image showing same base URL and different endpoints](/docs/esc/get-started/esc-base-url.png)

Since this base URL would be the same across environments, it would be more efficient to define it once in one place rather than multiple times across multiple environment files.

With Pulumi ESC, you can import other environments into your environment file and make use of the imported configuration values and secrets. Similar to `values`, `imports` is a top-level key you will need to define in the environment file, meaning the syntax to create an import looks like the following:

```yaml
imports:
  - environment-name-1
  - environment-name-2
values:
    ...
    ...
```

## Import an environment

To demonstrate how this works, you will need to create a second environment. For the purposes of this guide, we will name this new environment `app-global-config`. In this environment, replace the placeholder content with the following configuration:

```yaml
values:
  ENDPOINT_URL: "https://wordsapiv1.p.rapidapi.com/"
```

{{< video title="Creating a global config environment in the Pulumi Console" src="/docs/esc/get-started/esc-create-global-config.mp4" autoplay="true" loop="true" >}}

Then, open your first environment (e.g. `my-dev-environment`) via the Pulumi console or the ESC CLI and add the following configuration to the top of your file:

```yaml
imports:
  - app-global-config
```

Your updated environment file should look similar to the following:

```yaml
# Example contents of my-dev-environment
imports:
  - app-global-config
values:
  myEnvironment: "development"
  myPassword:
    fn::secret:
      ciphertext: ZXNjeAA....
```

{{< video title="Importing the global config environment in the Pulumi Console" src="/docs/esc/get-started/esc-import-global-config.mp4" autoplay="true" loop="true" >}}

You should now see `"ENDPOINT_URL": "https://wordsapiv1.p.rapidapi.com/"` in the environment preview pane. This indicates that this value was successfully imported from the `app-global-config` environment, and you can now retrieve this value in the same way as the other values that are manually defined in this environment.

{{% notes type="info" %}}
You can test this out by retrieving the imported value via the console or the CLI. Refer to the [Store and Retrieve Secrets guide](/docs/esc/get-started/store-and-retrieve-secrets/#retrieve-environment-values) for the steps on how to do this.
{{% /notes %}}

In the next section, you will learn how to run local commands without manually configuring local secrets.

{{< get-started-stepper >}}
