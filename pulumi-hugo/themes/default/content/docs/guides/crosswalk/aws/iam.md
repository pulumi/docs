---
title: "AWS Identity and Access Management (IAM)"
meta_desc: Pulumi Crosswalk for AWS adds strongly typed IAM resource classes, for creating, updating, and
           otherwise managing AWS users, groups, and roles securely.
linktitle: Identity and Access Management (IAM)
menu:
  userguides:
    parent: crosswalk-aws
    weight: 8

aliases: ["/docs/reference/crosswalk/aws/iam/"]
---

<a href="{{< relref "./" >}}">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) enables you to manage access to AWS services
and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and
deny their access to AWS resources.

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

For more extensive details about IAM policies and their contents, please [refer to the AWS documentation online](
https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

### Using the PolicyDocument Interface

Pulumi Crosswalk for AWS defines [the `aws.iam.PolicyDocument` interface](
{{< relref "/docs/reference/pkg/nodejs/pulumi/aws/iam#PolicyDocument" >}}) to add strong type checking to your policy documents. By using
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

### Using Pre-Defined IAM Managed Policies

An AWS managed policy is a standalone policy that is created and administered by AWS. Standalone policy means that
the policy has its own Amazon Resource Name (ARN) that includes the policy name. For example,
`arn:aws:iam::aws:policy/IAMReadOnlyAccess` is an AWS managed policy. The `aws.iam` module exports a collection of
constants for all available managed policies so that you don't need to remember the ARNs.

For example, the above is available as `aws.iam.IAMReadOnlyAccess`:

```typescript
const role = ...;
const rolePolicyAttachment = new aws.iam.RolePolicyAttachment("rpa", {
    role: role,
    policyArn: aws.iam.IAMReadOnlyAccess,
});
```

For a full list of available managed policy ARNs, please refer to the
[API documentation]({{< relref "/docs/reference/pkg/aws/iam" >}}).

## Creating IAM Users, Groups, and Roles

### IAM Users

An AWS Identity and Access Management (IAM) user is an entity that you create in AWS to represent the person or
application that uses it to interact with AWS. A user in AWS consists of a name and credentials.

Use the [`User` resource]({{< relref "/docs/reference/pkg/aws/iam/user" >}}) to create new
IAM users. This example creates an IAM user and attaches a policy:

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

For more options available when configuring IAM users, please see the [API documentation](
{{< relref "/docs/reference/pkg/nodejs/pulumi/aws/iam#User" >}}).

If you'd like to configure non-service account users that can login to the
AWS console, see [`UserLoginProfile`]({{< relref "/docs/reference/pkg/aws/iam/userloginprofile" >}}),
and for creating access keys, see [`AccessKey`]({{< relref "/docs/reference/pkg/aws/iam/accesskey" >}}).

If you need to attach a managed policy ARN to your user, use the [`UserPolicyAttachment` resource](
{{< relref "/docs/reference/pkg/aws/iam/userpolicyattachment" >}}).

Finally, for detailed information about IAM Users, please refer to the [AWS documentation](
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html).

### IAM Groups

An IAM group is a collection of IAM users, making it easier for you specify permissions for multiple users at once.
For example, you could have a group called Admins and give that group the types of permissions that administrators need.
Any user in that group automatically has the permissions assigned to the group. If a new user joins your organization
and needs administrator privileges, you can assign the appropriate permissions by adding the user to that group.
Similarly, if a person changes jobs in your organization, instead of editing that user's permissions, you can remove
them from the old groups and add them to the appropriate new groups.

Use the [`Group` resource]({{< relref "/docs/reference/pkg/aws/iam/group" >}}) to manage
IAM groups. For example, this code creates a new group for an organization's developers, specifies a policy for that
group, and adds a couple users into it, thereby granting them permissions from the developer group all at once:

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
    group: devs,
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
    group: devs,
    users: [ jane, mary ],
});
```

For more information, please refer to the API documentation for [groups](
{{< relref "/docs/reference/pkg/aws/iam/group" >}}), [group membership](
{{< relref "/docs/reference/pkg/aws/iam/groupmembership" >}}), and [group policies](
{{< relref "/docs/reference/pkg/aws/iam/grouppolicy" >}}). If you need to attach a managed policy ARN to your group, use the
[`GroupPolicyAttachment` resource]({{< relref "/docs/reference/pkg/aws/iam/grouppolicyattachment" >}}).

Finally, for detailed information about IAM Groups, please refer to the
[AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html).

### IAM Roles

An IAM role is an IAM identity that you can create in your account that has specific permissions. This is similar to
an IAM user, in that it is an AWS identity with permission policies that determine what the identity can and cannot do
in AWS. Instead of being uniquely associated with one person, however, a role is assumable by anyone who needs it. Also,
a role does not have standard long-term credentials such as a password or access keys associated with it. Instead, when
you assume a role, it provides you with temporary security credentials for your role session.

To manage IAM roles, use the [`Role` resource]({{< relref "/docs/reference/pkg/aws/iam/role" >}}).
The following example creates a new role with a custom policy document, and also attaches a managed policy afterwards:

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

Roles are often useful for creating [instance profiles](
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html), which
controls the IAM role assumed by compute running inside of your AWS account, whether that be in EC2, ECS, EKS, or
Lambda, for example. To create one, use the [`InstanceProfile` resource](
{{< relref "/docs/reference/pkg/aws/iam/instanceprofile" >}}) and simply pass in your role:

```typescript
const profile = new aws.iam.InstanceProfile("instance-profile", { role });
```

For specific information about configuring roles, please refer to [the API documentation](
{{< relref "/docs/reference/pkg/aws/iam/role" >}}). For more general information about IAM Roles, please refer to the
[AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html).

## Additional IAM Resources

For more information about AWS IAM, please see the following:

* [Pulumi AWS IAM API Documentation]({{< relref "/docs/reference/pkg/aws/iam" >}})
* [Amazon Identity and Access Management (IAM) homepage](https://aws.amazon.com/iam/)
