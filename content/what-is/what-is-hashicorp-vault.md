---
title: What is HashiCorp Vault?
meta_desc: |
     HashiCorp Vault is a tool for securing, storing, and tightly controlling access to tokens, passwords, certificates, and encryption keys.

type: what-is
page_title: "What is HashiCorp Vault?"
---

Modern applications run across many clouds, regions, and runtime environments, and each of them needs access to sensitive data — API keys, database credentials, TLS certificates, and encryption keys. Storing those secrets safely, rotating them regularly, and controlling who can read them is a problem every cloud team has to solve. [HashiCorp Vault](https://www.hashicorp.com/products/vault) is one of the most widely adopted tools for that job.

## What is HashiCorp Vault?

HashiCorp Vault is an open-source tool for securely storing, generating, and tightly controlling access to secrets such as tokens, passwords, certificates, and encryption keys. Vault encrypts secrets at rest, brokers access through identity-based policies, and produces a detailed audit log of every access — giving teams a single, centralized way to manage sensitive data across applications, infrastructure, and clouds.

### Key features

- **Secure secret storage**: Vault stores arbitrary key/value secrets and encrypts them before writing to persistent storage. It supports multiple storage backends, including disk, Consul, and cloud providers.
- **Dynamic secrets**: Vault can generate short-lived, on-demand credentials for systems like databases and cloud platforms. Each request gets a unique secret that can be automatically revoked, drastically reducing the blast radius of a leak.
- **Encryption as a service**: Applications can ask Vault to encrypt and decrypt data without ever storing the data itself in Vault — useful for offloading the complexity of key management.
- **Leasing and renewal**: Secrets can be issued with a lease. When the lease expires, the secret is revoked automatically; clients can renew leases to extend validity.
- **Revocation**: Vault can revoke individual secrets or entire trees of secrets — for example, every credential a compromised application has accessed.
- **Identity and access management**: Vault supports many auth methods (tokens, username/password, cloud IAM, OIDC, Kubernetes service accounts, and more) and uses policies to control which secrets each identity can access.
- **Audit logging**: Vault writes detailed logs of every access and configuration change, which is essential for security audits and compliance.

## Creating secrets in HashiCorp Vault

HashiCorp Vault configurations can be managed via the Vault CLI. Before you begin, ensure that you have [Vault installed](https://www.vaultproject.io/downloads). After installation, initialize and start the Vault server.

Use the `vault kv put` command to create a new secret within a specified mount path:

```bash
# Create a new secret
vault kv put secret/hello myvalue=s3cr3t
```

Replace `myvalue=s3cr3t` with the key-value pair you wish to store as a secret.

{{< notes type="info" >}}

The commands in this article include `<key>=<value>` parameters that pass secrets to Vault directly through the CLI. Be aware that executing these commands can leave sensitive data in your shell's unencrypted history. Consult the [Static Secrets: Key/Value Secrets Engine tutorial](https://www.vaultproject.io/docs/secrets/kv/kv-v2) for best practices in production scenarios.

{{< /notes >}}

## Reading a secret from HashiCorp Vault

Once you've stored a secret, you can read it back to verify it was stored correctly or to use it.

Use the `vault kv get` command to retrieve your secret:

```bash
vault kv get secret/hello
```

The output will display the secret stored at the specified path:

```plaintext
====== Data ======
Key         Value
---         -----
myvalue     s3cr3t
```

## HashiCorp Vault use cases

Vault fits a wide range of cloud architectures. The most common patterns are:

- **Public, hybrid, and multi-cloud environments**: Vault provides a single place to manage secrets across AWS, Azure, Google Cloud, and on-premises systems, avoiding vendor lock-in and keeping the secrets workflow consistent across providers.
- **Containerized and Kubernetes workloads**: Vault dynamically issues secrets and injects them into containers and pods, so applications never need long-lived credentials baked into images or config maps.
- **Microservices**: Each service can be issued its own short-lived credentials, limiting lateral movement if a single service is compromised.
- **CI/CD pipelines**: Build servers and deployment automation can fetch dynamic credentials from Vault at runtime instead of storing static tokens in pipeline configuration.
- **Encryption for applications**: Vault's transit engine lets applications encrypt and decrypt data without ever managing the underlying keys themselves.

## Best practices

- **Prefer dynamic secrets over static ones**: Whenever a backend supports it (databases, cloud IAM, SSH, PKI), use Vault's dynamic secret engines so credentials are short-lived and automatically revoked.
- **Apply least-privilege policies**: Scope each Vault policy to the smallest set of paths and capabilities the consumer needs, and bind policies to identities rather than to long-lived tokens.
- **Rotate the root and recovery keys**: Rotate Vault's encryption key (`rotate`) and re-key the master/recovery keys (`rekey`) on a regular schedule.
- **Enable and monitor audit devices**: Always run at least one audit device, and ship the logs to a SIEM so secret access is visible and alertable.
- **Manage Vault itself as code**: Define mounts, auth methods, and policies declaratively so the Vault configuration is reviewable, reproducible, and recoverable.

## Challenges and considerations

Vault is powerful, but operating it well takes investment. Common considerations include:

- **Operational complexity**: Running Vault in production means managing seal/unseal flows, high availability, storage backends, and disaster recovery. Teams often choose [HCP Vault](https://www.hashicorp.com/products/vault/pricing) to offload this.
- **Initial setup overhead**: Designing auth methods, policies, and namespaces up front takes time, especially in larger organizations with many teams and environments.
- **Secret sprawl across tools**: Many organizations end up with secrets in Vault, cloud-native secret managers (AWS Secrets Manager, Azure Key Vault, Google Secret Manager), and CI/CD systems, making consistent access patterns harder to enforce.
- **Application integration**: Wiring applications to fetch secrets at runtime (sidecars, agents, SDKs) adds moving parts that have to be deployed, monitored, and upgraded.

## Conclusion

HashiCorp Vault gives cloud teams a centralized, auditable way to store secrets, issue short-lived credentials, and encrypt sensitive data. Those capabilities get more valuable as infrastructure spreads across more clouds and environments.

Pairing Vault with Pulumi covers both halves of the problem. Pulumi lets you define your Vault configuration (mounts, policies, auth methods, and secrets) as code in the language you already use, and [Pulumi ESC](/docs/pulumi-cloud/esc/) lets your applications consume secrets from Vault, alongside other providers, through a single environment abstraction.

- **Manage Vault as code with Pulumi**: Define Vault mounts, policies, and KV secrets using the [Pulumi Vault provider](/registry/packages/vault/). Below is a minimal example that creates a KV v2 mount and writes a secret:

{{< chooser language "typescript,python,go,csharp" / >}}

{{% choosable language typescript %}}

```typescript
import * as vault from "@pulumi/vault";

const kv = new vault.Mount("kv", {
    path: "secret",
    type: "kv",
    options: { version: "2" },
});

const example = new vault.kv.SecretV2("example", {
    mount: kv.path,
    name: "hello",
    dataJson: JSON.stringify({ myvalue: "s3cr3t" }),
});

export const secretPath = example.path;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import json
import pulumi
import pulumi_vault as vault

kv = vault.Mount("kv",
    path="secret",
    type="kv",
    options={"version": "2"},
)

example = vault.kv.SecretV2("example",
    mount=kv.path,
    name="hello",
    data_json=json.dumps({"myvalue": "s3cr3t"}),
)

pulumi.export("secret_path", example.path)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-vault/sdk/v7/go/vault"
	"github.com/pulumi/pulumi-vault/sdk/v7/go/vault/kv"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		kvMount, err := vault.NewMount(ctx, "kv", &vault.MountArgs{
			Path: pulumi.String("secret"),
			Type: pulumi.String("kv"),
			Options: pulumi.StringMap{
				"version": pulumi.String("2"),
			},
		})
		if err != nil {
			return err
		}

		data, err := json.Marshal(map[string]string{"myvalue": "s3cr3t"})
		if err != nil {
			return err
		}

		example, err := kv.NewSecretV2(ctx, "example", &kv.SecretV2Args{
			Mount:    kvMount.Path,
			Name:     pulumi.String("hello"),
			DataJson: pulumi.String(string(data)),
		})
		if err != nil {
			return err
		}

		ctx.Export("secretPath", example.Path)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Text.Json;
using Pulumi;
using Pulumi.Vault;
using Pulumi.Vault.Kv;

return await Deployment.RunAsync(() =>
{
    var kv = new Mount("kv", new MountArgs
    {
        Path = "secret",
        Type = "kv",
        Options = { { "version", "2" } },
    });

    var example = new SecretV2("example", new SecretV2Args
    {
        Mount = kv.Path,
        Name = "hello",
        DataJson = JsonSerializer.Serialize(new { myvalue = "s3cr3t" }),
    });

    return new Dictionary<string, object?>
    {
        ["secretPath"] = example.Path,
    };
});
```

{{% /choosable %}}

- **Centralize secrets and configuration with Pulumi ESC**: [Pulumi ESC](/docs/pulumi-cloud/esc/) lets teams aggregate secrets and configuration from many sources, organize them into hierarchical environments, and consume them from any application or infrastructure tool. Get started by using ESC's [vault-secrets](/docs/pulumi-cloud/esc/providers/vault-secrets/) provider to dynamically import secrets from HashiCorp Vault into your environment.
- **Advanced configuration management**: Dive into Pulumi's [Configuration Management docs](/docs/concepts/config/) for in-depth information on creating and managing configuration across stacks and projects.

Our [community on Slack](https://slack.pulumi.com/) is always open for discussions, questions, and sharing experiences. Join us there and become part of our growing community of cloud professionals.
