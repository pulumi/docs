---
title: State and Backends
meta_desc: Learn about how Pulumi handles your infrastructure state files and supported backend options for these state files.
keywords:
 - IaC
 - infrastructure state
 - state backend
menu:
  intro:
    parent: concepts
    weight: 5

aliases: ["/docs/reference/state/"]
---

Pulumi stores metadata about your infrastructure so that it can manage your cloud resources. This metadata is called _state_. Each [stack]({{< relref "stack" >}}) has its own state, and state is how Pulumi knows when and how to create, read, delete, or update cloud resources.

Pulumi stores state in a _backend_ of your choosing. A backend is an API and storage endpoint used by the CLI to coordinate updates, and read and write stack state whenever appropriate. Backend options include the Pulumi Service, an easy-to-use, secure, and reliable hosted application with policies and safeguards to facilitate team collaboration, in addition to simple object storage in AWS S3, Microsoft Azure Blob Storage, Google Cloud Storage, any AWS S3 compatible server such as Minio or Ceph, or a local filesystem.

The default experience is to use the hosted Pulumi Service, which takes care of the state and backend details for you. Conversely, when using cloud storage or a local filesystem as your backend, you gain control over where your state is located at the expense of having to handle security, state management, auditing, and other concerns the Pulumi Service would otherwise handle for you.

> Pulumi state does not include your cloud credentials. Credentials are kept local to your client &mdash; wherever the CLI runs &mdash; even when using the managed Pulumi Service backend. Pulumi _does_ store configuration and secrets, but encrypts those secrets using your chosen encryption provider. To learn more, see [Configuration and Secrets]({{< relref "config" >}}).

## Backends

Pulumi supports two classes of  _backends_ for storing your infrastructure state:

- **Service**: a managed cloud experience using the online or self-hosted Pulumi Service application
- **Self-Managed**: a manually managed object store, including AWS S3, Azure Blob Storage, Google Cloud Storage, any AWS S3 compatible server such as Minio or Ceph, or your local filesystem

Pulumi's SDK works great with all backends, although some details differ between them.

### Deciding On a Backend

Pulumi uses the Service backend hosted at <a href="https://app.pulumi.com" target="_blank">`app.pulumi.com`</a> by default as it provides the best combination of usability, safety, and security for most users. Important features include:

- Robust state management, with transactional checkpointing for fault tolerance and recovery
- Concurrent state locking to prevent corrupting your infrastructure state in a team environment
- Full deployment history for auditing and rollback purposes
- Encrypted state in transit and at rest
- Managed encryption and key management for secrets
- Secure access to cloud resource metadata, with client-side authentication to your cloud provider
- Team policies, including Policy as Code and Role Based Access Control (RBAC)

The Pulumi Service backend requires no additional configuration after [installing the CLI]({{< relref "/docs/get-started/install" >}}). Pulumi offers this backend hosted online free for individuals, with [advanced tiers]({{< relref "/pricing" >}}) available for teams and enterprises (with <a href="https://app.pulumi.com/site/trial" target="_blank">free trials</a>). It has successfully undergone multiple security audits including SOC2, pen-testing, and more.

> To learn more about the Pulumi Service backend's design, including why it doesn't need your cloud credentials, see [Pulumi Service Architecture](#pulumi-service-architecture). If you are interested in the hosting your own instance, see the [Self-Hosting User Guide]({{< relref "/docs/guides/self-hosted" >}}).

Pulumi also lets you manage state yourself using a self-managed backend. Your state is stored as simple JSON files in AWS S3, Azure Blob Store, Google Cloud Storage, an alternative AWS S3 API compatible server such as Minio or Ceph, or on your local filesystem. These self-managed backends are all open source and free to use in any setting. Using a self-managed backend trades off some amount of reliability for additional control over where metadata is stored. For instance, you will need to manually configure secure access, encryption, and history, and devise your own concurrency control and recovery capabilities. To choose a self-managed backend, use the `pulumi login` command [as documented below](#logging-into-a-self-managed-backend).

### Logging In

The [`login` command]({{< relref "/docs/reference/cli/pulumi_login" >}}) logs you into a backend:

```sh
$ pulumi login
```

The basic form of `login` will use the Pulumi Service by default. If you wish to log in to a specific backend, pass the backend-specific URL as the sole argument:

```sh
$ pulumi login <backend-url>
```

Alternatively, you may set the `PULUMI_BACKEND_URL` environment variable to avoid needing to type it each time.

For details on the various backend URL formats and options, please see the following sections:

- [Pulumi Service (default)](#logging-into-the-pulumi-service-backend)
- [Pulumi Self-Hosted Service](#logging-into-a-self-hosted-pulumi-service-backend)
- [Local Filesystem](#logging-into-the-local-filesystem-backend)
- [AWS S3 (or compatible server)](#logging-into-the-aws-s3-backend)
- [Azure Blob Storage](#logging-into-the-azure-blob-storage-backend)
- [Google Cloud Storage](#logging-into-the-google-cloud-storage-backend)

If you forget to log in, you will be automatically prompted to do so before you do anything that requires stacks or state.

After logging in, your credentials are recorded in the `~/.pulumi/credentials.json` file, and all subsequent operations will use the chosen backend. From time to time, you will see a helpful URL to your update or stack pages. For example, after an update completes, you will see a link to that update's details. You can always go there to see a full history of updates.

If you ever want to check what user is logged in, use the [`whoami` CLI command]({{< relref "/docs/reference/cli/pulumi_whoami" >}}). To additionally see what  backend is currently being used, pass the `--verbose` (or `-v`) flag:

```bash
$ pulumi whoami -v
User: <your-username>
Backend URL: https://app.pulumi.com/<your-username>
```

#### Logging Into the Pulumi Service Backend

Running `pulumi login` without any argument will log into the default Pulumi Service backend:

```sh
$ pulumi login
```

This will display a prompt that asks for an access token:

```
Manage your Pulumi stacks by logging in.
Run `pulumi login --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account/tokens
    or hit <ENTER> to log in using your browser:
```

To automatically generate and use a new access token, hit `<ENTER>`. This will open a web browser to interact with the service and request a token. If this is your first time using the service, you will be asked to authenticate using your chosen identity provider (GitHub, GitLab, Atlassian, SAML/SSO, or email).

To view your access tokens, or create a new one manually, view the <a href="https://app.pulumi.com/account/tokens" target="_blank">Access Tokens</a> page.  You will see a list of past tokens, when they were last used, as well as the ability to revoke them.

<img src="/images/docs/reference/state_tokens.png" alt="Pulumi.com Tokens Page" class="img-bordered">

##### Logging Into a Self-Hosted Pulumi Service Backend

To log into a self-hosted instance of the Pulumi Service, pass its API URL to the `login` command:

```sh
$ pulumi login https://pulumi.acmecorp.com
```

Everything works the same as with the standard Pulumi Service, except that Pulumi will target your private instance instead of the shared one hosted at `app.pulumi.com`.

#### Logging Into a Self-Managed Backend

The filesystem and cloud storage backends allow you to store state locally on your machine or remotely within a cloud object store. For self-managed backends, state management including backup, sharing, and team access synchronization is custom and implemented manually.

> **Note**: The Pulumi Service backend was designed to be robust and easy to use. If you decide to use a self-managed backend, you will need to be more aware of how state works (see [Advanced State](#advanced-state)). If you lose the checkpoint for your stack, or it drifts from reality, Pulumi will not behave as you might expect &mdash; for instance, if your state file is empty, Pulumi will think your stack is empty, and will attempt to recreate all of the resources. Some commands may also behave slightly differently between backends. For example, the Pulumi Service ensures there are no other updates in flight for a given stack, and in general, reliability, security, and collaboration is automatic with the Pulumi Service.

To use a self-managed backend, specify a storage endpoint URL as `pulumi login`'s `<backend-url>` argument: `s3://<bucket-path>`, `azblob://<container-path>`, `gs://<bucket-path>`, or `file://<fs-path>`. This will tell Pulumi to store state in AWS S3, Azure Blob Storage, Google Cloud Storage, or the local filesystem, respectively. Checkpoint files are stored in a relative`.pulumi` directory. For example, if you were using the Amazon S3 self-managed backend, your checkpoint files would be stored at `s3://my-pulumi-state-bucket/.pulumi` where `my-pulumi-state-bucket` represents the name of your S3 bucket.

The detailed format of the `<backend-url>` differs by backend and each has different options such as how to authenticate, as described below.

##### Logging Into the Local Filesystem Backend

To use the filesystem backend to store your checkpoint files locally on your machine, pass the `--local` flag when logging in:

```sh
$ pulumi login --local
```

You will see `Logged into <my-machine> as <my-user> (file://~)` as a result where `<my-machine>` and `<my-user>` are your configured machine and user names, respectively. All subsequent stack state and checkpoints will be store as JSON files locally on your machine.

The default directory for these JSON files is `~/.pulumi`. To store checkpoint files in an alternative location, specify a `file://<path>` URL instead, where `<path>` is the full path to the target directory where state files will be stored. For instance, to store state underneath `/app/data/.pulumi/` instead, run:

```sh
$ pulumi login file:///app/data
```

> **Note:** If you use a relative path (e.g. `file://./einstein`), it will be relative to _the current working directory_.

Notice that `pulumi login --local` is simply syntactic sugar for `pulumi login file://~`.

##### Logging Into the AWS S3 Backend

To use the [AWS S3](https://aws.amazon.com/s3/) backend, pass the `s3://<bucket-path>` as your `<backend-url>`:

```sh
$ pulumi login s3://<bucket-path>
```

To configure credentials and authorize access, please see the [AWS Session documentation](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/). For additional configuration options, see [AWS Setup]({{< relref "/docs/intro/cloud-providers/aws/setup" >}}). If you're new to AWS S3, see [the AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html).

This backend also supports [alternative object storage servers with AWS S3 compatible REST APIs](https://en.wikipedia.org/wiki/Amazon_S3#S3_API_and_competing_services), including [Minio](https://www.minio.io/), [Ceph](https://ceph.io/), or [SeaweedFS](https://github.com/chrislusf/seaweedfs). To use such a server, you may pass `endpoint`, `disableSSL`, and `s3ForcePathStyle` querystring parameters to your `<backend-url>`, as follows:

```sh
$ pulumi login s3://<bucket-path>?endpoint=my.minio.local:8080&disableSSL=true&s3ForcePathStyle=true
```

##### Logging Into the Azure Blob Storage Backend

To use the [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) backend, pass the `azblob://<container-path>` as your `<backend-url>`:

```sh
$ pulumi login azblob://<container-path>
```

To tell Pulumi what Azure storage account to use, set the `AZURE_STORAGE_ACCOUNT` environment variable. Also, set either `AZURE_STORAGE_KEY` or `AZURE_STORAGE_SAS_TOKEN` to authorize access. For additional configuration options, see [Azure Setup]({{< relref "/docs/intro/cloud-providers/azure/setup" >}}). If you're new to Azure Blob Storage, see [the Azure documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-cli).

##### Logging Into the Google Cloud Storage Backend

To use the [Google Cloud Storage](https://cloud.google.com/storage/) backend pass the `gs://<bucket-path>` as your `<backend-url>`:

```sh
$ pulumi login gs://<my-pulumi-state-bucket>
```

To configure credentials for this backend, see [Application Default Credentials](https://cloud.google.com/docs/authentication/production). For additional configuration options, see [GCP Setup]({{< relref "/docs/intro/cloud-providers/gcp/setup" >}}). If you're new to Google Cloud Storage, see [the Google Cloud documentation](https://cloud.google.com/storage/docs/quickstarts).

### Logging Out

To log out from your currently chosen backend, run the [`pulumi logout` CLI command]({{< relref "/docs/reference/cli/pulumi_logout" >}}). This will remove all credentials information from `~/.pulumi/credentials.json` and you will need to log in again before performing any subsequent stack or state operations.

To change backends, simply run `pulumi logout` followed by `pulumi login` with the desired backend (or just leave it blank for the default).

### Migrating Between Backends

It is possible to start with one backend and then later migrate to another. This is common if you have began your project with Pulumi using a self-managed backend but later decided to adopt the Pulumi Service for easier use within your team. This section describes how to perform this operation, however, if you would like our assistance with a migration, [please get in touch](/contact).

The state for a stack includes information about its backend as well as other unique information such as its encryption provider. As such, moving a stack between backends isn't as simple as merely copying its state file. The [`pulumi stack rename` command]({{< relref "/docs/reference/cli/pulumi_stack_rename" >}}) can be used for simple renames within the same backend; however, Pulumi also supports migrating stacks between backends using the `pulumi stack export` and `pulumi stack import` commands, which understand how to perform the necessary translations.

As an example, imagine you'd like to migrate a stack named `my-app-production` from a self-managed backend to the Pulumi Service backend. To perform the migration, run the following sequence commands:

```sh
# switch to the backend/stack we want to export
$ pulumi login --local
$ pulumi stack select my-app-production

# export the stack's checkpoint to a local file
$ pulumi stack export --show-secrets --file my-app-production.checkpoint.json

# logout and login to the desired new backend
$ pulumi logout
$ pulumi login # default to Pulumi Service

# create a new stack with the same name on pulumi.com
$ pulumi stack init my-app-production

# import the new existing checkpoint into pulumi.com
$ pulumi stack import --file my-app-production.checkpoint.json
```

After performing these steps, your stack will now be under the management of the Pulumi Service. All subsequent operations should be performed using this new backend.

> **Note:**: After migration, your stack's state will be managed by the the Pulumi Service backend, but the stack will continue using the same secrets provider. You can separately [change the secrets provider]({{< relref "docs/intro/concepts/config#changing-the-secrets-provider-for-a-stack" >}}) for your stack if needed.

### Pulumi Service Architecture

The Pulumi Service is comprised of two Internet-accessible endpoints &mdash; a web application at `app.pulumi.com` (called [the "Pulumi Console"]({{< relref "/docs/intro/console" >}})) and a REST API at `api.pulumi.com` &mdash; with an assortment of cloud infrastructure to support its features. A simplified diagram of its architecture looks like this:

<img src="/images/docs/reference/state_saas.png" alt="Pulumi Service Architecture" class="img-bordered">

The Pulumi Service doesn't ever acquire your cloud credentials, and does not communicate with your cloud provider directly. Instead, the CLI itself coordinates with both the Pulumi Service's API and your cloud provider's API directly. This ensures your IAM and key management does not need to change while adopting Pulumi. In particular, if you are running Pulumi deployments from [within a CI/CD environment]({{< relref "/docs/guides/continuous-delivery" >}}), you can rely on existing mechanisms and security practices that your organization has already put in place.

The Pulumi Service is reliable, secure, and has undergone multiple audits, including SOC2 and professional pen-testing. Because of the client/server division of responsibilities &mdash; notably that the server doesn't have direct access to your cloud credentials, runtime data, or PII &mdash; the Pulumi Service has been used in organizations with advanced compliance needs, including PCI, ISO 27001, HIPAA, and more. If you'd like to discuss any of these topics, please [contact us](/contact).

It is possible to host your own version of the Pulumi Service in your private cloud environment. Pulumi offers versions that run natively on AWS, Azure, GCP, Kubernetes, or simple virtual machine-based private and hybrid cloud environments. The architecture is very similar to the online version, but is privately hosted and does not depend on public access over the Internet:

<img src="/images/docs/reference/state_enterprise.png" alt="Pulumi Enterprise Architecture" class="img-bordered">

To learn more about self-host options, see [Self-Hosted Pulumi Service]({{< relref "/docs/guides/self-hosted" >}}) or [Contact Us]({{< relref "/pricing#contact" >}}).

## Advanced State

Pulumi is designed to abstract state management away from you so that you can operate in terms of declarative infrastructure as code. In certain advanced cases, you may want or need to interact with state more directly, especially when using self-managed backends. In those cases, the following sections may be helpful.

### Importing Existing Resources

Pulumi supports importing resources that were already created outside of Pulumi, such as resources created using the cloud console, a cloud CLI or SDK, or even another infrastructure as code tool. Resource metadata is imported into your Pulumi state and source code is generated in your chosen language to match that state.

To learn more about importing existing resources, see [Importing Infrastructure]({{< relref "/docs/guides/adopting/import" >}}).

### Checkpoints

Pulumi state is usually stored in a transactional snapshot called a _checkpoint_. Pulumi records checkpoints early and often as it executes so that Pulumi can operate reliably, similar to how database transactions work. The basic functions of state allow Pulumi to diff your program's goal state against the last known update, recover from failure, and destroy resources accurately to clean up afterwards. The checkpoint format augments this with additional failure recovery capabilities in the face of partial failure.

The Pulumi Service backends records every checkpoint so that it is possible to recover from exotic failure scenarios. Self-managed backends may have more trouble recovering from these situations as they typically store a singular Pulumi state file.

### State Encryption

State is stored in your target backend in the form of checkpoints. In the case of the Pulumi Service backend, all remote communication is done over TLS and data is encrypted at rest.

### Secrets

A Pulumi "secret" can be used to store sensitive configuration values like database passwords and cloud tokens, and will always be handled safely. Pulumi understands the transitive usage of that secret in your state and will ensure everything it touches is encrypted, no matter which backend you've chosen.

A secret can be created one of two ways: passing `--secret` to the `pulumi config set` command, or by [creating one programmatically]({{< relref "/docs/intro/concepts/secrets#secrets" >}}). In both cases, the value is encrypted using your stack's chosen encryption provider. By default with the Pulumi Service, a server-side HMS key is used, but you may customize the encryption provider if you'd like more control over keys, rotation, and so on.

To learn more about available encryption providers and how to customize your stack's, see [Configuring Secrets Encryption]({{< relref "config/#configuring-secrets-encryption" >}}).

### Exporting and Importing State

The `pulumi stack export` and `pulumi stack import` commands can be used to export the latest or a specific version of a stack's state. This can be used to simply inspect or even manually edit the contents for advanced use cases. For more information on usage, [refer to the CLI documentation]({{< relref "/docs/reference/cli/pulumi_stack" >}}).

### Editing State Manually

Although Pulumi was designed to shield you from manually needing to manage state, there are some circumstances where you will want or need to. This includes certain catastrophic failure scenarios, adding, deleting, renaming resources, and other advanced scenarios.

The Pulumi state file uses a relatively easy to understand JSON format. The precise JSON format these state files use is not documented, but is defined in the [APIType source code](https://github.com/pulumi/pulumi/tree/master/sdk/go/common/apitype/). The [`pulumi state` CLI command]({{< relref "/docs/reference/cli/pulumi_state" >}}) also includes some helpful commands to edit your state.
