---
title_tag: "State and Backends | Pulumi Concepts"
meta_desc: Learn about how Pulumi handles your infrastructure state files and supported backend options for these state files.
title: "State & backends"
h1: Managing state & backend options
keywords:
 - IaC
 - infrastructure state
 - state backend
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    weight: 9

aliases:
- /docs/reference/state/
- /docs/intro/concepts/state/
---

Pulumi stores metadata about your infrastructure so that it can manage your cloud resources. This metadata is called _state_. Each [stack](/docs/concepts/stack/) has its own state, and state is how Pulumi knows when and how to create, read, delete, or update cloud resources.

Pulumi stores state in a _backend_ of your choosing. A backend is an API and storage endpoint used by the CLI to coordinate updates, and read and write stack state whenever appropriate. Backend options include the Pulumi Cloud, an easy-to-use, secure, and reliable hosted application with policies and safeguards to facilitate team collaboration, in addition to simple object storage in AWS S3, Microsoft Azure Blob Storage, Google Cloud Storage, any AWS S3 compatible server such as Minio or Ceph, or a local filesystem.

The default experience is to use the hosted Pulumi Cloud, which takes care of the state and backend details for you. Conversely, when using cloud storage or a local filesystem as your backend, you gain control over where your state is located at the expense of having to handle security, state management, auditing, and other concerns the Pulumi Cloud would otherwise handle for you.

> Pulumi state does not include your cloud credentials. Credentials are kept local to your client &mdash; wherever the CLI runs &mdash; even when using the managed Pulumi Cloud backend. Pulumi _does_ store configuration and secrets, but encrypts those secrets using your chosen encryption provider. To learn more, see [Configuration and Secrets](/docs/concepts/secrets/).

## Deciding On a State Backend

Pulumi supports two classes of state backends for storing your infrastructure state:

- **Pulumi Cloud**: a managed cloud experience using the online or self-hosted Pulumi Cloud application
- **Self-Managed**: a manually managed object store, including AWS S3, Azure Blob Storage, Google Cloud Storage, any AWS S3 compatible server such as Minio or Ceph, or your local filesystem

Pulumi's SDK works great with all backends, although some details differ between them.

Pulumi Cloud, hosted at <a href="https://app.pulumi.com" target="_blank">`app.pulumi.com`</a>, is the default backend, as it provides the best combination of usability, safety, and security for most users. Important features include:

- Robust state management, with transactional checkpointing for fault tolerance and recovery
- Concurrent state locking to prevent corrupting your infrastructure state in a team environment
- Full deployment history for auditing and rollback purposes
- Encrypted state in transit and at rest
- Managed encryption and key management for secrets
- Secure access to cloud resource metadata, with client-side authentication to your cloud provider
- Team policies, including Policy as Code and Role Based Access Control (RBAC)

The Pulumi Cloud backend requires no additional configuration after [installing the CLI](/docs/install/). Pulumi offers this backend hosted online free for individuals, with [advanced tiers](/pricing/) available for teams and enterprises (with <a href="https://app.pulumi.com/site/trial" target="_blank">free trials</a>). It has successfully undergone multiple security audits including SOC2, pen-testing, and more.

> To learn more about the Pulumi Cloud backend's design, including why it doesn't need your cloud credentials, see [Pulumi Cloud Architecture](#pulumi-cloud-architecture). If you are interested in the hosting your own instance, see the [Self-Hosting User Guide](/docs/pulumi-cloud/self-hosted/).

Pulumi also lets you manage state yourself using a self-managed backend. Your state is stored as simple JSON files in AWS S3, Azure Blob Store, Google Cloud Storage, an alternative AWS S3 API compatible server such as Minio or Ceph, or on your local filesystem. These self-managed backends are all open source and free to use in any setting. Using a self-managed backend trades off some amount of reliability for additional control over where metadata is stored. For instance, you will need to manually configure secure access, encryption, and history, and devise your own concurrency control and recovery capabilities. To choose a self-managed backend, use the `pulumi login` command [as documented below](#using-a-self-managed-backend).

## Logging into and out of State Backends

The [`login` command](/docs/cli/commands/pulumi_login) logs you into a backend:

```sh
$ pulumi login
```

The [`logout` command](/docs/cli/commands/pulumi_logout) logs you out of the current backend.

```sh
$ pulumi logout
```

This will remove all credentials information from `~/.pulumi/credentials.json` and you will need to log in again before performing any subsequent stack or state operations.

To change backends, run `pulumi logout` followed by `pulumi login`.

The basic form of `login` will use the Pulumi Cloud by default. If you wish to log in to a specific backend, pass the backend-specific URL as the sole argument:

```sh
$ pulumi login <backend-url>
```

Alternatively, there are 2 other options that help to avoid the need to type it every time:

1. Set the `PULUMI_BACKEND_URL` environment variable.
2. Set `backend` property in the project `Pulumi.yaml` config file as below:

```yaml
....
backend:
  url: <backend-url>
....
```

For details on the various backend URL formats and options, please see the sections on using the Pulumi Cloud and self-managed backends.

If you forget to log in, you will be automatically prompted to do so before you do anything that requires stacks or state.

After logging in, your credentials are recorded in the `~/.pulumi/credentials.json` file, and all subsequent operations will use the chosen backend. From time to time, you will see a helpful URL to your update or stack pages. For example, after an update completes, you will see a link to that update's details. You can always go there to see a full history of updates.

If you ever want to check what user is logged in, use the [`whoami` command](/docs/cli/commands/pulumi_whoami). To additionally see what  backend is currently being used, pass the `--verbose` (or `-v`) flag:

```bash
$ pulumi whoami -v
User: <your-username>
Backend URL: https://app.pulumi.com/<your-username>
```

## Pulumi Cloud Backend

Running `pulumi login` without any argument will log into the default Pulumi Cloud backend:

```sh
$ pulumi login
```

This will display a prompt that asks for an [access token](/docs/pulumi-cloud/accounts#access-tokens):

```
Manage your Pulumi stacks by logging in.
Run `pulumi login --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account/tokens
    or hit <ENTER> to log in using your browser:
```

To automatically generate and use a new access token, hit `<ENTER>`. This will open a web browser to interact with Pulumi Cloud and request a token. If this is your first time using Pulumi Cloud, you will be asked to authenticate using your chosen identity provider (GitHub, GitLab, Atlassian, SAML/SSO, or email).

To view your access tokens, or create a new one manually, view the <a href="https://app.pulumi.com/account/tokens" target="_blank">Access Tokens</a> page.  You will see a list of past tokens, when they were last used, as well as the ability to revoke them.

<img src="/images/docs/reference/state_tokens.png" alt="Pulumi.com Tokens Page" class="img-bordered">

To log into a self-hosted instance of the Pulumi Cloud, pass its API URL to the `login` command:

```sh
$ pulumi login https://pulumi.acmecorp.com
```

Everything works the same as with the standard Pulumi Cloud, except that Pulumi will target your private instance instead of the shared one hosted at `app.pulumi.com`.

### Pulumi Cloud Architecture

The Pulumi Cloud is comprised of two Internet-accessible endpoints&mdash;a web application at `app.pulumi.com` and a REST API at `api.pulumi.com`&mdash;with an assortment of cloud infrastructure to support its features. A simplified diagram of its architecture looks like this:

<img src="/images/docs/reference/state_saas.png" alt="Pulumi Cloud Architecture" class="img-bordered">

The Pulumi Cloud doesn't ever acquire your cloud credentials, and does not communicate with your cloud provider directly. Instead, the CLI itself coordinates with both the Pulumi Cloud's API and your cloud provider's API directly. This ensures your IAM and key management does not need to change while adopting Pulumi. In particular, if you are running Pulumi deployments from [within a CI/CD environment](/docs/using-pulumi/continuous-delivery/), you can rely on existing mechanisms and security practices that your organization has already put in place.

The Pulumi Cloud is reliable, secure, and has undergone multiple audits, including SOC2 and professional pen-testing. Because of the client/server division of responsibilities &mdash; notably that the server doesn't have direct access to your cloud credentials, runtime data, or PII &mdash; the Pulumi Cloud has been used in organizations with advanced compliance needs, including PCI, ISO 27001, HIPAA, and more. If you'd like to discuss any of these topics, please [contact us](/contact/).

It is possible to host your own version of the Pulumi Cloud in your private cloud environment. Pulumi offers versions that run natively on AWS, Azure, Google Cloud, Kubernetes, or simple virtual machine-based private and hybrid cloud environments. The architecture is very similar to the online version, but is privately hosted and does not depend on public access over the Internet:

<img src="/images/docs/reference/state_enterprise.png" alt="Pulumi Enterprise Architecture" class="img-bordered">

To learn more about self-host options, see [Self-Hosted Pulumi Cloud](/docs/pulumi-cloud/self-hosted/) or [Contact Us](/pricing#contact).

## Using a Self-Managed Backend

The filesystem and cloud storage backends allow you to store state locally on your machine or remotely within a cloud object store. For self-managed backends, state management including backup, sharing, and team access synchronization is custom and implemented manually.

> **Note**: The Pulumi Cloud backend was designed to be robust and easy to use. If you decide to use a self-managed backend, you will need to be more aware of how state works (see [Advanced State](#advanced-state)). If you lose the checkpoint for your stack, or it drifts from reality, Pulumi will not behave as you might expect &mdash; for instance, if your state file is empty, Pulumi will think your stack is empty, and will attempt to recreate all of the resources. Some commands may also behave slightly differently between backends. For example, the Pulumi Cloud ensures there are no other updates in flight for a given stack, and in general, reliability, security, and collaboration is automatic with the Pulumi Cloud.

To use a self-managed backend, specify a storage endpoint URL as `pulumi login`'s `<backend-url>` argument: `s3://<bucket-path>`, `azblob://<container-path>`, `gs://<bucket-path>`, or `file://<fs-path>`. This will tell Pulumi to store state in AWS S3, Azure Blob Storage, Google Cloud Storage, or the local filesystem, respectively. Checkpoint files are stored in a relative`.pulumi` directory. For example, if you were using the Amazon S3 self-managed backend, your checkpoint files would be stored at `s3://my-pulumi-state-bucket/.pulumi` where `my-pulumi-state-bucket` represents the name of your S3 bucket.

Inside the `.pulumi` folder, we access the following subdirectories:

1. `meta.yaml`: This is the metadata file. It does not hold information about the stacks but rather information about the backend itself.
1. `stacks/`: Active state files for each stack (e.g. `dev.json` or `proj/dev.json` if the stack is scoped to a project).
1. `locks/`: Optional lock files for each stack if the stack is currently being operated on by a Pulumi operation (e.g. `dev/$lock.json` or `proj/dev/$lock.json` where `$lock` is a unique identifier for the lock).
1. `history/`: History for each stack (e.g. `dev/dev-$timestamp.history.json` or `proj/dev/dev-$timestamp.history.json` where `$timestamp` records the time the history file was created).

The detailed format of the `<backend-url>` differs by backend and each has different options such as how to authenticate, as described below.

### Local Filesystem

To use the filesystem backend to store your state files locally on your machine, pass the `--local` flag when logging in:

```sh
$ pulumi login --local
```

You will see `Logged into <my-machine> as <my-user> (file://~)` as a result where `<my-machine>` and `<my-user>` are your configured machine and user names, respectively. All subsequent stack state will be stored as JSON files locally on your machine.

The default directory for these JSON files is `~/.pulumi`. To store state files in an alternative location, specify a `file://<path>` URL instead, where `<path>` is the full path to the target directory where state files will be stored. For instance, to store state underneath `/app/data/.pulumi/` instead, run:

```sh
$ pulumi login file:///app/data
```

> **Note:** If you use a relative path (e.g. `file://./einstein`), it will be relative to _the current working directory_.

Notice that `pulumi login --local` is syntactic sugar for `pulumi login file://~`.

### AWS S3

To use the [AWS S3](https://aws.amazon.com/s3/) backend, pass the `s3://<bucket-name>` as your `<backend-url>`:

```sh
$ pulumi login s3://<bucket-name>
```

{{% notes type="info"%}}
As of Pulumi CLI v3.33.1, instead of specifying the AWS Profile, add `awssdk=v2` along with the region and profile to the query string. The URL should be quoted to escape the shell operator `&`, and used as follows:

```sh
pulumi login 's3://<bucket-name>?region=us-east-1&awssdk=v2&profile=<profile-name>'
```

{{% /notes %}}

{{% notes type="info"%}}
The `bucket-name` value can include multiple folders, such as `my-bucket/app/project1`. This is useful when storing multiple projects' state in the same bucket.
{{% /notes %}}

To configure credentials and authorize access, please see the [AWS Session documentation](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/). For additional configuration options, see [AWS Setup](/registry/packages/aws/installation-configuration/). If you're new to AWS S3, see [the AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html).

This backend also supports [alternative object storage servers with AWS S3 compatible REST APIs](https://en.wikipedia.org/wiki/Amazon_S3#S3_API_and_competing_services), including [Minio](https://www.minio.io/), [Ceph](https://ceph.io/), or [SeaweedFS](https://github.com/chrislusf/seaweedfs). To use such a server, you may pass `endpoint`, `disableSSL`, and `s3ForcePathStyle` querystring parameters to your `<backend-url>`, as follows:

```sh
$ pulumi login 's3://<bucket-name>?endpoint=my.minio.local:8080&disableSSL=true&s3ForcePathStyle=true'
```

### Azure Blob Storage

To use the [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) backend, pass the `azblob://<container-path>` as your `<backend-url>`:

```sh
$ pulumi login azblob://<container-path>
```

To tell Pulumi what Azure storage account to use, set the `AZURE_STORAGE_ACCOUNT` environment variable. Also, set either `AZURE_STORAGE_KEY` or `AZURE_STORAGE_SAS_TOKEN` to authorize access. For additional configuration options, see [Azure Setup](/registry/packages/azure/installation-configuration/). If you're new to Azure Blob Storage, see [the Azure documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-cli).

{{% notes type="info"%}}
As of Pulumi CLI v3.41.1, instead of the environment variables above, Azure CLI authentication may be used by specifying the storage account in the URL like so after using `az login`:

```sh
$ pulumi login azblob://<container-path>?storage_account=account_name
```

{{% /notes %}}

{{% notes type="info"%}}
The Azure account must have the [Storage Blob Data Contributor role](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) or an equivalent role with permissions to read, write, and delete blobs.
{{% /notes %}}

### Google Cloud Storage

To use the [Google Cloud Storage](https://cloud.google.com/storage/) backend pass the `gs://<bucket-path>` as your `<backend-url>`:

```sh
$ pulumi login gs://<my-pulumi-state-bucket>
```

To configure credentials for this backend, see [Application Default Credentials](https://cloud.google.com/docs/authentication/production). For additional configuration options, see [Google Cloud Setup](/registry/packages/gcp/installation-configuration/). If you're new to Google Cloud Storage, see [the Google Cloud documentation](https://cloud.google.com/storage/docs/quickstarts).

### Scoping

Versions of Pulumi prior to v3.61.0 placed stacks in a global namespace in self-managed backends. This meant that you couldn't share stack names (e.g. `dev`, `prod`, `staging`) across multiple projects in the same self-managed backend. With Pulumi v3.61.0 and later, stacks created in new or empty self-managed backends are scoped by project by default&mdash;same as the Pulumi Cloud backend.

Existing self-managed backends will continue to use the global namespace for stacks. You can upgrade an existing self-managed backend to use project-scoped stacks using the `pulumi state upgrade` command. This command will upgrade all stacks in the backend to be scoped by project.

{{% notes type="info"%}}
`pulumi state upgrade` will make upgraded stacks inaccesible to older versions of Pulumi. This is a one-way operation. Once you have upgraded your backend, you cannot downgrade to the previous version.
{{% /notes %}}

## Migrating Between State Backends

It is possible to start with one backend and then later migrate to another. This is common if you have began your project with Pulumi using a self-managed backend but later decided to adopt the Pulumi Cloud for easier use within your team. This section describes how to perform this operation, however, if you would like our assistance with a migration, [please get in touch](/contact/).

The state for a stack includes information about its backend as well as other unique information such as its encryption provider. As such, moving a stack between backends isn't as simple as merely copying its state file. The [`pulumi stack rename` command](/docs/cli/commands/pulumi_stack_rename) can be used for simple renames within the same backend; however, Pulumi also supports migrating stacks between backends using the `pulumi stack export` and `pulumi stack import` commands, which understand how to perform the necessary translations.

As an example, imagine you'd like to migrate a stack named `my-app-production` from a self-managed backend to the Pulumi Cloud backend. To perform the migration, run the following sequence commands:

```sh
# switch to the backend/stack we want to export
$ pulumi login --local
$ pulumi stack select my-app-production

# export the stack's state to a local file
$ pulumi stack export --show-secrets --file my-app-production.stack.json

# logout and login to the desired new backend
$ pulumi logout
$ pulumi login # default to Pulumi Cloud

# create a new stack with the same name on pulumi.com
$ pulumi stack init my-app-production

# import the new existing state into pulumi.com
$ pulumi stack import --file my-app-production.stack.json
```

After performing these steps, your stack will now be under the management of the Pulumi Cloud. All subsequent operations should be performed using this new backend.

> **Note:**: After migration, your stack's state will be managed by the Pulumi Cloud backend, but the stack will continue using the same secrets provider. You can separately [change the secrets provider](/docs/concepts/secrets#changing-the-secrets-provider-for-a-stack) for your stack if needed.

## Advanced State

Pulumi is designed to abstract state management away from you so that you can operate in terms of declarative infrastructure as code. In certain advanced cases, you may want or need to interact with state more directly, especially when using self-managed backends. In those cases, the following sections may be helpful.

### Importing Existing Resources

Pulumi supports importing resources that were already created outside of Pulumi, such as resources created using the cloud console, a cloud CLI or SDK, or even another infrastructure as code tool. Resource metadata is imported into your Pulumi state and source code is generated in your chosen language to match that state.

To learn more about importing existing resources, see [Importing Infrastructure](/docs/using-pulumi/adopting-pulumi/import/).

### Checkpoints

Pulumi state is usually stored in a transactional snapshot called a _checkpoint_. Pulumi records checkpoints early and often as it executes so that Pulumi can operate reliably, similar to how database transactions work. The basic functions of state allow Pulumi to diff your program's goal state against the last known update, recover from failure, and destroy resources accurately to clean up afterwards. The checkpoint format augments this with additional failure recovery capabilities in the face of partial failure.

The Pulumi Cloud backends records every checkpoint so that it is possible to recover from exotic failure scenarios. Self-managed backends may have more trouble recovering from these situations as they typically store a singular Pulumi state file.

### State Encryption

State is stored in your target backend in the form of checkpoints. In the case of the Pulumi Cloud backend, all remote communication is done over TLS and data is encrypted at rest.

### Secrets

A Pulumi "secret" can be used to store sensitive configuration values like database passwords and cloud tokens, and will always be handled safely. Pulumi understands the transitive usage of that secret in your state and will ensure everything it touches is encrypted, no matter which backend you've chosen.

A secret can be created one of two ways: passing `--secret` to the `pulumi config set` command, or by [creating one programmatically](/docs/concepts/secrets#secrets). In both cases, the value is encrypted using your stack's chosen encryption provider. By default with the Pulumi Cloud, a server-side HMS key is used, but you may customize the encryption provider if you'd like more control over keys, rotation, and so on.

To learn more about available encryption providers and how to customize your stack's, see [Configuring Secrets Encryption](/docs/concepts/secrets#configuring-secrets-encryption).

### Exporting and Importing State

The `pulumi stack export` and `pulumi stack import` commands can be used to export the latest or a specific version of a stack's state. This can be used to inspect or even manually edit the contents for advanced use cases. For more information on usage, [refer to the CLI documentation](/docs/cli/commands/pulumi_stack/).

### Editing State Manually

Although Pulumi was designed to shield you from manually needing to manage state, there are some circumstances where you will want or need to. This includes certain catastrophic failure scenarios, adding, deleting, renaming resources, and other advanced scenarios.

The Pulumi state file uses a relatively easy to understand JSON format. The precise JSON format these state files use is not documented, but is defined in the [APIType source code](https://github.com/pulumi/pulumi/tree/master/sdk/go/common/apitype/). The [`state` command](/docs/cli/commands/pulumi_state) also includes some helpful commands to edit your state.
