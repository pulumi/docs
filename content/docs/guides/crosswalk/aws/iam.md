---
title_tag: "Using AWS Identity & Access Management (IAM) | Crosswalk"
title: Using AWS Identity & Access Management (IAM)
meta_desc: Pulumi Crosswalk for AWS adds strongly typed IAM resource classes, for creating, updating, and
           otherwise managing AWS users, groups, and roles securely.
linktitle: Identity and Access Management (IAM)
menu:
  userguides:
    parent: crosswalk-aws
    weight: 8

aliases: ["/docs/reference/crosswalk/aws/iam/"]
---

<a href="./">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) enables you to manage access to AWS services
and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and
deny their access to AWS resources.

{{% notes type="info" %}}
This functionality is available in TypeScript only and as part of the [AWS Classic provider](/registry/packages/aws/).
{{% /notes %}}

## Overview

Pulumi Crosswalk for AWS adds strongly typed IAM resource classes, to ensure that you can create, update, and
otherwise manage AWS users, groups, and roles securely and robustly.

## Creating IAM Policy Documents Safely and Easily

You manage access in AWS by creating policies and attaching them to IAM identities or AWS resources. A policy is an
object in AWS that, when associated with an entity or resource, defines their permissions. AWS evaluates these
policies when a principal, such as a user, makes a request. Permissions in the policies determine whether the request
is allowed or denied.

### Policy Documents

IAM policies define permissions for an action regardless of the method that you use to perform the operation. For
example, if a policy allows the GetUser action, then a user with that policy can get user information from the AWS
Management Console, the AWS CLI, or the AWS API. When you create an IAM user, you can set up the user to allow console
or programmatic access. The IAM user can sign in to the console using a user name and password. Or they can use
access keys to work with the CLI or API.

Most policies are stored in AWS as JSON documents. Identity-based policies, policies used to set boundaries, or AWS
STS boundary policies are JSON policy documents that you attach to a user or role. Resource-based policies are JSON
policy documents that you attach to a resource. SCPs are JSON policy documents with restricted syntax that you attach
to an AWS Organizations organizational unit (OU). ACLs are also attached to a resource, but you use a different syntax.

A JSON policy document includes these elements:

* Optional policywide information at the top of the document
* One or more individual statements

Each statement includes information about a single permission. If a policy includes multiple statements, AWS applies
a logical OR across the statements when evaluating them. If multiple policies apply to a request, AWS applies a logical
OR across all of those policies when evaluating them.

For more extensive details about IAM policies and their contents, refer to the [AWS access policies documentation](
https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

#### Strongly Typed Policy Documents (TypeScript-only)

Pulumi Crosswalk for AWS in TypeScript defines [the `aws.iam.PolicyDocument` interface](
/registry/packages/aws/api-docs/iam) to add strong type checking to your policy documents. By using
this type, we will know at compile time whether we've mistyped an attribute:

```typescript
import * as aws from "@pulumi/aws";

const policy: aws.iam.PolicyDocument = {
    Version: "2012-10-17",
    Statement: [
        {
            Action: "sts:AssumeRole",
            Principal: {
               Service: "ec2.amazonaws.com"
            },
            Effect: "Allow",
            Sid: "",
        },
    ],
};
```

This policy object can then be used to configure a variety of IAM objects, as we will see below. For example, we can
use the above policy to configure an IAM role that permits an assume role action for a given principal:

```typescript
const role = new aws.iam.Role("instance-role", {
    assumeRolePolicy: policy,
    path: "/",
});
const profile = new aws.iam.InstanceProfile("instance-profile", { role });
```

### Pre-Defined IAM Managed Policies

An AWS managed policy is a standalone policy that is created and administered by AWS. Standalone policy means that
the policy has its own Amazon Resource Name (ARN) that includes the policy name. For example,
`arn:aws:iam::aws:policy/IAMReadOnlyAccess` is an AWS managed policy.

In places that accept a policy ARN, such as the `RolePolicyAttachment` resource, you can pass the ARN as a string,
but that requires that you either memorize or look up the ARN each time. Instead, you can use the strongly typed
`ManagedPolicy` enum, which exports a collection of constants for all available managed policies.

For example, instead of typing out the ARN by hand, we can just reference `ManagedPolicy`'s `IAMReadOnlyAccess`
enum value:

{{< chooser language "typescript,python,go,csharp" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
const role = ...;
const rolePolicyAttachment = new aws.iam.RolePolicyAttachment("rpa", {
    role: role,
    policyArn: aws.iam.ManagedPolicy.IAMReadOnlyAccess,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
role = ...
role_policy_attachment = aws.iam.RolePolicyAttachment('rpa',
    role=role,
    policy_arn=aws.iam.ManagedPolicy.IAMReadOnlyAccess,
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
role := ...
rolePolicyAttachment, err := iam.NewRolePolicyAttachment("rpa", &iam.RolePolicyAttachmentArgs{}
    Role: role,
    PolicyArn: iam.ManagedPolicyIAMReadOnlyAccess,
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var role = ...;
var rolePolicyAttachment = new Iam.RolePolicyAttachment("rpa", new Iam.RolePolicyAttachmentArgs
{
    Role = role,
    PolicyArn = Iam.ManagedPolicy.IAMReadOnlyAccess.ToString(),
})
```

{{% /choosable %}}

For a full list of available managed policy ARNs, refer to the
[API documentation](/registry/packages/aws/api-docs/iam/).

## Creating IAM Users, Groups, and Roles

The primary IAM object types are users, groups, and roles. This section demonstrates how they
relate and how to create and configure them.

### IAM Users

An AWS Identity and Access Management (IAM) user is an entity that you create in AWS to represent the person or
application that uses it to interact with AWS. A user in AWS consists of a name and credentials.

Use the [`User` resource](/registry/packages/aws/api-docs/iam/user) to create new
IAM users. This example creates an IAM user and attaches a policy:

{{< chooser language "typescript,python,go,csharp" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as aws from "@pulumi/aws";

const user = new aws.iam.User("webmaster", {
    path: "/system/",
    tags: { "Name": "webmaster" },
});
const userAccessKey = new aws.iam.AccessKey("webmasterKey", { user: user.name });
const userPolicy = new aws.iam.UserPolicy("webmasterPolicy", {
    user,
    policy: {
        Version: "2012-10-17",
        Statement: [{
            Action: [ "ec2:Describe*" ],
            Effect: "Allow",
            Resource: "*",
        }],
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import json
import pulumi_aws as aws

user = aws.iam.User('webmaster',
    path='/system/',
    tags={ 'Name': 'webmaster' },
)
user_access_key = aws.iam.AccessKey('webmasterKey',
    user=user.name,
)
user_policy = aws.iam.UserPolicy('webmasterPolicy',
    user=user.id,
    policy=json.dumps({
        'Version': '2012-10-17',
        'Statement': [{
            'Action': [ 'ec2:Describe*' ],
            'Effect': 'Allow',
            'Resource': '*'
        }],
    }),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		user, err := iam.NewUser(ctx, "webmaster", &iam.UserArgs{
			Path: pulumi.String("/system/"),
			Tags: pulumi.StringMap{
				"Name": pulumi.String("webmaster"),
			},
		})
		if err != nil {
			return err
		}

		userAccessKey, err := iam.NewAccessKey(ctx, "webmasterKey", &iam.AccessKeyArgs{
			User: user.Name,
		})
		if err != nil {
			return err
		}

		userPolicy, err := iam.NewUserPolicy(ctx, "webmasterPolicy", &iam.UserPolicyArgs{
			User: user.ID().ToStringOutput(),
			Policy: pulumi.String(`{
	"Version": "2012-10-17",
	"Statement": [{
		"Action": [ "ec2:Describe*" ],
		"Effect": "Allow",
		"Resource": "*"
	}]
}
`),
		})
		if err != nil {
			return err
		}

		ctx.Export("userId", user.ID())
		ctx.Export("userAccessKeyId", userAccessKey.ID())
		ctx.Export("userPolicyId", userPolicy.ID())
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Iam = Pulumi.Aws.Iam;
using System.Collections.Generic;
using System.Collections.Immutable;

class MyStack : Stack
{
    public MyStack()
    {
        var user = new Iam.User("webmaster", new Iam.UserArgs
        {
            Path = "/system",
            Tags = new Dictionary<string, string>
            {
                { "Name", "webmaster" },
            }.ToImmutableDictionary(),
        });
        var userAccessKey = new Iam.AccessKey("webmasterKey", new Iam.AccessKeyArgs
        {
            User = user.Name,
        });
        var userPolicy = new Iam.UserPolicy("webmasterPolicy", new Iam.UserPolicyArgs
        {
            User = user.Name,
            Policy = @"{
    ""Version"": ""2012-10-17"",
    ""Statement"": [{
        ""Action"": [ ""ec2:Describe*"" ],
        ""Effect"": ""Allow"",
        ""Resource"": ""*""
    }]
}
",
        });
    }
}
```

{{% /choosable %}}

For more options available when configuring IAM users, see the [API documentation](
/registry/packages/aws/api-docs/iam/user).

If you'd like to configure non-service account users that can login to the
AWS console, see [`UserLoginProfile`](/registry/packages/aws/api-docs/iam/userloginprofile),
and for creating access keys, see [`AccessKey`](/registry/packages/aws/api-docs/iam/accesskey).

If you need to attach a managed policy ARN to your user, use the [`UserPolicyAttachment` resource](
/registry/packages/aws/api-docs/iam/userpolicyattachment).

Finally, for detailed information about IAM Users, refer to the [AWS documentation](
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html).

### IAM Groups

An IAM group is a collection of IAM users, making it easier for you specify permissions for multiple users at once.
For example, you could have a group called Admins and give that group the types of permissions that administrators need.
Any user in that group automatically has the permissions assigned to the group. If a new user joins your organization
and needs administrator privileges, you can assign the appropriate permissions by adding the user to that group.
Similarly, if a person changes jobs in your organization, instead of editing that user's permissions, you can remove
them from the old groups and add them to the appropriate new groups.

Use the [`Group` resource](/registry/packages/aws/api-docs/iam/group) to manage
IAM groups. For example, this code creates a new group for an organization's developers, specifies a policy for that
group, and adds a couple users into it, thereby granting them permissions from the developer group all at once:

{{< chooser language "typescript,python,go,csharp" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as aws from "@pulumi/aws";

// Create our users.
const jane = new aws.iam.User("jane", ...);
const mary = new aws.iam.User("mary", ...);

// Define a group and assign a policy for it.
const devs = new aws.iam.Group("devs", {
    path: "/users/",
});
const myDeveloperPolicy = new aws.iam.GroupPolicy("my_developer_policy", {
    group: devs.id,
    policy: {
        Version: "2012-10-17",
        Statement: [{
            Action: [ "ec2:Describe*" ],
            Effect: "Allow",
            Resource: "*",
        }],
    },
});

// Finally add the users as members to this group.
const devTeam = new aws.iam.GroupMembership("dev-team", {
    group: devs.id,
    users: [ jane.id, mary.id ],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import json
import pulumi_aws as aws

# Create our users.
jane = aws.iam.User('jane', ...)
mary = aws.iam.User('mary', ...)

# Define a group and assign a policy for it.
devs = aws.iam.Group('devs',
    path='/users/',
)
my_developer_policy = aws.iam.GroupPolicy('my_developer_policy',
    group=devs.id,
    policy=json.dumps({
        'Version': '2012-10-17',
        'Statement': [{
            'Action': [ 'ec2:Describe*' ],
            'Effect': 'Allow',
            'Resource': '*',
        }],
    }),
)

# Finally add the users as members to this group.
dev_team = aws.iam.GroupMembership('dev-team',
    group=devs.id,
    users=[ jane.id, mary.id ],
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create our users.
		jane, err := iam.NewUser(ctx, "jane", &iam.UserArgs{...})
		if err != nil {
			return err
		}
		mary, err := iam.NewUser(ctx, "mary", &iam.UserArgs{...})
		if err != nil {
			return err
		}

		// Define a group and assign a policy for it.
		devs, err := iam.NewGroup(ctx, "devs", &iam.GroupArgs{
			Path: pulumi.String("/users/"),
		})
		if err != nil {
			return err
		}
		myDeveloperPolicy, err := iam.NewGroupPolicy(
			ctx, "my_developer_policy", &iam.GroupPolicyArgs{
				Group: devs.ID().ToStringOutput(),
				Policy: pulumi.String(`{
	"Version": "2012-10-17",
	"Statement": [{
		"Action": [ "ec2:Describe*" ],
		"Effect": "Allow",
		"Resource": "*"
	}]
}
`),
            },
		)
		if err != nil {
			return err
		}

		// Finally add the users as members to this group.
		devTeam, err := iam.NewGroupMembership(
			ctx, "dev-team", &iam.GroupMembershipArgs{
				Group: devs.ID().ToStringOutput(),
				Users: pulumi.StringArray{
					jane.ID().ToStringOutput(),
					mary.ID().ToStringOutput(),
				},
			},
		)
		if err != nil {
			return err
		}

		ctx.Export("devsGroupId", devs.ID())
		ctx.Export("devsGroupPolicyId", myDeveloperPolicy.ID())
		ctx.Export("devsGroupMembershipId", devTeam.ID())
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Iam = Pulumi.Aws.Iam;
using System.Collections.Generic;
using System.Collections.Immutable;

class MyStack : Stack
{
    public MyStack()
    {
        // Create our users.
        var jane = new Iam.User("jane", new Iam.UserArgs{});
        var mary = new Iam.User("mary", new Iam.UserArgs{});

        // Define a group and assign a policy for it.
        var devs = new Iam.Group("devs", new Iam.GroupArgs
        {
            Path = "/users/",
        });
        var myDeveloperPolicy = new Iam.GroupPolicy("my_developer_policy", new Iam.GroupPolicyArgs
        {
            Group = devs.Id,
            Policy = @"{
    ""Version"": ""2012-10-17"",
    ""Statement"": [{
        ""Action"": [ ""ec2:Describe*"" ],
        ""Effect"": ""Allow"",
        ""Resource"": ""*""
    }]
}
",
        });

        // Finally add the users as members to this group.
        var devTeam = new Iam.GroupMembership("dev-team", new Iam.GroupMembershipArgs
        {
            Group = devs.Id,
            Users = { jane.Id, mary.Id },
        });
    }
}
```

{{% /choosable %}}

For more information, refer to the API documentation for [groups](
/registry/packages/aws/api-docs/iam/group), [group membership](
/registry/packages/aws/api-docs/iam/groupmembership), and [group policies](
/registry/packages/aws/api-docs/iam/grouppolicy). If you need to attach a managed policy ARN to your group, use the
[`GroupPolicyAttachment` resource](/registry/packages/aws/api-docs/iam/grouppolicyattachment).

Finally, for detailed information about IAM Groups, refer to the
[AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html).

### IAM Roles

An IAM role is an IAM identity that you can create in your account that has specific permissions. This is similar to
an IAM user, in that it is an AWS identity with permission policies that determine what the identity can and cannot do
in AWS. Instead of being uniquely associated with one person, however, a role is assumable by anyone who needs it. Also,
a role does not have standard long-term credentials such as a password or access keys associated with it. Instead, when
you assume a role, it provides you with temporary security credentials for your role session.

To manage IAM roles, use the [`Role` resource](/registry/packages/aws/api-docs/iam/role).
The following example creates a new role with a custom policy document, and also attaches a managed policy afterwards:

{{< chooser language "typescript,python,go,csharp" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as aws from "@pulumi/aws";

const role = new aws.iam.Role("my-role", {
    assumeRolePolicy: {
        Version: "2012-10-17",
        Statement: [{
            Action: "sts:AssumeRole",
            Principal: {
                Service: "ec2.amazonaws.com"
            },
            Effect: "Allow",
            Sid: "",
        }]
    },
});
const rolePolicyAttachment = new aws.iam.RolePolicyAttachment("my-rpa", {
    role: role,
    policyArn: aws.iam.IAMReadOnlyAccess,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import json
import pulumi_aws as aws

role = aws.iam.Role('my-role',
    assume_role_policy=json.dumps({
        'Version': '2012-10-17',
        'Statement': [{
            'Action': 'sts:AssumeRole',
            'Principal': {
                'Service': 'ec2.amazonaws.com'
            },
            'Effect': 'Allow',
            'Sid': '',
        }],
    }),
)
role_policy_attachment = aws.iam.RolePolicyAttachment('my-rpa',
    role=role.id,
    policy_arn='arn:aws:iam::aws:policy/ReadOnlyAccess',
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		role, err := iam.NewRole(ctx, "my-role", &iam.RoleArgs{
			AssumeRolePolicy: pulumi.String(`{
	"Version": "2012-10-17",
	"Statement": [{
		"Action": [ "sts:AssumeRole" ],
		"Principal": {
			"Service": "ec2.amazonaws.com"
		},
		"Effect": "Allow",
		"Sid": ""
	}]
}
`),
		    },
		)
		if err != nil {
			return err
		}

		_, err = iam.NewRolePolicyAttachment(
			ctx, "my-rpa", &iam.RolePolicyAttachmentArgs{
				Role:      role.ID().ToStringOutput(),
				PolicyArn: pulumi.String("arn:aws:iam::aws:policy/ReadOnlyAccess"),
			},
		)
		return err
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Iam = Pulumi.Aws.Iam;
using System.Collections.Generic;
using System.Collections.Immutable;

class MyStack : Stack
{
    public MyStack()
    {
        var role = new Iam.Role("my-role", new Iam.RoleArgs
        {
            AssumeRolePolicy = @"{
    ""Version"": ""2012-10-17"",
    ""Statement"": [{
        ""Action"": [ ""sts:AssumeRole"" ],
        ""Principal"": {
            ""Service"": ""ec2.amazonaws.com""
        },
        ""Effect"": ""Allow"",
        ""Sid"": """"
    }]
}
",
        });
        var rolePolicyAttachment = new Iam.RolePolicyAttachment("my-rpa",
            new Iam.RolePolicyAttachmentArgs
            {
                Role = role.Id,
                PolicyArn = "arn:aws:iam::aws:policy/ReadOnlyAccess",
            }
        );
    }
}
```

{{% /choosable %}}

Roles are often useful for creating [instance profiles](
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html), which
controls the IAM role assumed by compute running inside of your AWS account, whether that be in EC2, ECS, EKS, or
Lambda, for example. To create one, use the [`InstanceProfile` resource](
/registry/packages/aws/api-docs/iam/instanceprofile) and pass in your role:

{{< chooser language "typescript,python,go,csharp" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
const profile = new aws.iam.InstanceProfile("instance-profile", { role });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
profile = aws.iam.InstanceProfile('instance-profile', role=role.id)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
profile, err := aws.iam.NewInstanceProfile(
    ctx, "instance-profile", &aws.iam.InstanceProfileArgs{
        Role: role.ID().ToStringOutput(),
    },
)
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var profile = new Iam.InstanceProfile("instance-profile", { Role = role.Id });
```

{{% /choosable %}}

For specific information about configuring roles, refer to [the API documentation](
/registry/packages/aws/api-docs/iam/role). For more general information about IAM Roles, refer to the
[AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html).

## Additional IAM Resources

For more information about AWS IAM, see the following:

* [Pulumi AWS IAM API Documentation](/registry/packages/aws/api-docs/iam/)
* [Amazon Identity and Access Management (IAM) homepage](https://aws.amazon.com/iam/)
