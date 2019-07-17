---
title: "Managing your MySQL databases with Pulumi"
authors: ["linio-engineering"]
tags: ["Applications","MySQL"]
date: "2019-05-28"

meta_image: "hero.png"
---

One of the most critical components of an application’s infrastructure is its
database, and one of the most popular databases in use in the cloud today is
[MySQL](https://www.mysql.com/).

Pulumi can already be used to create managed MySQL instances in a wide variety of clouds, including
AWS, Azure and GCP. In addition to this, Pulumi recently added support for managing the MySQL
instances themselves to manage permissions, create databases, and other common tasks.

In this post, we’ll walk through a quick tutorial of how to use this new
[Pulumi MySQL provider]({{< ref "/docs/reference/pkg/nodejs/pulumi/mysql" >}}) to manage existing
and new MySQL databases.
<!--more-->

## Setup

Create a new Pulumi program:

```
$ pulumi new aws-typescript
```

Install the MySQL provider SDK:

```
$ npm add @pulumi/mysql
```

Create the database in index.ts as shown in either of the two examples below.

## Examples

### Example 1: Using an existing MySQL server

In this scenario, the following configuration is required:

> Note: please use your own endpoint, username and password.

```bash
$ pulumi config set mysql:endpoint localhost:3306
$ pulumi config set mysql:username root
$ pulumi config set --secret mysql:password foo
$ pulumi config set --secret jdoePassword hunter2
```

In this example, we will create a database in the previously configured MySQL server, add a user (jdoe) with the given password and grant this user SELECT and UPDATE access to it.

```javascript
import * as mysql from '@pulumi/mysql';
import * as pulumi from ‘@pulumi/pulumi’;

const config = new pulumi.Config();
const jdoePassword = config.requireSecret(‘jdoePassword’);

const database = new mysql.Database('sample', {
  name: 'sample',
});

const user = new mysql.User('jdoe', {
  user: 'jdoe',
  // Since the password is a Pulumi Secret, it will be encrypted and not stored in plaintext
  plaintextPassword: jdoePassword,
});

new mysql.Grant('jdoe', {
  user: user.user,
  host: user.host.apply(h => h.toString()),
  database: database.name,
  privileges: ['SELECT', 'UPDATE'],
});
```

Now deploy the infrastructure to provision the database and user:

```
$ pulumi up
```

### Example 2: Using a RDS instance

In this scenario, the following configuration is required:

```bash
$ pulumi config set mysqlUsername rooUser
$ pulumi config set --secret mysqlPassword rootPassword
```

In this example, we will create an AWS RDS Instance to be our MySQL server, create a "first-class"
provider to manage the MySQL database, and add a user (`jdoe`) with the given password and grant
this user `SELECT` and `UPDATE` access to it:

> Note: This requires the default VPC security group to allow access from where the Pulumi deployment is being executed.

```javascript
import * as mysql from '@pulumi/mysql';
import * as aws from '@pulumi/aws';

const config = new pulumi.Config();
const mysqlUser = config.require(mysqlUser);
const mysqlPassword = config.requireSecret(mysqlPassword);

const rds = new aws.rds.Instance('sample', {
  engine: 'mysql',
  username: mysqlUser,
  password: mysqlPassword,
  availabilityZone: 'us-east-1b',
  instanceClass: 'db.t2.micro',
  allocatedStorage: 20,
  protect: true,
  
  // For a VPC cluster, you will also need the following:
  // dbSubnetGroupName: 'sg-db01-replication-1',
  // vpcSecurityGroupIds: ['sg-c1c63aba'],
});

const mysqlProvider = new mysql.Provider('mysql', {
  endpoint: rds.endpoint,
  username: rds.username,
  password: rds.password.apply(p => p.toString()),
});

const database = new mysql.Database('sample', {
  name: 'sample',
}, {
  provider: mysqlProvider
});

const user = new mysql.User('jdoe', {
  user: "jdoe",
  host: "example.com",
  plaintextPassword: "password",
}, {
  provider: mysqlProvider
});

new mysql.Grant('jdoe', {
  user: user.user,
  host: user.host.apply(h => h.toString()),
  database: database.name,
  privileges: ["SELECT", "UPDATE"],
}, {
  provider: mysqlProvider
});
```

Now deploy the infrastructure:

```
$ pulumi up
```

Wrapping Up
Pulumi allows you to manage your MySQL cloud instances in AWS, Azure, and GCP, as well as manage MySQL databases,
users and more. Together, this enables end-to-end provisioning of your application’s database infrastructure. 
Read more about the [Pulumi MySQL provider]({{< ref "/docs/reference/pkg/nodejs/pulumi/mysql" >}}).

We’ve only shown a little bit of what Pulumi can do. If you need any help, feel free to create an issue
[on GitHub](https://github.com/pulumi/) or join the [Pulumi Community Slack](https://slack.pulumi.io) channel.
