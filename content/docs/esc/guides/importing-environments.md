---
title_tag: Import Environments | Pulumi ESC
title: Importing Environments
h1: Importing Environments
meta_desc: Learn how to import and compose Pulumi ESC environments to share configuration across teams and projects.
menu:
  esc:
    parent: esc-guides
    identifier: esc-guides-importing-environments
    weight: 50
aliases:
  - /docs/esc/get-started/import-environments/
  - /docs/pulumi-cloud/esc/get-started/import-environments/
---

{{% notes type="info" %}}
This guide provides a step-by-step tutorial for getting started with environment imports. For complete technical reference including JSON Merge Patch semantics, implicit imports, and advanced composition patterns, see [Importing environments](/docs/esc/environments/imports/).
{{% /notes %}}

## Overview

There may be scenarios where the value you need to retrieve is stored in a different environment file. For example, imagine you are building a system that integrates with a third-party service such as:

- a payment provider
- weather data provider
- a content-management system

In the development environment, you might be integrating with the sandbox or development endpoint of the third-party service, while in the testing environment, you might be integrating with the production endpoint. Both endpoints may share the same base URL.

![Image showing same base URL and different endpoints](/docs/esc/assets/esc-base-url.png)

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

## Prerequisites

Before you begin, you should have:

1. [Created at least one environment](/docs/esc/get-started/) in Pulumi ESC
1. Basic familiarity with [defining values in environments](/docs/esc/environments/structure/)

## What you'll learn

In this guide, you will:

1. Create a shared environment with common configuration
1. Import that environment into another environment
1. Verify that imported values are accessible
1. Learn how to use both the code editor and table view to manage imports

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

You should now see `"ENDPOINT_URL": "https://wordsapiv1.p.rapidapi.com/"` in the environment preview pane. This confirms that the value was successfully imported from the `my-project/app-global-config` environment.

![Importing the global config environment in the Pulumi Console](/docs/esc/assets/esc-import-environments2.png)

**Success!** You've now imported an environment. The imported `ENDPOINT_URL` value is accessible in the same way as values defined directly in this environment. You can retrieve it via the console or CLI just like any other value.

{{% notes type="info" %}}
To test this, try retrieving the imported value via the console or CLI. See [Managing secrets](/docs/esc/guides/managing-secrets/#retrieving-secrets) for details on retrieving values.
{{% /notes %}}

### Import via the Table view

Alternatively, you can import environments using the Table view of the Pulumi console. Navigate to the **Table view** of your environment and select the **Import** button under the **Imports** section. You will be presented with a dropdown list of environments that you can import. Search for the name of the environment you want to import and select it. Then select **Import**.

![Importing the global config environment in the Pulumi Console](/docs/esc/assets/esc-import-pulumi-console.png)

To view the imported values, you will need to [open your environment](/docs/esc/guides/managing-secrets/#retrieving-secrets).

{{% notes type="info" %}}
You can import multiple environments and reorder them. Import order matters when the same keys appear in multiple imported environments. For details on merge behavior and override semantics, see the [imports reference](/docs/esc/environments/imports/).
{{% /notes %}}

## Next steps

- [Managing secrets](/docs/esc/guides/managing-secrets/) - Learn more about storing and retrieving values
- [Integrate with Pulumi IaC](/docs/esc/guides/integrate-with-pulumi-iac/) - Use composed environments in your infrastructure code
- [Composition and imports reference](/docs/esc/environments/imports/) - Complete documentation on import behavior and JSON Merge Patch semantics
