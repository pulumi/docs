---
layout: default 
nav_section: "how-to"
type: reference
---

<p><a href="/how-to">How-to Guides</a> &gt; <b>Pulumi Cloud Console</b></p>

# Using the Pulumi Cloud Console

<!-- 

So far in the quickstart we have been running Pulumi programs on your local machine. While the
Pulumi tool handled creating cloud resources based on the programs you wrote, all of the
information is still on your hard drive.

This means it is difficult to collaborate with other developers, and even worse means you are one
harddrive failure away from a very bad day. -->

The Pulumi Cloud Management Console is a hosted version of Pulumi. You write and run programs in
the same way, except rather than executing them on your local machine, the Pulumi Cloud Console
handles the deployment for you.

To access the Pulumi Cloud Console, visit [https://beta.pulumi.com](https://beta.pulumi.com).

> NOTE: The Pulumi Cloud Console is a work in progress. We will be adding many new features over
> the coming weeks. Your feedback is an important part of making it the Pulumi console the
> most friendly, intuitive, and useful management tool you've ever used. We want to hear from you!

## Logging in {#login-to-console}

Pulumi uses GitHub for authentication, so you must login with a GitHub account. Also, you must a member of an organization that has been enrolled in the Pulumi Console private beta.

### OAuth scopes

The Pulumi Cloud Management Console requests several GitHub OAuth scopes, as illustrate in the following screenshot. 

![oauth-scopes](/images/docs-console/02-oauth.png)

Here's what we ask for and why:

> Personal user data
> - Email addresses (read-only)
> - This application will be able to read your private email addresses.

We only use your email address for important service-related communication. We dislike marketing email just as much as you do!

> Repositories
> - Public and private
> - This application will be able to read and write all public and private repository data.

We use your GitHub repository information to associate updates to Pulumi programs with the relevant
source code. Showing Travis build results, git tags, etc.

Unfortunately, GitHub does not offer [a read-only scope for repository access](https://developer.github.com/apps/building-integrations/setting-up-and-registering-oauth-apps/about-scopes-for-oauth-apps/). But, the Pulumi Service **never** writes data to GitHub.

> Organizations and teams
> - Read-only access
> - This application will be able to read your organization and team membership.

This read-only permission just means that Pulumi can query to see which organizations you are a member of. Pulumi uses your organization membership to determine which Cloud Stacks are displayed to you. 

### Pulumi account {#account-page}

After you have logged in, you can access your Pulumi Account by clicking the avatar photo on the
top right.

![accounts-page](/images/docs-console/03-account-page.png)

The Pulumi Service picks up profile information (name, photo, etc.) from GitHub. If you've changed any information on GitHub, click **sync profile with GitHub** to have that information reflected in the Pulumi Console.

There are two key things to notice on this page: the Pulumi Access token and the organization list.

#### Pulumi Access Token {#access-token}

To authenticate with the Pulumi Service from the `pulumi` command-line tool, you'll need to use
your _Pulumi Access Token_. This is the value you enter when running `pulumi login`.

Keep this secret like you would any other access token.

The access token is associated with your GitHub username and is the same across all of the organizations you have access to.

#### Organizations list

Below the access token is your organizations list. These are mirrored from GitHub just like your
profile. Select **Review or add** to review the list of organizations that have been
authorized by GitHub, and potentially grant the Pulumi Service access. If make any changes, click **sync profile with GitHub**.

## Organizations

The Pulumi Cloud Management Console organizes Pulumi programs by *organizations*. An organization is either a GitHub user account or a GitHub organization. Currently, there no way to create an organization that is not tied to a GitHub organization.

![organizations-page](/images/docs-console/04-orgs-list.png)

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

The project name is set within the `Pulumi.yaml` file. And the stack name is set when you run
`pulumi stack init`.

#### Uniqueness Requirement

In the Pulumi Service, within an organization, the name of a repository, project, and stack must be
unique.

There is no way to rename things within the Pulumi Service once created. However, if a stack has no
resources associated with it you can delete it by using `pulumi stack rm <stack name>`.

### Pulumi Private Clouds

An Organization may have several _Pulumi Private Clouds_ (PPCs) associated with them. These can only be managed by Pulumi Console administrator. If you have questions or require that something be updated, contact [support@pulumi.com](mailto:support@pulumi.com).

Once a Pulumi Private Cloud is chosen during `pulumi stack init`, it cannot be changed. However, you can create new stacks that are tied to different clouds.

## Stacks

You can drill into stacks to view the last deployed resources, AWS ARNs, output properties, and so forth.

> NOTE: The stacks page is under active improvement! Expect more functionality and bug fixes during the private beta.

![stack-details](/images/docs-console/06-stack-details.png)

### Update Logs

The Update Logs page shows the latest update logs for the application. It will contain the same
data that was streamed to your command-line when you deployed the application.

![stack-update-log](/images/docs-console/07-stack-update-log.png)