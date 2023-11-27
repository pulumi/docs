---
title: What is Hashicorp Vault?
meta_desc: |
     HashiCorp Vault is a tool for securing, storing, and tightly controlling access to tokens, passwords, certificates, and encryption keys.

type: what-is
page_title: "What is Hashicorp Vault?"
---
### What is HashiCorp Vault?

HashiCorp Vault is a tool for secure secrets management, essential for storing and safeguarding sensitive data like API keys and passwords. It's one of many options in the ecosystem of secrets and configuration management tools supported by [Pulumi ESC](https://www.pulumi.com/product/esc/). As the complexity of modern cloud infrastructure has grown, so has the need for robust and scalable secrets management solutions. Vault's integration with Pulumi ESC addresses this need by providing a secure, centralized platform for managing sensitive information across multiple cloud environments. By leveraging Vault's capabilities within Pulumi ESC and [Pulumi Cloud](https://www.pulumi.com/product/pulumi-cloud/) infrastructure as code solutions, developers can ensure that their cloud infrastructure is secure and compliant with best practices, even as the underlying systems, complexity and requirements evolve.

In this article, we'll cover the key features of [HashiCorp Vault](https://www.hashicorp.com/products/vault), why secret management is important and share the use cases of how Vault integrates into various cloud architectures, enhancing the security and management of sensitive data in complex cloud environments.

### Key features of HashiCorp Vault?

- **Secure secret storage**: Vault has the capability to store a wide range of key/value secrets. Before these secrets are written to persistent storage, Vault encrypts them, ensuring that direct access to the raw storage does not compromise the secrets. Vault supports various storage backends, including disk storage, Consul, among others, for versatile secret storage solutions.
- **Dynamic secrets**: Vault can generate secrets on-demand for specific systems (like databases or cloud platforms). These secrets are generated dynamically for each request and can be automatically revoked, reducing the risk associated with static secrets.
- **Data encryption**: Vault provides encryption as a service, allowing users to encrypt and decrypt data without storing it in Vault. This is useful for applications that need to encrypt data but don’t want to handle the intricacies of key management.
- **Leasing and renewal**: Secrets in Vault can have a lease associated with them. When the lease expires, the secret is automatically revoked. Clients can also renew leases to extend their validity.
- **Revocation**: Vault can revoke not just individual secrets but entire trees of secrets. For instance, if a particular user or application is compromised, all secrets accessed by that entity can be revoked, enhancing security.
- **Identity and access management**: Vault supports various authentication methods (like tokens, username/password, cloud IAM, etc.) and uses policies to control what secrets an authenticated user or application can access.
- **Audit log**: Vault maintains detailed logs of all accesses and changes, which is crucial for security audits and compliance.

### Creating secrets in Hashicorp Vault

HashiCorp Vault configurations can be managed via the Vault CLI. Before you begin configuring Vault, ensure that you have [Vault installed](https://www.vaultproject.io/downloads). After installation, initialize and start the Vault server.

Use the `vault kv put` command to create a new secret within a specified mouth path.

```bash
# Create a new secret
vault kv put secret/hello myvalue=s3cr3t
```

Replace `myvalue=s3cr3t` with the key-value pair you wish to store as a secret.

{{< notes type="info" >}}

The commands provided in this article include `<key>=<value>` parameters to pass secrets to Vault directly through the CLI. Be aware that executing these commands can leave sensitive data in your shell's unencrypted history. Consult the [Static Secrets: Key/Value Secrets Engine tutorial](https://www.vaultproject.io/docs/secrets/kv/kv-v2) for best practices in production scenarios.

{{< /notes >}}

### Reading a secret from HashiCorp Vault

Once you've stored a secret, you can read it back to ensure it's stored correctly or to use it.

Use the `vault kv get` command to retrieve your secret:

```shell
vault kv get secret/hello
```

The output will display the secret stored at the specified path:

```plaintext
====== Data ======
Key         Value
---         -----
myvalue     s3cr3t
```

### HashiCorp Vault use cases

HashiCorp Vault is a tool that can be integrated into various cloud architecture platforms and architectures, catering to different needs and scenarios. The most common cloud architectures for use with Vault are:

- **Public cloud**: Vault is commonly used in public cloud environments like AWS, Azure, and Google Cloud Platform. It can manage secrets and sensitive data for cloud services and applications, leveraging cloud-specific features like IAM roles for authentication and auto-scaling.
- **Hybrid cloud**: In hybrid cloud setups, where some resources are managed on-premises and others in the cloud, Vault can serve as a centralized secrets manager. It can bridge on-premises and cloud environments, ensuring consistent secrets management across both.
- **Multi-cloud**: Organizations using multiple cloud providers often adopt Vault to manage secrets uniformly across these environments. This approach avoids vendor lock-in and ensures that the secrets management strategy remains consistent, regardless of the underlying cloud provider.
- **Containerized environments**: In architectures using container orchestration tools like Kubernetes, Vault is used to manage secrets for containers. It can dynamically generate secrets and inject them into containers, enhancing security in microservices architectures.
- **Serverless architectures**: For serverless functions (like AWS Lambda, Azure Functions), Vault can manage API keys and database credentials, providing them securely to serverless functions when needed.
- **CI/CD pipelines**: Vault is often integrated into CI/CD pipelines to provide dynamic secrets for deployment automation tools, build servers, and testing environments, ensuring these processes are secure and auditable.
- **Microservices architecture**: In microservices environments, Vault can provide each service with unique credentials, reducing the risk of lateral movement in case of a compromise.
- **Edge computing**: In edge computing scenarios, Vault can manage secrets used by edge devices and local data processing applications, ensuring security in distributed environments.

### Conclusion

Vault's role in each of these architectures is to provide the foundation of secure storage, strict access control, and auditing for secrets and sensitive data. When combined with Pulumi ESC, the capabilities extend even further, ensuring strong security and efficient management across your entire cloud infrastructure and target execution environments.

Pulumi ESC used in combination with Hashicorp Vault enables teams to aggregate secrets and configuration from many sources, manage hierarchical collections of configuration and secrets (“environments”), and consume those configuration and secrets from a variety of different infrastructure and application services. Pulumi ESC works hand-in-hand with Pulumi IaC to simplify configuration management, but also works independently from Pulumi IaC, as a solution for managing environments, secrets and configuration for any application or infrastructure project

- **Advanced configuration management**: Discover how to efficiently manage configuration data in your cloud applications. Dive into Pulumi's [Configuration Management docs](/docs/concepts/config/) for in-depth information on creating and managing configuration across stacks and projects.

Our [community on Slack](https://slack.pulumi.com/) is always open for discussions, questions, and sharing experiences. Join us there and become part of our growing community of cloud professionals!
