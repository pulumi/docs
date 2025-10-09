---
title: "Secure RDS Passwords with AWS Secrets Manager"
meta_desc: "Automatically manage RDS passwords with AWS Secrets Manager for improved security and compliance using Pulumi."
canonical_url: "https://www.pulumi.com/recipes/aws/rds-secrets-manager"
date: 2025-10-08
category: "Database"
tags: ["aws", "rds", "secrets-manager", "security", "database"]
faq:
  - question: How do I retrieve the password from Secrets Manager?
    answer: The password is stored in AWS Secrets Manager automatically. Use the AWS SDK or Pulumi's aws.secretsmanager.getSecretVersion function to retrieve it programmatically. The secret ARN is available in the RDS instance's masterUserSecret output.
  - question: Does enabling Secrets Manager integration cost extra?
    answer: Yes, AWS Secrets Manager charges approximately $0.40 per month per secret, plus $0.05 per 10,000 API calls. This is a small cost for significantly improved security and automatic password rotation capabilities.
  - question: Can I use this with existing RDS instances?
    answer: Yes, you can enable manageMasterUserPassword on existing RDS instances. AWS will generate a new password and store it in Secrets Manager. Make sure to update your application connection strings to retrieve the password from Secrets Manager.
  - question: How does automatic password rotation work?
    answer: When you enable manageMasterUserPassword, AWS can automatically rotate the password based on a schedule you configure in Secrets Manager. The rotation is performed without downtime, and applications using the Secrets Manager SDK automatically receive the new password.
  - question: What happens to my current password when I enable this feature?
    answer: When you enable manageMasterUserPassword on an existing instance, AWS generates a new random password and stores it in Secrets Manager. Your old password is no longer valid. Ensure your applications are configured to use Secrets Manager before enabling this feature.
---

## How do I secure RDS passwords with AWS Secrets Manager?

**To secure RDS database passwords using AWS Secrets Manager**, enable the `manageMasterUserPassword` option when creating or updating your RDS instance. AWS automatically generates a strong password, stores it securely in Secrets Manager, and can rotate it on a schedule. The following example shows how to deploy this configuration in TypeScript, Python, Go, C#, and Java.

{{< chooser language "typescript,python,go,csharp,java" >}}
{{% choosable language typescript %}}
```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const _default = new aws.rds.Instance("default", {
    allocatedStorage: 10,
    dbName: "mydb",
    engine: "mysql",
    engineVersion: "8.0",
    instanceClass: aws.rds.InstanceType.T3_Micro,
    manageMasterUserPassword: true,
    username: "foo",
    parameterGroupName: "default.mysql8.0",
});
```
{{% /choosable %}}

{{% choosable language python %}}
```python
import pulumi
import pulumi_aws as aws

default = aws.rds.Instance("default",
    allocated_storage=10,
    db_name="mydb",
    engine="mysql",
    engine_version="8.0",
    instance_class=aws.rds.InstanceType.T3_MICRO,
    manage_master_user_password=True,
    username="foo",
    parameter_group_name="default.mysql8.0")
```
{{% /choosable %}}

{{% choosable language go %}}
```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/rds"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := rds.NewInstance(ctx, "default", &rds.InstanceArgs{
			AllocatedStorage:          pulumi.Int(10),
			DbName:                    pulumi.String("mydb"),
			Engine:                    pulumi.String("mysql"),
			EngineVersion:             pulumi.String("8.0"),
			InstanceClass:             pulumi.String(rds.InstanceType_T3_Micro),
			ManageMasterUserPassword:  pulumi.Bool(true),
			Username:                  pulumi.String("foo"),
			ParameterGroupName:        pulumi.String("default.mysql8.0"),
		})
		if err != nil {
			return err
		}
		return nil
	})
}
```
{{% /choosable %}}

{{% choosable language csharp %}}
```csharp
using System.Collections.Generic;
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var @default = new Aws.Rds.Instance("default", new()
    {
        AllocatedStorage = 10,
        DbName = "mydb",
        Engine = "mysql",
        EngineVersion = "8.0",
        InstanceClass = Aws.Rds.InstanceType.T3_Micro,
        ManageMasterUserPassword = true,
        Username = "foo",
        ParameterGroupName = "default.mysql8.0",
    });
});
```
{{% /choosable %}}

{{% choosable language java %}}
```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.rds.Instance;
import com.pulumi.aws.rds.InstanceArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var default_ = new Instance("default", InstanceArgs.builder()
            .allocatedStorage(10)
            .dbName("mydb")
            .engine("mysql")
            .engineVersion("8.0")
            .instanceClass("db.t3.micro")
            .manageMasterUserPassword(true)
            .username("foo")
            .parameterGroupName("default.mysql8.0")
            .build());
    }
}
```
{{% /choosable %}}
{{< /chooser >}}

## Key configuration details

**Automatic password generation**: Setting `manageMasterUserPassword: true` instructs AWS to automatically generate a strong, random password and store it in AWS Secrets Manager. You never need to handle the password in your infrastructure code.

**Master user secret**: The RDS instance exposes a `masterUserSecret` output containing the ARN of the Secrets Manager secret. Use this ARN to retrieve the password programmatically in your applications.

**Database engine support**: This feature is supported for MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server engines. Ensure your engine version supports managed passwords.

**Application integration**: Your applications must be configured to retrieve the password from Secrets Manager using the AWS SDK. Connection strings should reference the secret ARN rather than hardcoded passwords.

**Automatic rotation**: After enabling Secrets Manager integration, you can configure automatic password rotation policies in Secrets Manager. AWS handles rotation without application downtime.

**Security benefits**: This approach eliminates hardcoded passwords in your code, provides audit trails of password access, and meets compliance requirements for credential management.

## Frequently asked questions

**How do I retrieve the password from Secrets Manager?**
The password is stored in AWS Secrets Manager automatically. Use the AWS SDK or Pulumi's aws.secretsmanager.getSecretVersion function to retrieve it programmatically. The secret ARN is available in the RDS instance's masterUserSecret output.

**Does enabling Secrets Manager integration cost extra?**
Yes, AWS Secrets Manager charges approximately $0.40 per month per secret, plus $0.05 per 10,000 API calls. This is a small cost for significantly improved security and automatic password rotation capabilities.

**Can I use this with existing RDS instances?**
Yes, you can enable manageMasterUserPassword on existing RDS instances. AWS will generate a new password and store it in Secrets Manager. Make sure to update your application connection strings to retrieve the password from Secrets Manager.

**How does automatic password rotation work?**
When you enable manageMasterUserPassword, AWS can automatically rotate the password based on a schedule you configure in Secrets Manager. The rotation is performed without downtime, and applications using the Secrets Manager SDK automatically receive the new password.

**What happens to my current password when I enable this feature?**
When you enable manageMasterUserPassword on an existing instance, AWS generates a new random password and stores it in Secrets Manager. Your old password is no longer valid. Ensure your applications are configured to use Secrets Manager before enabling this feature.

