---
title: Deploying K3s with the Command Package
date: 2022-02-02T13:25:00Z
draft: true
meta_desc: In this article, we deploy k3s and use the Command package to retrieve our kubeconfig from the virtual-machine and create a Kubernetes provider
meta_image: meta.png
authors: ["david-flanagan"]
tags: ["kubernetes"]
---

We recently announced in our [release blog (66)](https://www.pulumi.com/blog/pulumi-release-notes-66/) a new package: [Command](https://www.pulumi.com/registry/packages/command/). In this article, I want to show you a practical application of this that will allow us to deploy [k3s](https://k3s.io) to a [DigitalOcean](digitalocean.com/products/kubernetes/) droplet. We'll then leverage the Command package to run a remote command to fetch the kubeconfig, generated on the VM, and pull it down to create a Kubernetes provider to deploy nginx.

So, let's get started by deploying our Digital Ocean droplet.

The first thing we're going to do is generate an SSH key for the machine.

```ts
const sshKey = new tls.PrivateKey("sshKey", {
  algorithm: "RSA",
  rsaBits: 4096,
});

// Optional export of the key in-case you want to store it on disk.
export const privateKey = sshKey.privateKeyPem;

// Register the SSH key with DigitalOcean
const doSshkey = new digitalocean.SshKey("sshKey", {
  publicKey: sshKey.publicKeyOpenssh,
});
```

Then we'll want to create a cloud-init configuration to pass to the droplet as user-data.

```ts
const cloudConfig = cloudinit.getConfig({
  gzip: false,
  base64Encode: false,
  parts: [
    {
      contentType: "text/x-shellscript",
      content: fs.readFileSync("../cloud-init/ensure-curl.sh", "utf8"),
    },
    {
      contentType: "text/x-shellscript",
      content: fs.readFileSync("../cloud-init/install-k3s.sh", "utf8"),
    },
  ],
});
```

There's nothing terribly fancy about these scripts, but we'll share them anyway 😃

This first one makes sure that `curl` is available on the machine.

```shell
#!/usr/bin/env sh
# ../cloud-init/ensure-curl.sh
DEBIAN_FRONTEND=noninteractive apt update && apt install --yes curl
```

This script will fetch the public IPv4 address from the DigitalOcean metadata service and pass that IP address through to k3s installer as the listen/bind address. This ensures that our Kubernetes provider in the Pulumi program can speak with the API server.

```shell
#!/usr/bin/env sh
# ../cloud-init/install-k3s.sh
PUBLIC_IP=$(curl -w "\n" http://169.254.169.254/metadata/v1/interfaces/public/0/ipv4/address)
curl -sfL https://get.k3s.io | sh -s - --bind-address ${PUBLIC_IP}
```

Now that we have some user-data, we can create a droplet and pass it through.

```ts
const k3sVm = new digitalocean.Droplet(
  "k3s",
  {
    name: "k3s",
    image: "ubuntu-20-04-x64",
    region: "lon1",
    size: "s-1vcpu-1gb",
    sshKeys: [civoSshKey.id],
    userData: cloudConfig.then((c) => c.rendered),
  },
  {
    replaceOnChanges: ["diskImage", "script"],
  }
);
```

Now, for the fun bit. Previously, there'd be no way to get the kubeconfig from the VM. Meaning that we'd need to use static manifests to deploy our workloads to k3s. This would usually be done by adding more and more scripts to the user-data and rendering them with cloud-init. This approach is not bad, but we lose the rich interface that Pulumi provides for authoring our Kubernetes resources. With the Command package, we can now execute a command on our VM and pull down that kubeconfig to be used to create our provider.

```ts
const fetchKubeconfig = new command.remote.Command("fetch-kubeconfig", {
  connection: {
    host: k3sVm.ipv4Address,
    user: "root",
    privateKey: sshKey.privateKeyPem,
  },
  create:
    // First, we use `until` to monitor for the k3s.yaml (our kubeconfig) being created.
    // Then we sleep 10, just in-case the k3s server needs a moment to become healthy. Sorry?
    "until [ -f /etc/rancher/k3s/k3s.yaml ]; do sleep 5; done; cat /etc/rancher/k3s/k3s.yaml; sleep 10;",
});
```

The Command package makes the `stdout` of the command we run available in our program, so creating the Kubernetes provider is as simple as:

```ts
const kubernetesProvider = new kubernetes.Provider("k3s", {
  kubeconfig: fetchKubeconfig.stdout,
});
```

Now, for the final step - deploying nginx.

```ts
const nginx = new kubernetes.apps.v1.Deployment(
  "nginx",
  {
    spec: {
      selector: {
        matchLabels: {
          app: "nginx",
        },
      },
      template: {
        metadata: {
          labels: {
            app: "nginx",
          },
        },
        spec: {
          containers: [
            {
              name: "nginx",
              image: "nginx",
            },
          ],
        },
      },
    },
  },
  {
    provider: kubernetesProvider,
  }
);
```

Simple.

The Command package works for local and remote commands and the possibilities are endless.

Happy hacking!
