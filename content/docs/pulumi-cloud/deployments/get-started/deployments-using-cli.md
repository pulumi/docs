---
title: Use Pulumi Deployments with the Pulumi and GitHub CLIs
title_tag: Use Pulumi Deployments with the Pulumi and GitHub CLIs
meta_desc: Learn how to use Pulumi Deployments the Pulumi and GitHub CLIs
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Pulumi and GitHub CLIs
    parent: pulumi-cloud-deployments-get-started
    weight: 1
    identifier: pulumi-cloud-deployments-get-started-cli
---

## Creating a new project manually

This walk-through shows you how to create a new project using `pulumi new`, upload to GitHub using the `gh` CLI, and then configure Pulumi Deployments.

### Prerequisites

Before you start, see the GitHub app [installation instructions](/docs/pulumi-cloud/deployments/reference/#github-app-installation) to configure your Pulumi organization to work seamlessly with Deployments.

You will need the following tools to complete this tutorial:

* The [Pulumi CLI](/docs/install/)
* The [GitHub CLI](https://cli.github.com/)

Let's get started!

### Create project and upload to a new GitHub repository

* Create a project by running `pulumi new`.  If you do not specify the template and configuration, you will be prompted.
Here we are selecting the `aws-typescript` template and accepting the defaults for project name and description, as well as stack name.

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

* Initialize the local git repository:

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

Now that we have a GitHub repository, we can configure it to use Pulumi Deployments.

* Navigate to your stack in Pulumi Cloud.  It should be at `https://app.pulumi.com/<your_organization>/test_deployments/dev` if you accepted the defaults.  Replace `<your_organization>` with your Pulumi organization name.

{{< notes type="info" >}}
Alternatively, you can navigate to `https://app.pulumi.com`, select `Stacks` in the left navigation, and click on your project/stack in the list.
{{< /notes >}}

* Click on `Settings` and then `Deploy` on the left.

![Navigation to settings](../../ui-deployment-settings-nav.gif)

* You should see settings like this:

![Deployment Settings](../../ui-settings.png)

* Fill out the `Source control settings`

  * Select `GitHub` as Source Control
  * Select your `test_deployment` repository we created earlier.
  * Select the `main` branch
  * Leave the `Pulumi.yaml folder` blank, we put our project in the root folder.

![Github Repo](../../ui-github-repo.gif)

* Now configure settings specific to your Deployment, such as:
  * [OIDC Connect](/docs/pulumi-cloud/oidc/)
  * [Environment Variables](/docs/pulumi-cloud/deployments/reference/#environment-variables)

See [Pulumi Deployment Settings](/docs/pulumi-cloud/deployments/using/settings) for more information about all of the available settings.

Finally, click the `Save deployment configuration` button to save our settings, and click the "Deploy" button in the top right to trigger a deployment.

![Deploy Button](../../ui-deploy-button.gif)
