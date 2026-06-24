---
title_tag: "State and Backends | Pulumi Concepts"
meta_desc: Learn about how Pulumi manages infrastructure state, supported backend options, and how to use pulumi refresh to synchronize state with your cloud provider.
title: "State & backends"
h1: Managing state & backend options
keywords:
 - IaC
 - infrastructure state
 - state backend
 - pulumi refresh
 - drift detection
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: State & backends
        parent: iac-concepts
        weight: 70
    concepts:
        weight: 9

aliases:
- /docs/reference/state/
- /docs/intro/concepts/state/
- /docs/concepts/state/
- /docs/iac/concepts/state
---

Pulumi stores metadata about your infrastructure so that it can manage your cloud resources. This metadata is called _state_. Each [stack](/docs/concepts/stack/) has its own state, and state is how Pulumi knows when and how to create, read, delete, or update cloud resources.

Pulumi stores state in a _backend_ of your choosing. A backend is an API and storage endpoint used by the CLI to coordinate updates, and read and write stack state whenever appropriate. Backend options include Pulumi Cloud, an easy-to-use, secure, and reliable hosted application with policies and safeguards to facilitate team collaboration, in addition to simple object storage in AWS S3, Microsoft Azure Blob Storage, Google Cloud Storage, any AWS S3 compatible server such as Minio or Ceph, or a local filesystem.

The default experience is to use the hosted Pulumi Cloud, which takes care of the state and backend details for you. Conversely, when using cloud storage or a local filesystem as your backend, you gain control over where your state is located at the expense of having to handle security, state management, auditing, and other concerns Pulumi Cloud would otherwise handle for you.

{{% notes "info" %}}
Pulumi state does not include your cloud credentials. Credentials are kept local to your client &mdash; wherever the CLI runs &mdash; even when using the managed Pulumi Cloud backend. Pulumi _does_ store configuration and secrets, but encrypts those secrets using your chosen encryption provider. To learn more, see [Configuration and Secrets](/docs/concepts/secrets/).

This page covers the technical details of state management and backend configuration. To understand the benefits and features of Pulumi Cloud versus DIY backends, see [Pulumi Cloud vs. OSS](/docs/iac/guides/basics/pulumi-cloud-vs-oss/).
{{% /notes %}}

## Choosing a state backend

Pulumi supports two classes of state backend:

- **Pulumi Cloud**: a managed backend using the online or self-hosted Pulumi Cloud application. It is the default backend and requires no additional configuration after [installing the CLI](/docs/install/).
- **DIY backend**: a "Do It Yourself" backend that stores state in an object store you manage—AWS S3, Azure Blob Storage, Google Cloud Storage, an S3-compatible server such as Minio or Ceph, a PostgreSQL database, or your local filesystem.

Pulumi's SDK works with all backends, although some details differ between them. For a full comparison of the two options—including the operational concerns each one entails—see [Pulumi Cloud vs. OSS](/docs/iac/guides/basics/pulumi-cloud-vs-oss/). For DIY backend setup instructions, see [Using a DIY backend](/docs/iac/operations/stack-management/using-a-diy-backend/).

## Logging into and out of State Backends

The [`login` command](/docs/iac/cli/commands/pulumi_login) logs you into a backend:

```sh
$ pulumi login
```

The [`logout` command](/docs/iac/cli/commands/pulumi_logout) logs you out of the current backend.

```sh
$ pulumi logout
```

This will remove the credentials for the current backend from `~/.pulumi/credentials.json` and you will need to log in again before performing any subsequent stack or state operations. To remove credentials for all backends at once, use `pulumi logout --all`.

To change backends, run `pulumi logout` followed by `pulumi login`.

The basic form of `login` will use Pulumi Cloud by default. If you wish to log in to a specific backend, pass the backend-specific URL as the sole argument:

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

For details on the various backend URL formats and options, see the Pulumi Cloud backend section below and [Using a DIY backend](/docs/iac/operations/stack-management/using-a-diy-backend/).

If you forget to log in, you will be automatically prompted to do so before you do anything that requires stacks or state.

After logging in, your credentials are recorded in the `~/.pulumi/credentials.json` file, and all subsequent operations will use the chosen backend. From time to time, you will see a helpful URL to your update or stack pages. For example, after an update completes, you will see a link to that update's details. You can always go there to see a full history of updates.

If you ever want to check what user is logged in, use the [`whoami` command](/docs/iac/cli/commands/pulumi_whoami). To additionally see what  backend is currently being used, pass the `--verbose` (or `-v`) flag:

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

To view your access tokens, or create a new one manually, view the <a href="https://app.pulumi.com/account/tokens">Access Tokens</a> page.  You will see a list of past tokens, when they were last used, as well as the ability to revoke them.

To log into a self-hosted instance of Pulumi Cloud, pass its API URL to the `login` command:

```sh
$ pulumi login https://pulumi.acmecorp.com
```

Everything works the same as with the standard Pulumi Cloud, except that Pulumi will target your private instance instead of the shared one hosted at `app.pulumi.com`.

To learn how the Pulumi Cloud backend is designed—including why it never needs your cloud credentials—see [Pulumi Cloud architecture](/docs/iac/guides/basics/how-pulumi-works/#pulumi-cloud-architecture). If you are interested in hosting your own instance, see [Self-Hosted Pulumi Cloud](/docs/pulumi-cloud/self-hosted/).

## Using a DIY backend

You can manage state yourself with a DIY backend that stores state in AWS S3, Azure Blob Storage, Google Cloud Storage, an S3-compatible server, a PostgreSQL database, or your local filesystem. For setup instructions and per-backend configuration details, see [Using a DIY backend](/docs/iac/operations/stack-management/using-a-diy-backend/).

## Migrating Between State Backends

It is possible to start with one backend and then later migrate to another. This is common if you have began your project with Pulumi using a DIY backend but later decided to adopt Pulumi Cloud for easier use within your team. This section describes how to perform this operation, however, if you would like our assistance with a migration, [please get in touch](/contact/).

The state for a stack includes information about its backend as well as other unique information such as its encryption provider. As such, moving a stack between backends isn't as simple as merely copying its state file. The [`pulumi stack rename` command](/docs/iac/cli/commands/pulumi_stack_rename) can be used for simple renames within the same backend; however, Pulumi also supports migrating stacks between backends using the `pulumi stack export` and `pulumi stack import` commands, which understand how to perform the necessary translations.

As an example, imagine you'd like to migrate a stack named `my-app-production` from a DIY backend to the Pulumi Cloud backend. To perform the migration, run the following sequence commands:

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

After performing these steps, your stack will now be under the management of Pulumi Cloud. All subsequent operations should be performed using this new backend.

{{% notes type="info" %}}
After migration, your stack's state will be managed by the Pulumi Cloud backend, but the stack will continue using the same secrets provider. You can separately [change the secrets provider](/docs/concepts/secrets#changing-the-secrets-provider-for-a-stack) for your stack if needed.
{{% /notes %}}

## Refreshing state

Pulumi's state records what your infrastructure looked like after the last `pulumi up` or `pulumi refresh`. When you run `pulumi preview` or `pulumi up`, Pulumi compares this recorded state against the configuration declared in your program to determine which changes need to be made. It does not query each resource directly from your cloud provider on every run.

This means that if someone modifies a resource _outside_ of Pulumi (by editing it in the cloud provider's console, applying a change with a provider CLI, or by some other out-of-band means), that change is not automatically reflected in Pulumi's state. The next `pulumi up` or `pulumi preview` will not account for those changes, and may produce unexpected results including overwriting them.

### Why Pulumi does not refresh automatically

Pulumi intentionally does not refresh state before every operation, for several reasons:

- **Performance**: Querying every resource's live state from the cloud provider can be slow, particularly for large stacks with hundreds or thousands of resources. Doing this implicitly on every `pulumi up` or `pulumi preview` would add significant latency for the typical case where no out-of-band changes have been made.
- **Explicit control**: Pulumi treats your program as the source of truth for desired state. Automatically reconciling out-of-band changes before each operation could cause your program and your actual infrastructure to diverge silently, or could cause Pulumi to preserve changes you intended to overwrite.
- **Predictability**: Keeping refresh explicit means you decide when and whether to incorporate external changes versus overwrite them, giving you confidence about what each `pulumi up` will do.

### Running `pulumi refresh`

To synchronize Pulumi's recorded state with the actual state of your cloud resources, run:

```sh
$ pulumi refresh
```

This command queries each resource in your stack from the cloud provider and updates Pulumi's state file to reflect any differences. If a resource has been deleted outside of Pulumi, Pulumi removes it from the state. If properties have changed, Pulumi updates the state to match.

`pulumi refresh` updates only the state. It does not modify your Pulumi program or apply any changes to your infrastructure. If you want to preserve external changes going forward, you also need to update your program to reflect the new configuration; otherwise, the next `pulumi up` will attempt to revert those properties back to what your program declares.

Run `pulumi refresh` when:

- Resources have been modified or deleted outside of Pulumi, such as through the cloud console or another tool.
- You are troubleshooting unexpected diffs during a `pulumi preview` and suspect the state may be stale.
- You want to verify that Pulumi's recorded state accurately reflects reality before running a `pulumi destroy`.

### Refreshing as part of an update

To refresh state and then apply your program's desired state in a single step, pass the `--refresh` flag to `pulumi up`:

```sh
$ pulumi up --refresh
```

Similarly, to preview what an update would look like after first refreshing state:

```sh
$ pulumi preview --refresh
```

### Automated drift detection

For teams that want to detect and remediate out-of-band changes on a schedule, Pulumi Cloud provides built-in [drift detection and remediation](/docs/deployments/concepts/drift/). With drift detection configured, Pulumi Cloud periodically runs `pulumi refresh` against your stacks and alerts you (or optionally remediates automatically) when the actual state of your infrastructure diverges from Pulumi's recorded state.

To learn more, see [Drift detection](/docs/deployments/concepts/drift/) for the Pulumi Cloud feature, and [Detecting and reconciling drift](/docs/iac/operations/stack-management/drift/) for the CLI-side workflow (remediation vs. adoption, GitOps continuous reconciliation, and false-positive reduction).

## Advanced State

Pulumi is designed to abstract state management away from you so that you can operate in terms of declarative infrastructure as code. In certain advanced cases, you may want or need to interact with state more directly, especially when using DIY backends. In those cases, the following sections may be helpful.

### Importing Existing Resources

Pulumi supports importing resources that were already created outside of Pulumi, such as resources created using the cloud console, a cloud CLI or SDK, or even another infrastructure as code tool. Resource metadata is imported into your Pulumi state and source code is generated in your chosen language to match that state.

To learn more about importing existing resources, see [Importing Infrastructure](/docs/using-pulumi/adopting-pulumi/import/).

### Checkpoints

Pulumi state is usually stored in a transactional snapshot called a _checkpoint_. Pulumi records checkpoints early and often as it executes so that Pulumi can operate reliably, similar to how database transactions work. The basic functions of state allow Pulumi to diff your program's goal state against the last known update, recover from failure, and destroy resources accurately to clean up afterwards. The checkpoint format augments this with additional failure recovery capabilities in the face of partial failure.

The Pulumi Cloud backend records every checkpoint through a transactional API, making it possible to recover from unusual failure scenarios such as network interruptions during updates. DIY backends also maintain checkpoint history (in the `.pulumi/history/` directory), but blob storage backends use a less transactional protocol that may have more difficulty recovering from partial failures.

### State Encryption

State is stored in your target backend in the form of checkpoints. In the case of the Pulumi Cloud backend, all remote communication is done over TLS and data is encrypted at rest.

### Secrets

A Pulumi "secret" can be used to store sensitive configuration values like database passwords and cloud tokens, and will always be handled safely. Pulumi understands the transitive usage of that secret in your state and will ensure everything it touches is encrypted, no matter which backend you've chosen.

A secret can be created one of two ways: passing `--secret` to the `pulumi config set` command, or by [creating one programmatically](/docs/concepts/secrets#secrets). In both cases, the value is encrypted using your stack's chosen encryption provider. By default with Pulumi Cloud, a server-side HSM key is used, but you may customize the encryption provider if you'd like more control over keys, rotation, and so on.

To learn more about available encryption providers and how to customize your stack's, see [Configuring Secrets Encryption](/docs/concepts/secrets#configuring-secrets-encryption).

### Exporting and Importing State

The `pulumi stack export` and `pulumi stack import` commands can be used to export the latest or a specific version of a stack's state. This can be used to inspect or even manually edit the contents for advanced use cases. For more information on usage, [refer to the CLI documentation](/docs/iac/cli/commands/pulumi_stack/).

### Editing State Manually

Although Pulumi was designed to shield you from manually needing to manage state, there are some circumstances where you will want or need to. This includes certain catastrophic failure scenarios, adding, deleting, renaming resources, and other advanced scenarios.

The Pulumi state file uses a relatively easy to understand JSON format. The precise JSON format these state files use is not documented, but is defined in the [APIType source code](https://github.com/pulumi/pulumi/tree/master/sdk/go/common/apitype/). The [`state` command](/docs/iac/cli/commands/pulumi_state) also includes some helpful commands to edit your state.
