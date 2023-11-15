---
title: What are Kubernetes Secrets?
meta_desc: |
     Learn about Kubernetes Secrets and how to manage sensitive information securely in your Kubernetes clusters.

type: what-is
page_title: "What are Kubernetes Secrets"

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

Kubernetes, or K8S, is an open-source container orchestration platform designed to automate the deployment, scaling, and management of containerized applications.

## What are Kubernetes Secrets?

Kubernetes Secrets, or [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) for short, are a built-in Kubernetes solution to manage the lifecycle of secrets, which are sensitive data such as passwords, API keys, and tokens. These secrets are consumed by containerized applications directly thereby preventing exposure of sensitive data in code, Docker images, or configuration files.

## Understanding Kubernetes Secrets

One crucial aspect of securing applications is managing sensitive data. We will delve into the use of Kubernetes Secrets by following the lifecycle of database credentials. In particular, you'll learn how to perform the basic CRUD (Create, Read, Update, Delete) operations against a Secret.

## Why Use Kubernetes Secrets?

Manual secrets management is prone to introducing errors and poses high-lift operational challenges. At the same time,  the absence of a dedicated secret management solution,  means carrying a higher risk of accidental data leaks or unauthorized access to private information. One should never use ConfigMaps to hold secrets. Kubernetes Secrets come into play by providing an integrated mechanism for the secure storage and distribution of sensitive data to pods.

Kubernetes Secrets are fundamental to the cloud native stack. It provides a secure and standardized means to manage sensitive information like credentials, tokens, or API keys within our cloud apps so these don't have to be passed around in plain text.

### Key Features

Securing sensitive data in Kubernetes Secrets is essential for various reasons:

- **Managed Lifecycle:** Secrets can be created, updated, and removed without restarting containers, ensuring seamless management.
- **Easy Integration:** Applications can access secrets as environment variables or mounted files.
- **Dynamic Updates:** Secrets can be updated without redeploying your applications.
- **Role-Based Access Control (RBAC):** You can control who can access and modify secrets.
- **Enable Auditing** When required for compliance

## Kubernetes Secrets Best Practices

- **Use Namespacing:** Organize your secrets within namespaces to control access and limit exposure.
- **Encrypt Sensitive Data:** Ensure that secrets are encrypted at rest and in transit. Secret resources stored within etcd need to be encrypted at rest as this is not the default.
- **Implement Access Control:** Leverage Kubernetes RBAC to restrict access to secrets.
- **Regularly Rotate Secrets:** Periodically update your secrets to enhance security.

For more details visit the [Kubernetes Secrets security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/#secrets )

## Kubernetes Secrets CRUD examples

Let's look at a practical example of how to create, read, update, and delete a Kubernetes Secret.

### Example 1: Creating a Secret

1. Define a new secret resource called `shhhhhh` that contains a user and a password. These are saved in the `dbcreds.yaml` file.

    ```bash
    $ cat <<EOF > dbcreds.yaml
    apiVersion: v1
    kind: Secret
    metadata:
        name: shhhhhh
    type: Opaque
    data:
        username: cm9vdA==
        password: cm9vdA==
    EOF
    ```

    The keys in the `data` section are encoded in base64. Given this is a basic example, we use 'root' for the credentials. This can be confirmed by running `echo "cm9vdA==" | base64 -d` which outputs
  `root`

2. Apply the new resource definition:

    ```bash
    $ kubectl apply -f dbcreds.yaml
    ```

3. Verify the contents:

    ```bash
    $ kubectl describe secrets shhhhhh  
    ```

### Example 2: Reading a Secret

1. Run the following `kubectl` command along with the name of the secret:

    ```bash
    $ kubectl get secret shhhhhh
    # NAME      TYPE     DATA   AGE
    # shhhhhh   Opaque   2      2m
    ```

2. To read a specific value within the secret, use `jsonpath` to specify the key:

    ```bash
    $ kubectl get secret shhhhhh -o jsonpath="{.data.user}" | base64 -d
    # root
    $ kubectl get secret shhhhhh -o jsonpath="{.data.password}" | base64 -d
    # r00t
    ```

    Recall that the values are stored as base64 thus we have to decode them to read the actual value. Hence the `base64 -d`.

### Example 3: Updating a Secret

In this example we update the password of our secret so that it's a tad harder and does not match the username.

1. Determine the base64 encoding of the new password:

    ```bash
    echo "r00t123" | base64
    # cjAwdDEyMwo=
    ```

2. Open the editor to modify the secret:

    ```bash
    $ kubectl edit secrets shhhhhh
    ```

3. Replace the `data.password` with the new base64-encoded value from Step 1.

4. View the changes

    ```bash
    kubectl get secret shhhhhh -o jsonpath="{.data.password}" | base64 -d
    # r00t123
    ```

### Example 4: Deleting a Secret

1. Run the following `kubectl` command along with the name of the secret:

    ```bash
    $ kubectl delete secret shhhhhh
    # secret "shhhhhh" deleted
    ```

## A real world example with database credentials

When managing database credentials, you can use Kubernetes Secrets to securely define, store, and deploy the necessary credentials to your pods. This ensures that your application has secure access to the database, without exposing the credentials in your codebase.

Let's explore a real-world example that demonstrates the use of Kubernetes Secrets management.

In the below example, we have MongoDB in the backend provisioned via helm. It was configured by mounting a secret volume containing user credential(s). We then create a pod that mounts the same secret to test the connection to the backend.

1. Define a new secret resource

    ```bash
    $ cat <<EOF > demo-dbcreds.yaml
    apiVersion: v1
    kind: Secret
    metadata:
        name: demo-dbcreds
    type: Opaque
    stringData:
        mongodb-root-password: 'r00t'
        mongodb-passwords: ''
    EOF
    ```

2. Apply the new resource definition:

    ```bash
    $ kubectl apply -f demo-dbcreds.yaml  --namespace mongodb
    ```

3. Use helm to deploy MongoDB

  ```bash
    helm install backend \
   --set auth.username=root,auth.database=admin,architecture=standalone,persistence.enabled=false,auth.existingSecret=demo-dbcreds \
  oci://registry-1.docker.io/bitnamicharts/mongodb --namespace mongodb
    ```

4. Confirm the secrets reference in the MongoDB pod

    ```bash
    $ kubectl describe pod backend-mongodb-776ff496b7-hmlrq --namespace mongodb
    # ...
    # other output not shown
   # Environment:
   #   BITNAMI_DEBUG:                    false
   #   MONGODB_EXTRA_USERNAMES:          root
   #   MONGODB_EXTRA_DATABASES:          admin
   #   MONGODB_EXTRA_PASSWORDS:          <set to the key 'mongodb-passwords' in secret 'demo-dbcreds'>  Optional: false
   #   MONGODB_ROOT_USER:                root
   #   MONGODB_ROOT_PASSWORD:            <set to the key 'mongodb-root-password' in secret 'demo-dbcreds'>  Optional: false
    # ...
    ```

5. Create another pod to test connectivity. Note this pod will have the `demo-dbcreds` secret mounted.

    ```bash
    $ cat <<EOF > mongo-conn-test.yaml
    apiVersion: v1
    kind: Pod
    metadata:
     name: mongo-conn-test
    spec:
     containers:
     - name: mongo-conn-test
       image: mongo:latest
       command: ["/bin/sh", "-c"]
       args:
         - |
           echo "Waiting for MongoDB to be ready..."
           until mongosh --host=backend-mongodb.mongodb.svc.cluster.local -u root -p \$(cat /mnt/secrets/mongodb-root-password) --authenticationDatabase admin --eval "db.stats()" > /dev/null 2>&1; do
             sleep 5
           done
           echo "Connected to MongoDB!"
       volumeMounts:
       - name: secret-volume
         mountPath: "/mnt/secrets"
     volumes:
     - name: secret-volume
       secret:
         secretName: demo-dbcreds
    EOF
    ```

    Update your host if using a different resource name or namespace. This examples uses `backend-mongodb.mongodb.svc.cluster.local`

6. Create the pod

    ```bash
    $ kubectl apply -f mongo-conn-test.yaml   --namespace mongodb
    ```

7. Verify connectivity

    ```bash
    $ kubectl logs mongo-conn-test --namespace mongodb
    # Waiting for MongoDB to be ready...
    # Connected to MongoDB!
    ```

8. Delete the test pod

    ```bash
    $ kubectl delete pod mongo-conn-test  --namespace mongodb
    ```

### Conclusion

Kubernetes secrets are crucial to many applications and we must have a solution to the lifecycle of these. Kubernetes Secrets is the native way to manage secrets. By following best practices and using Kubernetes secrets, you can ensure the security of your applications and sensitive data.

Now that you're equipped with the knowledge of Kubernetes Secrets, take your cloud infrastructure management to the next level with Pulumi. Explore these key resources to deepen your understanding and enhance your implementation strategies:

- **Advanced Secrets Management**: Discover how to efficiently manage sensitive data and secrets in your cloud applications. Dive into Pulumi's [Secrets Management guide](/blog/managing-secrets-with-pulumi/) for in-depth information on encrypting specific values for added security and ensuring that these values never appear in plain text in your state file​.

Our [community on Slack](https://slack.pulumi.com/) is always open for discussions, questions, and sharing experiences. Join us there and become part of our growing community of cloud professionals!
