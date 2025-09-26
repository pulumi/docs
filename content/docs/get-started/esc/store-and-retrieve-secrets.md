---
title_tag: Store and Retrieve Secrets | Pulumi ESC
title: Store and retrieve secrets
h1: "Pulumi ESC: Store and Retrieve Secrets"
meta_desc: This page provides an overview on how to store and retrieve secrets in Pulumi ESC.
weight: 4
menu:
  esc:
    parent: esc-get-started
    identifier: esc-get-started-store-retrieve-secrets

---

In an environment file, values are defined as a series of key-value pairs in YAML format. All variables will be defined under a top-level key named `values`. These values can be strings, numbers, or arrays, and they can be manually provided, dynamically generated from external sources, or referenced from other values in the file. They can also be stored in plain-text or as secrets.

```yaml
values:
  myKey1: "myValue1"
  myNestedKey:
    myKey2: "myValue2"
    myNumber: 1
  myPassword:
    fn::secret:
      ciphertext: ZXN....
```

You can store and retrieve values in an environment via one of the following methods:

- the Pulumi Cloud console Document view
- the Pulumi Cloud console Table view
- the ESC CLI

## Store Environment values

### Store via the document view

To store values in your environment using the Document view, first click on the name of the environment to open it. You will be presented with a split pane view. The left side is the YAML-based code document view, and this is where you will write the definition of your environment configuration. The right side will show a preview of your configuration in JSON format.

![Open environment in Pulumi ESC console](/docs/esc/assets/esc-open-env.png)

Next, delete the placeholder text in the environment file and add the following simple configuration definition in its place:

```yaml
values:
  myEnvironment: "development"
  myPassword:
    fn::secret: "demo-password-123"
```

As shown above, you can specify that a value should be stored as a secret by using the `fn::secret` function. Once you have added the configuration, click the **Save** button located at the bottom of the editor.

{{< video title="Adding values to the environment in the Pulumi ESC console" src="https://www.pulumi.com/uploads/esc-add-env-values.mp4" autoplay="true" loop="true" >}}

The **Environment preview** pane on the right-hand side will then update to show your added configuration in JSON format. You will notice that the value of "myPassword" has been hidden from view in both the definition and preview panes.

### Store via the Table view

To store values in your environment using the Document view, first click on the name of the environment to open it. From the **Editor** menu, click the **Table view** button to switch the editor from the document YAML view to the table view.

{{< video title="Adding values to the environment in the Pulumi ESC console" src="https://www.pulumi.com/uploads/esc-open-env-table-view.mp4" autoplay="true" loop="true" >}}

Next, under the **Configuration** section, you will see fields labeled **Path** and **Value**. You will define your configuration values using these fields. In the **Path** field, type in `myEnvironment`, and in the **Value** field, type in `development`. Then click **Done** and **Save**.

![Adding values to the environment in the Pulumi ESC console](/docs/esc/assets/esc-add-env-values.png)

Next, click the **+Secret/config** button to create a new configuration. This time, you will create a configuration that will be stored as a secret. To do so, enter `myPassword` for the value of **Path** and `demo-password-123` for the value of **Value**. Select the **secret** option from the drop-down to indicate that this configuration will be stored as a secret, then click **Done** and **Save**.

![Adding values to the environment in the Pulumi ESC console](/docs/esc/assets/esc-add-secret-value.png)

You will notice that the value of `myPassword` is hidden from view after saving.

### Store via the CLI

To store values or update an existing value via the CLI, use the `esc env set` command as shown below, where `<org-name>` is optional and defaults to your Pulumi Cloud username:

```bash
esc env set [<org-name>/]<project-name>/<environment-name> <key> <value>
```

To demonstrate how this works, add the following simple configuration definition to your environment using the following command, making sure to replace the value of `my-project/dev-environment` with the name of your own environment:

```bash
esc env set my-project/dev-environment myEnvironment development
esc env set my-project/dev-environment myPassword demo-password-123 --secret
```

As shown above, you can specify that a value should be stored as a secret by using the `--secret` flag.

Alternatively, you can directly [edit your environment file with a code editor](/docs/pulumi-cloud/esc/environments/#with-the-pulumi-esc-cli) using the following command, making sure to replace `<project-name>/<environment-name>` with the identifier of your own environment (e.g. `my-project/dev-environment`):

```bash
esc env edit <project-name>/<environment-name>
```

Using this method enables you to add your configuration values in the same way that you would [via the console](/docs/esc/get-started/store-and-retrieve-secrets/#store-via-the-console).

## Retrieve Environment values

### Retrieve via the Document view

To retrieve values using the Document view, click the **Open** button. This will return any statically defined plain-text values and definitions.

![Clicking the open button in the Pulumi ESC console](/docs/esc/assets/esc-open-environment.png)

As shown above, it does not return the value of secrets defined, nor does it resolve values that are dynamically generated from a provider. To view these values, you will need to click the **Show secrets** slider.

![Clicking the show secrets slider the Pulumi ESC console](/docs/esc/assets/esc-show-secret-document-view.png)

### Retrieve via the Table view

Non-secret configuration values remain visible in the Table view after their creation, but secret values are automatically hidden. To reveal the value of a secret using the Table view, click the small eye icon.

{{< video title="Clicking the show secrets slider the Pulumi ESC console" src="https://www.pulumi.com/uploads/esc-show-secret-table-view.mp4" autoplay="true" loop="true" >}}

### Retrieve via the CLI

The CLI has a built-in `get` command that enables you to retrieve a single value from your environment. The format of the full command looks like the following:

```bash
esc env get [<your-org>/]<your-project-name>/<your-environment-name> <variable-key-name>
```

To retrieve the value of the `myEnvironment` variable you created earlier, the command to do so would look like the following, making sure to replace the value of `my-project/dev-environment` with the identifier of your own environment:

```bash
esc env get my-project/dev-environment myEnvironment
```

Running this command should return the following response:

```bash
$ esc env get my-project/dev-environment myEnvironment

   Value

    "development"

   Definition

    development

   Defined at

  • my-project/dev-environment:2:8
```

It is also possible to retrieve all values in an environment. To do so, run the `esc env get` command without specifying a value as shown below:

```bash
esc env get my-project/dev-environment
```

Running this command should return the following response:

```bash
$ esc env get my-project/dev-environment

   Value

    {
      "myEnvironment": "development",
      "myPassword": "[secret]"
    }

   Definition

    values:
      myEnvironment: "development"
      myPassword:
        fn::secret:
          ciphertext: ZXNjeAA....

```

The `esc env get` command only returns statically defined plain-text values and definitions. This means that it does not return the value of any defined secrets, nor does it resolve values that are dynamically generated from a provider. To view these values, you must run the `esc env open` command as shown below. This will open the environment and resolve any secrets or dynamically retrieved values:

```bash
$ esc env open my-project/dev-environment

{
  "myEnvironment": "development",
  "myPassword": "demo-password-123"
}

```

In the next section, you will learn how to import configuration values from other environments.

{{< get-started-stepper >}}
