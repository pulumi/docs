---
title: "Building a Development Environment for Cloud Engineering"
date: 2021-02-03
meta_desc: "A complete guide to preparing your development environment for building infrastructure with code."
meta_image: anti-patterns.png
authors:
    - sophia-parafina
tags:
    - Development Environment
    - Cloud Engineering
---

Starting can be daunting. Before you take your first step, there's a lot to consider, but you can prepare your development environment ahead of time to make your first steps in cloud engineering smooth and productive.  In this article, we'll cover how to set up your development environment to work across cloud providers, multiple languages, and different operating systems.

<!--more-->

## Building your toolbox

You might have heard of the French culinary term "mise-en-place," which means laying out all the ingredients and cookware before starting to cook. That's what we're going to do here; layout all the accounts, authorizations, and software that you need to be a successful cloud engineer. We are going to need the following:

- **A package manager:** Every operating system has a package manager for installing software. Unlike binary installers, a package manager lets you manage all software packages, including updates. Package managers can help resolve dependencies, saving you from frustration.
- **Cloud provider accounts:** You can choose to set up one or multiple accounts. The important thing is how to configure credentials in your development environment,
- **Programming languages:** You can choose one or many, but they all have different versions and dependencies.
- **Code editor:** This is personal preference but make sure that it can perform code completion, error checking, and use enums. These features can be the difference between hitting `Tab` and searching through online documentation for a function.
- **Pulumi:** You can install Pulumi with a package manager and configure

## Decisions

Before proceeding, you need to answer three questions:

- Which operating system to use for building cloud resources: macOS, Windows, or Linux?
- Which cloud provider are you using? This guide covers AWS, Azure, and Google Cloud.
- Which programming language will you use? Pulumi supports Node.js (JavaScript and Typescript), Python 3.6 or higher, Golang, and .NET (C#, F#, and VB).

Once you've made these choices, you can follow this guide in a choose-your-own-adventure style.

## Package manager

Let's start with the package manager. We'll use it to install and manage all the software we need, including cloud provider CLIs, programming languages, editors, and Pulumi. Choose your operating system below.

{{< chooser os "macos,windows,linux" >}}
{{% choosable os macos %}}
[Homebrew](https://docs.brew.sh/Installation) is the most popular package manager for macOS. The Command Line Tools (CLT) for XCode is required to install and build Homebrew. Install the XCode Tools first, then install Homebrew from the command line.

```bash
$ xcode-select --install
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

If you are uncomfortable with downloading and running an online shell script (with good reason), Homebrew provides an [alternate installation method](https://docs.brew.sh/Installation#alternative-installs).
{{% /choosable %}}

{{% choosable os windows %}}
[Chocolatey](https://chocolatey.org/) is a popular package manager for Windows. It should be installed using an [administrative shell](https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/).

Make sure that [`Get-ExecutionPolicy`](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.1) is not restricted.

```cmd
> Get-ExecutionPolicy
```

If the command returns `Restricted`, we can use `Bypass` to install Chocolatey with the following command:

```
> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

To check if it's installed type:

```cmd
> choco
```

{{% /choosable %}}
{{% choosable os linux %}}

Linux distributions include a package manager, [apt](https://wiki.debian.org/Apt) for Debian based distributions or  [yum](https://www.redhat.com/sysadmin/how-manage-packages) for Red Hat-based Linux systems. However, they are primarily used for application and system management.

[Homebrew](https://docs.brew.sh/Homebrew-on-Linux) is a popular package manager for utilities, Software Development Kits, and programming tools.  Install Homebrew from the command line.

```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

To add Homebrew to your `PATH` and your bash shell profile script (`~/.profile` on Debian or `~/.bash_profile` on Red Hat), follow the `Next steps` instructions to install and configure brew. To check if it's installed, install a package;

```bash
$ brew install hello
```

{{% /choosable %}}
{{< /chooser >}}

## Setting up a cloud account

The first task is signing up for an account. Once you have that out of the way, the next steps are installing the CLI and configuring your credentials.

### macOS

{{< chooser cloud "aws,azure,gcp" >}}
{{% choosable cloud aws %}}
We'll use brew to install AWS CLI version 2 and verify if it's installed by checking the version.

```bash
$ brew update && brew install awscli
$ aws --version
```

The next step is to create and download your AWS access keys and configure your environment to make them available to both the AWS CLI. To create your access keys, follow these directions for [programmatic access](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys).

{{% notes type="info" %}}
Pulumi uses the AWS SDK to authenticate requests. Your AWS access keys are never sent to pulumi.com.
{{% /notes %}}

To configure the AWS CLI with your credentials, use `aws configure`:

```bash
$ aws configure
AWS Access Key ID [None]: <YOUR_ACCESS_KEY_ID>
AWS Secret Access Key [None]: <YOUR_SECRET_ACCESS_KEY>
Default region name [None]:
Default output format [None]:
```

This creates a `~/.aws/credentials` file used by the AWS CLI to authenticate requests.
{{% /choosable %}}

{{% choosable cloud azure %}}
We'll use brew to install Azure CLI and check if it's installed.

```bash
$ brew update && brew install azure-cli
$ az --version

To log into Azure, run the `login` command, which opens a browser to log into [Azure](https://login.microsoftonline.com/common/oauth2/authorize).

```bash
$ az login
The default web browser has been opened at https://login.microsoftonline.com/common/oauth2/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
You have logged in. Now let us find all the subscriptions to which you have access...
```

The Azure client is authenticated and ready to use.

{{% notes type="info" %}}
Pulumi uses the Azure SDK to authenticate requests. Your AWS access keys are never sent to pulumi.com.
{{% /notes %}}

{{% /choosable %}}
{{% choosable cloud gcp %}}
We'll use brew to install the Google Cloud SDK and CLI.

```bash
$ brew update && brew install --cask google-cloud-sdk
Update done!
==> Source [/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/completion.bash.inc] in your profile to enable shell command completion for gcloud.
==> Source [/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/path.bash.inc] in your profile to add the Google Cloud SDK command line tools to your $PATH.
```

Add the gcloud SDK to $PATH in you ~/.bash_profile

```bash
source /usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/completion.bash.inc
source /usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/path.bash.inc
```

Open a new shell or source `~/.profile` for Debian or `~/.bash_profile` for Red Hat and check to see if it's installed and pathed.

```bash
$ source ~/.bash_profile
$ gcloud version
Google Cloud SDK 325.0.0
bq 2.0.64
core 2021.01.22
gsutil 4.58
```

Authenticate using the gcloud CLI.

```bash
gcloud init
```

{{% notes type="info" %}}
Pulumi uses the Google Cloud SDK to authenticate requests. Your AWS access keys are never sent to pulumi.com.
{{% /notes %}}
{{% /choosable %}}
{{< /chooser >}}

### Windows

{{< chooser cloud "aws,azure,gcp" >}}

{{% choosable cloud aws %}}
We'll use chocolatey to install AWS CLI version 2 and check if it's installed. Open a `cmd` Command Prompt as Administrator:

```cmd
> choco install awscli
> aws --version
```

The install adds the AWS CLI client to the `$PATH`, so either open a new `cmd` window or use the `refreshenv` command to update the window's environment variables and use the AWS CLI.

The next step is to create and download your AWS access keys and configure your environment to make them available to both the AWS CLI. To create your access keys, follow these directions for [programmatic access](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys).

{{% notes type="info" %}}
Pulumi uses the AWS SDK to authenticate requests. Your AWS access keys are never sent to pulumi.com.
{{% /notes %}}

To configure the AWS CLI with your credentials, use `aws configure`:

```cmd
> aws configure
AWS Access Key ID [None]: <YOUR_ACCESS_KEY_ID>
AWS Secret Access Key [None]: <YOUR_SECRET_ACCESS_KEY>
Default region name [None]:
Default output format [None]:
```

This will create the `~/.aws/credentials` file used by the AWS CLI to authenticate requests.
{{% /choosable %}}

{{% choosable cloud azure %}}
We'll use chocolatey to install Azure CLI and check if it's installed. Open a `cmd` Command Prompt as Administrator:

```cmd
> choco install azure-cli
```

The Azure CLI client was added to the path, so either open a new `cmd` window or use the `refreshenv` command to update the window's environment variables. To log into Azure, run the `login` command, which opens a browser to log into [Azure](https://login.microsoftonline.com/common/oauth2/authorize).

```cmd
> refreshenv
> az login
```

The Azure client will open a browser window and prompt you to sign-in to your account. Once signed-in, the Azure CLI is authenticated and ready to use.

{{% notes type="info" %}}
Pulumi uses the Azure SDK to authenticate requests. Your AWS access keys are never sent to pulumi.com.
{{% /notes %}}

{{% /choosable %}}

{{% choosable cloud gcp %}}
We'll use chocolatey to install the Google Cloud SDK and CLI.

```cmd
> choco install gcloudsdk --ignore-checksums
```

The `gcloud` CLI was added to the path, so either open a new `cmd` window or use the `refreshenv` command to update the window's environment variables. Check to see if `gcloud` CLI is installed and pathed correctly.

```cmd
> refreshenv
> gcloud version
Google Cloud SDK 325.0.0
bq 2.0.64
core 2021.01.22
gsutil 4.58
```

Authenticate using the gcloud CLI

```cmd
> gcloud init
Welcome! This command will take you through the configuration of gcloud.

Your current configuration has been set to: [default]

You can skip diagnostics next time by using the following flag:
  gcloud init --skip-diagnostics

Network diagnostic detects and fixes local network connection issues.
Checking network connection...done.
Reachability Check passed.
Network diagnostic passed (1/1 checks passed).

You must log in to continue. Would you like to log in (Y/n)?  Y

Your browser has been opened to visit:
   https://accounts.google.com/o/oauth2/...
```

A browser window will open to authenticate your client.

{{% notes type="info" %}}
Pulumi uses the Google Cloud SDK to authenticate requests. Your AWS access keys are never sent to pulumi.com.
{{% /notes %}}

{{% /choosable %}}
{{< /chooser >}}

### Linux

{{< chooser cloud "aws,azure,gcp" >}}
{{% choosable cloud aws %}}
We'll use brew to install AWS CLI version 2 and check if it's installed.

```bash
$ brew update && brew install awscli
$ aws --version
```

The next step is to create and download your AWS access keys and configure your environment to make them available to both the AWS CLI. To create your access keys, follow these directions for [programmatic access](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys).

{{% notes type="info" %}}
Pulumi uses the AWS SDK to authenticate requests. Your AWS access keys are never sent to pulumi.com.
{{% /notes %}}

To configure the AWS CLI with your credentials, use `aws configure`:

```bash
$ aws configure
AWS Access Key ID [None]: <YOUR_ACCESS_KEY_ID>
AWS Secret Access Key [None]: <YOUR_SECRET_ACCESS_KEY>
Default region name [None]:
Default output format [None]:
```

This will create the `~/.aws/credentials` file used by the AWS CLI to authenticate requests.

{{% /choosable %}}

{{% choosable cloud azure %}}
We'll use brew to install Azure CLI and check if it's installed.

```bash
$ brew update && brew install azure-cli
$ az --version

To log into Azure, run the `login` command, which opens a browser to log into [Azure](https://login.microsoftonline.com/common/oauth2/authorize).

```bash
$ az login
The default web browser has been opened at https://login.microsoftonline.com/common/oauth2/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
You have logged in. Now let us find all the subscriptions to which you have access...
```

The Azure client is authenticated and ready to use.

{{% notes type="info" %}}
Pulumi uses the Azure SDK to authenticate requests. Your AWS access keys are never sent to pulumi.com.
{{% /notes %}}

{{% /choosable %}}
{{% choosable cloud gcp %}}
We'll use brew to install the Google Cloud SDK and CLI.

```bash
$ brew update && brew install --cask google-cloud-sdk

Update done!

==> Source [/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/completion.bash.inc] in your profile to enable shell command completion for gcloud.
==> Source [/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/path.bash.inc] in your profile to add the Google Cloud SDK command line tools to your $PATH.
```

Add the gcloud SDK to $PATH to your `~/.bash_profile` or `~/.profile`.

```bash
source /usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/completion.bash.inc
source /usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/path.bash.inc
```

Open a new shell or source `~/.profile` for Debian or `~/.bash_profile` for Red Hat and check to see if it's installed and pathed.

```bash
$ source ~/.bash_profile
$ gcloud version
Google Cloud SDK 325.0.0
bq 2.0.64
core 2021.01.22
gsutil 4.58
```

Authenticate using the gcloud CLI

```bash
gcloud init
```

{{% notes type="info" %}}
Pulumi uses the Google Cloud SDK to authenticate requests. Your AWS access keys are never sent to pulumi.com.
{{% /notes %}}

{{% /choosable %}}
{{< /chooser >}}

## Choose a Programming Language

Pulumi supports Node.js (JavaScript and Typescript), Python 3, Golang, and .NET Core (C#, VB, and F#) languages.

### Node.js

{{< chooser os "macos,windows,linux" >}}
{{% choosable os macos %}}
Use brew to install Node.js for JavaScript and Typescript.

```bash
$ brew install node
```

{{% /choosable %}}

{{% choosable os windows %}}
Use chocolatey to install Node.js for JavaScript and Typescript.

```cmd
> choco install nodejs
```

{{% /choosable %}}

{{% choosable os linux %}}
Use brew to install Node.js for JavaScript and Typescript.

```bash
$ brew install node
```

{{% /choosable %}}
{{< /chooser >}}

### Python

{{< chooser os "macos,windows,linux" >}}
{{% choosable os macos %}}
MacOS includes Python; however, versions shipped before December 2019 have Python 2.7 installed, which is deprecated. Pulumi requires Python 3.6 or higher. Use brew to install Python, which installs it at `/usr/bin/local/python3`.

```bash
$ brew install python
```

In macOS versions with Python 2 installed, calling `python` uses the 2.7 binary. To ensure that you will always use Python 3, you can add an alias to your `.bash_profile`.

```bash
alias python=/usr/local/bin/python3
```

It is a best practice to create a virtual environment and activate it for a Python project. Pulumi creates a new `venv` environment when you start a new Project with `pulumi new`.

{{% /choosable %}}

{{% choosable os windows %}}
You can install Python in several ways, including typing 'python` in the command prompt, which brings up the Microsoft Store application. In this article, we'll continue using chocolatey to install Python 3.

```cmd
> choco install python --pre
```

It is a best practice to create a virtual environment and activate it for a Python project. Pulumi creates a new `venv` environment when you start a new Project with `pulumi new`.

{{% /choosable %}}
{{% choosable os linux %}}
Use brew to install Python3.

```bash
$ brew install python
```

Use `python3` to call Python, but you can add an alias to your `.bash_profile` or `.profile` to use just `python` to run scripts.

```bash
alias python=/usr/local/bin/python3
```

It is a best practice to create a virtual environment and activate it for a Python project. Pulumi creates a new `venv` environment when you start a new Project with `pulumi new`.
{{% /choosable %}}
{{% /chooser %}}

### Golang

{{< chooser os "macos,windows,linux" >}}
{{% choosable os macos %}}
Use brew to install golang.

```bash
$ brew install golang
```

It is a best practice to create a local programming environment and set `GOPATH` as an environment variable, although it is not required for golang versions after 1.8. Pulumi creates a new local environment and `go.mod` to work with modules each time you start a new Project with `pulumi new`.

{{% /choosable %}}
{{% choosable os windows %}}
Use chocolatey to install golang.

```cmd
> choco install golang
```

It is a best practice to create a local programming environment and set `GOPATH` as an environment variable, although it is not required for golang versions after 1.16. Pulumi creates a new local environment and `go.mod` to work with modules each time you start a new Project with `pulumi new`.

{{% /choosable %}}
{{% choosable os linux %}}
Use brew to install golang.

```bash
$ brew install golang
```

It is a best practice to create a local programming environment and set `GOPATH` as an environment variable, although it is not required for golang versions after 1.8. Pulumi creates a new local environment and `go.mod` to work with modules each time you start a new Project with `pulumi new`.

{{% /choosable %}}
{{% /chooser %}}

### .NET

{{< chooser os "macos,windows,linux" >}}
{{% choosable os macos %}}
Install .NET with brew, Pulumi requires .NET Core 3.1 or higher.

```bash
$ brew install dotnet
```

{{% /choosable %}}
{{% choosable os windows %}}
Install .NET with chocolatey. Pulumi requires .NET Core 3.1 or higher.

```cmd
> choco install dotnet-sdk
```

{{% /choosable %}}
{{% choosable os linux %}}
Install .NET with brew, Pulumi requires .NET Core 3.1 or higher.

```bash
$ brew install dotnet
```

{{% /choosable %}}
{{< /chooser >}}

## Get a code editor

While knowing how to use vim or similar text editors is a worthwhile skill, you should use a modern code editor. Here's a non-exhaustive list why you should use a code editor.

- Quickly navigating to a type
- Autocompletion when you can't remember the names of all members by heart
- Automatic code generation
- Refactoring
- Organise imports
- Warnings as you type.
- Hovering over something to see the docs
- Keeping a view of files, errors/warnings/console/unit-tests and source code  on the screen
- Running unit tests from the same window
- Integrated debugging
- Integrated source control
- Navigating to where a compile-time error or run-time exception occurred directly from the error details.

You can use an IDE (Integrated Development Environment) such as [Microsoft Visual Studio](https://visualstudio.microsoft.com/), [Xcode](https://developer.apple.com/xcode/), or any one of [JetBrains' language-specific IDEs](https://www.jetbrains.com/products/#type=ide). Alternatively, you can use a lightweight solution with many of the features of an IDE. Popular code editors include [Visual Studio Code](https://code.visualstudio.com/), [Sublime Text](https://www.sublimetext.com/), and [Atom](https://atom.io/).

You can install some editors with brew.

```bash
$ brew install --cask visual-studio-code
$ brew install --cask sublime-text
$ brew install --cask atom
$ brew install --cask pycharm-ce
$ brew install --cask goland
```

## Install Pulumi

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

macOS Sierra (10.12) or later is required.

### Homebrew

You can install Pulumi through the [Homebrew package manager](https://brew.sh/):

```bash
$ brew install pulumi
```

This will install the `pulumi` CLI to the usual place (often `/usr/local/bin/pulumi`) and add it to your path.

Subsequent updates can be installed in the usual way:

```bash
$ brew upgrade pulumi
```

{{% /choosable %}}

{{% choosable os linux %}}

### Installation Script

To install, run our installation script:

```bash
$ curl -fsSL https://get.pulumi.com | sh
```

This will install the `pulumi` CLI to `~/.pulumi/bin` and add it to your path. When it can't automatically add `pulumi` to your path, you will be prompted to add it manually.
See [How to permanently set $PATH on Unix](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix) for guidance.

{{% /choosable %}}

{{% choosable os windows %}}

Windows 8 and 10 are supported.

### Chocolatey

You can install Pulumi using elevated permissions through the [Chocolatey package manager](https://chocolatey.org):

```powershell
> choco install pulumi
```

This will install the `pulumi` CLI to the usual place (often `$($env:ChocolateyInstall)\lib\pulumi`) and generate the [shims](https://docs.chocolatey.org/en-us/features/shim) (usually `$($env:ChocolateyInstall)\bin`) to add Pulumi your path.

Subsequent updates can be installed in the usual way:

```powershell
> choco upgrade pulumi
```

{{% /choosable %}}

{{< /chooser >}}

## Verifying your Installation

After installing Pulumi, verify everything is in working order by running the `pulumi` CLI:

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

```bash
$ pulumi version
v{{< latest-version >}}
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
$ pulumi version
v{{< latest-version >}}
```

{{% /choosable %}}

{{% choosable os windows %}}

```bash
> pulumi version
v{{< latest-version >}}
```

{{% /choosable %}}

{{< /chooser >}}

## Next steps

Congratulations! You have a fully configured environment, and you're ready to jump into cloud engineering. You can maintain your development environment using the package manager to add or update your toolset. Your code editor provides a modern development platform that takes advantage of all the advances in software engineering. Your coding experience will be more productive and less frustrating.

What are the next steps? Begin with Pulumi's [Getting Started]({{< relref "/docs/get-started" >}}). You can skip the configuration sections and jump straight into your [first project]({{< relref "/docs/get-started/aws/create-project" >}}). Once you're done with your first project, try out example projects on [Github](https://github.com/pulumi/examples). You can start with simple projects using the `pulumi` CLI, such as deploying a web server on AWS with python.

```bash
$ pulumi new https://github.com/pulumi/examples/tree/master/aws-py-webserver
```

This command will download the project from Github, create a virtual environment and activate it, and download all the python package dependencies. You're ready to go and deploy with `pulumi up`. Want more? How about deploying Kubernetes on Azure with python?

```bash
$ pulumi new https://github.com/pulumi/examples/tree/master/azure-py-aks
```

You can use the examples as a starting point for building your cloud infrastructure and add resources documented on Pulumi's [API reference]({{< relref "/registry" >}}) and [Guides]({{< relref "/docs/guides" >}}).
