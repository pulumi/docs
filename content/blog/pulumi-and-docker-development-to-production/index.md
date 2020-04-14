---
title: "Pulumi and Docker: Development to Production"
authors: ["sean-gillespie"]
tags: ["Containers","Kubernetes","Docker"]
date: "2019-05-15"
meta_desc: "Use Pulumi's infrastructure as software capability to define your Docker resources without running YAML or Docker Compose."

---

Here at Pulumi, we're big fans of Docker: at this point there is little
doubt that Docker has completely revolutionized the way that we think
about deploying software. However, even in 2019, it's quite difficult to
get Docker containers to production. `docker run` is great, and we all
love it, but unfortunately it's quite a big leap from `docker run` to
running your container in a production-ready environment.

We recently wrote a blog post about
[using AWS Fargate to run your docker containers with our open source packages]({{< relref "get-started-with-docker-on-aws-fargate-using-pulumi" >}}).
In this blog post we're going to focus on another interesting aspect of
Pulumi: being able to re-use your infrastructure code for both
development and production!
<!--more-->

## It's All Code: Composing Docker Containers

In addition to the number of cloud and infrastructure providers that
Pulumi supports, Pulumi also supports
[defining Docker resources]({{< relref "/docs/intro/cloud-providers/docker" >}})
in code. Let's look at this code snippet of Pulumi TypeScript code:

    // This program encodes a complete application: a container running Redis Commander,
    // and a container running Redis. Redis Commander connects directly with Redis.
    //
    // In order for the two containers to communicate directly, they must be placed in the
    // same network. Before creating the containers themselves, we first create the network
    // that will contain both of them.
    const network = new docker.Network("net");

    // Also before creating a container, we must first obtain a "RemoteImage", which is a reference to an external image
    // that is downloaded to the local machine. In this case, we're referring to an image on Docker Hub.
    const redisImage = new docker.RemoteImage("redis-image", {
        name: "redis:latest",
        keepLocally: true, // don't delete the image from the local machine when deleting this resource.
    });

    // We can create a container using a reference to the name of the image we just downloaded and a reference to the name
    // of the network that this container should use.
    const redisContainer = new docker.Container("redis", {
        image: redisImage.name,
        networksAdvanced: [{ name: network.name }],
        restart: "on-failure",
    });

    // We do the same thing for the Redis Commander container.
    const redisCommanderImage = new docker.RemoteImage("redis-commander-image", {
        name: "rediscommander/redis-commander:latest",
        keepLocally: true,
    });

    const redisCommanderContainer = new docker.Container("redis-commander", {
        image: redisCommanderImage.name,
        restart: "on-failure",
        networksAdvanced: [{ name: network.name }],
        envs: [
            // Pulumi resources have "output" properties, which are properties that are set upon successful completion of
            // the resource operation. These "outputs" are like promises - they can't be used directly but instead must be
            // manipulated through use of the `apply` function.
            //
            // Here, we are using the name of the Redis commander to build an environment variable `REDIS_HOST` that points
            // to the network identity of the Redis container we just created.
            redisContainer.name.apply(name => `REDIS_HOST=${name}`),
        ],
        // Finally, we expose some ports. Redis Commander listens on port 8081, so we'll map that to external
        // port 3000 for easy consumption on the user machine.
        ports: [{
            internal: 8081,
            external: 3000,
        }]
    });

Here we are looking at a complete Pulumi program that does a *bunch* of
things with Docker:

1. We create a Docker network named `net`, which we'll use to connect
   two containers together
2. We pull the `redis:latest` image from Docker Hub and create a
   container using it, named `redis`, which we attach to the network we
   just created
3. We pull the `rediscommander/redis-commander:latest` image from
   Docker Hub and also create a container using it, named
   `redis-commander`, which likewise is attached to the network and
   exposes some ports on the host machine.

This is fairly nontrivial, but we've done it in code right here. Using
code we've replicated many of the features offered by tools like
`docker-compose`, but without writing a single line of YAML. Running
`pulumi up` with this code results in a working instance of Redis
Commander listening on port 3000 on your machine. Nice and simple!

## Moving to Production

Orchestrating Docker containers on your local machine while developing
is great, but when it comes time to pushing containers to production,
you can't rely on Docker alone anymore. There are a number of excellent
container orchestrators out there but there few are as successful as
Kubernetes. The way that you launch production workloads in Kubernetes
is significantly different than how you would do it using `docker run`
on your own, so it's often the case that you'd need to write another
series of YAML documents to get your application into production.

With Pulumi, we're just writing code. Since we're just writing code, we
can do exactly what we would do if we were writing application code:
**abstract!**

```typescript
// Since we're using a general-purpose programming language, we can now use that language to provide multiple
// implementations of the same abstraction. In this case, we define an abstract "Redis" component whose only property is
// that it has some network identity (host) that consumers can connect to and talk to a Redis connection.
export abstract class Redis extends pulumi.ComponentResource {
    public abstract readonly host: pulumi.Output<string>;

    public static create(name: string, args: RedisArgs, opts?: pulumi.ComponentResourceOptions): Redis {
        // Since we are using TypeScript and RedisArgs is the union of argument types for each resource. Since args.type
        // has type "amazon" | "docker" | "kubernetes", the compiler assists us in making sure that we don't
        // accidentally mix up argument types.
        switch (args.type) {
        case "amazon":
            return new AmazonRedis(name, args, opts);
        case "docker":
            return new DockerRedis(name, args, opts);
        case "kubernetes":
            return new KubernetesRedis(name, args, opts);
        }
    }

    constructor(ty: string, name: string, args: RedisArgs, opts?: pulumi.ComponentResourceOptions) {
        super(ty, name, args, opts);
    }
}

export type RedisArgs = DockerRedisArgs | KubernetesRedisArgs | AmazonRedisArgs;
```

We've departed a bit from our previous example, but we're still writing
code. In particular, what we're doing here is defining a new,
***abstract***, Redis component that takes the Redis container from the
previous example and abstracts it away a little bit. This class we've
created still represents Redis, but completely abstracts away where and
how the Redis instance is running. In this case, it can run in any one
of three different configurations:

1. Redis backed by AWS ElastiCache ("amazon")
2. Redis running as a Docker container on your machine ("docker")
3. Redis running as a Deployment on a Kubernetes cluster ("kubernetes")

Now, you can use this Redis component completely in the abstract, like
this:

```typescript
const redis = Redis.create("redis", {
    type: "docker",
    network: network,
});
```

We're requesting a "docker" container, but we could just as easily
switch this out for "amazon" and "kubernetes", and suddenly our Redis
workload is transparently deployed in different ways, all without
disrupting our development environment!

## Pulumi: Infrastructure as Software

We often say on this blog that Pulumi is "infrastructure as code", and
that sentence is definitely true, but I prefer calling it
"infrastructure as software" instead. The distinction is subtle, but in
my mind Pulumi brings to the realm of infrastructure the variety of
tools we already use for software engineering:

1. Abstraction, encapsulation, and code reuse for infrastructure and
   applications
2. [Testing]({{< relref "/blog/testing-your-infrastructure-as-code-with-pulumi" >}}),
   both unit and integration
3. IDEs and tools for detecting errors extremely early in a developer's
   inner loop, instead of at deployment time

Pulumi is open source, free to use, and works today with
[a variety of clouds]({{< relref "/docs/intro/cloud-providers" >}}) and bring a little more
software and less code into your infrastructure! If you'd like to see
more about this particular code demo,
[check out my DockerCon EU 2018 talk](https://www.youtube.com/watch?v=EbsE4p3uCu0)
where I dive into this in detail. The code for this post and the talk are in
[this repository](https://github.com/swgillespie/dockercon18).
