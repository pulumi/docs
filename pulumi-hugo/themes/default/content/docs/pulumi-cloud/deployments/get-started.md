---
title: Get started
title_tag: Get started with Pulumi Deployments
meta_desc: Here is a placeholder meta description of between 50 and 150 characters.
menu:
  pulumicloud:
    parent: deployments
    weight: 1
---

## Prerequisites

Before you start, see the GitHub app [installation instructions](/docs/pulumi-cloud/deployments/reference/#github-app-installation) to configure your Pulumi organization to work seamlessly with Deployments.

## New Project Wizard

It's possible to create a new Pulumi project, commit its code, and deploy it entirely from within your browser by using Deployments in combination with the New Project Wizard.

Navigate to the "New Project" tab.
Select "Use a template" if you'd like to create a fully featured project, or select "Use a starter" if you want to create a bare-bones project with only the minimal necessary boilerplate.

In order to use templates you will need to authorize Pulumi with GitHub so that it can clone private repositories as template sources and commit new code for your projects.
Click the button and accept the required permissions if you would like to use templates.

{{% notes "info" %}}
If you select "Use a template" and your Pulumi administrator has configured [custom templates](/docs/pulumi-cloud/developer-portals/templates) for your organization, you will be able to choose from your organization's custom templates in a later step.
If you select "Use a template" but your organization doesn't have custom templates, you'll be able to choose one of Pulumi's public templates.
{{% /notes %}}

On the next screen, select "Pulumi Deployments" as your deployment method.

{{% notes "info" %}}
You may need to [install the Pulumi GitHub app](/docs/pulumi-cloud/deployments/reference/#github-app-installation) if you haven't already.
{{% /notes %}}

You'll now to prompted to enter some information about the project you're about to create.

### Project details

Provide a name for the project you're about to create, along with an optional description and a stack name to include.

This impacts the resulting `Pulumi.yaml` file, and the name of `Pulumi.<stack>.yaml`.

### Configuration

This section allows you to provide values for any necessary configuration, if you're using a [template](/docs/pulumi-cloud/developer-portals/templates) that declares required configuration keys.

This impacts the `config` stanza in `Pulumi.<stack>.yaml`.

### Environment

If you've configured [environments](/docs/pulumi-cloud/esc) with your organization you can specify one to use with the resulting stack.

This enables the resulting stack to use a bundle of pre-configured secrets and configuration values without needing to re-specify all of them during project creation.

### Repository details

Here you can configure the repository and optional subdirectory to use when committing your new project code.

{{% notes "info" %}}
If you granted the Pulumi GitHub app access to _all_ repostories, the New Project Wizard will allow users to create projects with Deployments enabled in new repositories.

If the app only has access to _some_ repositories, users will only be able to create new projects with Deployments enabled in _existing_ repositories.
{{% /notes %}}

The GitHub owner is not configurable, as that must match the Pulumi GitHub app's owner in order to work with Deployments.

### Deployment settings

After you've configured your project settings you will be able to configure the behavior of Deployments, including when to trigger new Deployments and environment variables to include with your updates.

A full description of each setting is available [here](/docs/pulumi-cloud/deployments/reference/#deployment-settings).

After you've configured everything you should see a new Deployment of your project.

In summary, after going through this wizard you will have:

* A new Pulumi project and stack, created from a project template or starter.
* Code committed and pushed into a new or existing GitHub repository.
* Pulumi Deployments configured on your new stack, and a preview Deployment in progress.

## Creating a new project manually

This walkthrough shows you how to create a new project using `pulumi new`, upload to GitHub using the `gh` cli, and then configure Pulumi Deployments.

### Prerequisites

Before you start, see the GitHub app [installation instructions](/docs/pulumi-cloud/deployments/reference/#github-app-installation) to configure your Pulumi organization to work seamlessly with Deployments.

You will need the following tools to complete this tutorial:

* The [Pulumi CLI](/docs/install/)
* The [GitHub CLI](https://cli.github.com/)

Let's get started!

### Create project and upload to a new GitHub repository

* *Create project with `pulumi new`.  If you do not specify the template and configuration, you will be prompted.  Here we are selecting the `aws-typescript` when presented with a list of options and accepting the defaults for project name and description, as well as stack name.

```bash
$ mkdir test_deployments
$ cd test_deployments
$ pulumi new
Please choose a template (34/221 shown):
 aws-typescript                     A minimal AWS TypeScript Pulumi program
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name (test_deployments):
project description (A minimal AWS TypeScript Pulumi program):
Created project 'test_deployments'

Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name (dev):
Created stack 'dev'

aws:region: The AWS region to deploy into (us-east-1):
Saved config

Installing dependencies...


added 219 packages, and audited 220 packages in 5s

68 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
Finished installing dependencies

Your new project is ready to go!

To perform an initial deployment, run `pulumi up`
```

* Init the local git repository

```bash
$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
Initialized empty Git repository in /home/cleve/code/test_deployments/.git/

$ git branch -M main

$ git add .

$ git commit -m "first commit"
[main (root-commit) 5b22a59] first commit
 7 files changed, 2454 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 Pulumi.dev.yaml
 create mode 100644 Pulumi.yaml
 create mode 100644 index.ts
 create mode 100644 package-lock.json
 create mode 100644 package.json
 create mode 100644 tsconfig.json
```

This will create a stack for you under your default Pulumi organization in the Pulumi Cloud.

* Create a new GitHub repository and push the local code.  Replace `<github_owner>` with your own GitHub owner.

```bash
$ gh repo create <github_owner>/test_deployments --private --source=. --push
✓ Created repository <github_owner>/test_deployments on GitHub
✓ Added remote https://github.com/<github_owner>/test_deployments.git
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 20 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (9/9), 25.15 KiB | 12.58 MiB/s, done.
Total 9 (delta 0), reused 0 (delta 0), pack-reused 0
To ssh://github.com/<github_owner>/test_deployments.git
 * [new branch]      HEAD -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
✓ Pushed commits to https://github.com/<github_owner>/test_deployments.git
```

### Configure deployment settings

Now that we have a GitHub repository, we can configure out Pulumi Deployment.

* Navigate to your stack in Pulumi Cloud.  It should be at `https://app.pulumi.com/<your_organization>/test_deployments/dev` if you accepted the defaults.  Replace `<your_organization>` with your Pulumi organization name.

{{< notes type="info" >}}
Alternatively, you can navigate to `https://app.pulumi.com`, select `Stacks` in the left navigation, and click on your project/stack in the list.
{{< /notes >}}

* Click on `Settings` and then `Deploy` on the left.

![Navigation to settings](../ui-deployment-settings-nav.gif)

* You should see settings like this:

![Deployment Settings](../ui-settings.png)

* Fill out the `Source control settings`

    * Select `GitHub` as Source Control
    * Select your `test_deployment` repository we created earlier.
    * Select the `main` branch
    * Leave the `Pulumi.yaml folder` blank, we put our project in the root folder.

![Github Repo](../ui-github-repo.gif)

* Now configure settings specific to your Deployment, such as:

    * [OIDC Connect](/docs/pulumi-cloud/deployments/oidc/)
    * [Environment Variables](/docs/pulumi-cloud/deployments/reference/#environment-variables)

Go to [Using Deployments](/docs/pulumi-cloud/deployments/reference/) for more information

* Click the `Save deployment configuration` button

* Click the Deploy button in the top right to deploy.

![Deploy Button](../ui-deploy-button.gif)
