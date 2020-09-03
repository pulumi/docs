---
title: "Deploying a PERN stack application to AWS"
date: 2020-09-04
meta_desc: Creating and quickly deploying a PERN stack application to the cloud Using Pulumi
meta_image: meta.png
authors: ["vova-ivanov"]
tags: ["aws", "typescript", "docker"]
---

In this blog post, we will explore the basics behind PERN stack applications, and will deploy one to AWS. Additionally, we will use a bit of Pulumi Crosswalk to decrease the amount of code that we need to write, and allow for a quick and straightforward path to getting the application up and running.

<!--more-->

The word *PERN* is an acronym for PostgreSQL, Express, React, and NodeJS. A PERN stack application is simply a project that uses PostgreSQL as a database, Express as an application framework, React as a user interface framework, and which runs on Node.

The nature of the project means that it has 4 distinct tiers: a database that keeps track of our data, a stateless server that receives commands and manipulates the database, a clientside server that contains and send out the user interface code, and the internet browser that downloads that code, presents the UI, and sends requests to the stateless server.
<Project diagram>

As React and the other components use NodeJS, we'll use it for our infrastructure too by writing it TypeScript. The first step is to create a new directory and initialize a Pulumi project with `pulumi new aws-typescript`.

```bash
$ mkdir aws-pern-voting-app && cd aws-pern-voting-app
$ pulumi new aws-typescript
```

This tutorial was written for the [aws-pern-voting-app example](https://github.com/pulumi/examples/tree/vova/aws-pern-voting-app/aws-pern-voting-app) but will work with any other PERN stack application. The example uses two folders to hold the client and server tiers, and a Dockerfile in each to turn both into images that can be run on AWS.

As the specific code for the application can vary widely, the most important part of our project is the infrastructure. We require several configuration variables, which we set using `pulumi config set`. They are used to configure the PostgreSQL admin account, a user account for initializing the schema and table, and the region of our database.

```bash
$ pulumi config set sql-admin-name <NAME>
$ pulumi config set sql-admin-password <PASSWORD> --secret
$ pulumi config set sql-user-name <NAME>
$ pulumi config set sql-user-password <PASSWORD> --secret
$ pulumi config set aws:region <REGION>
```

The `package.json` file lists the libraries used by the project. We will need to add the following to the `dependancies` section:

```json
"@pulumi/cloud-aws": "^0.19.0",
"@pulumi/postgresql": "^2.3.0",
"pg": "^8.3.3"
```

Our project uses a Dynamic Provider written in TypeScript to help create tables and Schemas. It offers the same exact features as our [MySQL provider]({{< relref "/blog/deploying-mysql-schemas-using-dynamic-providers" >}}), but for PostgreSQL.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as crypto from "crypto";

export interface SchemaInputs {
    creatorName: pulumi.Input<string>
    creatorPassword: pulumi.Input<string>
    serverAddress: pulumi.Input<string>
    databaseName: pulumi.Input<string>
    creationScript: pulumi.Input<string>
    deletionScript: pulumi.Input<string>
    postgresUserName: pulumi.Input<string>
}

export class SchemaProvider implements pulumi.dynamic.ResourceProvider {
    async create(args: SchemaInputs): Promise<pulumi.dynamic.CreateResult> {
        const { Pool } = require("pg");
        const pool = new Pool({
            user: args.creatorName,
            password: args.creatorPassword,
            host: args.serverAddress,
            port: 2000,
            database: args.databaseName
        });
        const scriptExecuted = await pool.query(args.creationScript);

        await pool.end();
        return {id: "postgresqlSchema-" + crypto.randomBytes(16).toString('hex'), outs: args};
    }

    async delete(id: string, args: SchemaInputs): Promise<void> {
        const { Pool } = require("pg");
        const pool = new Pool({
            user: args.creatorName,
            password: args.creatorPassword,
            host: args.serverAddress,
            port: 2000,
            database: args.databaseName
        });
        const scriptExecuted = await pool.query(args.deletionScript);
        await pool.end();
    }

    async diff(id: string, oldArgs: SchemaInputs, newArgs: SchemaInputs): Promise<pulumi.dynamic.DiffResult> {
        let changes: boolean = ((oldArgs.creatorName != newArgs.creatorName) ||
            (oldArgs.creatorPassword != newArgs.creatorPassword) || (oldArgs.serverAddress != newArgs.serverAddress) ||
            (oldArgs.databaseName != newArgs.databaseName) || (oldArgs.creationScript != newArgs.creationScript) ||
            (oldArgs.deletionScript != newArgs.deletionScript));

        let replaces: string[] = [];
        if (oldArgs.serverAddress != newArgs.serverAddress) { replaces.push("serverAddress") };
        if (oldArgs.databaseName != newArgs.databaseName) { replaces.push("databaseName") };
        if (oldArgs.creationScript != newArgs.creationScript) { replaces.push("creationScript") };

        return {
            changes: changes,
            replaces: replaces,
            stables: [],
            deleteBeforeReplace: true
        }
    }

    async update(id: string, oldArgs: SchemaInputs, newArgs: SchemaInputs): Promise<pulumi.dynamic.UpdateResult> {
        return { outs: newArgs };
    }
}

export class Schema extends pulumi.dynamic.Resource {
    public readonly creatorName!: pulumi.Output<string>;
    public readonly creatorPassword!: pulumi.Output<string>;
    public readonly serverAddress!: pulumi.Output<string>;
    public readonly databaseName!: pulumi.Output<string>;
    public readonly creationScript!: pulumi.Output<string>;
    public readonly deletionScript!: pulumi.Output<string>;
    constructor(name: string, args: SchemaInputs) {
        super(new SchemaProvider, name, args);
    }
}
```

With the Dynamic provider ready, we can focus on the main `index.ts` file. The first few lines indicate the libraries to import and describe the application's configuration options.

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as pulumi from "@pulumi/pulumi";
import * as postgresql from "@pulumi/postgresql";
import { Schema } from "./PostgreSqlDynamicProvider";
import { table } from "console";

const config = new pulumi.Config();
const sql_admin_name = config.require("sql-admin-name");
const sql_admin_password = config.requireSecret("sql-admin-password");
const sql_user_name = config.require("sql-user-name");
const sql_user_password = config.requireSecret("sql-user-password");
const awsConfig = new pulumi.Config("aws");
const availabilityZone = awsConfig.get("region");
```

Besides for a few language differences, the code for creating the VPC, subnets, and tables is almost identical to our previous projects. Since we will be using Crosswalk, we can leave out a few components and have them be automatically created later.

```typescript
const appVpc = new aws.ec2.Vpc("app-vpc", {
    cidrBlock: "172.31.0.0/16",
    enableDnsHostnames: true
});

const appGateway = new aws.ec2.InternetGateway("app-gateway", {
    vpcId: appVpc.id
});

const appRoutetable = new aws.ec2.RouteTable("app-routetable", {
    routes: [
        {
            cidrBlock: "0.0.0.0/0",
            gatewayId: appGateway.id,
        }
    ],
    vpcId: appVpc.id
});

const appRoutetableAssociation = new aws.ec2.MainRouteTableAssociation("app-routetable-association", {
    routeTableId: appRoutetable.id,
    vpcId: appVpc.id
});

const rdsSecurityGroup = new aws.ec2.SecurityGroup("rds-security-group", {
	vpcId: appVpc.id,
	description: "Enables HTTP access",
    ingress: [{
		protocol: 'tcp',
		fromPort: 0,
		toPort: 65535,
		cidrBlocks: ['0.0.0.0/0'],
    }],
    egress: [{
		protocol: '-1',
		fromPort: 0,
		toPort: 0,
		cidrBlocks: ['0.0.0.0/0'],
    }]
});

const firstRdsSubnet = new aws.ec2.Subnet("first-rds-subnet", {
    vpcId: appVpc.id,
    cidrBlock: "172.31.0.0/20",
    availabilityZone: availabilityZone + "a"
});

const secondRdsSubnet = new aws.ec2.Subnet("second-rds-subnet", {
    vpcId: appVpc.id,
    cidrBlock: "172.31.128.0/20",
    availabilityZone: availabilityZone + "b"
});
```

A SubnetGroup and an RDS instance are created. The latter uses PostgreSQL instead of MySQL, and is given an example port of 2000.

```typescript
const rdsSubnetGroup = new aws.rds.SubnetGroup("rds-subnet-group", {
    subnetIds: [firstRdsSubnet.id, secondRdsSubnet.id]
});

const postgresqlRdsServer = new aws.rds.Instance("postgresql-rds-server", {
    engine: "postgres",
    username: sql_admin_name,
    password: sql_admin_password,
    instanceClass: "db.t2.micro",
    allocatedStorage: 20,
    skipFinalSnapshot: true,
    publiclyAccessible: true,
    port: 2000,
    dbSubnetGroupName: rdsSubnetGroup.name,
    vpcSecurityGroupIds: [rdsSecurityGroup.id]
});
```

Pulumi offers some additional tools to make handling PostgreSQL easier.

```typescript
const postgresqlProvider = new postgresql.Provider("postgresql-provider", {
        host: postgresqlRdsServer.address,
        port: postgresqlRdsServer.port,
        username: sql_admin_name,
        password: sql_admin_password,
        superuser: false
});
```

We initialize the example database and create a user to manage it.

```typescript
const postgresDatabase = new postgresql.Database("postgresql-database", {
    name: "votes"}, {
    provider: postgresqlProvider
});

const postgresUser = new postgresql.Role("postgres-standard-role", {
    name: sql_user_name,
    password: sql_user_password,
    superuser: false,
    login: true,
    connectionLimit: -1}, {
    provider: postgresqlProvider
});
```

The Dynamic provider is used to create a schema and a table, grant permissions for our user to edit and select it, and to populate the table with two initial voting options.

```typescript
const creation_script = `
    CREATE SCHEMA voting_app;
    CREATE TABLE voting_app.choice(
        choice_id SERIAL PRIMARY KEY,
        text VARCHAR(255) NOT NULL,
        vote_count INTEGER NOT NULL
    );
    GRANT USAGE ON SCHEMA voting_app TO ${sql_user_name};
    GRANT SELECT, UPDATE ON ALL TABLES IN SCHEMA voting_app TO ${sql_user_name};
    INSERT INTO voting_app.choice (text, vote_count) VALUES('Tabs', 0);
    INSERT INTO voting_app.choice (text, vote_count) VALUES('Spaces', 0);
`;

const deletion_script = "DROP SCHEMA IF EXISTS voting_app CASCADE";

const postgresqlVotesTable = new Schema("postgresql-votes-schema", {
    creatorName: sql_admin_name,
    creatorPassword: sql_admin_password,
    serverAddress: postgresqlRdsServer.address,
    databaseName: postgresDatabase.name,
    creationScript: creation_script,
    deletionScript: deletion_script,
    postgresUserName: postgresUser.name
});
```

With the basic infrastructure and provider finished, we can now write the code that deploys our application to ECS. As mentioned before, we will use Pulumi Crosswalk, a collection of libraries that use automatic well-architected best practices to make common infrastructure-as-code tasks in AWS easier and more secure.

The first item we set up will be the server. The Network Listener is assigned the same port that the server is configured for, which in our case is 5000. A set of environment variables representing our PostgreSQL connection credentials are given directly to the `awsx.ecs.FargateService`. In the end, what would have otherwise been over 150 lines of code can be done in just under 20.

```typescript
const serversideListener = new awsx.elasticloadbalancingv2.NetworkListener("server-side-listener", { port: 5000 });
const serversideService = new awsx.ecs.FargateService("server-side-service", {
    taskDefinitionArgs: {
        containers: {
            serversideService: {
                image: awsx.ecs.Image.fromPath("server-side-service", "./serverside"),
                memory: 512,
                portMappings: [serversideListener],
                environment: [
                    { name: "USER_NAME", value: sql_user_name },
                    { name: "USER_PASSWORD", value: sql_user_password },
                    { name: "RDS_ADDRESS", value: postgresqlRdsServer.address },
                    { name: "RDS_PORT", value: String(2000) },
                    { name: "DATABASE_NAME", value: postgresDatabase.name },
                ],
            },
        },
    },
});
```

The same is true for the client service, which can be reduced to a short and easily understandable format. By default, React is configured to use the port 3000, but it can easily be updated to a different one. The `SERVER_HOSTNAME` environment variable which we pass in is used when the container starts to generate a tiny configuration file at runtime called `serverParams.js` with the URL. This way, we do not have to rebuild the entire docker image should the server URL change.

```typescript
const clientsideListener = new awsx.elasticloadbalancingv2.NetworkListener("client-side-listener", { port: 3000 });
const clientsideService = new awsx.ecs.FargateService("client-side-service", {
    taskDefinitionArgs: {
        containers: {
            clientsideService: {
                image: awsx.ecs.Image.fromPath("client-side-service", "./clientside"),
                memory: 512,
                portMappings: [clientsideListener],
                environment: [
                    { name: "SERVER_HOSTNAME", value: serversideListener.endpoint.hostname },
                ],
            },
        },
    },
});
```

To connect to our PERN stack application, we export the address of the clientside listener and its port, and open it
in a browser window under a port of 3000.

```typescript
export let URL = clientsideListener.endpoint.hostname;
```

In this example, I explained a few basic principles behind PERN stack applications, and showed how simple it is to create infrastructure to deploy them on ECS. A flexible and optimized tool, Pulumi Crosswalk allows everything from creating simple example applications, to scaling workload, securing and integrating it with your existing infrastructure, or going to production in multiple complex environments.

Next week, I'll _______.

The blog post's full code can be [found on Github](https://github.com/pulumi/examples/tree/vova/aws-pern-voting-app/aws-pern-voting-app).
