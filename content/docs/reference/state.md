---
title: State and Backends
description: Learn about how Pulumi handles your infrastructure state files and supported backend options for these state files.
keywords: 
 - IaC
 - infrastructure state
 - state backend
expanded_url: /docs/reference/concepts/
menu:
  reference:
    parent: concepts
    weight: 7
---

## State

Pulumi stores its own copy of the current state of your infrastructure. This is often simply called _state_, and is
stored in transactional snapshots we call _checkpoints_. A _checkpoint_ is recorded by Pulumi at various points so that
it can operate reliably &mdash; whether that means diffing goal state versus current state during an update, recovering from
failure, or destroying resources accurately to clean up afterwards. Because _state_ is critical to how Pulumi
operates, this page gives an overview of the options.

## Backends

Pulumi supports multiple so-called _backends_ for storing your infrastructure state. By default, the CLI uses a web backend hosted at [app.pulumi.com](https://app.pulumi.com). Pulumi offers this backend as a free service with [advanced tiers](https://www.pulumi.com/pricing/) for team and enterprise features. Using the `pulumi.com` backend and the CLI together provides a great combination of usability, safety,
and security for most users. However, if you would prefer to manage this yourself, you can do so by opting into the filesystem or cloud storage backend for more flexibility if you need it.

<div class="table w-full py-2">
    <div class="table-row align-baseline">
        <div class="table-cell bg-gray-400 text-gray-700 px-4 py-2 text-base">Backend</div>
        <div class="table-cell bg-gray-400 text-gray-700 px-4 py-2 text-base">Setup</div>
    </div>
    <div class="table-row align-top">
        <div class="table-cell bg-gray-100 px-4 py-2 text-sm">pulumi.com</div>
        <div class="table-cell bg-gray-100 text-gray-700 px-4 py-2 text-sm">
            No additional configuration after <a class="text-blue-700" href="{{< relref "/docs/reference/install">}}" target="_blank">installing
            Pulumi</a>. The <code>pulumi.com</code> backend is accessed by the CLI through REST API calls.
        </div>
    </div>
    <div class="table-row align-top">
        <div class="table-cell px-4 py-2 text-sm">Self-managed (filesystem or cloud storage)</div>
        <div class="table-cell px-4 py-2 text-sm">
            Your <span class="italic">checkpoint</span> files are stored locally on your computer’s filesystem, or remotely using a cloud storage service.
            <ul class="p-0 list-none">
                <li>
                    <div class="mb-2">
                        To use the <a href="#filesystem-or-local">filesystem or local</a> option, run <code>pulumi login --local</code> so Pulumi
                        stores your <span class="italic">checkpoint</span> files locally on your machine. The default directory for these JSON files is <code>~/.pulumi</code>.
                    </div>
                </li>
                <li>
                    <div class="mb-2">
                        To use the <a href="#cloud-storage-or-remote">cloud storage or remote</a> option, run
                        <code>pulumi login --cloud-url &lt;your-cloud-storage-url&gt;</code> so Pulumi stores your <span class="italic">checkpoint</span> files at your specified URL for your cloud storage object, also in a <code>.pulumi</code> directory. For example, <code>https://s3.console.aws.amazon.com/s3/buckets/my-pulumi-state-bucket>/.pulumi</code> where <span class="font-bold">my-pulumi-state-bucket</span> is the name of your S3 bucket. See the following links for details on cloud provider CLI and storage setup:
                    </div>
                        <div>
                            <div class="mb-2">
                                <span class="font-bold">AWS S3</span>:
                                <span class="italic">See <a href="{{< relref "/docs/reference/clouds/aws/setup">}}">AWS Setup</a>
                                and <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html">Working with Amazon S3 buckets</a>.</span>
                            </div>
                            <div class="mb-2">
                                <span class="font-bold">Azure Blob</span>:
                                <span class="italic">See <a href="{{< relref "/docs/reference/clouds/aws/setup">}}">Azure Setup</a> and Microsoft's <a href="https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-cli">Storage Blobs Quickstart</a>.</span>
                        </div>
                        <div class="mb-2">
                            <span class="font-bold">Google Cloud Storage</span>:
                            <span class="italic">See <a href="{{< relref "/docs/reference/clouds/aws/setup" >}}">GCP Setup</a>
                            and Google's <a href="https://cloud.google.com/storage/docs/quickstarts">Cloud Storage Quickstarts</a>.</span>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</div>

### Pulumi backend features

The `pulumi.com` backend stores all checkpoint state securely, and the CLI always communicates directly with your cloud provider via client-side authentication. All state is encrypted in transit and at rest.

Although backends are primarily responsible for storing state reliably, the `pulumi.com` backend also supports additional features that the filesystem or cloud backend does not. In particular, the `pulumi.com` backend supports keeping track of full
deployment history (for auditing and rollback purposes), and supports concurrent locking so that you don't accidentally
corrupt your infrastructure state when using Pulumi in a team environment. It also supports advanced policy and RBAC.

The `app.pulumi.com` architecture can be visualized as follows:

<img src="/images/docs/reference/state_saas.png" alt="Pulumi SaaS Architecture" class="img-bordered">

The Pulumi Enterprise product offers self-hosting options for the `pulumi.com` backend, if you wish to use these features
without depending on `app.pulumi.com`. The Enterprise web architecture looks like the following:

<img src="/images/docs/reference/state_enterprise.png" alt="Pulumi Enterprise Architecture" class="img-bordered">

[Contact us](https://www.pulumi.com/pricing/#contact) for more information on Pulumi Enterprise.

## Logging In

The `pulumi login` <a href="{{< relref "/docs/reference/cli/pulumi_login" >}}" target="_blank">CLI command</a> lets you log in to a backend. By default, anytime you try to do something that requires
stacks or state, you will be prompted to log in.

### To the pulumi.com backend

The `pulumi.com` backend login process involves using access tokens. The prompt looks like the following:

```sh
$ pulumi login
Manage your Pulumi stacks by logging in.
Run `pulumi login --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account/tokens
    or hit <ENTER> to log in using your browser            :
```

If you hit `<ENTER>` as instructed, a web browser _should_ pop up, and will interact with the service to generate a new access token. If this is your first time using the service, you will need to authenticate.

To view your generated tokens, or create a new one, visit <a href="https://app.pulumi.com/account/tokens" target="_blank">app.pulumi.com/account/tokens</a>.
The **Access Tokens** page displays a list of past tokens, when they were last used, and gives you the option to revoke them.

<img src="/images/docs/reference/state_tokens.png" alt="Pulumi.com Tokens Page" class="img-bordered">

After logging in, _state_ will automatically get persisted with the service. From time to time, you will see
a helpful URL to your update or stack pages. You can always go there to see a full history of updates.

To log in to a privately hosted version of Pulumi Enterprise, simply pass its URL to the command:

```sh
$ pulumi login https://pulumi.acmecorp.com
```

Everything else works the same, except that Pulumi will target your private service instead of `app.pulumi.com`.

### To a self-managed backend

The filesystem or cloud storage backend allows you to store state locally on your machine, or remotely with your cloud provider. For self-managed backends, state management
including backup, sharing, and team access synchronization is entirely up to
you. Pulumi built the `pulumi.com` backend to solve all of these problems "out of the box", but we understand that some users prefer to have more control.

#### Filesystem or local

To use the filesystem backend instead, simply pass the `--local` flag when logging in:

```sh
$ pulumi login --local
```

You should see `Logged into <my-machine> as <myuser> (file://~)` as a result where `<my-machine>` and `<my-user>` are your configured machine and user names respectively. This stores all stack checkpoints as JSON files to`/home/.pulumi` directory on your machine.

To control where these checkpoints get stored, you may specify a `file://<path>` URL instead,
where `<path>` is the full path to the target directory where _checkpoint_ files will get stored. For instance, to store state underneath `/app/data/.pulumi/` instead, you can run this command:

```sh
$ pulumi login file:///app/data
```

> **Note:** If you use a relative path (e.g. `file://./einstein`), Pulumi will always make it relative to ***the current working directory.***

Notice that `pulumi login --local` is simply syntactic sugar for `pulumi login file://~`.


#### Cloud storage or remote

To use a remote backend instead with your preferred cloud storage provider, simply pass the `--cloud-url` or `-c` flag and your storage bucket or blob URL when logging in:

```sh
$ pulumi login --cloud-url s3://my-pulumi-state-bucket 
```

You should see `Logged into <my-machine> as <myuser> (s3://my-pulumi-state-bucket)` where `<my-machine>` and `<my-user>` are your configured machine and user names respectively. 

In the previous example, we passed an AWS S3 bucket URL, but you can also use Google
Cloud or Azure Blob storage.

##### Amazon S3

<pre><code>pulumi login --cloud-url s3://my-pulumi-state-bucket</code></pre>

##### Google Cloud Storage

<pre><code>pulumi login --cloud-url gs://my-pulumi-state-bucket</code></pre>


##### Azure Blob Storage

<pre><code>pulumi login --cloud-url az://my-pulumi-state-bucket</code></pre>

This stores all stack checkpoints as JSON files to the `.pulumi` directory of
your specified cloud URL.

To control where these checkpoints get stored, refer to your cloud storage provider's documentation. See [Backends](#backends) for quick links to Amazon, Google, and Microsoft Azure's storage service quickstarts.

You may omit `--cloud-url` or `-c` when logging in to a remote backend and just use `pulumi login s3://my-pulumi-state-bucket`.

The precise JSON format these checkpoint files use is not documented, but is defined in the [APIType source code](
https://github.com/pulumi/pulumi/blob/master/pkg/apitype/) if you'd like to understand their contents. Note that
this is the same JSON format used by the `pulumi stack export` and `pulumi stack import` commands.

If you lose the checkpoint for your stack, Pulumi will be unable to manage any existing resources. Additionally, since Pulumi thinks your stack is empty, Pulumi will attempt to recreate all of the resources in your stack the next time you run `pulumi up`.

Some commands may behave slightly differently when using the local or remote storage endpoint. For example, when connected to `pulumi.com`,
`pulumi up` ensures there are no other updates in flight for a given stack. This doesn't happen with self-managed backends. Pulumi also manages secrets using a key encrypted with a passphrase and stored in
`Pulumi.<stack-name>.yaml`. This requires you enter the passphrase when you `preview`, `update`, or `delete` your stack. If you want to collaborate with another person, you'll need to share this passphrase with them as well. All of these overhead tasks will have to be managed separately when you opt into the local or remote state backend.

### Going back to the pulumi.com backend

So you've tried a self-managed backend and want to switch to the `pulumi.com` backend? This scenario can happen once users realize the benefit from the features that the `pulumi.com` backend delivers, particularly when operationalizing their usage.

To delete stored credentials on your machine and log out from your current backend, run `pulumi logout`. See <a href="{{< relref "/docs/reference/cli/pulumi_logout">}}" target="_blank">pulumi logout</a> for more details. To use the `pulumi.com` backend instead, just run `pulumi login` again, and you’ll be back to using `app.pulumi.com`.

> **Note:** Existing stacks on a self-managed backend have to be migrated. It's easiest to just plan on recreating them.
>
> In addition, if you have any encrypted configuration in your stack, you'll need to rerun
`pulumi config set --secret <key> <value>` because `pulumi.com` uses a different key to encrypt your secrets than the local endpoint.

If you'd like to migrate your stacks from the filesystem to the `pulumi.com` backend, you can follow the steps below. Suppose the stack
"my-app-production" has been managed with a local checkpoint file, and you want to migrate it to `pulumi.com`, run the following commands if you are logged in to the local endpoint:

```sh
$ pulumi stack select my-app-production # switch to the stack we want to export
$ pulumi stack export --file my-app-production.checkpoint.json # export the stack's checkpoint to a local file
$ pulumi login
$ pulumi stack init my-app-production # create a new stack with the same name on pulumi.com
$ pulumi stack import --file my-app-production.checkpoint.json # import the new existing checkpoint into pulumi.com
```

To migrate from a remote backend, you will have to download the checkpoint
files stored in the `.pulumi` directory of your cloud storage URL.

### Secrets Encryption

When a secret value is provided via secret configuration &mdash; by passing `--secret` to `pulumi config set`, or created inside your program by using `pulumi.secret` (JavaScript) or `Output.secret` (Python) &mdash; the value is encrypted with a key managed by the backend you are connected to.  When using the local or remote backend, this key is derived from a passphrase you set when creating your stack, and when using the `pulumi.com` backend, it is handled by a key managed by the service.

For new stacks managed with the `pulumi.com` backend, you may choose to use the passphrase-based key instead. Pass `--secrets-provider passphrase` when you create the stack (either via `pulumi new` or `pulumi stack init`). You'll be prompted to choose a passphrase and future operations like `update`, `preview` and `destroy` will require you enter this passphrase before the operation will run.

When using the filesystem or cloud storage backend, you must use the passphrase-based secrets provider.
