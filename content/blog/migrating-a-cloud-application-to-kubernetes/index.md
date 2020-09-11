---
title: "Migrating a cloud application to Kubernetes"
date: 2020-09-11
meta_desc: Using Pulumi to integrate applications with Kubernetes and allow for on-demand scalability of cloud architecture and freedom of design.
meta_image: meta.png
authors: ["vova-ivanov"]
tags: ["aws", "typescript", "docker", "kubernetes"]
---

In this blog post, we will explore the advantages of Kubernetes, and will demonstrate how to use it by converting and deploying our [PERN application]({{< relref "/blog/deploying-a-pern-stack-application-to-aws" >}}) to Amazon EKS. With the help of Pulumi, the process becomes greatly simplified and allows us to focus more on the big picture of designing our cloud architecture.

<!--more-->

Kubernetes offers several distinct advantages over individually deploying Docker containers to the cloud. Firstly, is its robust system for minimizing downtime and rolling out updates. If a pod or node were to be shut down, a new one will be automatically allocated to take its place. Secondly, is the ability to scale and distribute your infrastructure. By simplifying containers into pods, Kubernetes allows you to effortlessly design the right cloud setup to fit your target. And lastly, is the interchangeability of cloud providers that comes with it. Since AWS, Azure, and GCP all support deploying Kubernetes, it means that you are not forced to stick with one provider, and have the option of easily switching if the need arises.

The first step to creating the app is to clone the [Typescript PERN example](https://github.com/pulumi/examples/tree/master/aws-pern-voting-app). We'll use a sparse clone to copy only the `aws-pern-voting-app` directory.

```bash
$ mkdir examples && cd examples
$ git init
$ git remote add origin -f https://github.com/pulumi/examples/
$ git config core.sparseCheckout true
$ echo aws-pern-voting-app >> .git/info/sparse-checkout
$ git pull origin master
```

The next step is to create a new directory and initialize a Pulumi project with `pulumi new aws-typescript`.

```bash
$ mkdir aws-ts-k8s-voting-app && cd aws-ts-k8s-voting-app
$ pulumi new aws-typescript
```

The project will require several configuration variables, which we set using `pulumi config set`. The variables are used to configure the PostgreSQL admin account, a user account for initializing the schema and table, and the database's region.

```bash
$ pulumi config set sql-admin-name <NAME>
$ pulumi config set sql-admin-password <PASSWORD> --secret
$ pulumi config set sql-user-name <NAME>
$ pulumi config set sql-user-password <PASSWORD> --secret
$ pulumi config set aws:region <REGION>
```

The `package.json` file lists the libraries used by the project. We will add the following to the `dependencies` section:

```json
"@pulumi/eks": "^0.20.0",
"@pulumi/cloud-aws": "^0.19.0",
"@pulumi/postgresql": "^2.3.0",
"pg": "^8.3.3"
```

Some of the components of our Kubernetified project will be almost identical to that of the PERN application. We can copy most of these files from the example into our directory.

```bash
$ cd ..
$ cp -r aws-pern-voting-app/clientside/ aws-ts-k8s-voting-app/clientside
$ cp -r aws-pern-voting-app/serverside/ aws-ts-k8s-voting-app/serverside
$ cp -r aws-pern-voting-app/postgresql_dynamic_provider.ts aws-ts-k8s-voting-app//postgresql_dynamic_provider.ts
$ cd aws-ts-k8s-voting-app
```

Because we haven't set up our database with any SSL certificates to authenticate and encrypt internet traffic, the PostgreSQL Dynamic Provider used in the PERN app to create schemas will need to be slightly modified to include an `ssl: false` pool parameter in the `create` and `delete` functions.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as crypto from "crypto";

export interface SchemaInputs {...}

export class SchemaProvider implements pulumi.dynamic.ResourceProvider {
    async create(args: SchemaInputs): Promise<pulumi.dynamic.CreateResult> {
        const { Pool } = require("pg");
        const pool = new Pool({
            user: args.creatorName,
            password: args.creatorPassword,
            host: args.serverAddress,
            port: 5432,
            database: args.databaseName,
            ssl: false,
        });

        const scriptExecuted = await pool.query(args.creationScript);
        await pool.end();
        return {id: "postgresqlSchema-" + crypto.randomBytes(16).toString("hex"), outs: args};
    }

    async delete(id: string, args: SchemaInputs): Promise<void> {
        const { Pool } = require("pg");
        const pool = new Pool({
            user: args.creatorName,
            password: args.creatorPassword,
            host: args.serverAddress,
            port: 5432,
            database: args.databaseName,
            ssl: false,
        });

        const
        scriptExecuted = await pool.query(args.deletionScript);
        await pool.end();
    }

    async diff(id: string, oldArgs: SchemaInputs, newArgs: SchemaInputs): Promise<pulumi.dynamic.DiffResult> {...}
    async update(id: string, oldArgs: SchemaInputs, newArgs: SchemaInputs): Promise<pulumi.dynamic.UpdateResult> {...}
}
```

Likewise, we need to add an `ssl: false` option to `serverside/server/db.js` as well.

```typescript
const Pool = require("pg").Pool;

const pool = new Pool({
    user: process.env["USER_NAME"],
    password: process.env["USER_PASSWORD"],
    host: process.env["POSTGRES_ADDRESS"],
    port: process.env["POSTGRES_PORT"],
    database: process.env["DATABASE_NAME"],
    ssl: false,
});

module.exports = pool;
```

In order to fully prepare our application for Kubernetes, a Docker container has to be created to act as the PostgreSQL database for the application. Although this is slightly more complex than directly asking AWS to provision an RDS instance, the underlying mechanics behind both approaches are the same.

The first step, is to create two directories:

```bash
$ mkdir databaseside && cd databaseside
$ mkdir database
```

Similar to the PERN app, the outer `databaseside` folder will hold our Dockerfile, while the inner `database` folder will contain any code that we need.

```bash
FROM ubuntu:18.04

WORKDIR /

EXPOSE 5432

RUN apt update && \
    apt install -y postgresql

ADD database /database

CMD [ "/database/startDatabase.sh" ]
```

Our setup doesn't require any files, and so the only thing we need to put in the `database` folder is the `startDatabase.sh` script that launches it.

```bash
#!/bin/bash
set -exu
FILE=/persistentVolume/postgresqlDb/postgresql.conf

chown postgres:postgres /persistentVolume

if test -f "$FILE"; then
    echo "/persistentVolume already contains postgresqlDb, no need to initialize database."
else
    echo "/persistentVolume is empty, and we need to initialize the postgresql database."
    cd /persistentVolume
    su postgres -c "/usr/lib/postgresql/10/bin/initdb -D /persistentVolume/postgresqlDb"

    echo "host all  all    0.0.0.0/0  md5" >> /persistentVolume/postgresqlDb/pg_hba.conf
    echo "host all  all    ::/0       md5" >> /persistentVolume/postgresqlDb/pg_hba.conf
    echo "listen_addresses='*'" >> /persistentVolume/postgresqlDb/postgresql.conf

    su postgres -c "/usr/lib/postgresql/10/bin/pg_ctl -D /persistentVolume/postgresqlDb --wait -l logfile start"

    set +x
    echo "psql -U postgres -c \"CREATE ROLE $ADMIN_NAME LOGIN SUPERUSER PASSWORD '*********';\""
    psql -U postgres -c "CREATE ROLE $ADMIN_NAME LOGIN SUPERUSER PASSWORD '$ADMIN_PASSWORD';"
    echo "psql -U postgres -c \"ALTER ROLE `postgres` WITH NOLOGIN\";"
    psql -U postgres -c "ALTER ROLE \"postgres\" WITH NOLOGIN;"
    set -x

    su postgres -c "/usr/lib/postgresql/10/bin/pg_ctl -D /persistentVolume/postgresqlDb --wait -l logfile stop"
fi

su postgres -c "/usr/lib/postgresql/10/bin/postgres -D /persistentVolume/postgresqlDb"
```

With our Dynamic Provider, server, client, and database in place, we can focus on the main `index.ts` file. We start with importing libraries and describing the application's configuration options.

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";
import * as postgresql from "@pulumi/postgresql";
import * as pulumi from "@pulumi/pulumi";
import { Schema } from "./postgresql_dynamic_provider";

const config = new pulumi.Config();
const sqlAdminName = config.require("sql-admin-name");
const sqlAdminPassword = config.requireSecret("sql-admin-password");
const sqlUserName = config.require("sql-user-name");
const sqlUserPassword = config.requireSecret("sql-user-password");
const awsConfig = new pulumi.Config("aws");
const region = aws.config.region;
```

The central part of our application will be an AWS Elastic Kubernetes Cluster. It holds our application, and dictates how many nodes should be allocated for the processes running inside the cluster.

```typescript
const eksCluster = new eks.Cluster("eksCluster", {
    name: "eksCluster",
    instanceType: "t2.medium",
    desiredCapacity: 3,
    minSize: 2,
    maxSize: 4,
    deployDashboard: false,
    enabledClusterLogTypes: [
        "api",
        "audit",
        "authenticator",
    ],
});
```

Kubernetes nodes use ephemeral storage, meaning that when they shut down or get restarted, everything is erased. To create a permanent storage system suitable for our database, we need a Persistent Volume instance.

```typescript
const ebsVolume = new aws.ebs.Volume("storage-volume", {
    size: 10,
    type: "gp2",
    availabilityZone: region + "a",
    encrypted: true,
    }, {
    protect: false,
});
```

Now that the infrastructure for our database is ready, we can launch our very own PostgreSQL server on the cloud in the form of a Deployment. Deployments offer a multitude of different customization options ranging from attaching volumes, setting the memory and CPU requirements, to specifying which deployments can and cannot be run on the same node.

```typescript
const databaseAppName = "database-side-service";
const databaseAppLabels = { appClass: databaseAppName };
const databaseDeployment = new k8s.apps.v1.Deployment(databaseAppName, {
    metadata: { name: databaseAppName, labels: databaseAppLabels },
    spec: {
        replicas: 1,
        selector: { matchLabels: databaseAppLabels },
        template: {
            metadata: { labels: databaseAppLabels },
            spec: {
                containers: [{
                    name: databaseAppName,
                    image: awsx.ecr.buildAndPushImage("database-side-service", "./databaseside").image(),
                    ports: [{ name: "http", containerPort: 5432 }],
                    env: [
                        { name: "ADMIN_NAME", value: sqlAdminName },
                        { name: "ADMIN_PASSWORD", value: sqlAdminPassword },
                    ],
                    volumeMounts: [{
                        name: "persistent-volume",
                        mountPath: "/persistentVolume"
                    }],
                    resources: {
                        limits: {
                            memory: "1Gi",
                            cpu: "1000m"
                        }
                    }
                }],
                volumes: [{
                    name: "persistent-volume",
                    awsElasticBlockStore: {
                        volumeID: ebsVolume.id,
                    },
                }],
                affinity: {  
                    nodeAffinity: {
                        requiredDuringSchedulingIgnoredDuringExecution: {
                            nodeSelectorTerms: [{
                                matchExpressions: [{
                                    key: "failure-domain.beta.kubernetes.io/zone",
                                    operator: "In",
                                    values: [ebsVolume.availabilityZone],
                                }]
                            }]
                        }
                    }
                }
            }
        },
        strategy: {
            type: "Recreate"
        }
    }}, {
    deleteBeforeReplace: true,
    provider: eksCluster.provider,
});
```

In order to have a clean, simple URL through which we can access the database, we create a Kubernetes service for it.

```typescript
const databasesideListener = new k8s.core.v1.Service("database-side-listener", {
    metadata: { labels: databaseDeployment.metadata.labels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 5432, targetPort: "http" }],
        selector: databaseAppLabels,
        publishNotReadyAddresses: false,
    }}, {
    provider: eksCluster.provider,
    }
);

const postgresqlAddress = databasesideListener.status.loadBalancer.ingress[0].hostname;
});
```

We can now treat our Kubernetes database the same way as we did our RDS one. Like the PERN application, we create a user, schema, and table, grant permissions for our user to edit and select it, and populate the table with two initial voting options.

```typescript
const postgresqlProvider = new postgresql.Provider("postgresql-provider", {
        host: postgresqlAddress,
        port: 5432,
        username: sqlAdminName,
        password: sqlAdminPassword,
        superuser: false,
        sslmode: "disable",
});

const postgresDatabase = new postgresql.Database("postgresql-database", {
    name: "votes"}, {
    provider: postgresqlProvider,
});

const postgresUser = new postgresql.Role("postgres-standard-role", {
    name: sqlUserName,
    password: sqlUserPassword,
    superuser: false,
    login: true,
    connectionLimit: -1}, {
    provider: postgresqlProvider,
});

const creationScript = `
    CREATE SCHEMA voting_app;
    CREATE TABLE voting_app.choice(
        choice_id SERIAL PRIMARY KEY,
        text VARCHAR(255) NOT NULL,
        vote_count INTEGER NOT NULL
    );
    GRANT USAGE ON SCHEMA voting_app TO ${sqlUserName};
    GRANT SELECT, UPDATE ON ALL TABLES IN SCHEMA voting_app TO ${sqlUserName};
    INSERT INTO voting_app.choice (text, vote_count) VALUES('Tabs', 0);
    INSERT INTO voting_app.choice (text, vote_count) VALUES('Spaces', 0);
`;

const deletionScript = "DROP SCHEMA IF EXISTS voting_app CASCADE";

const postgresqlVotesSchema = new Schema("postgresql-votes-schema", {
    creatorName: sqlAdminName,
    creatorPassword: sqlAdminPassword,
    serverAddress: postgresqlAddress,
    databaseName: postgresDatabase.name,
    creationScript: creationScript,
    deletionScript: deletionScript,
    postgresUserName: postgresUser.name,
});
```

And now, all that remains is to deploy the client and server containers to Kubernetes. Since the PERN application already deployed them as docker containers, it doesn't take too much effort to reconfigure it for Kubernetes.

We'll first set up the server deployment:

```typescript
const serverAppName = "server";
const serverAppLabels = { appClass: serverAppName };
const serverDeployment = new k8s.apps.v1.Deployment("server-side-service", {
    metadata: { labels: serverAppLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: serverAppLabels },
        template: {
            metadata: { labels: serverAppLabels },
            spec: {
                containers: [{
                    name: serverAppName,
                    image: awsx.ecr.buildAndPushImage("server-side-service", "./serverside").image(),
                    ports: [{ name: "http", containerPort: 5000 }],
                    env: [
                        { name: "USER_NAME", value: sqlUserName },
                        { name: "USER_PASSWORD", value: sqlUserPassword },
                        { name: "POSTGRES_ADDRESS", value: postgresqlAddress },
                        { name: "POSTGRES_PORT", value: String(5432) },
                        { name: "DATABASE_NAME", value: postgresDatabase.name },
                    ],
                    resources: {
                        limits: {
                            memory: "500Mi",
                            cpu: "500m"
                        }
                    }
                }],
            }
        }
    }}, {
    provider: eksCluster.provider,
});

const serversideListener = new k8s.core.v1.Service("server-side-listener", {
    metadata: { labels: serverDeployment.metadata.labels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 5000, targetPort: "http" }],
        selector: serverAppLabels,
        publishNotReadyAddresses: false,
    }}, {
    provider: eksCluster.provider,
    }
);
```

And lastly, the client deployment.

```typescript
const clientAppName = "client";
const clientAppLabels = { appClass: clientAppName };
const clientDeployment = new k8s.apps.v1.Deployment("client-side-service", {
    metadata: { labels: clientAppLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: clientAppLabels },
        template: {
            metadata: { labels: clientAppLabels },
            spec: {
                containers: [{
                    name: clientAppName,
                    image: awsx.ecr.buildAndPushImage("client-side-service", "./clientside").image(),
                    ports: [{ name: "http", containerPort: 3000 }],
                    env: [
                        { name: "SERVER_HOSTNAME", value: serversideListener.status.loadBalancer.ingress[0].hostname },
                    ],
                    resources: {
                        limits: {
                            memory: "500Mi",
                            cpu: "500m"
                        }
                    },
                }],
            }
        }
    }}, {
    provider: eksCluster.provider,
});

const clientsideListener = new k8s.core.v1.Service("client-side-listener", {
    metadata: { labels: clientDeployment.metadata.labels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 3000, targetPort: "http" }],
        selector: clientAppLabels,
        publishNotReadyAddresses: false,
    }}, {
    provider: eksCluster.provider,
    }
);
```

To make our Kubernetes application available on the Internet, we export the clientside listener's address. We can open a browser window with the URL and port to view our application.

```typescript
export const kubeConfig = eksCluster.kubeconfig;
export const URL = clientsideListener.status.loadBalancer.ingress[0].hostname;
```

In this example, we went over the benefits that Kubernetes offers and showed how to use Pulumi to convert an application to Kubernetes and deploy it on AWS. Although it might seem unnecessary to use such a system for only a single voting app, the advantages of running your project in the form of containerized services quickly become apparent as your application grows in size.  

Next week, we'll explore applications using the MERN stack: MongoDB, Express, React, and NodeJS.

The blog post's code can be [found on Github](https://github.com/pulumi/examples/tree/vova/aws-ts-k8s-voting-app/aws-ts-k8s-voting-app).
