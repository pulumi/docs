---
title_tag: "Pulumi Deployments REST API Documentation"
meta_desc: Documentation for the Pulumi Deployments REST API including configuring settings and OIDC
title: "REST API docs"
h1: Pulumi Deployments REST API docs
menu:
  pulumicloud:
    parent: deployments
    weight: 7
aliases:
- /docs/reference/deployments-rest-api/
- /docs/intro/deployments/api/
---


The Pulumi Deployments REST API provides a fully-managed remote execution interface for your Pulumi programs.

{{% notes "info" %}}
Pulumi Deployments is currently in preview.

Please post any bug reports or feature requests in the [Service Requests repo](https://github.com/pulumi/service-requests/issues/new/choose).
{{% /notes %}}

## Authentication

All requests must be authenticated using a token via the `Authorization` HTTP header.

The `Authorization` header must be in the form below with the literal string `token`, then a space, then your access token value.

```
Authorization: token {token}
```

To view your access tokens, or create a new one, view the <a href="https://app.pulumi.com/account/tokens" target="_blank">Access Tokens</a> page. You will see a list of past tokens, when they were last used, and have the ability to revoke them.

The Pulumi Deployments REST API will return a 401 status code if the token is missing or invalid.

## Deployment Settings

Several endpoints accept or return deployment settings. Deployment settings are composed of several parts:

* An [ExecutorContext](#executorcontext) that defines information about the executor where the Pulumi operation is executed.
* A [SourceContext](#sourcecontext) that defines where the source code for your project is located. Currently, only git repos are supported.
* An [OperationContext](#operationcontext) that defines how the Pulumi project is to be executed (i.e. the Pulumi operation to execute and any associated context it requires).
* An optional [GitHub block](#github) that contains information for GitHub integration.

### ExecutorContext

The executor context defines information about the executor where the Pulumi operation is executed. If unspecified, the default [pulumi/pulumi](https://hub.docker.com/r/pulumi/pulumi) image is used.

* **executorImage** (Optional[string]): Allows overriding the default executor image with a custom image.

Image requirements:

* It must be a unix-based image which includes `curl`.
* It must include the `pulumi` CLI in its `$PATH`.
* It must include the required SDK runtime(s) for your Pulumi program.

{{% notes "info" %}}

Using a custom image may result in slower execution due to time spent pulling the image.

{{% /notes %}}

#### Example

```json
{
    "executorImage": "pulumi/pulumi-nodejs:latest"
}
```

### SourceContext

The source context contains information about where the source code for your project is located. Currently, only git repos are supported as a source.

* **repoURL** (Optional[string]): The URL of the git repository where the source code is located. Must not be specified if a [GitHub block](#github) is present.
* **branch** (Optional[string]): The repository branch to use.
* **repoDir** (Optional[string]): The directory where Pulumi.yaml is located, if not in the project source root.
* **commit** (Optional[string]): The hash of the commit to deploy. If used, HEAD will be in detached mode. This is mutually exclusive with the branch setting. Either value must be specified.
* **gitAuth** (Optional[object]): The authentication information for the git repo. If not specified, the repo is assumed to be public. Only one type is supported at a time.
    * **sshAuth** (Optional[object]): SSHAuth is the authentication information for the git repo
        * **sshPrivateKey** (Secret): The private key to use
        * **password** (Optional[Secret]): The password to use
    * **basicAuth** (Optional[object]): Basic auth information
        * **userName** (string): The username to use for authentication
        * **password** (Secret): The password to use for authentication

Secret types should have the following structure:

```json
  "key": { "secret": "value" }
```

#### Examples

##### No authentication required (public repo)

```json
{
  "git": {
    "repoURL": "https://github.com/pulumi/examples.git",
    "branch": "refs/heads/master",
    "repoDir": "aws-ts-s3-folder"
  }
}
```

##### Using SSH authentication

```json
{
  "git": {
    "repoURL": "https://github.com/pulumi/examples.git",
    "branch": "refs/heads/master",
    "repoDir": "aws-ts-s3-folder",
    "gitAuth": {
      "sshAuth": {
        "sshPrivateKey": {
          "secret": "myPrivateKey"
        },
        "password": {
          "secret": "myPassword"
        }
      }
    }
  }
}
```

##### Using basic authentication

```json
{
  "git": {
    "repoURL": "https://github.com/pulumi/examples.git",
    "branch": "refs/heads/master",
    "repoDir": "aws-ts-s3-folder",
    "gitAuth": {
      "basicAuth": {
        "userName": "myUserName",
        "password": {
          "secret": "myPassword"
        }
      }
    }
  }
}
```

##### Using an access token

```json
{
  "git": {
    "repoURL": "https://github.com/pulumi/examples.git",
    "branch": "refs/heads/master",
    "repoDir": "aws-ts-s3-folder",
    "gitAuth": {
      "basicAuth": {
        "userName": "git",
        "password": {
          "secret": "myAccessToken"
        }
      }
    }
  }
}
```

### OperationContext

The operation context describes any context required for Pulumi operations to execute such as pre-run commands and environment variables.

* **preRunCommands** (Optional[list[string]]): A list of commands to run before the Pulumi command is executed. Each command is run in a separate subshell. A command may export environment variables by writing
  them as `NAME=value` pairs to a file named `PULUMI_ENV`. For example, a pre-run command could set the `HELLO` environment variable to `world` as follows:

  ```sh
  echo HELLO=world >PULUMI_ENV
  ```

* **environmentVariables** (Optional[map[string]EnvironmentVariable]): A list of environment variables to set for the operation.
* **options** (Optional[OperationContextOptions]): Options is a bag of settings that allows you to set or override default behavior.

`OperationContextOptions` has the following structure:

* **skipInstallDependencies**: Allows you to skip the automated dependency installation. You can then customize your dependency installation step in `preRunCommands`.

`EnvironmentVariable` types can have either of the following structures:

```json
  "key": {
    "secret": "value" <-- secret environment variable
  },
  "key": "value" <-- plaintext environment variable
```

{{% notes "info" %}}

The following environment variables are used internally by Pulumi Deployments, and therefore should not be used as they will be overwritten:

* `PULUMI_CI_BUILD_URL`
* `PULUMI_CI_SYSTEM`
* `PULUMI_CI_BUILD_NUMBER`
* `PULUMI_CI_BUILD_ID`
* `PULUMI_ACCESS_TOKEN`
* `PULUMI_BACKEND_URL`

{{% /notes %}}

* **oidc** (Optional[OIDCConfiguration]): Allows the deployment to exchange an OIDC token for short-term credentials from a cloud provider.

`OIDCConfiguration` has the following structure:

* **aws** (Optional[AWSOIDCConfiguration]): Configures OIDC for AWS.
* **azure** (Optional[AzureOIDCConfiguration]): Configures OIDC for Azure.
* **gcp**: (Optional[GCPOIDCConfiguration]): Configures OIDC for GCP.

`AWSOIDCConfiguration` has the following structure:

* **duration** (Optional[string]): The duration of the assume-role session in "XhYmZs" format.
* **policyArns** (Optional[list[string]]): A set of IAM policy ARNs that further restrict the assume-role session.
* **roleArn** (string): The ARN of the role to assume using the OIDC token.
* **sessionName** (string): The name of the assume-role session.

`AzureOIDCConfiguration` has the following structure:

* **clientId** (string): The client ID of the federated workload identity.
* **tenantId** (string): The tenant ID of the federated workload identity.
* **subscriptionId** (string): The ID of the subscription to use.

`GCPOIDCConfiguration` has the following structure:

* **projectId** (string): The numerical ID of the Google Cloud project.
* **region** (Optional[string]): The region of the Google Cloud project.
* **workloadPoolId** (string): The ID of the workload pool to use.
* **providerId** (string): The ID of the identity provider associated with the workload pool.
* **serviceAccount** (string): The email address of the service account to use.
* **tokenLifetime** (Optional[string]): The lifetime of the temporary credentials in "XhYmZs" format.

#### Examples

##### Pre-run commands and environment variables

```json
{
  "preRunCommands": [
    "go get sigs.k8s.io/kind@v0.16.0"
  ],
  "environmentVariables": {
    "AWS_REGION": "us-east-2",
    "CUSTOM_VARIABLE": "foo",
    "MY_PASSWORD": {
      "secret": "my-secret-password"
    }
  }
}
```

##### Override default dependency installation step to use poetry

```json
{
  "preRunCommands": [
      "curl -sSL https://install.python-poetry.org | python3",
      "poetry install"
  ],
  "environmentVariables": {
      "POETRY_HOME": "/usr/local"
  },
  "options": {
    "skipInstallDependencies": true
  }
}
```

##### Override default dependency installation step to use a different version of node

```json
{
  "preRunCommands": [
    "node --version",
    "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash",
    "nvm use 17 && yarn"
  ],
  "environmentVariables": {
    "NODE_VERSION": "17"
  },
  "options": {
    "skipInstallDependencies": true
  }
}
```

##### Use OIDC with AWS

```json
{
  "environmentVariables": {
    "AWS_REGION": "us-west-2"
  },
  "oidc": {
    "aws": {
      "roleArn": "arn:aws:iam::123456789000:role/pulumi-deploy-role",
      "sessionName": "pulumi-deploy-session"
    }
  }
}
```

{{% notes "info" %}}

Environment variables may be automatically marked `secret` by the API even if they are not explicitly marked as such in the request if they "look" like secrets. We evaluate "secretness" based on specific key terms and the entropy of the associated value.

{{% /notes %}}

### GitHub

The GitHub block describes settings for Pulumi Deployments' GitHub integration.

* **repository** (string): The GitHub repository that contains the Pulumi program to deploy.
* **deployCommits** (boolean): True to run `update` deployments for each commit pushed to the configured branch.
* **previewPullRequests** (boolean): True to run `preview` deployments for each pull request that targets the configured branch.
* **paths** (Optional[list[string]]): A list of path filters that determine whether or not a commit or pull request should trigger a deployment based on the paths affected by the commit or pull request. Path
  filters may use the `*` and `**` elements to match a single path component or any number of path components, respectively. If a path filter begins with a `!`, it excludes matching paths rather than including
  matching paths. If all filters are excludes, there is an implicit `**` filter. A deployment will run if any non-excluded file is modified. Note that the list of changed paths returned by GitHub is limited to
  300 files. If there are files changed that aren't matched in the first 300 files returned by the filter, a deployment will not run. You may need to create additional filters so that a deployment will run.

#### Examples

##### Use GitHub integration for push-to-deploy and PR previews with path filters

```json
{
  "repository": "pulumi/deploy-demos",
  "deployCommits": true,
  "previewPullRequests": true,
  "paths": [ "pulumi-programs/bucket-time/**", "!pulumi/programs/bucket-time/README.md" ]
}
```

##### Use GitHub integration but disable push-to-deploy

```json
{
  "repository": "pulumi/deploy-demos",
  "deployCommits": false,
  "previewPullRequests": true,
  "paths": [ "pulumi-programs/bucket-time/**", "!pulumi/programs/bucket-time/README.md" ]
}
```

##### Use GitHub integration for source control only

```json
{
  "repository": "pulumi/deploy-demos",
}
```

## Endpoints

### Get Settings

Gets the [deployment settings](#deploymentsettings) associated with a stack.

```
GET https://api.pulumi.com/api/preview/{organization}/{project}/{stack}/deployment/settings
```

#### Example

##### Request

```shell
curl -XGET -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/preview/my-org/aws-ts-s3-folder/dev/deployment/settings"
```

##### Response

```json
{
  "sourceContext": {
    "git": {
      "repoURL": "https://github.com/pulumi/deploy-demos.git",
      "branch": "refs/heads/demo",
      "repoDir": "pulumi-programs/aws-ts-s3"
    }
  },
  "operationContext": {
    "preRunCommands": [
      "echo \"hello world\""
    ],
    "environmentVariables": {
      "AWS_REGION": "us-west-2",
      "AWS_ACCESS_KEY_ID": "$AWS_ACCESS_KEY_ID",
      "AWS_SECRET_ACCESS_KEY": "$AWS_SECRET_ACCESS_KEY",
      "AWS_SESSION_TOKEN": "$AWS_SESSION_TOKEN"
    }
  }
}
```

### Patch Settings

Patches the [deployment settings](#deploymentsettings) associated with a stack.

```
POST https://api.pulumi.com/api/preview/{organization}/{project}/{stack}/deployment/settings
```

The final settings for the stack are calculated by merging the settings present in the request with the stack's current settings according to the following rules:

* For object properties:
    * Start with a copy of the current property value
    * Remove all properties that are explicitly set to `null` in the patch value
    * Merge all non-`null` properties from the patch value that exist in the current property value
    * Add all non-`null` properties from the patch value that do not exist in the current property value
* For other propertries, replace the current value with the the patch value

For example, if the current settings for a stack are:

```json
{
  "sourceContext": {
    "git": {
      "repoURL": "https://github.com/pulumi/deploy-demos.git",
      "branch": "refs/heads/demo",
      "repoDir": "pulumi-programs/aws-ts-s3"
    }
  },
  "operationContext": {
    "preRunCommands": [
      "echo \"hello world\""
    ],
    "environmentVariables": {
      "AWS_REGION": "us-west-2",
      "AWS_ACCESS_KEY_ID": "$AWS_ACCESS_KEY_ID",
      "AWS_SECRET_ACCESS_KEY": "$AWS_SECRET_ACCESS_KEY",
      "AWS_SESSION_TOKEN": "$AWS_SESSION_TOKEN"
    }
  }
}
```

And we apply this patch:

```shell
curl -i -XPOST -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/preview/my-org/aws-ts-s3/dev/deployment/settings" \
-d '{
  "sourceContext": {
    "git": {
      "repoURL": null,
    }
  },
  "operationContext": {
    "preRunCommands": [
      "echo \"bonjour\""
    ],
    "environmentVariables": {
      "AWS_ACCESS_KEY_ID": null,
      "AWS_SECRET_ACCESS_KEY": null,
      "AWS_SESSION_TOKEN": null
    },
    "oidc": {
      "aws" {
        "roleArn": "my-role-arn",
        "sessionName": "pulumi-deploy"
      }
    }
  },
  "gitHub": {
    "repository": "pulumi/deploy-demos"
  }
}'
```

Then the new settings for the stack are:

```json
{
  "sourceContext": {
    "git": {
      "branch": "refs/heads/demo",
      "repoDir": "pulumi-programs/aws-ts-s3"
    }
  },
  "operationContext": {
    "preRunCommands": [
      "echo \"bonjour\""
    ],
    "environmentVariables": {
      "AWS_REGION": "us-west-2"
    }
    "oidc": {
      "aws" {
        "roleArn": "my-role-arn",
        "sessionName": "pulumi-deploy"
      }
    }
  },
  "gitHub": {
    "repository": "pulumi/deploy-demos"
  }
}
```

### Clear Settings

Clears the [deployment settings](#deploymentsettings) associated with a stack.

```
DELETE https://api.pulumi.com/api/preview/{organization}/{project}/{stack}/deployment/settings
```

#### Example

```shell
curl -i -XDELETE -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/preview/my-org/aws-ts-s3/dev/deployment/settings"
```

### Create Deployment

Creates a new deployment to execute a Pulumi program via the Pulumi Cloud.

```
POST https://api.pulumi.com/api/preview/{organization}/{project}/{stack}/deployments
```

{{% notes "info" %}}

The stack **must** exist before a deployment can be created for it. If you attempt to create a deployment for a stack that does not exist, the request will return an error stating as such.

{{% /notes %}}

A deployment request consists of optional [deployment settings](#deploymentsettings) and the operation to perform.

#### Examples

##### Stack deployment settings

The following request will create a deployment in the "my-org" Pulumi organization for "aws-ts-s3" project and "dev" stack. It will use only the settings associated with the stack.

```shell
curl -i -XPOST -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/preview/my-org/aws-ts-s3/dev/deployments" \
-d '{
	"operation": "update",
	"inheritSettings": true
}'
```

##### Merged stack and request deployment settings

The following request will create a deployment in the "my-org" Pulumi organization for "aws-ts-s3" project and "dev" stack. It will use merge the settings associated with the stack with the settings present
in the request according to the rules used by [the Patch Settings endpoint](#patchsettings).

```shell
curl -i -XPOST -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/preview/my-org/aws-ts-s3/dev/deployments" \
-d '{
	"operation": "update",
	"inheritSettings": true,
    "operationContext": {
        "environmentVariables": {
            "AWS_REGION": "us-east-1"
        }
    }
}'
```

##### Request deployment settings only

The following request will create a deployment in the "my-org" Pulumi organization for "aws-ts-s3" project and "dev" stack. Any deployment settings associated with the stack will be ignored; instead, the
deployment will use only the deployment settings present in the request. The request uses the [Pulumi examples repo](https://github.com/pulumi/examples) as a source, specifically
targeting [aws-ts-s3-folder](https://github.com/pulumi/examples/tree/master/aws-ts-s3-folder) program. First, any pre-run commands defined in the request are run, in this case printing the string
"hello world". Finally, it will run a `pulumi update` against the stack, as specified in the "operation".

```shell
curl -i -XPOST -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/preview/my-org/aws-ts-s3/dev/deployments" \
-d '{
	"operation": "update",
    "sourceContext": {
        "git": {
            "repoURL": "https://github.com/pulumi/deploy-demos.git",
            "branch": "refs/heads/demo",
            "repoDir": "pulumi-programs/aws-ts-s3"
        }
    },
    "operationContext": {
        "preRunCommands": [
            "echo \"hello world\""
        ],
        "environmentVariables": {
            "AWS_REGION": "us-west-2",
            "AWS_ACCESS_KEY_ID": "$AWS_ACCESS_KEY_ID",
            "AWS_SECRET_ACCESS_KEY": "$AWS_SECRET_ACCESS_KEY",
            "AWS_SESSION_TOKEN": "$AWS_SESSION_TOKEN"
        }
    }
}'
```

### Get Deployment

Gets details for a specific deployment.

```
// Get deployment by ID
GET https://api.pulumi.com/api/preview/{organization}/{project}/{stack}/deployments/{deploymentID}

// Get deployment by version
GET https://api.pulumi.com/api/preview/{organization}/{project}/{stack}/deployments/version/{deploymentVersion}
```

#### Example

##### Request

```shell
curl -XGET -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/preview/my-org/aws-ts-s3-folder/dev/deployments/9e5e1331-a018-4845-8714-1598ba8dc52e"
```

##### Response

```json
{
  "id": "9e5e1331-a018-4845-8714-1598ba8dc52e",
  "created": "2022-10-17 22:12:34.834",
  "modified": "2022-10-17 22:12:42.411",
  "status": "running",
  "version": 34,
  "requestedBy": {
    "name": "my-org",
    "githubLogin": "my-org",
    "avatarUrl": "https://avatars.githubusercontent.com/u/1234567?v=4",
    "email": "example@gmail.com"
  },
  "jobs": [
    {
      "status": "running",
      "started": "2022-10-17T22:12:41.191646Z",
      "lastUpdated": "2022-10-17T22:12:42.411732Z",
      "steps": [
        {
          "name": "Download deployment executor",
          "status": "succeeded",
          "started": "2022-10-17T22:12:41.191646Z",
          "lastUpdated": "2022-10-17T22:12:42.244429Z"
        },
        {
          "name": "Get source",
          "status": "running",
          "started": "2022-10-17T22:12:42.411732Z",
          "lastUpdated": "2022-10-17T22:12:42.411732Z"
        },
        {
          "name": "Download dependencies",
          "status": "not-started",
          "started": "0001-01-01T00:00:00Z",
          "lastUpdated": "0001-01-01T00:00:00Z"
        },
        {
          "name": "Pre-run command 1",
          "status": "not-started",
          "started": "0001-01-01T00:00:00Z",
          "lastUpdated": "0001-01-01T00:00:00Z"
        },
        {
          "name": "Pulumi operation",
          "status": "not-started",
          "started": "0001-01-01T00:00:00Z",
          "lastUpdated": "0001-01-01T00:00:00Z"
        }
      ]
    }
  ],
  "latestVersion": 34,
  "configuration": {
    "environmentVariables": [
      {
        "name": "AWS_REGION",
        "value": "us-west-2",
        "secret": false
      },
      {
        "name": "AWS_SECRET_ACCESS_KEY",
        "secret": true
      },
      {
        "name": "PULUMI_CI_BUILD_ID",
        "value": "9e5e1331-a018-4845-8714-1598ba8dc52e",
        "secret": false
      },
      {
        "name": "PULUMI_CI_BUILD_NUMBER",
        "value": "34",
        "secret": false
      },
      {
        "name": "PULUMI_CI_SYSTEM",
        "value": "Pulumi Deploy",
        "secret": false
      },
      {
        "name": "AWS_ACCESS_KEY_ID",
        "secret": true
      },
      {
        "name": "PULUMI_ACCESS_TOKEN",
        "secret": true
      },
      {
        "name": "PULUMI_BACKEND_URL",
        "value": "https://api.pulumi.com/",
        "secret": false
      },
      {
        "name": "AWS_SESSION_TOKEN",
        "secret": true
      }
    ],
    "source": {
      "git": {
        "repoURL": "https://github.com/pulumi/examples.git",
        "branch": "refs/heads/master",
        "repoDir": "aws-ts-s3-folder"
      }
    }
  }
}
```

### List Deployments

Gets a list of deployments.

```
GET https://api.pulumi.com/api/preview/{organization}/{project}/{stack}/deployments
```

The following query parameters may be used for pagination.

* **page** (Optional[int]): The page of results to return (min: 1)
* **pageSize** (Optional[int]): The number of results to return per page (min: 1, max: 100)

#### Example

##### Request

```shell
curl -XGET -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/preview/my-org/aws-ts-s3-folder/dev/deployments?page=1&pageSize=5"
```

##### Response

```json
[
  {
    "id": "94f6ce58-7bdb-42ca-85a7-80296fe2072e",
    "created": "2022-10-31 16:07:58.629",
    "modified": "2022-10-31 16:08:16.463",
    "status": "failed",
    "version": 1,
    "requestedBy": {
      "name": "Norm Normy",
      "githubLogin": "norm-pulumi",
      "avatarUrl": "https://api.pulumi.com/static/avatars/12345.png",
      "email": "norm@normy.com"
    }
  },
  {
    "id": "e77c6363-038c-4972-9b57-dee3e6a73014",
    "created": "2022-10-31 16:58:31.859",
    "modified": "2022-10-31 16:58:50.302",
    "status": "failed",
    "version": 2,
    "requestedBy": {
      "name": "Norm Normy",
      "githubLogin": "norm-pulumi",
      "avatarUrl": "https://api.pulumi.com/static/avatars/12345.png",
      "email": "norm@normy.com"
    }
  },
  {
    "id": "7536b3a1-4171-46bc-98ac-b81f681ce0d5",
    "created": "2022-10-31 17:02:54.277",
    "modified": "2022-10-31 17:03:13.660",
    "status": "failed",
    "version": 3,
    "requestedBy": {
      "name": "Norm Normy",
      "githubLogin": "norm-pulumi",
      "avatarUrl": "https://api.pulumi.com/static/avatars/12345.png",
      "email": "norm@normy.com"
    }
  },
  {
    "id": "303ba93c-0fa5-466f-9f2f-3878800cea26",
    "created": "2022-10-31 17:06:03.016",
    "modified": "2022-10-31 17:07:09.665",
    "status": "succeeded",
    "version": 4,
    "requestedBy": {
      "name": "Turk Turkleton",
      "githubLogin": "turkyturk",
      "avatarUrl": "https://api.pulumi.com/static/avatars/B154678.png",
      "email": "turk@turkleton.com"
    }
  },
  {
    "id": "fd4e838c-7b0c-4382-af3f-202c94e086b8",
    "created": "2022-10-31 17:14:58.430",
    "modified": "2022-10-31 17:16:46.557",
    "status": "succeeded",
    "version": 5,
    "requestedBy": {
      "name": "Turk Turkleton",
      "githubLogin": "turkyturk",
      "avatarUrl": "https://api.pulumi.com/static/avatars/B154678.png",
      "email": "turk@turkleton.com"
    }
  }
]
```

### Get Deployment Logs

Gets logs for a specific deployment.

```
GET https://api.pulumi.com/api/preview/{organization}/{project}/{stack}/deployments/{deploymentID}/logs
```

#### Streaming logs

Streaming logs provide a simple interface to get all logs for a deployment, starting at the beginning. Each response
includes a `token` which can be used to get the next set of logs, until no more logs are available.
The `token` is a string that contains the `job`, `offset` and `step` of the next set of logs, but the requester doesn't need to be concerned with the details.

The following query parameters are available:

* **nextToken**: A string returned by the previous response, that can be used to get the next set of logs.

##### Example

Request

```shell
curl -XGET -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/preview/my-org/aws-ts-s3-folder/dev/deployments/6b1ec06b-4f41-4cce-a7c9-13ceded14db2/logs"
```

Response

```json
{
    "lines": [
        {
            "header": "Download deployment executor",
            "timestamp": "0001-01-01T00:00:00Z"
        },
        {
            "timestamp": "2022-10-06T22:34:02.058756202Z",
            "line": "  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current\n"
        },
        {
            "timestamp": "2022-10-06T22:34:02.059046831Z",
            "line": "                                 Dload  Upload   Total   Spent    Left  Speed\n"
        },
        {
            "timestamp": "2022-10-06T22:34:02.736395042Z",
            "line": "\r  0     0    0     0    0     0      0     0 --:--:-- --:--:-- --:--:--     0\r100  3905    0  3905    0     0  10728      0 --:--:-- --:--:-- --:--:-- 10698\r100 11.9M    0 11.9M    0     0  17.6M      0 --:--:-- --:--:-- --:--:-- 17.6M\n"
        },
        {
            "header": "Get Source",
            "timestamp": "0001-01-01T00:00:00Z"
        },
        {
            "timestamp": "2022-10-06T22:34:22.732527584Z",
            "line": "Successfully cloned: https://github.com/pulumi/examples.git\n"
        },
        {
            "header": "Download Dependencies",
            "timestamp": "0001-01-01T00:00:00Z"
        }
    ],
    "nextToken": "0.2.1"
}
```

Following request (using `nextToken`)

```shell
curl -XGET -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/preview/my-org/aws-ts-s3-folder/dev/deployments/6b1ec06b-4f41-4cce-a7c9-13ceded14db2/logs?nextToken=0.2.1"
```

Response

```json
{
  "lines": [
    {
      "timestamp": "2022-10-06T22:34:43.207012804Z",
      "line": "npm WARN deprecated querystring@0.2.0: The querystring API is considered Legacy. new code should use the URLSearchParams API instead.\n"
    },
    {
      "timestamp": "2022-10-06T22:34:43.236380318Z",
      "line": "npm WARN deprecated read-package-tree@5.3.1: The functionality that this package provided is now in @npmcli/arborist\n"
    },
    {
      "timestamp": "2022-10-06T22:34:50.108263451Z",
      "line": "\n"
    },
    {
      "timestamp": "2022-10-06T22:34:50.108270709Z",
      "line": "added 163 packages, and audited 164 packages in 12s\n"
    }
  ]
}
```

#### Getting logs for individual steps

Step logs return logs for individual steps of the deployment. This is helpful to walk through logs of a single step,
or start requesting logs in the middle of the deployment.

There are no more logs in the step if there is no `nextOffset` included in the response.

The following query parameters are available:

* **job**: The zero-indexed job number to request logs for (currently always 0).
* **step**: The step of the deployment to return logs for (starts at 1).
* **offset**: The line offset from the beginning of the step logs (returned as `nextOffset` in the response).
* **count**: The batch size of lines to return (defaults to 100).

##### Example

Request

```shell
# Get logs for a deployment starting at the zero offset and a count size of 10
curl -i -XGET -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/preview/my-org/aws-ts-s3-folder/dev/deployments/2ee5b292-28bb-44a5-8532-b6ac32f4ec49/logs/?step=5&count=10&offset=0"
```

Response

```json
{
    "nextOffset": 10,
    "lines": [
        {
            "timestamp": "2022-09-14T18:07:26.012974756Z",
            "line": "Updating (k8s/dev)\n"
        },
        {
            "timestamp": "2022-09-14T18:07:26.013002465Z",
            "line": "\n"
        },
        {
            "timestamp": "2022-09-14T18:07:26.637569798Z",
            "line": "\n"
        },
        {
            "timestamp": "2022-09-14T18:07:30.834521134Z",
            "line": "    pulumi:pulumi:Stack resource-test-dev running \n"
        },
        {
            "timestamp": "2022-09-14T18:07:39.927540055Z",
            "line": "    pulumi:pulumi:Stack resource-test-dev running Done!\n"
        },
        {
            "timestamp": "2022-09-14T18:07:40.210973346Z",
            "line": "    pulumi:pulumi:Stack resource-test-dev  1 message\n"
        },
        {
            "timestamp": "2022-09-14T18:07:40.211008513Z",
            "line": " \n"
        },
        {
            "timestamp": "2022-09-14T18:07:40.211811513Z",
            "line": "Diagnostics:\n"
        },
        {
            "timestamp": "2022-09-14T18:07:40.211861221Z",
            "line": "  pulumi:pulumi:Stack (resource-test-dev):\n"
        },
        {
            "timestamp": "2022-09-14T18:07:40.211863638Z",
            "line": "    Done!\n"
        }
    ]
}
```

### Cancel Deployment

Cancels an in-progress deployment.

{{% notes type="warning" %}}

Canceling a deployment is a *very dangerous* action and may leave the stack in an inconsistent state
if the deployment is canceled during the execution of a Pulumi operation.

{{% /notes %}}

```
POST https://api.pulumi.com/api/preview/{organization}/{project}/{stack}/deployments/{deploymentID}/cancel
```

#### Example

```shell
curl -i -XPOST -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/preview/my-org/aws-ts-s3-folder/dev/deployments/2ee5b292-28bb-44a5-8532-b6ac32f4ec49/cancel"
```
