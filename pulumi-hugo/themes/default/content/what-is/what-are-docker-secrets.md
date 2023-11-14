---
title: What are Docker Secrets?
meta_desc: |
     Learn more about what Docker Secrets are and how to use them.

type: what-is
page_title: "What are Docker Secrets"

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - ware2go
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - skai
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro
---

Docker, a leading platform in containerization technology, has revolutionized how applications are developed, shipped, and deployed. One critical aspect of this process is managing sensitive information, commonly known as "secrets." [Docker Secrets](https://docs.docker.com/engine/swarm/secrets/) is a feature specifically designed for safely transmitting and storing confidential data within Docker environments. This guide explores the ins and outs of Docker Secrets, highlighting its importance, functionality, and best practices.

### What are Docker Secrets?

Docker Secrets is a resource for securely managing sensitive data like passwords, tokens, and SSH keys within [Docker Swarm](https://docs.docker.com/engine/swarm/) environments. It's designed to keep this information safe both in transit and at rest.

#### Key Features

- **Secure Storage**: Docker Secrets are encrypted during transit and at rest, offering a robust level of security.
- **Managed Lifecycle**: Secrets can be created, updated, and removed without restarting containers, ensuring seamless management.
- **Access Control**: Only services granted explicit access can retrieve these secrets, enhancing security through compartmentalization.

### Creating Secrets

Secrets can be created via the Docker CLI or Docker Compose files. Once created, they are stored in a secure part of the Docker Swarm. Before creating secrets in Docker, you must first make sure you have [Docker installed](https://docs.docker.com/get-docker/). Once you have installed Docker, enable and start the Docker service.

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

#### Create a secret via CLI

You can create a secret by piping the secret data into the `docker secret create` command.

```bash
$ echo "my_secret_data" | docker secret create my_secret -

ix4v0pm352e7a4idpshbrbrt4
```

Verify the secret is created

```bash
$ docker secret ls

ID                          NAME        DRIVER    CREATED          UPDATED
ix4v0pm352e7a4idpshbrbrt4   my_secret             14 seconds ago   14 seconds ago
```

Now you will create a [service](https://docs.docker.com/engine/swarm/how-swarm-mode-works/services/). When doing so, you can grant it access to specific secrets. These secrets are then available to the service in a `tmpfs` mount, which is not stored on disk and gets deleted when the container stops.

```bash
$ docker service create --name myservice --secret my_secret nginx

u7drojmomleop9fz8pi9aosmw
overall progress: 1 out of 1 tasks
1/1: running   [==================================================>]
verify: Service converged
```

Inspect the running service to ensure the secret is attached.

```bash
$ docker service ps myservice
ID             NAME          IMAGE          NODE                                            DESIRED STATE   CURRENT STATE            ERROR     PORTS
w6i5cct5o9gw   myservice.1   nginx:latest   ip-172-31-30-90.eu-central-1.compute.internal   Running         Running 52 seconds ago
```

#### Create a secret via Docker Compose

Before implementing Docker Secrets with Docker Compose, ensure [Docker Compose is installed](https://docs.docker.com/compose/install/) on your system.

Next, create a file named `my_secret_data.txt` and add your secret data to this file. Then, create a `docker-compose.yml` file for your application. Add a secrets section in your Docker Compose file and define your secret, making sure to specify the file containing the secret data.

```yaml
version: "3.9"  # or higher
services:
  my_service:
    image: "nginx:latest" # or the name of your image
    secrets:
      - my_secret
secrets:
  my_secret:
    file: ./my_secret_data.txt
```

In this example, `my_secret` is the name of your secret, and `my_secret_data.txt` contains the secret data.

Now use Docker Compose to deploy your stack. This will create the secret and attach it to your service.

```bash
docker-compose up -d
```

#### Accessing secrets inside a container

Now that you have created a service with a secret, you can access the value of this secret from within the container.

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

The secret is mounted into the service's containers under `/run/secrets/`. Once inside the container, you can access the secret like a regular file:

```bash
root@00a6ae3d1bd5:/# cat /run/secrets/my_secret
my_secret_data
```

### Challenges and Considerations

While Docker Secrets is a valuable tool for managing sensitive data in Docker Swarm, it has its limitations. One major challenge is its confinement to Docker Swarm environments, meaning it's not applicable for standalone Docker containers or other orchestrators like Kubernetes. Additionally, Docker Secrets lacks a direct mechanism for automatic secrets rotation, a crucial aspect for maintaining security over time.

### Conclusion

Docker Secrets is a vital feature for anyone using Docker Swarm, offering a secure and straightforward way to handle sensitive data. By understanding and implementing Docker Secrets correctly, teams can significantly enhance the security posture of their containerized applications.
