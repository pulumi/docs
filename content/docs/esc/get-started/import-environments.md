---
title_tag: Import Environments | Pulumi ESC
title: Import environments
h1: "Pulumi ESC: Import Environments"
meta_desc: This page provides an overview on how to import environments in Pulumi
  ESC.
weight: 5
menu:
  esc:
    parent: esc-get-started
    identifier: esc-get-started-import-environments
search:
  keywords:
    - esc
    - import
    - environments
    - overview
    - environment
    - provides
    - page
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
  - project-name/environment-name-1
  - project-name/environment-name-2
values:
    ...
    ...
```

## Import an environment

To demonstrate how this works, you will need to create a second environment. For the purposes of this guide, we will name this new environment `my-project/app-global-config`. In this environment, replace the placeholder content with the following configuration:

```yaml
values:
  ENDPOINT_URL: "https://wordsapiv1.p.rapidapi.com/"
```

![Image showing same base URL and different endpoints](/docs/esc/assets/esc-import-environments.png)

Then, open your first environment (e.g. `my-project/dev-environment`) via the Pulumi console or the ESC CLI and add the following configuration to the top of your file:

```yaml
imports:
  - my-project/app-global-config
```

Your updated environment file should look similar to the following:

```yaml
# Example contents of my-project/dev-environment
imports:
  - my-project/app-global-config
values:
  myEnvironment: "development"
  myPassword:
    fn::secret:
      ciphertext: ZXNjeAA....
```

You should now see `"ENDPOINT_URL": "https://wordsapiv1.p.rapidapi.com/"` in the environment preview pane. This indicates that this value was successfully imported from the `my-project/app-global-config` environment, and you can now retrieve this value in the same way as the other values that are manually defined in this environment.

![Importing the global config environment in the Pulumi Console](/docs/esc/assets/esc-import-environments2.png)

{{% notes type="info" %}}
You can test this out by retrieving the imported value via the console or the CLI. Refer to the [Store and Retrieve Secrets guide](/docs/esc/get-started/store-and-retrieve-secrets/#retrieve-environment-values) for the steps on how to do this.
{{% /notes %}}

### Import via the Table view

Alternatively, you can import environments using the Table view of the Pulumi console. Navigate to the **Table view** of your environment and click the **Import** button under the **Imports** section. You will be presented with a dropdown list of environments that you can import. Search for the name of the environment you want to import and select it. Then click **Import**.

![Importing the global config environment in the Pulumi Console](/docs/esc/assets/esc-import-pulumi-console.png)

To view the imported values, you will need to [open your environment](/docs/esc/get-started/store-and-retrieve-secrets/#retrieve-environment-values).

{{% notes type="info" %}}
You can import multiple environments and reorder them. The order of the imported environments is important because if you have two environments that have the same name for a key/path, then the last imported environment will override the value of that key/paths for any environments that are imported before it. This behavior can be useful for scenarios where you need to intentionally override the value of a particular key/path.
{{% /notes %}}

In the next section, you will learn how to run local commands without manually configuring local secrets.

{{< get-started-stepper >}}
