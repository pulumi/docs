---
title: "Switching the application stack from PERN to MERN"
date: 2020-09-18
meta_desc: Demonstrating the simplicity, modularity, and reusability of running an application on Kubernetes using Pulumi.
meta_image: meta.png
authors: ["vova-ivanov"]
tags: ["aws", "typescript", "containers", "kubernetes", "docker"]
---

In this blog post, we return to the PERN application we previously [migrated to Kubernetes]({{< relref "/blog/deploying-a-pern-stack-application-to-aws" >}}) and replace the PostgreSQL database with MongoDB. Although it might seem like a difficult task initially, the straightforward design of Pulumi and Kubernetes allows us to easily transition the application form a PERN stack to a MERN one.

<!--more-->

The main difference between PostgreSQL and MongoDB is data is stored. PostgreSQL is a relational database that allows users to create complex tables and relations between values. In contrast, MongoDB is a key-value database that stores data in simple collections instead of a relational model. Because the application takes the form of three distinct components--the client, server, and database--almost all of the changes will occur in the database component. In fact, we can reuse most of the existing code and will be able to change the database without additional hassle.

The first step to switching the stack is to clone the [PERN Kubernetes example](https://github.com/pulumi/examples/tree/master/aws-ts-k8s-voting-app). We'll use a sparse clone to copy only the `aws-ts-k8s-voting-app` directory.

```bash
$ mkdir examples && cd examples
$ git init
$ git remote add origin -f https://github.com/pulumi/examples/
$ git config core.sparseCheckout true
$ echo aws-ts-k8s-voting-app >> .git/info/sparse-checkout
$ git pull origin master
```

The next step is to create a new directory and initialize a Pulumi project with `pulumi new aws-typescript`.

```bash
$ mkdir aws-ts-k8s-mern-voting-app && cd aws-ts-k8s-mern-voting-app
$ pulumi new aws-typescript
```

The project will require several configuration variables, which we set using `pulumi config set`. The variables are used to configure the MongoDB user account, initializing the database schema and table, and its region.

```bash
$ pulumi config set sql-user-name <NAME>
$ pulumi config set sql-user-password <PASSWORD> --secret
$ pulumi config set aws:region <REGION>
```

The `package.json` file lists the libraries used by the project. We will add the following to the `dependencies` section:

```json
    "@pulumi/eks": "^0.20.0",
    "@pulumi/cloud-aws": "^0.19.0"
```

As most of our project components are nearly identical to those in the PERN Kubernetes application, we can copy many of them into our directory.

```bash
$ cd ..
$ cp -r aws-ts-k8s-voting-app/clientside/ aws-ts-k8s-mern-voting-app/clientside
$ cp -r aws-ts-k8s-voting-app/serverside/ aws-ts-k8s-mern-voting-app/serverside
$ cp -r aws-ts-k8s-voting-app/databaseside/ aws-ts-k8s-mern-voting-app/databaseside

$ cd aws-ts-k8s-voting-app
```

Hosting MongoDB will require a rework of the database Docker container and startup scripts. Like before, the outer `databaseside` folder holds our Dockerfile, while the inner `database` folder contains code.

```bash
FROM ubuntu:18.04

WORKDIR /

EXPOSE 5432

RUN apt update && \
    apt install -y mongodb

ADD database /database

CMD [ "/database/startDatabase.sh" ]
```

Our setup doesn't require any files, and so the only thing we need to put in the `database` folder is a `startDatabase.sh` script that launches the database, configures users, and creates a table.

```bash
#!/bin/bash
set -exu
FILE=/persistentVolume/mongod.lock

if test -f "$FILE"; then
    echo "/persistentVolume already contains MongoDB, no need to initialize database."
    mongod --fork --dbpath /persistentVolume/ --bind_ip_all --logpath /persistentVolume/mongoLogs
else
    echo "/persistentVolume is empty, and we need to initialize the MongoDB database."
    mongod --fork --dbpath /persistentVolume/ --bind_ip_all --logpath /persistentVolume/mongoLogs
    echo "use $DATABASE_NAME
    db.choices.insert({ _id: 0, text: \"Tabs\", vote_count: 0 })
    db.choices.insert({ _id: 1, text: \"Spaces\", vote_count: 0 })
    db.createUser(
        {
            user: \"$USER_NAME\",
            pwd: \"$USER_PASSWORD\",
            roles: [ { role: \"readWrite\", db: \"$DATABASE_NAME\" } ]
        }
    )" | mongo
fi

while true; do
    sleep 3600
done
```

With the database in place, all that is left is to make some small MongoDB-specific changes to how the client and server components send queries.

The server component will be changed to use a model.js file, which acts as a blueprint for the database's choices.

```javascript
const mongoose = require("mongoose");

let Choice = new mongoose.Schema({
    _id: Number,
    text: {
        type: String
    },
    vote_count: {
        type: Number
    },
});

module.exports = mongoose.model("choice", Choice);
```

Likewise, the `db.js` file will be modified to create a specialized to our database.

```javascript
const mongoose = require("mongoose");

const url = "mongodb://"
  + process.env["MONGODB_ADDRESS"]
  + ":" + process.env["MONGODB_PORT"]
  + "/" + process.env["DATABASE_NAME"]

mongoose.connect(url, {
  useNewUrlParser: true,
  user: process.env["USER_NAME"],
  pass: process.env["USER_PASSWORD"]
});

const connection = mongoose.connection;
module.exports = connection;
```

And finally, the `index.js` file holding the main code of our server will be modified to send queries to the MongoDB database.

```javascript
const express = require("express");
const app = express();
const cors = require("cors");
const connection = require("./db");

app.use(cors());
app.use(express.json());

connection.once("open", function() {
  console.log("Connection opened to database!");
})

let Choice = require("./model");

app.get("/voting", async (request, response) => {
  console.log("Get all request");
  Choice.find(function(error, result) {
    if (error) {
        console.log(error);
    } else {
      response.json(result);
    }
  });
});

app.post("/voting/:id", async (request, response) => {
  const { id } = request.params;
  console.log("Casting vote for: " + id);
  
  Choice.findById(id, function(error, result) {
    if (!result) {
      response.status(404).send("Choice not found");
    } else {
      result.vote_count = result.vote_count + 1;
      result.save().then(result => {
        response.json("Vote successfully cast");
      }).catch(error => {
        response.status(400).send("Failed to cast vote");
      });
    }
  });
});

app.listen(5000, async () => {
  console.log("server has started on port 5000");
});
```

The `VotingComponent.js` file in the client will be slightly modified to reference choices by their MongoDB `_id` parameter.

```javascript
import React, { Fragment, useEffect, useState } from "react";
const fullServerUrl = "http://" + window.SERVER_URL + ":5000/voting";

const ListChoices = () => {
  const [choices, setChoices] = useState([]);

  const getChoices = async () => {...};

  useEffect(() => {...}, []);

  return (
    <Fragment>
      <h1 className="text-center mt-5">Pulumi Voting App</h1>
      {" "}
      <table className="table mt-5 text-center">
        <thead>
          <tr>
            <th>Choice</th>
            <th>Votes</th>
          </tr>
        </thead>
        <tbody>
          {choices.map(choice => (
            <tr key={choice._id}>
              <td>{choice.text}</td>
              <td>{choice.vote_count}</td>
              <td>
                <button
                  className="btn btn-success"
                  onClick={() => castVote(choice._id)}
                >
                  Vote
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </Fragment>
  );
};

async function castVote(id) {...}

export default ListChoices;
```

Now that, server, client, and database have been fully converted to use MongoDB, we can make the last remaining change in the infrastructure by updating the database deployment and service.

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const sqlUserName = config.require("sql-user-name");
const sqlUserPassword = config.requireSecret("sql-user-password");
const region = aws.config.region;

const eksCluster = new eks.Cluster(...);

const ebsVolume = new aws.ebs.Volume(...);

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
                    ports: [{ name: "http", containerPort: 27017 }],
                    env: [
                        { name: "DATABASE_NAME", value: databaseName },
                        { name: "USER_NAME", value: sqlUserName },
                        { name: "USER_PASSWORD", value: sqlUserPassword },

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

const databasesideListener = new k8s.core.v1.Service("database-side-listener", {
    metadata: { labels: databaseDeployment.metadata.labels },
    spec: {
        type: "ClusterIP",
        ports: [{ port: 27017, targetPort: "http" }],
        selector: databaseAppLabels,
        publishNotReadyAddresses: false,
    }}, {
    provider: eksCluster.provider,
    }
);

const mongodbAddress = databasesideListener.spec.clusterIP;

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
                        { name: "MONGODB_ADDRESS", value: mongodbAddress },
                        { name: "MONGODB_PORT", value: String(27017) },
                        { name: "DATABASE_NAME", value: databaseName },
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

const serversideListener = new k8s.core.v1.Service(...);

const clientAppName = ...;
const clientAppLabels = { ... };
const clientDeployment = new k8s.apps.v1.Deployment(...);

const clientsideListener = new k8s.core.v1.Service(...);
```

To give us a simple way to connect to our application, we export the clientside listener's address. We can now open a browser window with the URL and port number to view our application.

```typescript
export const kubeConfig = eksCluster.kubeconfig;
export const URL = clientsideListener.status.loadBalancer.ingress[0].hostname;
```

In this example, we showed how to change a PERN stack-based application to use MERN, and demonstrated the ease with which a designer can swap out different components. The isolated nature of containerized applications allows for a great deal of modularity. It can significantly reduce the amount of time spent renovating previously written code to fit any added new components.

The MERN application code is [on Github](https://github.com/pulumi/examples/tree/master/aws-ts-k8s-mern-voting-app).
