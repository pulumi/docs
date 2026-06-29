---
title_tag: "Using a DIY Backend | Pulumi Operations"
meta_desc: Configure a self-managed Pulumi state backend with AWS S3, Azure Blob Storage, Google Cloud Storage, PostgreSQL, or the local filesystem.
title: Using a DIY Backend
h1: Using a DIY Backend
menu:
    iac:
        name: Using a DIY Backend
        parent: iac-operations-stack-management
        weight: 40
aliases:
- /docs/iac/guides/basics/using-a-diy-backend/
---

A DIY ("Do It Yourself") backend stores Pulumi [state](/docs/iac/concepts/state-and-backends/) in an object store or on your local machine instead of in Pulumi Cloud. The filesystem and cloud storage backends allow you to store state locally on your machine or remotely within a cloud object store. For DIY backends, state management—including backup, sharing, and team access synchronization—is custom and implemented manually. A basic file-based locking system is enabled by default for all DIY backends.

{{% notes "info" %}}
Both Pulumi Cloud and DIY backends provide reliable state management. DIY backends include built-in state locking and history tracking. However, most users find Pulumi Cloud to be the easiest way to get started and scale. Pulumi Cloud handles operational concerns automatically, including backup and recovery, team collaboration, RBAC, and audit logging. It also provides a transactional API that offers stronger guarantees than blob storage protocols. With DIY backends, you will need to implement your own backup procedures and manage access control. For a full comparison, see [Pulumi Cloud vs. OSS](/docs/iac/guides/basics/pulumi-cloud-vs-oss/). For advanced state management concepts, see [Advanced state](/docs/iac/concepts/state-and-backends/#advanced-state).
{{% /notes %}}

To use a DIY backend, specify a storage endpoint URL as `pulumi login`'s `<backend-url>` argument: `s3://<bucket-path>`, `azblob://<container-path>`, `gs://<bucket-path>`, or `file://<fs-path>`. This will tell Pulumi to store state in AWS S3, Azure Blob Storage, Google Cloud Storage, or the local filesystem, respectively. Checkpoint files are stored in a relative `.pulumi` directory. For example, if you were using the Amazon S3 DIY backend, your checkpoint files would be stored at `s3://my-pulumi-state-bucket/.pulumi` where `my-pulumi-state-bucket` represents the name of your S3 bucket.

Inside the `.pulumi` folder, we access the following subdirectories:

1. `meta.yaml`: This is the metadata file. It does not hold information about the stacks but rather information about the backend itself.
1. `stacks/`: Active state files for each stack (e.g. `dev.json` or `proj/dev.json` if the stack is scoped to a project).
1. `locks/`: Lock files for each stack if the stack is currently being operated on by a Pulumi operation (e.g. `dev/$lock.json` or `proj/dev/$lock.json` where `$lock` is a unique identifier for the lock).
1. `history/`: History for each stack (e.g. `dev/dev-$timestamp.history.json` or `proj/dev/dev-$timestamp.history.json` where `$timestamp` records the time the history file was created).

The detailed format of the `<backend-url>` differs by backend and each has different options such as how to authenticate. See the per-backend sections that follow.

## Local filesystem

To use the filesystem backend to store your state files locally on your machine, pass the `--local` flag when logging in:

```sh
$ pulumi login --local
```

You will see `Logged into <my-machine> as <my-user> (file://~)` as a result where `<my-machine>` and `<my-user>` are your configured machine and user names, respectively. Stack state will be stored as JSON files locally on your machine.

The default directory for these JSON files is `~/.pulumi`. To store state files in an alternative location, specify a `file://<path>` URL instead, where `<path>` is the full path to the target directory where state files will be stored. For instance, to store state underneath `/app/data/.pulumi/` instead, run:

```sh
$ pulumi login file:///app/data
```

{{% notes type="info" %}}
If you use a relative path (e.g. `file://./einstein`), it will be relative to _the current working directory_.
{{% /notes %}}

Notice that `pulumi login --local` is syntactic sugar for `pulumi login file://~`.

## AWS S3

To use the [AWS S3](https://aws.amazon.com/s3/) backend, pass the `s3://<bucket-name>` as your `<backend-url>`:

```sh
$ pulumi login s3://<bucket-name>
```

{{% notes type="info" %}}
As of Pulumi CLI v3.33.1, instead of specifying the AWS Profile, add `awssdk=v2` along with the region and profile to the query string. The URL should be quoted to escape the shell operator `&`, and used as follows:

```sh
pulumi login 's3://<bucket-name>?region=us-east-1&awssdk=v2&profile=<profile-name>'
```

{{% /notes %}}

{{% notes type="info" %}}
The `bucket-name` value can include multiple folders, such as `my-bucket/app/project1`. This is useful when storing multiple projects' state in the same bucket.
{{% /notes %}}

To configure credentials and authorize access, please see the [AWS Session documentation](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/). For additional configuration options, see [AWS Setup](/registry/packages/aws/installation-configuration/). If you're new to AWS S3, see [the AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html).

This backend also supports [alternative object storage servers with AWS S3 compatible REST APIs](https://en.wikipedia.org/wiki/Amazon_S3#S3_API_and_competing_services), including [Minio](https://www.minio.io/), [Ceph](https://ceph.io/), or [SeaweedFS](https://github.com/chrislusf/seaweedfs). To use such a server, you may pass `endpoint`, `disableSSL`, and `s3ForcePathStyle` querystring parameters to your `<backend-url>`, as follows:

```sh
$ pulumi login 's3://<bucket-name>?endpoint=my.minio.local:8080&disableSSL=true&s3ForcePathStyle=true'
```

### Required permissions

The S3 backend reads and writes state, lock, history, and metadata objects under the bucket's `.pulumi` prefix. Across the full stack lifecycle—`pulumi new`/`pulumi stack init`, `pulumi preview`, `pulumi up`, `pulumi refresh`, `pulumi destroy`, and `pulumi stack rm`—it needs exactly four S3 actions, and no more:

- `s3:ListBucket` to enumerate stacks and locks.
- `s3:GetObject` to read `meta.yaml`, stack state, and lock files.
- `s3:PutObject` to write stack state, history, and lock files.
- `s3:DeleteObject` to release locks and remove stacks.

Note that `s3:ListBucket` is a bucket-level action, so it must be granted on the bucket ARN (`arn:aws:s3:::<bucket-name>`), while the object-level actions are granted on the objects within it (`arn:aws:s3:::<bucket-name>/*`). The following least-privilege identity-based policy grants exactly what the backend requires:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PulumiStateBackendList",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::<bucket-name>"
        },
        {
            "Sid": "PulumiStateBackendObjects",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::<bucket-name>/*"
        }
    ]
}
```

The same four actions can be expressed as a [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) (add a `Principal` and use the bucket ARNs shown above) if you prefer to attach permissions to the bucket rather than to the calling identity. If you store multiple projects under a path prefix (for example, `s3://<bucket-name>/app/project1`), you can scope the object-level statement to that prefix—`arn:aws:s3:::<bucket-name>/app/project1/*`. S3-compatible servers such as Minio or Ceph require the equivalent read, write, list, and delete grants on the bucket.

## Azure Blob Storage

To use the [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) backend, pass the `azblob://<container-path>` as your `<backend-url>`:

```sh
$ pulumi login azblob://<container-path>
```

Set the `AZURE_STORAGE_ACCOUNT` environment variable to specify which Azure storage account to use. For authentication, you may set `AZURE_STORAGE_KEY` (a storage account access key) or `AZURE_STORAGE_SAS_TOKEN` (a shared access signature token). If neither is provided, the backend authenticates using [Azure SDK for Go's `DefaultAzureCredential`](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication), which attempts a series of methods in order, including managed identity, workload identity federation, service principal credentials (`AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`), and the Azure CLI. If you're new to Azure Blob Storage, see [the Azure documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-cli).

{{% notes type="info" %}}
This backend authenticates using [Azure SDK for Go](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication), not the Pulumi Azure provider's authentication mechanism. The Azure provider's environment variables — such as `ARM_TENANT_ID`, `ARM_CLIENT_ID`, and `ARM_USE_OIDC` — are not supported. Use the Azure SDK's own environment variables (`AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`) for service principal authentication.
{{% /notes %}}

{{% notes type="info" %}}
As of Pulumi CLI v3.41.1, you can also specify the storage account directly in the backend URL after authenticating with `az login`:

```sh
$ pulumi login azblob://<container-path>?storage_account=account_name
```

{{% /notes %}}

{{% notes type="info" %}}
The Azure account must have the [Storage Blob Data Contributor role](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) or an equivalent role with permissions to read, write, and delete blobs.
{{% /notes %}}

## Google Cloud Storage

To use the [Google Cloud Storage](https://cloud.google.com/storage/) backend pass the `gs://<bucket-path>` as your `<backend-url>`:

```sh
$ pulumi login gs://<my-pulumi-state-bucket>
```

To configure credentials for this backend, see [Application Default Credentials](https://cloud.google.com/docs/authentication/production). For additional configuration options, see [Google Cloud Setup](/registry/packages/gcp/installation-configuration/). If you're new to Google Cloud Storage, see [the Google Cloud documentation](https://cloud.google.com/storage/docs/quickstarts).

## PostgreSQL

To use the [PostgreSQL](https://www.postgresql.org/) backend pass the `postgres://<username>:<password>@<hostname>:<port>/<database>` as your `<backend-url>`:

```sh
$ pulumi login postgres://<username>:<password>@<hostname>:<port>/<database>
```

{{% notes type="warning" %}}
Avoid including credentials directly in commands. Consider using environment variables or other secure credential management methods.
{{% /notes %}}

For additional configuration options, see the [README ↗](https://github.com/pulumi/pulumi/blob/master/pkg/backend/diy/postgres/README.md).

## Scoping

Versions of Pulumi before v3.61.0 placed stacks in a global namespace in DIY backends. This meant that you couldn't share stack names (e.g. `dev`, `prod`, `staging`) across multiple projects in the same DIY backend. With Pulumi v3.61.0 and later, stacks created in new or empty DIY backends are scoped by project by default—same as the Pulumi Cloud backend.

Existing DIY backends will continue to use the global namespace for stacks. You can upgrade an existing DIY backend to use project-scoped stacks using the `pulumi state upgrade` command. This command will upgrade all stacks in the backend to be scoped by project.

{{% notes type="info" %}}
`pulumi state upgrade` will make upgraded stacks inaccessible to older versions of Pulumi. This is a one-way operation. Once you have upgraded your backend, you cannot downgrade to the previous version.
{{% /notes %}}

## Troubleshooting

### Error reading `.pulumi/meta.yaml`

When the Pulumi CLI can't access your DIY backend's storage, you'll see an error similar to one of these when you run `pulumi login`, `pulumi config`, or another command that reads state:

```
error: read ".pulumi\\meta.yaml": blob (key ".pulumi/meta.yaml") (code=Unknown): AccessDenied: Access Denied
        status code: 403
```

```
error: read ".pulumi\\meta.yaml": blob (key ".pulumi/meta.yaml") (code=Unknown): MissingRegion: could not find region configuration
```

`meta.yaml` is the first file Pulumi reads from a DIY backend, so this error almost always means the CLI reached the storage provider but couldn't authenticate or wasn't configured correctly—not that the file itself is missing or corrupt. The error is surfaced directly from the cloud provider's SDK, which is why it can be hard to interpret. Common causes:

- **Expired or invalid credentials.** Temporary credentials—such as those from AWS SSO, `aws sts assume-role`, or short-lived Azure service principal tokens—may have expired. Refresh your credentials and try the command again.
- **Insufficient permissions.** The identity in use can authenticate but lacks read/write access to the bucket or container. Confirm it has the permissions required to read, write, and delete blobs. For AWS S3, this means the four actions listed under [Required permissions](#required-permissions). For Azure Blob Storage, this means the [Storage Blob Data Contributor role](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) or an equivalent role.
- **Missing region configuration (AWS S3).** The AWS SDK can't determine which region the bucket is in. Specify the region in the backend URL—for example, `pulumi login 's3://<bucket-name>?region=us-east-1'`—or set the `AWS_REGION` environment variable before logging in.
- **Missing authentication environment variables.** DIY backends authenticate using the cloud provider's own SDK. Verify that the variables that SDK expects are set—see the section for your backend ([AWS S3](#aws-s3), [Azure Blob Storage](#azure-blob-storage), or [Google Cloud Storage](#google-cloud-storage)) above for the specifics.

To get more detail while diagnosing the problem, re-run the command with [CLI verbose logging](/docs/support/debugging/logging/#cli-verbose-logging) enabled.
