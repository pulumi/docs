---
layout: default 
nav_section: "quickstart"
type: reference
---

<p><a href="/quickstart">Quickstart</a> &gt; <b>Pulumi Cloud Console</b></p>

# Pulumi Cloud Console

So far in the quickstart we have been running Pulumi programs on your local machine. While the
Pulumi tool handled creating cloud resources based on the programs you wrote, all of the
information is still on your hard drive.

This means it is difficult to collaborate with other developers, and even worse means you are one
harddrive failure away from a very bad day.

The Pulumi Cloud Management Console is a hosted version of Pulumi. You write and run programs in
the same way, except rather than executing thjem on your local machine, the Pulumi Cloud Console
handles the deployment for you.

To access the Pulumi Cloud Console, visit:

[https://beta.pulumi.com](https://beta.pulumi.com)

> NOTE: The Pulumi Cloud Console is a work in progress. We will be adding many new features over
> the comming weeks. But your feedback is an important part of making it the Pulumi console the
> most friendly, intuitive, and useful management tool you've ever used. We want to hear from you!

## Logging in

When you first visit the console you are greeted by a login form. Pulumi uses GitHub for
authentication. So to use the Pulumi service you need a GitHub account. (And, that account also
needs to be a member of one of the GitHub organizations in the Pulumi private beta.)

![login-with-github-page](/images/docs-console/01-login.png)

### OAuth Scopes

The Pulumi Cloud Management Console requests several GitHub OAuth scopes. Here's what we ask for
and why:

![oauth-scopes](/images/docs-console/02-oauth.png)

> Personal user data
> - Email addresses (read-only)
> - This application will be able to read your private email addresses.

We need your email address in case we need to contact you. Don't worry, we dislike marketing email
just as much as you do.

> Repositories
> - Public and private
> - This application will be able to read and write all public and private repository data.

We use your GitHub repository information to associate updates to Pulumi programs with the relevant
source code. Showing Travis build results, git tags, etc.

Sadly GitHub [does not offer a read-only scope](https://developer.github.com/apps/building-integrations/setting-up-and-registering-oauth-apps/about-scopes-for-oauth-apps/)
for repository access. But the Pulumi Service will not update any data on GitHub.

> Organizations and teams
> - Read-only access
> - This application will be able to read your organization and team membership.

This permission isn't about _your_ GitHub account, but rather the organization you may manage.
Pulumi checks access based on GitHub organization membership. But in order to do that, we need
the GitHub organization to authorize Pulumi to access it's membership data.

### Pulumi Account

After you have logged in, you can access your Pulumi Account by clicking the avatar photo on the
top right.

![accounts-page](/images/docs-console/03-account-page.png)

The Pulumi Service picks up profile information (name, photo, etc.) from GitHub If anything looks
out of sync, click "_sync profile with GitHub_".

There are two key things to notice on this page:

#### Pulumi Access Token

To authenticate with the Pulumi Service from the `pulumi` command-line tool, you'll need to use
your _Pulumi Access Token_. This is the value you enter when running `pulumi login`.

Keep this secret like you would any other access token.

#### Organizations List

Below the access token is your organizations list. These are mirroed from GitHub just like your
profile. You can click "Reivew or add" to review the list of organizations that have been
authorized by GitHub, and potentially grant the Pulumi Service access.

(To pick up any changes, you'll need to click "sync profile with GitHub".)

## Organizations

The Pulumi Cloud Management Console organizes Pulumi programs by "organizations". These can be
either a GitHub user account or a GitHub organization. There is currently no way to create one
that existsly solely on the Pulumi console.

![organizations-page](/images/docs-console/04-orgs-list.png)

### Repositories, Projects, and Stacks

Pulumi programs are organized within the following heirarchy:

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

In the Pulumi Service, within an organization the name of a repository, project, and stack must be
unique.

There is no way to rename things within the Pulumi Service once created. However, if a stack has no
resources associated with it you can delete it by using `pulumi stack rm <stack name>`.

### Pulumi Private Clouds

An Organization may have several _Pulumi Private Clouds_ (PPCs) associated with them. These are
the things that manage deploying Pulumi programs.

The "Clouds" section of the Pulumi Service show the PPCs available, along with current version
information.

![clouds-page](/images/docs-console/05-clouds-list.png)

> Currently managing these is done by a Pulumi console administrator. If you have questions or need
> something updated, contact us at support@pulumi.com.

The Pulumi Cloud used when a stack is deployed is set once during `pulumi stack init`. Once set it
cannot be changed for the lifetime of that stack.

## Stacks

You can drill into stacks to view the details about their resources, logs, etc.

> NOTE: The stacks page is something we expect will change dramatically in the comming weeks.

![stack-details](/images/docs-console/06-stack-details.png)

### Update Logs

The Update Logs page shows the latest update logs for the application. It will contain the same
data that was streamed to your command-line when you deployed the application.
