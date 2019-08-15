---
title: Accounts & Billing

menu:
    console:
        identifier: accounts
        weight: 1
---

You can create a [Pulumi User account]({{< relref "account" >}}) for free by signing into the
Pulumi Cloud Console. This is how you authenticate with the Pulumi Cloud Console.

You can then create and manage stacks within your own
[Community Edition]({{< relref "editions#community-edition" >}}) organization, or you can create a new
[Pulumi Organization]({{< relref "organizations" >}}) to collaborate with others. 

## User Accounts and Organizations

Your [Pulumi User account]({{< relref "account" >}})  and gives you access to Pulumi [organizations]({{< relref "organizations" >}}).
Pulumi organizations contain stacks.

When you first sign up for the Pulumi Cloud Console, an organization is automatically created for you.
If you later want to take advantage of more advanced features such as teams and role-based access controls,
you can create a new Pulumi organization that best suits your needs. Learn more about
[Pulumi editions]({{< relref "editions" >}}).

## Switching Organizations

When using Pulumi from the command-line, you can log using your Pulumi account using the `pulumi login`
command. You can also see the account you are logged in as by running `pulumi whoami`.

```
$ pulumi login
Logged into pulumi.com as chrsmith (https://app.pulumi.com/chrsmith)

$ pulumi whoami --verbose
User: chrsmith
Backend URL: https://app.pulumi.com/chrsmith
```

By default, whenever you create or refer to a stack, it will be within your individual organization.
However, if you wanted to select or switch to a stack within another organization you can simply
qualify the stack name with the organization.

For example, to create a stack in the `robot-co` organization named "production", you would run:

```
$ pulumi stack init robot-co/production
Created stack 'robot-co/production'

$ pulumi stack ls
NAME         LAST UPDATE    RESOURCE COUNT  URL
production*  n/a            n/a             https://app.pulumi.com/robot-co/database-svc/production
dev          n/a            n/a             https://app.pulumi.com/chrsmith/database-svc/dev
```
