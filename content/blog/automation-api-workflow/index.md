---
title: "Orchestrating Cloud Workflows with Automation API"
date: 2020-11-19
meta_desc: "Using Automation API to provision infrastructure and applications with only code."
meta_image: automation_api.png
authors:
    - sophia-parafina
tags:
    - Automation API
    - Aurora ADS
    - workflow orchestration
---

There are many moving parts when deploying infrastructure and applications. Playbooks are step-by-step maps that standardize how infrastructure and applications are deployed across your organization. Typically playbooks describe every action to build and deploy, requiring an operator to complete each step before moving on to the next. It's a process that can be tedious and prone to human error.

What if you could encapsulate a playbook into a single action? This is the promise of declarative infrastructure. You declare the desired state of your infrastructure and the infrastructure as code engine builds the infrastructure. However, you must still deploy the application and perform maintenance, and this is where you hit the limits of templating languages and where programming languages excel. In this hands-on article, we'll demonstrate how to use Pulumi's Automation API to create a program that builds infrastructure, installs an application, and can perform application maintenance.

<!--more-->

## Starting Point

Pulumi's Automation API has a set of [examples](https://github.com/pulumi/automation-api-examples) to get you started. These examples are sketches that demonstrate what is possible with Automation API. We'll start with the [database migration](https://github.com/pulumi/automation-api-examples/tree/main/nodejs/databaseMigration-ts) example in Node.js, described as:

"This example provisions an AWS Aurora SQL database and executes a database "migration" using the resulting connection info. This migration creates a table, inserts a few rows of data, and reads the data to verify the setup. This is all done in a single inline Pulumi program."

We'll expand on this example and add the following:

- show how to retrieve a password from AWS Secrets Manager
- add functions for database backup, mysqlcheck, optimize, and analyze

Let's get started by cloning the repository and open the `index.ts`.

```bash
$ git clone https://github.com/pulumi/automation-api-examples.git
$ cd ./automation-api-examples/nodejs/databaseMigration-ts/
```

## Program overview

Several pieces comprise the program; the first is the program's main scope, where we can pass values from the functions that make up the script. The next part is the `pulumiProgram` function that declares the infrastructure.

```typescript
const run = async () => {
    // This is our pulumi program in "inline function" form
    const pulumiProgram = async () => {
```

To deploy the infrastructure, we use the Automation API to instantiate the resources and create a stack. Like a Pulumi program invoked by the CLI, we need to provide a stack and project name and the inline program's name that declares the infrastructure.

```typescript
    // Create our stack
    const args: InlineProgramArgs = {
        stackName: "dev",
        projectName: "databaseMigration",
        program: pulumiProgram
    };

    // create (or select if one already exists) a stack that uses our inline program
    const stack = await LocalWorkspace.createOrSelectStack(args);
```

Once the infrastructure is created, we can call provisioning functions, such as `createdb`, maintenance functions, or other functions to manage the database.

## Adding arguments for new commands

First, we'll add the arguments for database creation, mysqlcheck, optimize, and analyze. These arguments call the functions that build the infrastructure, create and populate the database, and perform maintenance.

```typescript
const process = require('process');

const args = process.argv.slice(2);
let destroy = false;
let createdb =false;
let backup = false;
let mysqlcheck = false;
let optimize = false;
let analyze = false;

if (args.length > 0 && args[0]) {
    destroy = args[0] === "destroy";
    createdb = args[0] === "createdb";
    backup = args[0] === "backup";
    mysqlcheck  = args[0] ===  "mysqlcheck";
    optimize  = args[0] === "optimize";
    analyze = args[0] === "analyze";
}
```

## Declare infrastructure

The all the code used to create the infrastructure (a VPC, a security group, and an RDS, provision the database, and maintain the database is in an inline program, which is a function that we can call using Node.js instead of the Pulumi CLI.

Let's break down the infrastructure piece by piece, starting with setting up configuration variables for the database. In the original code, the database name, admin name, and admin password were hardcoded into the program. We would never do that in practice and get the database, admin name, and secret name from a configuration file and a secrets provider's password. We’ll keep those properties in the program for simplicity, but in our improved program, we’ll retrieve the password from the [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/). We set the password using the aws CLI.

```bash
$ aws secretsmanager create-secret --name dbpass --secret-string hellosql
```

We retrieve the secret with a function that retrieves it as a Pulumi [output]({{< relref "/docs/intro/concepts/inputs-outputs" >}}) and returns it as a string type, which is the type that Aurora MySQL requires for the  `masterpassword` property. This is a little complicated because we use the secret name to retrieve the secret properties with [`getSecret`]({{< relref "/docs/reference/pkg/aws/secretsmanager" >}}), which returns the secret ARN. Then, we use the ARN to retrieve the password with [`getSecretVersion`]({{< relref "/docs/reference/pkg/aws/secretsmanager/secretversion" >}}). Note that the function is wrapped in [`async/await`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-1-7.html) because we will need the password before creating the database.

```typescript
async function getSecret(name: string) {
            const secret = await aws.secretsmanager.getSecret({name: name});
            const sm = aws.secretsmanager.getSecretVersion( {secretId: secret.arn});
            return (await sm).secretString;
        }
```

The next part creates the VPC, the subnet, a security group for access, and the Aurora database cluster. Aside from calling the `getSecret` function, this part of the program remains unchanged. Note that the function returns several parameters that are available to other functions in the same scope.

```typescript
        // setup infrastructure
        const vpc = awsx.ec2.Vpc.getDefault();
        const subnetGroup = new aws.rds.SubnetGroup("dbsubnet", {
            subnetIds: vpc.publicSubnetIds,
        });

        // make a public SG for our cluster for the migration
        const securityGroup = new awsx.ec2.SecurityGroup("publicGroup", {
            egress: [
                {
                    protocol: "-1",
                    fromPort: 0,
                    toPort: 0,
                    cidrBlocks: ["0.0.0.0/0"],
                }
            ],
            ingress: [
                {
                    protocol: "-1",
                    fromPort: 0,
                    toPort: 0,
                    cidrBlocks: ["0.0.0.0/0"],
                }
            ]
        });

        // provision our db
        const cluster = new aws.rds.Cluster("db", {
            engine: "aurora-mysql",
            engineVersion: "5.7.mysql_aurora.2.03.2",
            databaseName: dbUser,
            masterUsername: dbName,
            masterPassword: getSecret("dbpass"),
            skipFinalSnapshot: true,
            dbSubnetGroupName: subnetGroup.name,
            vpcSecurityGroupIds: [securityGroup.id],
        });

        const clusterInstance = new aws.rds.ClusterInstance("dbInstance", {
            clusterIdentifier: cluster.clusterIdentifier,
            instanceClass: "db.t3.small",
            engine: "aurora-mysql",
            engineVersion: "5.7.mysql_aurora.2.03.2",
            publiclyAccessible: true,
            dbSubnetGroupName: subnetGroup.name,
        });

        return {
            host: pulumi.interpolate`${cluster.endpoint}`,
            dbName,
            dbUser,
            dbPass: getSecret("dbpass"),
        };
    };
```

## Creating the stack

If you're not familiar with the [Pulumi programming model]({{< relref "/docs/intro/concepts/stack" >}}), a `stack` is an instantiation of the infrastructure resources declared in the code. We start with calling the `createOrSelectStack` method from the `LocalWorkSpace` import. This method takes three arguments: a stack name, a project name, and the program to call, which is the `pulumiProgram` function, that creates the infrastructure. The stack installs the required plugins, sets the AWS region, and creates the infrastructure. We can also destroy the stack if we use the destroy argument, e.g., `yarn start destroy`.
.

```typescript
    // Create our stack
    const args: InlineProgramArgs = {
        stackName: "dev",
        projectName: "databaseMigration",
        program: pulumiProgram
    };

    // create (or select if one already exists) a stack that uses our inline program
    const stack = await LocalWorkspace.createOrSelectStack(args);

    console.info("successfully initialized stack");
    console.info("installing plugins...");
    await stack.workspace.installPlugin("aws", "v3.6.1");
    console.info("plugins installed");
    console.info("setting up config");
    await stack.setConfig("aws:region", { value: "us-west-2" });
    console.info("config set");
    console.info("refreshing stack...");
    await stack.refresh({ onOutput: console.info });
    console.info("refresh complete");

    if (destroy) {
        console.info("destroying stack...");
        await stack.destroy({ onOutput: console.info });
        console.info("stack destroy complete");
        process.exit(0);
    }

    console.info("updating stack...");
    const upRes = await stack.up({ onOutput: console.info });
    console.log(`update summary: \n${JSON.stringify(upRes.summary.resourceChanges, null, 4)}`);
    console.log(`db host url: ${upRes.outputs.host.value}`);
    console.info("configuring db...");
```

### Adding a table and data

Once our infrastructure is up, we can add a table and insert data with SQL statements. First, we need to create a connection object to talk to the database. The `upRes` variable is set to the stack, so the outputs it returns are available to the program's main scope.

```typescript
    // establish mysql client
    const connection = mysql.createConnection({
        host: upRes.outputs.host.value,
        user: upRes.outputs.dbUser.value,
        password: upRes.outputs.dbPass.value,
        database: upRes.outputs.dbName.value
    });
```

In the original program, the table and data are created as part of the inline program. We wrap this in a function that is called by yarn, e.g., `yarn start createdb`.

```typescript
    // create table and populate it
    if (createdb) {
        connection.connect();
        console.log("creating table...")

        // make sure the table exists
        connection.query(`
        CREATE TABLE IF NOT EXISTS hello_pulumi(
            id int(9) NOT NULL,
            color varchar(14) NOT NULL,
            PRIMARY KEY(id)
        );
        `, function (error, results, fields) {
            if (error) throw error;
            console.log("table created!")
            console.log('Result: ', JSON.stringify(results));
            console.log("seeding initial data...")
        });

        // seed the table with some data to start
        connection.query(`
        INSERT IGNORE INTO hello_pulumi (id, color)
        VALUES
            (1, 'Purple'),
            (2, 'Violet'),
            (3, 'Plum');
        `, function (error, results, fields) {
            if (error) throw error;
            console.log("rows inserted!")
            console.log('Result: ', JSON.stringify(results));
            console.log("querying to veryify data...")
        });


        // read the data back
        connection.query(`SELECT COUNT(*) FROM hello_pulumi;`, function (error, results, fields) {
            if (error) throw error;
            console.log('Result: ', JSON.stringify(results));
            console.log("database, tables, and rows successfuly configured!")
        });

        connection.end();
    }
```

## Adding maintenance features

The `createdb` function establishes the pattern for adding other MySQL operations. The pattern is to connect to the database, send a SQL query, and return the results and errors if any. These functions take the table name as input. To use these commands, we can run the program with yarn, as before:

```bash
$ yarn start <command> hello_pulumi
```

The program parses the arguments and sets the command and table name in the main scope. The additional MySQL operations are:

- checktable: [CHECK TABLE](https://dev.mysql.com/doc/refman/8.0/en/check-table.html),
- analyze: [ANALYZE TABLE](https://dev.mysql.com/doc/refman/8.0/en/analyze-table.html)
- optimize: [OPTIMIZE TABLE](https://dev.mysql.com/doc/refman/8.0/en/optimize-table.html).

We created the *hello_pulumi* table with the `createdb` function, but we can leave it as a future exercise to make a generic table creation and list table functions.

```typescript
    // MySQL command to check tables for integrity errors
    if (checktable) {
        connection.connect();
        console.log("checking table...")
        if (tableName) {
            connection.query(`CHECK TABLE ${tableName};`, function (error, results, fields) {
                if (error) throw error;
                console.log('Result: ', JSON.stringify(results));
                console.log("table checked for integrity errors!")});
        } else {
            console.log("Error: Table not specified.");
            console.log("Try: yarn start checktable {table name}");
        }

        connection.end();
    }

    // MySQL command to rebuild index for slow database response
    if (analyze) {
        connection.connect();
        console.log(" analyze table...")
        if (tableName) {
            connection.query(`ANALYZE TABLE ${tableName};`, function (error, results, fields) {
                if (error) throw error;
                console.log('Result: ', JSON.stringify(results));
                console.log("table index rebuilt!")});
        } else {
            console.log("Error: Table not specified.");
            console.log("Try: yarn start analyze {table name}");
        }

        connection.end();
    }

    // MySQL command to reclaim space and rebuild tables and indices
    if (optimize) {
        connection.connect();
        console.log(" optimize table...")
        if (tableName) {
            connection.query(`OPTIMIZE TABLE ${tableName};`, function (error, results, fields) {
                if (error) throw error;
                console.log('Result: ', JSON.stringify(results));
                console.log("table space reclaimed, table and index rebuilt!")});
        } else {
            console.log("Error: Table not specified.");
            console.log("Try: yarn start analyze {table name}");
        }

        connection.end();
    }
```

### Summary

So what have we accomplished? Most importantly, we can turn a playbook into code. Encapsulating your workflow with code means that you have modern software tools such as an IDE with code completion, hints, type checking, debugging, and versioning available to you. In addition to declaring infrastructure, you can also provision it with applications and data. Because it's code, you can extend it as we have done by adding maintenance functions, something not possible with a markup language. Finally, you don't have to use a proprietary CLI to deploy infrastructure and apps. Automation API lets you do all these things and much more.

You can download our improved program as a [gist](https://gist.github.com/pulumipus/61edcdd8ab3f50a42b4bd34a7e1f789b) to replace the one included in the example.

Automation API is currently in alpha and available in Typescript and Go. Check out these resources to learn more.

- [The Pulumi Automation API - The Next Quantum Leap in IaC]({{< relref "/blog/automation-api" >}})
- [Automation API Examples](https://github.com/pulumi/automation-api-examples)
- [Build Self-Service Cloud Infrastructure with Automation API]({{< relref "/blog/automation-api-as-platform" >}})
