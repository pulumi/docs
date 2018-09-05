---
title: State and Backends
---

Pulumi stores its own copy of the current state of your infrastructure. This is often simply called _state_, and is
stored in transactional snapshots we call _checkpoints_. A checkpoint is recorded by Pulumi at various points so that
it can operate reliably, whether that means diffing goal state versus current state during an update, recovering from
failure, or destroying resources accurately to clean up afterwards, for example. Because state is critical to how Pulumi
operates, this page gives an overview of the options.

## Backends

Pulumi supports multiple so-called _backends_ for storing this state. There are two primary kinds:

1. **Web**: a backend accessed by the CLI through REST API calls
2. **Filesystem**: a backend stored locally on your computer's filesystem

By default, the CLI uses a web backend hosted at https://app.pulumi.com. This is a free service offered by Pulumi
that also offers advanced tiers for team and enterprise features. It is possible to opt-in to the filesystem backend.

We think that using the web backend and the CLI together provides the right combination of usability, safety,
and security for most users. But the filesystem backend provides more flexibility for those who need it.

### Web Backend Features

The web backend stores all checkpoint state securely, and the CLI always communicates directly with your cloud provider
using client-side authentication. All state is encrypted in transit and at rest.

Although backends are primarily responsible for storing state reliably, the web backend also supports additional
features that the filesystem backend does not. In particular, the web backend supports keeping track of full
deployment history (for auditing and rollback purposes), and supports concurrent locking so that you don't accidentally
corrupt your infrastructure state when using Pulumi in a team environment. It also supports advanced policy and RBAC.

The app.pulumi.com architecture can be visualized as follows:

![Pulumi SaaS Architecture](/images/reference/state_saas.png){:class="img-bordered"}

The Pulumi Enterprise product offers self-hosting options for the web backend, if you wish to use these features
without depending on app.pulumi.com. The Enterprise web architecture looks like the following:

![Pulumi Enterprise Architecture](/images/reference/state_enterprise.png){:class="img-bordered"}

For more information on Pulumi Enterprise, please [contact us](https://www.pulumi.com/pricing/#contact).

## Logging In

The `pulumi login` command lets you log into a backend. By default, anytime you try to do something that requires 
stacks or state, you will be prompted to log in.

### To the Web Backend

The web backend login process involves using access tokens. The prompt looks like the following:

```sh
$ pulumi login
Manage your Pulumi stacks by logging in.
Run `pulumi login --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account
    or hit <ENTER> to log in using your browser            :
```

If you hit `<ENTER>` as instructed, a web browser will pop up, and will interact with the service to generate a new
access token. If this is your first time using the service, you will need to authenticate.

If you wish to get a token manually, or view your generated tokens, you may go to https://app.pulumi.com/account/tokens.
This page will show you all past tokens, when they were last used, and allow you to revoke them:

![Pulumi.com Tokens Page](/images/reference/state_tokens.png){:class="img-bordered"}

After logging in, state will automatically get persisted with the service, and from time to time, you will see
a helpful URL to your update or stack pages. You can always go there to see a full history of updates.

To log into a privately hosted version of Pulumi Enterprise, simply add its URL to the command:

```sh
$ pulumi login https://pulumi.acmecorp.com
```

Everything else works the same, except that URLs will target your private service instead of app.pulumi.com.

### To the Filesystem Backend

The filesystem backend allows you to store state locally to your machine. Because it is stored locally, it's up to you
to back it up, share it across machines, and synchronize access to it properly in a team environment. We built the web
backend to solve all of these problems "out of the box," but we understand that some users will want more control.

To opt into using the filesystem backend, simply pass the `--local` flag when logging in:

```sh
$ pulumi login --local
Logged into my-machine as myuser (file://~)
```

This will store all stack checkpoints underneath my home directory, in the `.pulumi` directory, as JSON files.

If you'd like to control where these checkpoints get stored, you may instead log into a `file://<path>` URL,
where `<path>` is the full path to the target directory under which files will get stored. For instance, to store
state underneath `/app/data/.pulumi/` instead, you can run this command:

```sh
$ pulumi login file:///app/data
Logged into my-machine as myuser (file:///app/data)
```

Notice that `pulumi login --local` is simply syntactic sugar for `pulumi login file://~`.

The precise JSON format these checkpoint files use is not documented, but is defined [in source code here](
https://github.com/pulumi/pulumi/blob/master/pkg/apitype/) if you'd like to understand their contents. Note that
this is the same JSON format used by the `pulumi stack export` and `pulumi stack import` commands.

If you lose the checkpoint for your stack, Pulumi will be unable to manage any existing resources! Additionally, since
Pulumi will believe your stack is empty, the next update will attempt to re-create all of the resources in your stack.

Some commands may behave slightly differently when using the local endpoint. For example, when connected to pulumi.com,
`pulumi update` ensures there are no other updates in flight for a given stack, something that doesn't happen with the
local endpoint. Secrets are also managed using a key encrypted with a passphrase and stored in
`Pulumi.<stack-name>.yaml`. This requires you to enter the passphrase when you preview, update or delete your stack.
If you want to collaborate with another person, you'll need to share this passphrase with them as well.

### Going Back to the Web Backend

Some users initially try out Pulumi using the filesystem backend and then move to the web backend when it's clear
they will benefit from the features that it delivers (particularly when operationalizing their usage).

To use the web backend, just run `pulumi login` again, and you’ll be back to using app.pulumi.com. If you have any
existing stacks, however, you'll need to migrate them. It's easiest to just plan on recreating them.

If you'd like to migrate your stacks from the filesystem to web, however, you can do the following. Suppose the stack
"my-app-production" has been managed with a local checkpoint file, and you want to migrate it to pulumi.com. If you are
currently logged in to the local endpoint, run the following commands:

```sh
$ pulumi stack select my-app-production # switch to the stack we want to export
$ pulumi stack export --file my-app-production.checkpoint.json # export the stack's checkpoint to a local file
$ pulumi login
$ pulumi stack init my-app-production # create a new stack with the same name on pulumi.com
$ pulumi stack import --file my-app-production.checkpoint.json # import the new existing checkpoint into pulumi.com
```

In addition, if you have any encrypted configuration in your stack, you'll need to re-run
`pulumi config set --secret <key> <value>` because pulumi.com uses a different key to encrypt your secrets than the
local endpoint.
