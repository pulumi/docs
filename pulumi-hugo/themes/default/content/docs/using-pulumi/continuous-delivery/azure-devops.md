---
title_tag: "Using Azure DevOps | CI/CD"
meta_desc: This page details how to use Azure DevOps to manage deploying stacks based on
           commits to specific Git branches, and based on the build reason.
title: Azure DevOps
h1: Pulumi CI/CD & Azure DevOps
menu:
    usingpulumi:
        parent: cont_delivery
        weight: 1

aliases:
- /docs/reference/cd-azure-devops/
- /docs/console/continuous-delivery/azure-devops/
- /docs/guides/continuous-delivery/azure-devops/
- /docs/guides/continuous-delivery/cd-azure-devops/
- /docs/using-pulumi/continuous-delivery/cd-azure-devops/
---

This page details how to use [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/) to manage deploying
stacks based on commits to specific Git branches, and based on the build reason. You may also choose to introduce a
[Manual Intervention](https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/utility/manual-intervention?view=vsts) task to control the preview vs. update step for any Pulumi stack.

Pulumi doesn't require any particular arrangement of stacks or workflow to work in a
continuous integration / continuous deployment system. So the steps described here can be
altered to fit into any existing type of deployment setup.

This page shows you how to use the Pulumi Azure DevOps task extension and the YAML method to configure your DevOps pipeline, but you can easily adapt
the steps outlined in the sample YAML file below to the Visual Designer as well.

## Prerequisites

- An account on [https://app.pulumi.com](https://app.pulumi.com).
- The latest CLI.
    - [Installation instructions](/docs/install/).
- A git repo with your Azure DevOps project set as the remote URL.
    - To learn more about how to [create a git repo in your DevOps project](https://docs.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=vsts&tabs=new-nav).
- Optional, but recommended, the [Pulumi Azure DevOps task extension](https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task).
- Optional for VSCode users, configure intellisense for the task extension as per [Task Extension Intellisense](https://github.com/microsoft/azure-pipelines-vscode#specific-schema)

## Pulumi Task Extension for Azure Pipelines {#pulumi-task-extension}

Pulumi provides a task extension that lets you easily use Pulumi in your CI/CD pipelines. It can be used with the Azure Pipelines wizard UI or the YAML config.
The task handles installing the Pulumi CLI and running any commands without the need for any scripts.

> Pulumi Task Extension for Azure Pipelines can be used with [any cloud provider](#other-clouds) that Pulumi supports. You are not limited to using it only with Azure.

### Command Summary

Details regarding parameters and options supported by the extension can be found in the [Pulumi CLI](/docs/cli/) documentation.

| Parameter Name | Required? | Parameter Description |
|----|---|----|
| stack | Yes | Name of stack being managed. Can be of the form `ORG/STACK` or `ORG/PROJECT/STACK`. |
| azureSubscription | No | Optionally reference a service connection. If not used, environment variables can be configured with the credentials needed for the applicable Pulumi providers. |
| command | No | The applicable `pulumi` cli command (e.g. `preview`, `up`, `destroy`) |
| args | No | Option flags (e.g. `--yes`) that can be passed to the given `pulumi` command. Use space to separate multiple args. |
| cwd | No | The working directory to run the Pulumi commands. Use this if your Pulumi app is in a different directory. |
| versionSpec | No | The Pulumi version that should be used. Defaults to the latest version. If you require a specific version then the format is `1.5.0` or if you just need the latest version then `latest` can be used. |
| createStack | No | Set to `true` if the stack should be created if it does not already exist. Defaults to `false`. |
| createPrComment | No | Set to `true` to add a comment to your Pull Request (PR). Can only be used in pipelines driven by PRs. Defaults to `false`. See [Log Pulumi Output as PR Comments](#log-pulumi-output-as-pr-comments).
| useThreadedPrComments | No | Defaults to `true` to always add a comment to the previously-created comments thread. Set to `false` to have each comment added separately.

### Using the Pulumi Task Extension

Install the Pulumi task from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task) to your Azure DevOps organization.

The task requires the use of a service connection, which allows the pipeline to connect to your Azure Subscription. The task also looks for the build variable `pulumi.access.token`, and automatically maps it to the environment variable `PULUMI_ACCESS_TOKEN`, that is used by the CLI for non-interactive logins. You may still use the `env` directive to map any other environment variables you wish to make available to your Pulumi app.

You can obtain a [Pulumi access token](/docs/pulumi-cloud/accounts#access-tokens) from the Pulumi Cloud. Then use the task in your pipeline yaml.

```yaml
# Lines omitted for brevity.
...
...
  - task: Pulumi@1
    condition: or(eq(variables['Build.Reason'], 'PullRequest'), eq(variables['Build.Reason'], 'Manual'))
    inputs:
      azureSubscription: "My Service Connection"
      command: "preview"
      cwd: "infra/"
      stack: "acmeCorp/acmeProject/acme-ui"
...
...
```

### Log Pulumi Output as PR Comments {#log-pulumi-output-as-pr-comments}

> This feature is only supported for builds triggered by pull requests created in git repositories hosted by Azure DevOps. Repositories hosted by external VCS such as Bitbucket, GitHub, GitLab are not supported at this time.

The Pulumi task supports adding PR comments containing the log output from the Pulumi command that was executed in your build pipeline.
Your project's build service user will need additional permissions to perform that action. Follow these steps to grant the build service user the `Contribute to pull requests` permission:

- Navigate to the **Project Settings** page and select **Repositories** under the **Repos** heading.
- Select the repository where you will be using this feature and then select the **Security** tab.
- Now under the **Users** section find the build service user. If you are using the default build service user,
the naming convention is `<Project name> Build Service` where `<Project name>` is your project's name.
- Change the value of `Contribute to pull requests` to `Allow`.

### Using The Pulumi Task Extension With Other Clouds {#other-clouds}

To use the Pulumi Task Extension for Azure Pipelines with other clouds, you can specify the necessary environment variables
as build variables or link variable groups to your build and release pipelines.

For example, if you are using the [AWS provider](/registry/packages/aws/), you can set the [environment variables](/registry/packages/aws/installation-configuration/)
`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

## Using Pulumi in Azure DevOps Pipelines

More details on how to use Pulumi - with or without the [Task Extension](#pulumi-task-extension) - are provided below.

### Stack and Branch Mappings

> The names used below are purely for demonstration purposes only. You may choose a naming convention that best suits your organization.

The scripts below act on a hypothetical stack: `acmeCorp/acmeProject/acme-ui`.
`acme-ui` contains the infrastructure code or `pulumi` program. It also contains an Angular-based SPA.
The git repo for this look like this:

```
acme-ui
  src/
    app/
      components/
    index.html
  infra/
    index.ts
    Pulumi.yaml
    Pulumi.acme-ui.yaml
  azure-pipelines.yml
```

Once you login into the `pulumi` CLI on your machine, you can create a stack by running `pulumi stack init`.
To create a `pulumi` program using one of the many available templates, you may run `pulumi new <template>`.
You can find a suitable template to run, using the command `pulumi new --help`.
Learn more about the `pulumi` [CLI commands](/docs/cli/).

Once your stack has been initialized, the `Pulumi.<stack-name>.yaml` file will be created with some basic configuration.
The yaml file is used just for configuration values. All of your infrastructure will be built using your `pulumi` program.

For this walkthrough, we will assume a `TypeScript`-based `pulumi` program, which will deploy resources to an Azure Subscription.

#### About The `pulumi` Program

The code inside `infra/index.ts` creates a resource group, a storage account and a blob container in the storage account. It then `exports` three
values using the syntax `export const <variable_name> = <value>;`. Learn more about [stack outputs](/docs/concepts/stack#outputs).

### Build Variables

Build variables are an important aspect of any CI/CD pipeline. We will use some pre-defined [system build variables](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=vsts&tabs=yaml%2Cbatch#system-defined-variables) provided
by the Azure DevOps pipeline to decide whether or not we should run an update on our infrastructure.

> Build variable formats differ based on the agent in which your job is running. See [this](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=vsts&tabs=yaml%2Cbatch#set-in-script) to learn more about how
you can access a build variable correctly depending on your agent OS.

#### User-Defined Output Variables

You can set [job-scoped output variables](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=vsts&tabs=yaml%2Cbatch#set-a-job-scoped-variable-from-a-script) or [multi-job variables](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=vsts&tabs=yaml%2Cbatch#set-an-output-multi-job-variable). In this article, we demonstrate the use of multi-job variables with job dependencies, using the `dependsOn` job constraint.

#### Environment Variables

`pulumi` requires a few environment variables in order to work in a CI/CD environment. More specifically, `PULUMI_ACCESS_TOKEN` is required
to allow the `pulumi` CLI to perform an unattended login. In addition to this, you will also need to set the cloud provider-specific
variables. [Azure environment variables](/docs/clouds/azure/get-started/).

> If you are using the [Pulumi task extension](https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task) for Azure Pipelines, you don't need to manually configure the environment variables in your pipeline builds. You can use [Service Connections](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops) to centralize access to your Azure subscription(s).

### Agents

Azure DevOps allows you to specify a build agent for each of your jobs in your pipeline. You may have a requirement to run certain jobs on a
Ubuntu agent, and some on a Windows agent. If not using the task extension, `pulumi` can be installed on these agents by following the directions from [this](/docs/install/) page.

### Setup

For the YAML-driven DevOps pipeline, the repository must contain the `azure-pipelines.yml` in the root of the repo for Azure DevOps to use it automatically.
The following are samples only. You may choose to structure your configuration any way you like.

### Sample `azure-pipelines.yml`

```yaml
# Node.js with Angular
# Build a Node.js project that uses Angular.
# Add steps that analyze code, save build artifacts, deploy, and more:
# https://docs.microsoft.com/azure/devops/pipelines/languages/javascript

jobs:
- job: infrastructure
  pool:
    vmImage: 'ubuntu-20.04'
  steps:
  - task: Npm@1
    inputs:
      command: install
      workingDir: "infra/"
  - task: Pulumi@1
    condition: or(eq(variables['Build.Reason'], 'PullRequest'), eq(variables['Build.Reason'], 'Manual'))
    inputs:
      # Using a service connection is optional. Specify build variables for your pipeline or link variable groups
      # that contain the necessary environment variables needed by the Pulumi provider your Pulumi app uses.
      azureSubscription: 'My Service Connection'
      command: 'preview'
      cwd: 'infra/'
      stack: 'acmeCorp/acmeProject/acme-ui'
  - task: Pulumi@1
    condition: or(eq(variables['Build.Reason'], 'IndividualCI'), eq(variables['Build.Reason'], 'BatchedCI'))
    inputs:
      # Using a service connection is optional. Specify build variables for your pipeline or link variable groups
      # that contain the necessary environment variables needed by the Pulumi provider your Pulumi app uses.
      azureSubscription: 'My Service Connection'
      command: 'up'
      cwd: 'infra/'
      stack: 'acmeCorp/acmeProject/acme-ui'
      args: '--yes'
  - script: |
      RESOURCE_GROUP_NAME=$(pulumi stack output resourceGroupName)
      STORAGE_ACCOUNT_NAME=$(pulumi stack output storageAccountName)
      CONTAINER_NAME=$(pulumi stack output containerName)
      echo "##vso[task.setvariable variable=resourceGroupName;isOutput=true]$RESOURCE_GROUP_NAME"
      echo "##vso[task.setvariable variable=storageAccountName;isOutput=true]$STORAGE_ACCOUNT_NAME"
      echo "##vso[task.setvariable variable=containerName;isOutput=true]$CONTAINER_NAME"
    displayName: 'Set stack outputs as variables'
    name: 'pulumi'

# The following job is optional, and shown here for demonstration purposes only.
- job: build_and_deploy
  condition: ne(dependencies.infrastructure.outputs['pulumi.containerName'], '')
  dependsOn: infrastructure
  variables:
    resourceGroupName: $[ dependencies.infrastructure.outputs['pulumi.resourceGroupName'] ]
    storageAccountName: $[ dependencies.infrastructure.outputs['pulumi.storageAccountName'] ]
    containerName: $[ dependencies.infrastructure.outputs['pulumi.containerName'] ]
  steps:
  - task: NodeTool@0
    inputs:
      versionSpec: '16.x'
    displayName: 'Install Node.js'
  - task: Npm@1
    inputs:
      command: 'install'
  - script: |
      npm run build
    displayName: 'UI build'
  - task: AzurePowerShell@3
    displayName: 'Upload UI dist bundle to Storage Account'
    inputs:
      azureConnectionType: 'ConnectedServiceNameARM'
      azureSubscription: 'My Service Connection'
      scriptType: 'FilePath'
      # This script file is shown below in the next section.
      scriptPath: 'build-and-deploy.ps1'
      scriptArguments: '-resourceGroupName $(resourceGroupName) -storageAccountName $(storageAccountName) -containerName $(containerName) -isAzurePipelineBuild $true -skipBuild $true -localFolder $(Build.SourcesDirectory)/dist'
      errorActionPreference: 'stop'
      failOnStandardError: true
      azurePowerShellVersion: 'LatestVersion'
```

### Sample `build-and-deploy.ps1` (Optional)

This `PowerShell` script builds the UI app, and uploads the `dist/` folder to an Azure Storage blob container. You don't have to use a script like this. You can always use the built-in Azure DevOps task to accomplish the steps in this script. This script is just an example of how `pulumi` can be easily integrated into your existing app.

```powershell
Param(
  [string]$storageAccountName,
  [string]$containerName,
  [string]$resourceGroupName,
  [int] $maxAge = 86400,
  [int] $indexMaxAge = 3600,
  [boolean] $isProductionBuild = $false,
  [boolean] $skipBuild = $false,
  [boolean] $isAzurePipelineBuild = $false,
  # Upload files in the dist subfolder to Azure.
  [string] $localFolder = ".\dist"
)

function Get-MimeType() {
  param([parameter(Mandatory=$true, ValueFromPipeline=$true)][ValidateNotNullorEmpty()][System.IO.FileInfo]$CheckFile)
  begin {
      Add-Type -AssemblyName "System.Web"
      [System.IO.FileInfo]$check_file = $CheckFile
      [string]$mime_type = $null
  }
  process {
      if ($check_file.Exists) {
          $mime_type = [System.Web.MimeMapping]::GetMimeMapping($check_file.FullName)
      }
      else {
          $mime_type = "false"
      }
  }
  end {
    return $mime_type
  }
}

if ($false -eq $skipBuild) {
  npm ci

  if ($false -eq $isProductionBuild) {
    write-host "Building the UI for non-prod"
    npm run build
  } else {
    write-host "Building the UI for PROD"
    npm run build:prod
  }
  write-host "UI build completed"
  write-host "Launching Azure login pop-up.."
}

# The destination folder. BE SURE TO INCLUDE THE TRAILING SLASH IF YOU ENTER A NON-EMPTY VALUE HERE.
$destfolder = ""
$storageAccount = Get-AzureRmStorageAccount -ErrorAction Stop | where-object {$_.StorageAccountName -eq $storageAccountName}
If($storageAccount)
{
  $storageAccountKey = Get-AzureRmStorageAccountKey -ResourceGroupName $storageAccount.ResourceGroupName -StorageAccountName $storageAccountName
  $storageContext = New-AzureStorageContext -StorageAccountName $storageAccountName -StorageAccountKey $storageAccountKey[0].Value
  $storageContainer = Get-AzureStorageContainer -Context $storageContext -ErrorAction Stop | where-object {$_.Name -eq "$ContainerName"}

  Invoke-Expression -Command "ls $localFolder"
  $files = Get-ChildItem $localFolder  -File -Recurse
  foreach($file in $files)
  {
    $directoryName = $file.Directory.Name
    $filename = $file.Name
    if ($directoryName -ne "dist") {
      $blobName = $destfolder + $file.FullName.Substring($file.FullName.IndexOf("dist\") + 5)
    } else {
      $blobName = $destfolder + $filename
    }
    write-host "copying $directoryName\$filename to $blobName"
    if ($file.Name -like "*mp4*") {
      $mimeType = "video/mp4"
    } elseif ($file.Name -like "*webm*") {
      $mimeType = "video/webm"
    } else {
      $mimeType = $(Get-MimeType -CheckFile $file.FullName)
    }
    # For index.html, use the $indexMaxAge
    if ($file.Name -eq "index.html") {
      $maxAge = $indexMaxAge
    }
    $Properties = @{"CacheControl" = "max-age=$maxAge"; "ContentType" = $mimeType}
    Set-AzureStorageBlobContent -File $file.FullName -Container "$containerName" -Blob $blobName -Context $storageContext -Force -Properties $Properties
  }
  write-host "All files in $localFolder uploaded to $containerName!"
} else {
  Write-Warning "'$storageAccountName' storage account not found."
}
```

## Using Scripts (Manual Approach)

If you prefer to control the installation of the Pulumi CLI and how it runs your Pulumi app, you can use scripts in your pipeline builds. Below are some sample scripts to help you get started in order to install the CLI and run your Pulumi app.

The `run-pulumi.sh` script runs `pulumi preview` for PR builds and the `pulumi up --yes` command with explicit consent,
for master branches.

The following environment variables are set in the build pipeline using the Azure DevOps portal.

- `pulumi.access.token`
- `arm.client.id`
- `arm.client.secret`
- `arm.subscription.id`
- `arm.tenant.id`

The above variables are _mapped-in_ to the job using the `env:` directive as described in [Set secret variables](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=vsts&tabs=yaml%2Cbatch#secret-variables).

### `azure-pipelines.yml`

In your pipeline configuration, you need to then call these scripts when appropriate. Here's an example:

```yaml
...
...
  # Some lines omitted for brevity.
  - script: |
      chmod +x infra/scripts/*.sh
      ./infra/scripts/setup.sh
      ./infra/scripts/run-pulumi.sh
    displayName: 'Install pulumi and run infra code'
    name: pulumi
    env:
      PULUMI_ACCESS_TOKEN: $(pulumi.access.token)
      ARM_CLIENT_SECRET: $(arm.client.secret)
      ARM_SUBSCRIPTION_ID: $(arm.subscription.id)
      ARM_CLIENT_ID: $(arm.client.id)
      ARM_TENANT_ID: $(arm.tenant.id)
...
...
```

### Sample `setup.sh`

```bash
#!/bin/bash

# exit if a command returns a non-zero exit code and also print the commands and their args as they are executed
set -e -x
# Download and install required tools.
# pulumi
curl -fsSL https://get.pulumi.com/ | bash
export PATH=$PATH:$HOME/.pulumi/bin
# Login into pulumi. This will require the PULUMI_ACCESS_TOKEN environment variable
pulumi login
# update the GitLab Runner's packages
apt-get update -y
apt-get install sudo -y
# nodejs
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
apt-get install -y nodejs
# yarn
npm i -g yarn
```

### Sample `run-pulumi.sh`

```bash
#!/bin/bash

# exit if a command returns a non-zero exit code and also print the commands and their args as they are executed
set -e -x

# Add the pulumi CLI to the PATH
export PATH=$PATH:$HOME/.pulumi/bin

pushd infra/

npm install
npm run build

pulumi stack select acmeCorp/acmeProject/acme-ui

# https://docs.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=vsts
case $BUILD_REASON in
  PullRequest)
      pulumi preview
    ;;
  BuildCompletion|BatchedCI)
      pulumi up --yes
    ;;
  *)
esac

# Save the stack output variables to job variables.
# Note: Before the `pulumi up` is run for the first time, there are no stack output variables.
# The pulumi program exports three values: resourceGroupName, storageAccountName and containerName.
echo "##vso[task.setvariable variable=resourceGroupName;isOutput=true]$(pulumi stack output resourceGroupName)"
echo "##vso[task.setvariable variable=storageAccountName;isOutput=true]$(pulumi stack output storageAccountName)"
echo "##vso[task.setvariable variable=containerName;isOutput=true]$(pulumi stack output containerName)"

popd
```
