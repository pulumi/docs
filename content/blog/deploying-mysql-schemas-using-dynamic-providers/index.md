---
title: "Deploying a MySQL schema using Dynamic Providers"
date: 2020-08-18
meta_desc: Leveraging Pulumi Dynamic Providers to expand opportunities in cloud architecture design
meta_image: meta.png
authors: ["vova-ivanov"]
tags: ["aws", "python", "mysql"]
---

In our [previous post]({{< relref "/blog/creating-a-python-aws-application-using-flask-and-redis" >}}), we created a Python voting application using Flask and Redis. This blog post will explore creating a MySQL database and initializing it with a schema and data. What seems to be a simple step is much more interesting than it appears, because Pulumi's MySQL provider does not support creating and populating tables. To do it, we will extend it with a Dynamic Provider.

<!--more-->

The existing Pulumi MySQL provider allows us to create the MySQL server, database, and different users. However, it would be great to create the tables as part of the deployment, too, since database schema can be considered a type of infrastructure. Because creating tables requires admin credentials, deploying them along with the other infrastructure allows us to limit the sharing of admin credentials, and run the application under restricted permissions at all times.

A great advantage of Pulumi is its extensible and modular design. If support for something isn't implemented, you can write it yourself easily. We will be writing a Dynamic Provider that connects to a MySQL server, initializes a table, and creates some starting data all during `pulumi up`.

The first step is to create a new directory and initialize a Pulumi project with `pulumi new aws-python`.

```bash
$ mkdir aws-py-dynamicresource && cd aws-py-dynamicresource
$ pulumi new aws-python
```

This project requires several configuration variables, which we set using `pulumi config set`. They are used to configure the MySQL admin account during deployment, and a user account for initializing the table.

```bash
$ pulumi config set sql-admin-name <NAME>
$ pulumi config set sql-admin-password <PASSWORD> --secret
$ pulumi config set sql-user-name <NAME>
$ pulumi config set sql-user-password <PASSWORD> --secret
```

The `requirements.txt` file lists the libraries used in the project. We will need to add the following:

```
pulumi-mysql>=1.0.0,<3.0.0
mysql-connector-python>=1.0.0,<10.0.0
```

We will write the code for our Dynamic Provider in a separate file to reduce clutter, for example, `MySqlDynamicProvider.py`. The first few lines of the file will indicate which libraries to import.

```python
import mysql.connector as connector
from mysql.connector import errorcode
from pulumi import Input, Output, ResourceOptions
from pulumi.dynamic import *
from typing import Any, Optional
import binascii
import os
```

After setting up the imports, the next step is to write the code. The Dynamic Provider's first component is a class with the arguments that the dynamic provider requires when created. These arguments are given a type `Input[str]` and automatically converted to regular `str` before being passed to the provider's functions.

```python
class SchemaInputs(object):
    creator_name: Input[str]
    creator_password: Input[str]
    server_address: Input[str]
    database_name: Input[str]
    creation_script: Input[str]
    deletion_script: Input[str]
    def __init__(self, creator_name, creator_password, server_address, database_name, creation_script, deletion_script):
        self.creator_name = creator_name
        self.creator_password = creator_password
        self.server_address = server_address
        self.database_name = database_name
        self.creation_script = creation_script
        self.deletion_script = deletion_script
```

The second step is to write the Dynamic Provider. The provider handles the create, read, update, and delete operations the resource needs. The `create` function instantiates a new resource and assigns it a unique ID. The `delete` function deletes an existing resource. The `diff` function determines if we can update the resource without entirely replacing it, and the `update` function performs the update.

```python
class SchemaProvider(ResourceProvider):
    def create(self, args):
        connection = connector.connect(user=args["creator_name"],
        password=args["creator_password"],
        host=args["server_address"],
        database=args["database_name"])
        cursor = connection.cursor()
        cursor.execute(args["creation_script"])
        return CreateResult("schema-"+binascii.b2a_hex(os.urandom(16)).decode("utf-8"), outs=args)

    def delete(self, id, args):
        connection = connector.connect(user=args["creator_name"],
        password=args["creator_password"],
        host=args["server_address"],
        database=args["database_name"])
        cursor = connection.cursor()
        cursor.execute(args["deletion_script"])

    def diff(self, id, oldInputs, newInputs):
        replaces = []
        if (oldInputs["server_address"] != newInputs["server_address"]): replaces.append("server_address")
        if (oldInputs["database_name"] != newInputs["database_name"]): replaces.append("database_name")
        if (oldInputs["creation_script"] != newInputs["creation_script"]): replaces.append("creation_script")

        return DiffResult(
            changes=oldInputs != newInputs,
            replaces=replaces,
            stables=None,
            delete_before_replace=True)

    def update(self, id, oldInputs, newInputs):
        return UpdateResult(outs={**newInputs})
```

And lastly, we add the main Schema resource that we instantiate in our infrastructure code. We make all the inputs to our provider available as outputs, so that they can be accessed and exported.

```python
class Schema(Resource):
    creator_name: Output[str]
    creator_password: Output[str]
    server_address: Output[str]
    database_name: Output[str]
    creation_script: Output[str]
    deletion_script: Output[str]
    def __init__(self, name: str, args: SchemaInputs, opts = None):
        super().__init__(SchemaProvider(), name, vars(args), opts)
```

With the dynamic provider finished, all that is left is to create it in our infrastructure. Like the previous post, the project uses a `__main__.py` file; the first few lines indicate the libraries to import and describe the application's configuration options.

```python
import json
import base64
import pulumi
import pulumi_aws as aws
import pulumi_mysql as mysql
from MySqlDynamicProvider import *

config = pulumi.Config()
admin_name = config.require("sql-admin-name")
admin_password = config.require_secret("sql-admin-password")
user_name = config.require("sql-user-name")
user_password = config.require_secret("sql-user-password")
availability_zone = pulumi.Config("aws").get("region")
```

To allow different tasks within our project to communicate, we create a Virtual Private Cloud and an associated subnet. Two subnets are required for the project, so the availability zone suffix is set to "a".

```python
app_vpc = aws.ec2.Vpc("app-vpc",
    cidr_block="172.31.0.0/16",
    enable_dns_hostnames=True)

app_vpc_subnet = aws.ec2.Subnet("app-vpc-subnet",
    cidr_block="172.31.0.0/20",
    availability_zone=availability_zone + "a",
    vpc_id=app_vpc)
```

A gateway and routing table are needed to allow the VPC to communicate with the Internet.
Once created, we associate the routing table with our VPC.

```python
app_gateway = aws.ec2.InternetGateway("app-gateway",
    vpc_id=app_vpc.id)

app_routetable = aws.ec2.RouteTable("app-routetable",
    routes=[
        {
            "cidr_block": "0.0.0.0/0",
            "gateway_id": app_gateway.id,
        }
    ],
    vpc_id=app_vpc.id)

app_routetable_association = aws.ec2.MainRouteTableAssociation("app_routetable_association",
    route_table_id=app_routetable.id,
    vpc_id=app_vpc)
```

To control traffic flow between applications running inside our VPC, we create a security group.

```python
app_security_group = aws.ec2.SecurityGroup("security-group",
	vpc_id=app_vpc.id,
	description="Enables HTTP access",
    ingress=[{
		'protocol': 'tcp',
		'from_port': 0,
		'to_port': 65535,
		'cidr_blocks': ['0.0.0.0/0'],
    }],
    egress=[{
		'protocol': '-1',
		'from_port': 0,
		'to_port': 0,
		'cidr_blocks': ['0.0.0.0/0'],
    }])
```

Our MySQL database is created with an RDS instance. To create the instance, Amazon requires that it be given two subnets in different availability zones.

```python
extra_rds_subnet = aws.ec2.Subnet("extra-rds-subnet",
    cidr_block="172.31.128.0/20",
    availability_zone=availability_zone + "b",
    vpc_id=app_vpc)
```

Both subnets are assigned to a SubnetGroup and belong to the RDS instance.

```python
app_database_subnetgroup = aws.rds.SubnetGroup("app-database-subnetgroup",
    subnet_ids=[app_vpc_subnet.id, extra_rds_subnet.id])

mysql_rds_server = aws.rds.Instance("mysql-server",
    engine="mysql",
    username=admin_name,
    password=admin_password,
    instance_class="db.t2.micro",
    allocated_storage=20,
    skip_final_snapshot=True,
    publicly_accessible=True,
    db_subnet_group_name=app_database_subnetgroup.id,
    vpc_security_group_ids=[app_security_group.id])
```

Pulumi offers some additional tools to make handling MySQL easier.

```python
mysql_provider = mysql.Provider("mysql-provider",
    endpoint=mysql_rds_server.endpoint,
    username=admin_name,
    password=admin_password)
```

We initialize the example database and create a user to manage it.

```python
mysql_database = mysql.Database("mysql-database",
    name="votes-database",
    opts=pulumi.ResourceOptions(provider=mysql_provider))

mysql_user = mysql.User("mysql-standard-user",
    user=user_name,
    host="example.com",
    plaintext_password=user_password,
    opts=pulumi.ResourceOptions(provider=mysql_provider))
```

The user only needs the `SELECT` and `UPDATE` permissions to function.

```python
mysql_access_grant = mysql.Grant("mysql-access-grant",
    user=mysql_user.user,
    host=mysql_user.host,
    database=mysql_database.name,
    privileges= ["SELECT", "UPDATE"],
    opts=pulumi.ResourceOptions(provider=mysql_provider))
```

Now, we use our Dynamic Provider. The provider takes `creation_script` as a parameter, connects to our MySQL server, and runs it during deployment.

```python
creation_script = """
    CREATE TABLE votesTable (
        choice_id int(10) NOT NULL AUTO_INCREMENT,
        vote_count int(10) NOT NULL,
        PRIMARY KEY (choice_id)
    ) ENGINE=InnoDB;
    INSERT INTO votesTable(choice_id, vote_count) VALUES (0,0);
    INSERT INTO votesTable(choice_id, vote_count) VALUES (1,0);
    """
```

The `deletion_script` parameter drops the table and deletes stored data.

```python
deletion_script = "DROP TABLE votesTable CASCADE"
```

When we create our resource, it behaves the same way as any other Pulumi resource but takes its arguments as a `SchemaInputs` object.

```python
mysql_votes_table = Schema(name="mysql_votes_table",
    args=SchemaInputs(admin_name, admin_password, mysql_rds_server.address, mysql_database.name, creation_script, deletion_script))
```

We can export the ID of our new resource, and view it when deployed.

```python
pulumi.export("dynamic-resource-id",mysql_votes_table.id)
```

In this example, I showed how straightforward it is to expand functionality with Pulumi by writing additional code. Dynamic Providers enable excellent flexibility in cloud architecture design and help break down barriers that would otherwise be challenging to overcome.

Next week, I'll change the frontend from Flask to Django, and will show how to integrate it with our new MySQL server.

The blog post's full code and an in-depth explanation for each component can be [found on Github](https://github.com/pulumi/examples/tree/master/aws-py-dynamicresource).
