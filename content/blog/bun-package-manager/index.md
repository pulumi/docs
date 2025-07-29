---
title: "Pulumi + Bun: Supercharge Your Infrastructure Dependencies"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-07-28T09:50:26+01:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Learn how to use Bun as a package manager with Pulumi for faster dependency management. Get faster installations with step-by-step setup guides.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - piers-karsenbarg

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - typescript
    - package-manager

---

Today, we are announcing a new addition that allows Pulumi users to use [Bun](https://bun.sh/) as their package manager, offering an alternative to npm, Yarn, or pnpm. Bun, a recently released JavaScript runtime, bundler, transpiler, and package manager, provides a faster way to manage Pulumi project dependencies.

<!--more-->

## What is this Bun thing you're talking about?

If you've spent time around the JavaScript ecosystem, then you've probably heard of Bun. If you haven’t, then be aware that it presents itself as a JavaScript toolkit, a direct drop-in replacement for NodeJS. However, the part that we like at Pulumi is its use as a package manager. According to the [Bun install documentation](https://bun.com/docs/cli/install), switching from `npm install` to `bun install` can make your installations up to 25 times faster.

{{% notes type="warning" %}}

1. Pulumi uses Bun solely as a package manager. You cannot use Bun to write Automation API-based applications, nor do we have a language plugin for Bun.  
2. This requires Bun version 1.2 or greater due to the text-based lockfile introduced in this version.

{{% /notes %}}

## Getting started with Bun and Pulumi

Since you're probably already using NodeJS with Pulumi to want to use this, the easiest way to install Bun is to run the following:

```shell
npm install -g bun
```

The [Bun installation documentation](https://bun.com/docs/installation) has more information on other methods available.

## How to use in a new project

If you want to try this out on a new project, you can use

```shell
mkdir new-bun-project && cd new-bun-project
pulumi new typescript
```

You'll get the usual prompts to set the project name, the description, and the stack name:

```shell
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

Project name (new-bun-project):
Project description (A minimal TypeScript Pulumi program):
Created project 'new-bun-project'

Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
Stack name (dev):
```

Then you'll be shown a list of the package managers to choose from (obviously we'll use the arrow keys to select the bun option):

```shell
The package manager to use for installing dependencies  [Use arrows to move, type to filter]
  npm
  pnpm
  yarn
> bun
```

Hit the `ENTER` key to make your selection, and you'll see the `bun install` output:

```shell
The package manager to use for installing dependencies bun
Installing dependencies...

bun install v1.2.18 (0d4089ea)

+ @types/node@18.19.120 (v24.1.0 available)
+ typescript@5.8.3
+ @pulumi/pulumi@3.186.0

272 packages installed [1240.00ms]

Blocked 1 postinstall. Run `bun pm untrusted` for details.
Finished installing dependencies

Your new project is ready to go! ✨

To perform an initial deployment, run `pulumi up`
```

The files in the folder look a little different:

```shell
drwxr-xr-x@   - piers 28 Jul 18:13 node_modules
.rw-r--r--@  21 piers 28 Jul 18:11 .gitignore
.rw-r--r--@ 61k piers 28 Jul 18:13 bun.lock
.rw-r--r--@  42 piers 28 Jul 18:11 index.ts
.rw-r--r--@ 217 piers 28 Jul 18:11 package.json
.rw-r--r--@ 198 piers 28 Jul 18:13 Pulumi.yaml
.rw-r--r--@ 438 piers 28 Jul 18:11 tsconfig.json
```

(note the `bun.lock` instead of the `package-lock.json`)

and in the `Pulumi.yaml` file, the `packagemanager` option is set to `bun`:

```
name: new-bun-project
description: A minimal TypeScript Pulumi program
runtime:
  name: nodejs
  options:
    packagemanager: bun
config:
  pulumi:tags:
    value:
      pulumi:template: typescript

```

We will use the Random provider to generate a new password. Let's add the `@pulumi/random` package:

```shell
❯ bun add @pulumi/random
bun add v1.2.18 (0d4089ea)

installed @pulumi/random@4.18.3

[345.00ms] done
```

Since we're still using the Pulumi NodeJS runtime, that's all we need Bun for right now.

The rest is business as usual, so the `index.ts` file looks like:

```ts
import * as random from "@pulumi/random";

const password = new random.RandomPassword("password", {
    length: 20
});

export const pw = password.result;
```

Then it's just a case of running:

```shell
pulumi up
```

and creating the resources.

## Migrating an existing project

If you already have a project set up and are using npm as your package manager, there are a few steps you'll need to follow.

For this example, I'm going to use the code from the Bun example above but set it up using npm instead:

```shell
❯ pulumi new typescript
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

Project name (migrate-project):
Project description (A minimal TypeScript Pulumi program):
Created project 'migrate-project'

Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
Stack name (dev):

The package manager to use for installing dependencies npm
Installing dependencies...


added 293 packages, and audited 294 packages in 9s

43 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
Finished installing dependencies

Your new project is ready to go! ✨

To perform an initial deployment, run `pulumi up`
```

Then we'll install the `@pulumi/random` package:

```shell
npm install @pulumi/random
```

and checking the folder listing:

```shell
drwxr-xr-x@    - piers 28 Jul 18:32 node_modules
.rw-r--r--@   21 piers 28 Jul 18:32 .gitignore
.rw-r--r--@   42 piers 28 Jul 18:32 index.ts
.rw-r--r--@ 149k piers 28 Jul 18:32 package-lock.json
.rw-r--r--@  217 piers 28 Jul 18:32 package.json
.rw-r--r--@  198 piers 28 Jul 18:32 Pulumi.yaml
.rw-r--r--@  438 piers 28 Jul 18:32 tsconfig.json
```

we can see that we've got the usual `package-lock.json` file that we expect, and the `Pulumi.yaml` file looks like this:

```
name: migrate-project
description: A minimal TypeScript Pulumi program
runtime:
  name: nodejs
  options:
    packagemanager: npm
config:
  pulumi:tags:
    value:
      pulumi:template: typescript
```

(Note the `packagemanager` option).

To migrate this project to use Bun as the package manager instead, we need to update the `Pulumi.yaml` to set the `packagemanager` to be `bun`:

```
name: migrate-project
description: A minimal TypeScript Pulumi program
runtime:
  name: nodejs
  options:
    packagemanager: bun
config:
  pulumi:tags:
    value:
      pulumi:template: typescript
```

We can use the `bun` CLI to migrate the `package-lock.json` file to the `bun.lock` file, running the following command:

```
bun om migrate
```

which gives us the file structure:

```shell
drwxr-xr-x@    - piers 28 Jul 18:32 node_modules
.rw-r--r--@   21 piers 28 Jul 18:32 .gitignore
.rw-r--r--@  64k piers 28 Jul 18:43 bun.lock
.rw-r--r--@   42 piers 28 Jul 18:32 index.ts
.rw-r--r--@ 149k piers 28 Jul 18:32 package-lock.json
.rw-r--r--@  217 piers 28 Jul 18:32 package.json
.rw-r--r--@  198 piers 28 Jul 18:32 Pulumi.yaml
.rw-r--r--@  438 piers 28 Jul 18:32 tsconfig.json
```

We can then delete the `package-lock.json` if we want to.

Then we can run `pulumi install` to install the packages to Bun's global cache:

```shell
❯ pulumi install
Installing dependencies...

bun install v1.2.18 (0d4089ea)

15 packages installed [60.00ms]
Finished installing dependencies
```

and continue with

```shell
pulumi up
```

## What else?

We've baked Bun into the `pulumi/pulumi` container, allowing you to make use of the faster package installer in your CI/CD pipeline, including in Pulumi Deployments. If you'd like to see Bun become more integrated into Pulumi, there's [an open issue](https://github.com/pulumi/pulumi/issues/13904) that you can vote on, or even implement if you're interested.

## Final thoughts

Bun is in the process of establishing itself as the new player in the JavaScript ecosystem. Its focus on speed makes it a great alternative to NPM, Yarn, and pnpm when managing Pulumi project dependencies. Give it a try on your next project, and you may wonder how you ever lived without it.
