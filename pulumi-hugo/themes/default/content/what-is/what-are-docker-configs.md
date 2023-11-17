---
title: What are Docker Configs?
meta_desc: |
     Learn more about what Docker Configs are and how to use them.

type: what-is
page_title: "What are Docker Configs"
---

Docker, a leading platform in containerization technology, has revolutionized how applications are developed, shipped, and deployed. An essential facet of this ecosystem is the effective management of configuration data. [Docker Configs](https://docs.docker.com/engine/swarm/configs/) is a feature specially crafted to handle non-sensitive configuration information within Docker environments. This guide explores the ins and outs of Docker Configs, highlighting its importance, functionality, and best practices.

### What are Docker Configs?

Docker Configs are a resource in Docker for storing non-sensitive information such as configuration files, separate from a service's image or running containers within [Docker Swarm](https://docs.docker.com/engine/swarm/) environments. This enables keeping Docker images as generic as possible without the need for bind-mounting configuration files into containers or using environment variables. Unlike [Docker Secrets](/what-is/what-are-docker-secrets), Docker Configs are not encrypted at rest and are directly mounted into the container's filesystem.

#### Key Features

- **Separation of Configuration from Code**: Docker Configs allow you to store configuration files outside of your Docker images, leading to more generic and reusable images.
- **Flexibility in Management**: Configs can be added, updated, or removed from services dynamically, without the need to rebuild or restart containers.
- **Secure Transmission**: Configs are sent to the swarm manager over a mutual TLS connection and are stored securely.
- **Easy Access within Containers**: Configs are automatically mounted into the container's filesystem, making them easily accessible to applications.
- **Support for Various Data Types**: Configs can store generic strings or binary content, providing flexibility for different types of configuration data.

### Creating Configs

Docker Configs can be created via the Docker CLI. Before creating configs in Docker, you must first make sure you have [Docker installed](https://docs.docker.com/get-docker/). Once you have installed Docker, enable and start the Docker service.

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

You can optionally add your user to the Docker group to provide non-root access.

```bash
sudo usermod -a -G docker ${USER}
```

Restart your terminal to apply the changes to the group, then check that Docker has installed correctly.

```bash
docker --version
```

{{< notes type="info" >}}

The command to start Docker depends on your operating system. The above commands show examples for how to do this on Linux. You can find the commands relevant to your own operating system in the [Docker documentation](https://docs.docker.com/engine/install/).

{{< /notes >}}

You will also need to initialize a swarm since Docker Configs are a feature of [Docker Swarm](https://docs.docker.com/engine/swarm/key-concepts/).

```
$ docker swarm init

Swarm initialized: current node (u26cvq5cro6ro76sv47fs2nr4) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-5fev6zooqj2vi3n4ffhnkzjx96oiogfziizivyordmf12iv0yo-7bqlgowmz7sy2k932cjkbukpi 172.31.30.90:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

#### Create a config via the CLI

You can create a config by piping the configuration data into the `docker config create` command.

```bash
$ echo "This is my config data" | docker config create my-config -

ix4v0pm352e7a4idpshbrbrt4
```

Verify the config is created:

```bash
$ docker config ls

ID                          NAME        CREATED          UPDATED
j41rg08gmnx1t91l0zjnefosz   my-config   33 seconds ago   33 seconds ago
```

Now you will create a [service](https://docs.docker.com/engine/swarm/how-swarm-mode-works/services/). When doing so, you can grant it access to specific configs. Configs are available to the service from the default mount point within the container, which is `/<config-name>`. This means that the config will be available at the root of the container's filesystem with the same name as the config.

```bash
$ docker service create --name myservice --config src=my-config nginx

hfmhkka4zg6ea2j3sp9tkdd7h
overall progress: 1 out of 1 tasks
1/1: running   [==================================================>]
verify: Service converged
```

You can also explicitly specify a target location for the config to be stored:

```bash
docker service create --name myservice --config src=my-config,target=/etc/my-config nginx
```

Inspect the service to ensure it is running.

```bash
$ docker service ps myservice
ID             NAME          IMAGE          NODE                                            DESIRED STATE   CURRENT STATE            ERROR     PORTS
kf8ysfgiipkb   myservice.1   nginx:latest   ip-172-31-30-90.eu-central-1.compute.internal   Running         Running 35 seconds ago  
```

#### Accessing configs inside a container

Now that you have created a service with a config, you can access the value of this config from within the container.

First, login to the container using the `docker exec` command:

```bash
docker exec -it <container_id> /bin/bash
```

Replace `<container_id>` with the ID of the container created in the previous step. You can find this value by running the following command:

```bash
$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS     NAMES
00a6ae3d1bd5   nginx:latest   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   80/tcp    myservice.1.w6i5cct5o9gwmb3ud43c5ienl
```

Taking the value of the container ID in the output, the full command will look something like this:

```bash
$ docker exec -it 00a6ae3d1bd5 /bin/bash
root@00a6ae3d1bd5:/#

```

Once inside the container, you can access the secret like a regular file:

```bash
root@00a6ae3d1bd5:/# cat /my-config
This is my config data
```

### Challenges and Considerations

Docker Configs, similar to Docker Secrets, provide a useful way to manage configuration data in Docker environments, particularly in Docker Swarm. However, they also come with their own set of challenges and considerations:

- **Limited to Docker Swarm**: Like Docker Secrets, Docker Configs are specifically designed for Docker Swarm. This means they are not natively available for standalone Docker containers or other container orchestrators like Kubernetes. This limitation can be significant for teams not using Docker Swarm.

- **Not Suitable for Sensitive Data**: Docker Configs are not encrypted at rest, unlike Docker Secrets. This makes them unsuitable for storing sensitive data such as passwords, tokens, or private keys. They should be used only for non-sensitive configuration data.

- **Size Limitation**: There is a size limit for the contents of Docker Configs (typically around 500 KB). This limitation can be a challenge when dealing with large configuration files.

- **Immutable Once Attached to Running Services**: Once a config is attached to a running service, it cannot be edited. Any changes require creating a new config and updating the service to use this new config, which might cause service disruption.

### Best Practices

When using Docker Configs, it's important to follow best practices to ensure efficient and secure management of your configuration data:

- **Use for Non-Sensitive Data Only**: Given that Docker Configs are not encrypted at rest, use them only for non-sensitive configuration data. Store any sensitive information like passwords or API keys in Docker Secrets instead.
- **Naming Conventions and Organization**: Use clear and consistent naming conventions for your configs. This approach helps in quickly identifying the purpose of each config and its associated services.
- **Avoid Large Config Files**: Since Docker Configs have a size limitation, avoid using them for very large configuration files. Instead, consider splitting large configurations into smaller, more manageable pieces.
- **Documentation**: Document your configuration management strategy, including how configs are named, structured, and updated. This documentation is invaluable for new team members and for maintaining consistency across your deployments.

By following these best practices, you can maximize the benefits of Docker Configs in managing your application's configuration data effectively and securely.

### Conclusion

Docker Configs offer a flexible and secure way to manage non-sensitive configuration data in Docker environments. By storing configuration outside of application code, Docker Configs facilitate a more modular and maintainable architecture.

Now that you're equipped with the knowledge of Docker Configs, take your cloud infrastructure management to the next level with Pulumi. Explore these key resources to deepen your understanding and enhance your implementation strategies:

- **Advanced Configuration Management**: Discover how to efficiently manage configuration data in your cloud applications. Dive into Pulumi's [Configuration Management docs](/docs/concepts/config/) for in-depth information on creating and managing configuration across stacks and projects.
- **Container Management Solutions**: Learn about deploying containers with ease using Pulumi. Whether you prefer low-management solutions like AWS Fargate and Microsoft ACI for ease of deployment or require complete control with Kubernetes-based solutions, our [Container Management](/containers/) docs provide comprehensive insights. They cover everything from managing clusters and infrastructure to deploying application containers in various environments.

Our [community on Slack](https://slack.pulumi.com/) is always open for discussions, questions, and sharing experiences. Join us there and become part of our growing community of cloud professionals!
