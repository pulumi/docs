---
title: "Migrating a cloud application to Kubernetes"
date: 2020-09-14
meta_desc: Using Pulumi to integrate applications with Kubernetes for on-demand scalability and freedom of design.
meta_image: meta.png
authors: ["vova-ivanov"]
tags: ["aws", "typescript", "containers", "kubernetes", "docker"]
---

In this blog post, we will explore and demonstrate the advantages of Kubernetes by converting and deploying our [PERN application]({{< relref "/blog/deploying-a-pern-stack-application-to-aws" >}}) to Amazon EKS. With the help of Pulumi, the process becomes greatly simplified and allows us to focus more on the big picture of designing our cloud architecture.

<!--more-->

Kubernetes offers several distinct advantages over individually deploying Docker containers to the cloud. Firstly, it's a robust system for minimizing downtime and rolling out updates. If a pod or node is shut down, a new one is automatically allocated to take its place. Secondly, Kubernetes can scale and distribute your infrastructure. By placing containers into pods, Kubernetes allows you to design the right cloud setup to fit your target effortlessly. And lastly, Kubernetes runs on many cloud providers, letting you choose your organization's best cloud service provider. Since AWS, Azure, and GCP all support deploying Kubernetes, you have the option of switching if the need arises.

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

The project will require several configuration variables, which we set using `pulumi config set`. The variables are used to configure the PostgreSQL admin account, a user account for initializing the schema and table, and its region.

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
"@pulumi/cloud-aws": "^0.19.0"
```

Some of the components of our Kubernetes project are nearly identical to those in the PERN application. We can copy many of these files from the example into our directory.

```bash
$ cd ..
$ cp -r aws-pern-voting-app/clientside/ aws-ts-k8s-voting-app/clientside
$ cp -r aws-pern-voting-app/serverside/ aws-ts-k8s-voting-app/serverside
$ cd aws-ts-k8s-voting-app
```

To prepare our application for Kubernetes, we create a PostgreSQL Docker container for the application. Although this is slightly more complex than directly asking AWS to provision an RDS instance, the underlying mechanics are the same for either approach.

The first step is to create two directories:

```bash
$ mkdir databaseside && cd databaseside
$ mkdir database
```

Like the PERN app, the outer `databaseside` folder holds our Dockerfile, while the inner `database` folder contains code.

```bash
FROM ubuntu:18.04

WORKDIR /

EXPOSE 5432

RUN apt update && \
    apt install -y postgresql

ADD database /database

CMD [ "/database/startDatabase.sh" ]
```

Our setup doesn't require any files, and so the only thing we need to put in the `database` folder is a `startDatabase.sh` script that launches the database, configures users, and creates a table.

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
    echo "psql -U postgres -c \"CREATE ROLE $ADMIN_NAME LOGIN SUPERUSER PASSWORD *********;\""
    psql -U postgres -c "CREATE ROLE $ADMIN_NAME LOGIN SUPERUSER PASSWORD '$ADMIN_PASSWORD';"
    echo "psql -U postgres -c \"CREATE USER $USER_NAME WITH PASSWORD *********;\""
    psql -U postgres -c "CREATE USER $USER_NAME WITH PASSWORD '$USER_PASSWORD';"
    echo "psql -U postgres -c \"ALTER ROLE postgres WITH NOLOGIN;\""
    psql -U postgres -c "ALTER ROLE postgres WITH NOLOGIN;"
    set -x

    psql -U $ADMIN_NAME -d postgres -c "CREATE DATABASE $DATABASE_NAME;"
    psql -U $ADMIN_NAME -d $DATABASE_NAME -c "
        CREATE SCHEMA voting_app;
        CREATE TABLE voting_app.choice(
            choice_id SERIAL PRIMARY KEY,
            text VARCHAR(255) NOT NULL,
            vote_count INTEGER NOT NULL
        );
        GRANT USAGE ON SCHEMA voting_app TO $USER_NAME;
        GRANT SELECT, UPDATE ON ALL TABLES IN SCHEMA voting_app TO $USER_NAME;
        INSERT INTO voting_app.choice (text, vote_count) VALUES('Tabs', 0);
        INSERT INTO voting_app.choice (text, vote_count) VALUES('Spaces', 0);
    "
    su postgres -c "/usr/lib/postgresql/10/bin/pg_ctl -D /persistentVolume/postgresqlDb --wait -l logfile stop"
fi

su postgres -c "/usr/lib/postgresql/10/bin/postgres -D /persistentVolume/postgresqlDb"
```

Because we don't have any SSL certificates to authenticate and encrypt internet traffic, the way the server connects to the database needs to be modified to include an `ssl: false` pool parameter.

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

With our server, client, and database in place, we can focus on the infrastructure. We start with importing libraries and describing the application's configuration options.

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const sqlAdminName = config.require("sql-admin-name");
const sqlAdminPassword = config.requireSecret("sql-admin-password");
const sqlUserName = config.require("sql-user-name");
const sqlUserPassword = config.requireSecret("sql-user-password");
const awsConfig = new pulumi.Config("aws");
const region = aws.config.region;
```

The central part of our application is an AWS Elastic Kubernetes Cluster. It holds our application and dictates how many nodes should be allocated for the processes running inside the cluster.

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

Kubernetes nodes use ephemeral storage. When Pods shut down or get restarted, everything is erased. To create a permanent storage system suitable for our database, we need a Persistent Volume instance.

```typescript
const ebsVolume = new aws.ebs.Volume("storage-volume", {
    size: 1,
    type: "gp2",
    availabilityZone: region + "a",
    encrypted: true,
    }, {
    protect: false,
});
```

Now that the infrastructure for our database is ready, we can launch a PostgreSQL server on the cloud in the form of a Deployment. Deployments offer a multitude of customization options ranging from attaching volumes, setting the memory and cpu requirements, to specifying which deployments can and cannot be run on the same node.

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

In order to have a a way for the pods in cluster to communicate with our database, we create a Kubernetes service for it. It is best practice to keep databases and other similar components entirely within the cluster, and not allow them to be accessed directly the internet.

```typescript
const databasesideListener = new k8s.core.v1.Service("database-side-listener", {
    metadata: { labels: databaseDeployment.metadata.labels },
    spec: {
        type: "ClusterIP",
        ports: [{ port: 5432, targetPort: "http" }],
        selector: databaseAppLabels,
        publishNotReadyAddresses: false,
    }}, {
    provider: eksCluster.provider,
    }
);

const postgresqlAddress = databasesideListener.spec.clusterIP;
});
```

Now, all that remains is deploying the client and server containers to Kubernetes. Since the PERN application already deployed them as docker containers, it doesn't take much effort to reconfigure it for Kubernetes. Unlike the database, these components can safely be open to the Internet using a service with a Load Balancer type.

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

To give us a simple way to connect to our application, we export the clientside listener's address. We can now open a browser window with the URL and port number to view our application.

```typescript
export const kubeConfig = eksCluster.kubeconfig;
export const URL = clientsideListener.status.loadBalancer.ingress[0].hostname;
```

In this example, we demonstrated the benefits Kubernetes offers and showed how to use Pulumi to deploy an application to Kubernetes hosted on AWS. Although it might seem unnecessary to use such a system for only a single voting app, the advantages of running your project in the form of containerized services become apparent as your application grows in size.

Next week, we'll explore applications using the MERN stack: MongoDB, Express, React, and NodeJS.

The blog post's code can be [found on Github](https://github.com/pulumi/examples/tree/master/aws-ts-k8s-voting-app).
