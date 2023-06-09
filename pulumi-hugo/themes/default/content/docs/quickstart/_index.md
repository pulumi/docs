---
title_tag: Pulumi Quickstart
meta_desc: Get started with Pulumi with any cloud and any language in 5 minutes.
title: Quickstart
h1: Pulumi quickstart
pulumi_quickstart: true
menu:
  quickstart:
    name: Overview
    weight: 2
aliases:
- /start/
- /getting-started/
- /get-started/
- /docs/tour/
- /docs/get-started/
intro: Quickstart your Pulumi experience by learning how to install Pulumi, set up your cloud credentials, and run your first update.
customize:
  heading: Customize instructions
  # list of availabe configuration options.
  options:
    os:
      - id: osx
        displayName: macOs
        default: true
      - id: windows
        displayName: Windows
      - id: linux
        displayName: Linux
    clouds:
      - id: aws
        displayName: AWS
        default: true
      - id: azure
        displayName: Azure
      - id: gcp
        displayName: Google Cloud
      - id: kubernetes
        displayName: Kubernetes
    languages:
      - id: typescript
        displayName: TypeScript
        default: true
      - id: python
        displayName: Python
      - id: go
        displayName: Go
      - id: csharp
        displayName: "C#"
      - id: java
        displayName: Java
      - id: yaml
        displayName: YAML
    templates:
      - id: starter
        displayName: Starter
        cmdPrefix: ""
        default: true
      - id: container-service
        displayName: Container service
        cmdPrefix: container
      - id: serverless-app
        displayName: Serverless app
        cmdPrefix: serverless
      - id: static-website
        displayName: Static website
        cmdPrefix: static-website
      - id: virtual-machine
        displayName: Virtual machine
        cmdPrefix: vm
    credentials_label: I need to set up cloud credentials
steps:
  install:
    heading: Install the Pulumi CLI
    command:
      osx: brew install pulumi/tap/pulumi
      windows: choco install pulumi
      linux: curl -fsSL https://get.pulumi.com | sh
    accordion:
      title: More installation methods
      content: too add later
  credentials:
    clouds:
      - cloud: aws
        default: true
        heading: Set up AWS credentials
        content: <p>Pulumi requires cloud credentials to manage and provision resources. Use an IAM user account that has programmatic access with rights to deploy and manage resources.</p><p>If you have previously installed and configured the AWS CLI, Pulumi will respect and use your configuration settings.</p><p>If you do not have the AWS CLI installed or plan on using Pulumi from within a CI/CD pipeline, <a href="https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys" target="_blank">retrieve your access key ID and secret access key</a> and then set the <code>AWS_ACCESS_KEY_ID</code> and <code>AWS_SECRET_ACCESS_KEY</code> environment variables on your workstation.</p>
      - cloud: azure
        heading: Set up Azure credentials
        content: <p>Pulumi requires cloud credentials to manage and provision resources. Pulumi can authenticate to Azure using a user account or service principal that has programmatic access with rights to deploy and manage your Azure resources.</p><p>Pulumi relies on the Azure SDK to authenticate requests from your computer to Azure. Your credentials are never sent to pulumi.com.</p><p>When developing locally, we recommend that you install the Azure CLI and then authorize access with a user account.</p><p>The <a href="https://docs.microsoft.com/en-us/cli/azure/install-azure-cli" target="_blanl">Azure CLI</a>, and Pulumi, will use the default subscription for the account. Change the active subscription with the az account set command.</p>
      - cloud: gcp
        heading: Set up Google Cloud credentials
        content: <p>Pulumi requires cloud credentials to manage and provision resources. You must use an IAM user or service account that has programmatic access with rights to deploy and manage your Google Cloud resources.</p><p>When developing locally, we recommend that you install the <a href="https://cloud.google.com/sdk/install" target="_blank">Google Cloud SDK</a> and then <a href="https://cloud.google.com/sdk/docs/authorizing#authorizing_with_a_user_account" target="_blank">authorize access with a user account</a>. Next, Pulumi requires default application credentials to interact with your Google Cloud resources, so run auth application-default login command to obtain those credentials.</p><p>To configure Pulumi to interact with your Google Cloud project, set it with the pulumi config command using the project’s ID. You may also set your Google Cloud Project via environment variable.</p>
      - cloud: kubernetes
        heading: Set up Kubernetes credentials
        content: "<p>Like <code>kubectl</code>, Pulumi will look for a kubeconfig file in the following locations:</p><ul><li>The environment variable: <code>$KUBECONFIG</code>,<li>Or in current user’s default kubeconfig directory: <code>~/.kube/config</code></li></ul><p>Verify the cluster is configured and up by running <code>kubectl get pods</code>.</p>"
  directory:
    heading: Create a directory and move into it
    command: mkdir first-project && cd first-project
  template:
    heading: Use your first template
    accordion:
      heading: Learn about projects, stacks, and templates
      intro: <p>Pulumi <a href="/docs/concepts/projects/">projects</a> and <a href="/docs/concepts/stack/">stacks</a> organize Pulumi code. Projects are similar to GitHub repos and stacks are an instance of code with separate configuration. Projects can have multiple stacks for different development environments or for different cloud configurations.</p><p>The following files are generated when a new project is created:</p>
      closing: <p><code>pulumi new</code> uses a <a href="/templates/" target="_blank">template</a> to quickly deploy and modify common architectures.</p>
      content:
        typescript: <ul><li><code>Pulumi.yaml</code> defines the project.</li><li><code>Pulumi.dev.yaml</code> contains <a href="/docs/concepts/config/">configuration</a> values for the stack you just initialized.</li><li><code>index.ts</code> is the Pulumi program that defines your stack resources.</li></ul>
        python: <ul><li><code>Pulumi.yaml</code> defines the project.</li><li><code>Pulumi.dev.yaml</code> contains <a href="/docs/concepts/config/">configuration</a> values for the stack you just initialized.</li><li><code>main.py</code> is the Pulumi program that defines your stack resources.</li></ul>
        go: <ul><li><code>Pulumi.yaml</code> defines the project.</li><li><code>Pulumi.dev.yaml</code> contains <a href="/docs/concepts/config/">configuration</a> values for the stack you just initialized.</li><li><code>main.go</code> is the Pulumi program that defines your stack resources.</li></ul>
        csharp: <ul><li><code>Pulumi.yaml</code> defines the project.</li><li><code>Pulumi.dev.yaml</code> contains <a href="/docs/concepts/config/">configuration</a> values for the stack you just initialized.</li><li><code>program.cs</code> is the Pulumi program that defines your stack resources.</li></ul>
        java: <ul><li><code>Pulumi.yaml</code> defines the project.</li><li><code>Pulumi.dev.yaml</code> contains <a href="/docs/concepts/config/">configuration</a> values for the stack you just initialized.</li><li><code>src/main/java/myproject</code> defines the project’s Java package root.</li><li><code>app.java</code> is the Pulumi program that defines your stack resources.</li></ul>
        yaml: <ul><li><code>Pulumi.yaml</code> defines the project.</li><li><code>Pulumi.dev.yaml</code> contains <a href="/docs/concepts/config/">configuration</a> values for the stack you just initialized.</li></ul>
  deploy:
    heading: Deploy your infrastructure!
    command: pulumi up
    accordion:
      heading: Learn what happens during a deployment
      content: Pulumi evaluates the program and determines what resources need updates. By default pulumi runs a preview that outline the changes that will be made when you run the deployment. Pulumi computes the minimally disruptive change to achieve the desired state described by the program.
next_steps:
  heading: Learn more
  content:
    - cloud: aws
      body: Learn how to modify a program with Pulumi’s Get started tutorial for AWS.
      logo: /logos/tech/aws.svg
      link: https://www.pulumi.com/docs/clouds/aws/get-started/#modify-program
    - cloud: azure
      body: Learn how to modify a program with Pulumi’s Get started tutorial for Azure.
      logo: /logos/tech/azure.svg
      link: https://www.pulumi.com/docs/clouds/azure/get-started/#modify-program
    - cloud: gcp
      body: Learn how to modify a program with Pulumi’s Get started tutorial for Google Cloud.
      logo: /logos/tech/gcp.svg
      link: https://www.pulumi.com/docs/clouds/gcp/get-started/#modify-program
    - cloud: kubernetes
      body: Learn how to modify a program with Pulumi’s Get started tutorial for Kubernetes.
      logo: /logos/tech/k8s.svg
      link: https://www.pulumi.com/docs/clouds/kubernetes/get-started/#modify-program
---
