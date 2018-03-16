---
title: "--Using the Pulumi Console"
---

The Pulumi Console provides a web-based management experience for Pulumi. Visit [https://beta.pulumi.com](https://beta.pulumi.com).

> The Pulumi Console is a work in progress. We will be adding many new features over the coming weeks. Your feedback is an important part of making it the console the most friendly, intuitive, and useful management tool you've ever used. We want to hear from you!

## Logging in {#login-to-console}

Pulumi uses GitHub for authentication, so you must login with a GitHub account. You must also be a member of an organization that is enrolled in the Pulumi Console private beta.

### OAuth scopes

Pulumi requests several GitHub OAuth scopes, as illustrated in the following screenshot. 

![oauth-scopes](/images/docs-console/02-oauth.png){:width="500px"}

Here's what we ask for and why:

> Personal user data
> - Email addresses (read-only)
> - This application will be able to read your private email addresses.

We only use your email address for important service-related communication. We dislike marketing email just as much as you do!

> Repositories
> - Public and private
> - This application will be able to read and write all public and private repository data.

We use your GitHub repository information to link Pulumi program updates back to your GitHub repository. This allows the console to display Travis build results, git tags, and so on.

The Pulumi service **never** writes data to GitHub, but unfortunately, GitHub does not offer [a read-only scope for repository access](https://developer.github.com/apps/building-integrations/setting-up-and-registering-oauth-apps/about-scopes-for-oauth-apps/). 

> Organizations and teams
> - Read-only access
> - This application will be able to read your organization and team membership.

This read-only permission means that Pulumi can see which organizations you are a member of. Your organization membership is only used to determine which stacks you have access to.

### Pulumi account {#account-page}

After you have logged in, you can access your Pulumi Account by clicking the avatar photo on the
top right.

![accounts-page](/images/docs-console/03-account-page.png){:width="700px"}

Pulumi picks up profile information from GitHub, such as name and profile photo. If you've changed any information on GitHub, click **sync profile with GitHub** to have that information reflected in the Pulumi Console.

There are two key elements on this page: the Pulumi access token and the organization list.

#### Pulumi access token {#access-token}

To authenticate with Pulumi from the `pulumi` CLI, use your _Pulumi access token_. Enter it at the prompt to `pulumi login`. Keep this secret like you would any other access token.

```bash
$ pulumi login
Logging into Pulumi Cloud: https://api.pulumi.com
Enter your Pulumi access token: w3lc0m370pulum1cl0ud=
```

> The Pulumi access token is associated with your GitHub username and is the same across all your organizations.

#### Organization list

The organization list is mirrored from GitHub, just like your profile information. The link **Review or add** will take you to the GitHub Applications page for your connection to Pulumi, where you can review the organizations that have been authorized by GitHub. If make any changes, select **sync profile with GitHub**.

## Organizations

The Pulumi Console organizes stacks by *organizations*. An organization is either a GitHub user account or a GitHub organization. Currently, Pulumi organizations always map directly to GitHub organizations.

![organizations-page](/images/docs-console/04-orgs-list.png){:width="700px"}

### Repositories, projects, and stacks

Pulumi programs are organized within the following hierarchy:

* **Repositories** - These generally map to GitHub repositories. In fact, if
  if you create a Pulumi repository with the same name as an existing GitHub
  repository, we put a link to GitHub in the UI. The repository for a stack
  is set when you run `pulumi init`.
* **Projects** - Within a repository there can be many _Pulumi Projects_.
  A project _is_ the `Pulumi.yaml` file.
* **Stack** - Stacks are instances of a project, e.g. with cloud resources.
  The stack name is set via `pulumi stack init`.

When you run through the typical Pulumi workflow on your local machine, the
repository, project, and stack are identified as follows:

```bash
pulumi init
pulumi stack init steve-test

pulumi preview
pulumi update
```

The repository is set during `pulumi init`. If you are within a Git repository,
`pulumi` will infer the repository and organization from the Git remote. You
can override this behavior by using the `--owner` and `--name` parameters.

```bash
pulumi init --owner <account> --name <repository name>
```

The project name is set within the `Pulumi.yaml` file. The stack name is set when you run
`pulumi stack init`.

#### Uniqueness requirement

In the Pulumi Service, within an organization, the name of a repository, project, and stack must be
unique.

There is no way to rename things within the Pulumi Service once created. However, if a stack has no
resources associated with it you can delete it by using `pulumi stack rm <stack name>`.

### Pulumi deployment agents

An Organization may have several deployment agents associated with them, also known as _Pulumi Private Clouds_ (PPCs). These can only be managed by Pulumi Console administrator. If you have questions or require that something be updated, contact [support@pulumi.com](mailto:support@pulumi.com).

Once a deployment agent is chosen during `pulumi stack init`, it cannot be changed. However, you can create new stacks that use different deployment agents.

## Stacks

You can drill into stacks to view the last deployed resources, AWS ARNs, output properties, and so forth.

> NOTE: The stacks page is under active improvement! Expect more functionality and bug fixes during the private beta.

![stack-details](/images/docs-console/06-stack-details.png){:width="700px"}

### Update logs

The Update Logs page shows the latest update logs for the application. It will contain the same
data that was streamed to your command-line when you deployed the application.

![stack-update-log](/images/docs-console/07-stack-update-log.png){:width="700px"}