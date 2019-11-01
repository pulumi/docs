---
title: "Introducing kx: Kubernetes the Easy Way"
authors: ["levi-blackstone"]
tags: ["Kubernetes"]
meta_desc: "todo"
date: "2019-11-01"

---

# Introducing kx: Kubernetes the Easy Way

With great power comes great complexity. The sheer number of configuration
options can be overwhelming to users. YAML wasn't designed for programming, yet
that's exactly where most Kubernetes users spend their time. Templating tools
and YAML-transpilers add useful flexibility, but at the cost of even greater
complexity. We are often distracted by this complexity from the real problems we
are trying to solve. Helm charts are a pain to write, and even worse to maintain
because they do not meaningfully raise the level of abstraction. Kubernetes' API
is vast and verbose. 

In this post, we introduce the kx library, designed to make it easier to write
and maintain applications on Kubernetes. 

## Express yourself

YAML is the common language of Kubernetes. Most users either write YAML
directly, or use tools that indirectly produce YAML. The Kubernetes API is
powerful and well specified, but ease of use is not one of its strengths.
Kubernetes YAML has been compared to assembly language. I find this analogy to
be particularly apt: it gives users complete control over the system, but is
closely tied to low-level implementation details. Most Kubernetes applications
require users to define several different resource types, and then manually tie
them together with text strings using labels and selectors. The API for each of
these resource types is complex and deeply nested, so users often rely on
copy-pasted examples and frequent references to the API spec. Wouldn't it be
nice if there was a way to ignore these low-level implementation details and get
back to thinking about your application?

Enter kx: Kubernetes configuration built for humans rather than machines! Two
primary goals for kx are streamlined resource declarations, and the ability to
easily compose different resources to build all the required infrastructure for
an application.

In just a few lines of code, we can create everything we need to deploy a real
application on Kubernetes.

```ts
// Define the application configuration and secrets.
const configs = new kx.ConfigMap("appConfig", {
    file: "./my.cnf"
});
const secrets = new kx.Secret("appSecrets", {
    stringData: {
        "app-password": new kx.RandomPassword("app-password"),
        "database-password": config.databasePassword
    }
});

// Define the application Pod.
const appConfigPath = "/app/config";
const appPod = new kx.PodBuilder({
    containers: [
        {
            image: "app:1.0.0",
            env: {
                "APP_CONFIG_PATH": appConfigPath,
                "APP_USER": config.user,
                "APP_PASSWORD": secrets.asEnvValue("app-password"),
                "APP_DATABASE_PASSWORD": secrets.asEnvValue("database-password"),
            },
            volumeMounts: [
                configs.mount(appConfigPath)
            ],
        }
    ]
});

// Create the application Pod as a Deployment and a load-balanced Service.
const app = kx.LoadBalancerWorkload("app", {
    metadata: {
        labels: {
            wordpressLabels
        }
    },
    spec: appPod.asDeploymentSpec({
        replicas: 3,
    })
});
```

Let's break this down and see how it compares to writing the raw YAML.

First, we start off by defining configuration and secrets for our application.
In Kubernetes, this generally means creating ConfigMap and Secret resources that
can be used by application containers.

// TODO: finalize syntax and compare to kubectl and writing the raw YAML

Next, we define the core of the application: the Pod managing our application
container. Notice that this is a "builder" class for defining what the resource
looks like, but we're not creating a Pod on the cluster yet. The PodBuilder
class still gives you complete access to the Pod API, but simplifies the
required syntax in several important ways:

1. Metadata is not needed here. This will be added later when we decide how to
   deploy this Pod to the cluster.
1. Lists of objects have been flattened into maps where possible, so you don't
   have to repeatedly specify `name: "key", value: "value"`.
1. It's easier to refer to other resources in the cluster. This is a key area
   where a general purpose programming language enables completely new ways of
   writing Kubernetes config. Rather than managing labels, selectors, and
   resource names directly, you can refer to the objects themselves. This
   dramatically simplifies the syntax for declaring the environment variables
   and volumes used by the Pod. Compare this to the equivalent YAML declaration.

// TODO: add comparison snippets

Finally, we need to deploy our Pod to the cluster, and expose it to the
internet. This is a very common pattern, so we created a new class, the
`LoadBalancerWorkload` that handles the details for us. Kubernetes includes
several resource types to manage Pods, including the Deployment, StatefulSet,
and DaemonSet. Any of these are supported by calling the related function on the
PodBuilder class. Notice that we only need to specify the relevant details for
the deployed workload: the metadata and number of replicas. From this
information, the kx library is able to infer all of the other API fields and
create a Deployment and matching Service resource. This is a huge benefit, both
in terms of understanding, and also of maintainance. Compare this to the
equivalent YAML that would be required.

// TODO: add comparison snippets

We're excited to share the kx library with you today, and invite you to try it
out and let us know what you think!

## Learn more

// TODO: add links, etc
