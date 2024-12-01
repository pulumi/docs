---
title: Using ESC Environments at scale
title_tag: ESC Environments @ Scale | Pulumi ESC
h1: Pulumi ESC Environments at Scale
meta_desc: How to use ESC Environments within your enterprise organization
menu:
  esc:
    name: Using ESC at scale
    identifier: at-scale
    parent: esc-environments
    weight: 7
---

## ESC Environments at Scale

We have covered a lot of features that ESC environments have to offer. Let's see how we can use some of them in a real-world application using a somewhat simple example. In this walkthrough we will look at setting up a new environment with RBAC using Pulumi teams, creating and distributing a shared environment, distributing changes to downstream consumers, and rolling back changes.

### Platform Team Setup

Our Pulumi admin starts by changing the default permissions for environments to be `None`. This prevents new environments from being accessible by any users in the org other than admins and the creators of that environment.

<img style="width: 75%" src="/images/docs/guides/esc/default-env-permissions.png"><br>

Our admin then creates two teams for both the `identity` and `payments` teams at their company, adding application engineers Jane and Joe as members to their respective teams.

<div style="display: flex">
    <img style="width: 50%" src="/images/docs/guides/esc/identity-team.png">
    <img style="width: 50%" src="/images/docs/guides/esc/payments-team.png">
</div><br>

[Teams & Role-based access control (RBAC)](https://www.pulumi.com/docs/pulumi-cloud/access-management/teams/#teams-role-based-access-control-rbac) has more information on team creation and features.

Next our admin creates an ESC environment meant to be shared across the company that defines common AWS configuration, as that is their cloud provider of choice.
They name the shared environment `common/aws` and define it's contents as:

```yaml
values:
  login:
    fn::open::aws-login:
      oidc:
        duration: 1h
        roleArn: arn:aws:iam::012345678912:role/role-abcd123
        sessionName: pulumi-esc
  region: us-west-2
  # reserved key used to define environment variables
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${login.secretAccessKey}
    AWS_SESSION_TOKEN: ${login.sessionToken}
    AWS_REGION: ${region}
```

This environment uses the [AWS-login provider](https://www.pulumi.com/docs/esc/integrations/dynamic-login-credentials/aws-login/) to login to AWS using OpenID Connect. The provider will return a set of credentials that we can use to access and modify AWS resources. Here we are also setting these credentials as environment variables.

The admin then adds a new `stable` tag to this revision of the environment. This allows the admin to communicate what version of the environment is considered stable and application engineers to consume the stable environment only picking up changes when the tag moves.

<img src="/images/docs/guides/esc/common-env-rev-tag-stable.png"><br>

Once the environment exists the admin adds it to the new teams with open permissions. This allows application engineers to open the environment and use the credentials but does not allow them to directly modify any of the values.

<img src="/images/docs/guides/esc/common-env-permissions.png"><br>

### Environments in Applications

An application engineer on the identity team, Jane, can now see the environment and use it in their `auth-bucket` project. This program is small, focused solely on creating an s3 bucket. Jane also takes advantage of the ESC SDK which allows the program to resolve and reference the AWS OIDC credentials at runtime to authenticate with AWS.

{{% chooser language "go" / %}}

{{% choosable language go %}}

```go
package main

import (
	"fmt"
	"os"

	esc "github.com/pulumi/esc-sdk/sdk/go"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

const (
	projName = "common"
	envName  = "aws"
)

func valueForEnvKey(envID string, envDef map[string]interface{}, key string, isSecret bool) (string, error) {
	keyType := "configuration"
	if isSecret {
		keyType = "secret"
	}
	val, ok := envDef[key].(string)
	if !ok {
		return "", fmt.Errorf("%s key '%s' not found in environment %s", keyType, key, envID)
	}
	return val, nil
}

func getAwsProviderFromEnv(ctx *pulumi.Context, env map[string]any) (*aws.Provider, error) {
	envID := fmt.Sprintf("%s/%s", projName, envName)
	awsLogin, ok := env["login"]
	if !ok {
		return nil, fmt.Errorf("configuration key 'login' not found in environment %s", envID)
	}

	awsLoginMap, ok := awsLogin.(map[string]interface{})
	if !ok {
		return nil, fmt.Errorf("configuration key 'login' in environment %s is not map[string]string", envID)
	}

	awsAccessKeyID, err := valueForEnvKey(envID, awsLoginMap, "accessKeyId", true)
	if err != nil {
		return nil, err
	}

	awsSecretAccessKey, err := valueForEnvKey(envID, awsLoginMap, "secretAccessKey", true)
	if err != nil {
		return nil, err
	}

	awsSessionTkn, err := valueForEnvKey(envID, awsLoginMap, "sessionToken", true)
	if err != nil {
		return nil, err
	}

	awsRegion, err := valueForEnvKey(envID, env, "region", false)
	if err != nil {
		return nil, err
	}

	return aws.NewProvider(ctx, "awsProvider", &aws.ProviderArgs{
		AccessKey: pulumi.StringPtr(awsAccessKeyID),
		SecretKey: pulumi.StringPtr(awsSecretAccessKey),
		Region:    pulumi.StringPtr(awsRegion),
		Token:     pulumi.StringPtr(awsSessionTkn),
	})
}

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		accessToken := os.Getenv("PULUMI_ACCESS_TOKEN")
		orgName := ctx.Organization()
		configuration := esc.NewConfiguration()
		escClient := esc.NewClient(configuration)
		authCtx := esc.NewAuthContext(accessToken)

        // Always reference the `stable` version of this environment
		_, values, err := escClient.OpenAndReadEnvironmentAtVersion(authCtx, orgName, projName, envName, "stable")
		if err != nil {
			return fmt.Errorf("failed to open environment: %v", err)
		}

		awsProvider, err := getAwsProviderFromEnv(ctx, values)
		if err != nil {
			return err
		}

		// Create an AWS resource (S3 Bucket)
		bucket, err := s3.NewBucketV2(ctx, "my-bucket", nil, pulumi.Provider(awsProvider))
		if err != nil {
			return err
		}

		// Export the name of the bucket
		ctx.Export("bucketName", bucket.ID())
		return nil
	})
}
```

{{% /choosable %}}

Jane deploys `dev` and `production` stacks for this project.

Both stacks run successfully and create an s3 bucket in the configured region. However, Jane want to be able to move some of bucket configuration (such as the name) out of the source code and into ESC to allow others to easily modify and deploy these changes without having to commit back changes to the source.

Jane attempts to update the `common/aws` environment, adding a new value for their bucket name `bucketName: identity-auth-bucket`. However, when Jane tries to save the changes they are shown an error stating that they do not have sufficient permissions to write to the environment.

<img src="/images/docs/guides/esc/common-env-save-fail.png"><br>

This is because our admin set the access policy to this environment on Jane's team as open only. In order to achieve what Jane wants they create a new environment, `identity/common`, which imports the `common/aws` environemnt and specifies their additional configuration.

```yaml
imports:
  # Always reference the `stable` version of this environment
  - common/aws@stable

values:
  bucketName: identity-auth-bucket
```

Jane also adds two tags onto this environment's revision, `dev` and `production` so that the program can point to the corresponding revision for the right environment.

<img src="/images/docs/guides/esc/identity-common-env-rev-tags.png"><br>

Jane updates the `auth-bucket` program to use the new environment configuration via the ESC SDK and updates the `dev` and `production` stacks environment references to use the new environment.
Now the `auth-bucket` project's can be updated and deployed completely within the Pulumi console.

```diff
const (
-	projName = "common"
-	envName  = "aws"
+   projName = "identity"
+	envName  = "common"
)
...
+       stackName := ctx.Stack()
-       _, values, err := escClient.OpenAndReadEnvironmentAtVersion(authCtx, orgName, projName, envName, "stable")
+       _, values, err := escClient.OpenAndReadEnvironmentAtVersion(authCtx, orgName, projName, envName, stackName)
		if err != nil {
			return fmt.Errorf("failed to open environment: %v", err)
		}

+       envID := fmt.Sprintf("%s/%s", projName, envName)
+		bucketName, err := valueForEnvKey(envID, values, "bucketName", false)
+		if err != nil {
+			return err
+		}

        // Create an AWS resource (S3 Bucket)
-		bucket, err := s3.NewBucketV2(ctx, "my-bucket", nil, pulumi.Provider(awsProvider))
+		bucket, err := s3.NewBucketV2(ctx, bucketName, nil, pulumi.Provider(awsProvider))
		if err != nil {
			return err
		}
```

The program has been updated to use the new identity-specific environment, which leverages imports to inherit configuration from the `common/aws` environment.

### Distributing Changes

Eventually the Pulumi admin needs to change which AWS region the company is deploying into. Since they have set this value in the common AWS environment used by all application engineers, this should be easy! Additionally, since all applications reference the common environment using the `stable` tag the admin can make configuration updates to the environment without worrying about impacting downstream consumers.

When the admin is ready, they add a new tag `preview` to be able to test out the region changes in select downstream applications.

<img src="/images/docs/guides/esc/common-env-rev-tag-preview.png"><br>

In order to test their changes the admin uses the identity team's `dev` stack from the `auth-bucket` project, updating the environment reference to use the `preview` tag and moving the `identity/common`'s `dev` revision tag to the new version.

<img src="/images/docs/guides/esc/identity-common-env-rev-tag-dev.png"><br>

Everything looks good, the `dev` stack has successfully deployed to the new region while the `production` stack continues deploying to the legacy region.

```bash
+ pulumi:pulumi:Stack: (create)
    [urn=urn:pulumi:dev::auth-bucket::pulumi:pulumi:Stack::auth-bucket-dev]
    + pulumi:providers:aws: (create)
        [urn=urn:pulumi:dev::auth-bucket::pulumi:providers:aws::awsProvider]
        accessKey                : [secret]
        region                   : "us-west-1"
```

```bash
+ pulumi:pulumi:Stack: (create)
    [urn=urn:pulumi:production::auth-bucket::pulumi:pulumi:Stack::auth-bucket-production]
    + pulumi:providers:aws: (create)
        [urn=urn:pulumi:production::auth-bucket::pulumi:providers:aws::awsProvider]
        accessKey                : [secret]
        region                   : "us-west-2"
```

The admin moves the `stable` tag of the `common/aws` environment to that same revision `preview` is pointing at, updating all consumers.

### Rolling back

But wait! Joe from the payments team has pointed out that their program had logic that relied on the the region being `us-west-2` and that now updates are failing. Our admin proposes two options to unblock this team:

1. The admin can quickly move the stable tag from the `common/aws` environment back to revision 1. However, this will roll the change back for everyone.
1. Joe's team can pin their environment to the legacy version until they can fix the logic that relies on this legacy value.

Joe's team decides to go with option 2 as they are the only team impacted, updating their `production` stack defintion to pin the `common/aws` environment to version 2.

`Pulumi.yaml` of the `payments-service`

```diff
name: payments-service
description: Infrastructure to power payments service
runtime: go
environment:
-  - common/aws
+  # pin to v2 of the common/aws environment until we remove reliance on us-west-2 AWS region
+  - common/aws@2
```
