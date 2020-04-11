---
title: "Architecture as Code: Virtual Machines"
date: 2020-03-31
meta_desc: "Provisioning virtual machines and redeploying applications on existing instances using Pulumi"
meta_image: vm.png
authors:
    - sophia-parafina
tags:
    - virtual machines
    - provisioning
---

In a [previous article]({{< relref "/blog/architecture-as-code-intro" >}}), we presented an overview of four infrastructure patterns for deploying modern applications. The article reviewed virtual machines, serverless, Kubernetes, and microservices. In this post, we'll examine virtual machines in-depth.

<!--more-->

## The Minimum Virtual Machine

Whether you choose to build a virtual machine using VMWare or from a cloud service provider such as AWS, Azure, or Google Cloud Platform, they require three resources. First, the instance itself must be configured to meet application requirements. Second, network access for maintaining the instance and for applications. Finally, storage for application data.

Let's start with the EC2 provisioner example, which is available on [Github](https://github.com/pulumi/examples/tree/master/aws-ts-ec2-provisioners). Make an empty directory and clone the example in the directory using `pulumi new`.

```bash
$ mkdir virtual_machine && cd virtual_machine
$ pulumi new https://github.com/pulumi/examples/tree/master/aws-ts-ec2-provisioners
```

Follow the instructions in the [README](https://github.com/pulumi/examples/tree/master/aws-ts-ec2-provisioners) to create an OpenSSH keypair and set them as secrets, we'll need them to log into and provision the VM. Let's take a look at the [code](https://github.com/pulumi/examples/blob/master/aws-ts-ec2-provisioners/index.ts). The first part configures the VM with the OpenSSH keys that we stored as secrets in the Pulumi configuration file (Pulumi.dev.yaml).

The following part defines a security group that allows us to ssh via port 22 and receive requests on port 80.

```ts
// Create a new security group that permits SSH and web access.
const secgrp = new aws.ec2.SecurityGroup("secgrp", {
    description: "Foo",
    ingress: [
        { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});
```

Note that the security group only allows ingress, if we want to update the VM or add software via a package manager such as yum, we need to define egress.

```ts
// Create a new security group that permits SSH and http/https access.
const secgrp = new aws.ec2.SecurityGroup("secgrp", {
   description: "Foo",
   ingress: [
       { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
       { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
       { protocol: "tcp", fromPort: 443, toPort: 443, cidrBlocks: ["0.0.0.0/0"] },
   ],
   egress: [
       { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
       { protocol: "tcp", fromPort: 443, toPort: 443, cidrBlocks: ["0.0.0.0/0"] },
   ],
});
```

The code block below selects the AWS AMI and creates an EC2 instance with the OpenSSH keypair and security group with ingress and egress rules configured.

```ts
// Get the AMI.
const amiId = aws.getAmi({
   owners: ["amazon"],
   mostRecent: true,
   filters: [{
       name: "name",
       values: ["amzn2-ami-hvm-2.0.????????-x86_64-gp2"],
   }],
}, { async: true }).then(ami => ami.id);

// Create an EC2 server that we'll then provision stuff onto.
const size = "t2.micro";
if (!keyName) {
   const key = new aws.ec2.KeyPair("key", { publicKey });
   keyName = key.keyName;
}

const server = new aws.ec2.Instance("server", {
   instanceType: size,
   ami: amiId,
   keyName: keyName,
   vpcSecurityGroupIds: [ secgrp.id ],

});
```

Next, let's add storage to our virtual machine using AWS Elastic Block Storage and attach it to our EC2 instance. Add the following code after the virtual machine is created. The code creates a 10 GB volume and attaches it to our virtual machine via the `instanceId` property.

```ts
// Add EBS storage.
const ebsvolume = new aws.ebs.Volume("vm", {
   availabilityZone: "us-west-2a",
   size: 10,
   tags: {
       Name: "vm_volume",
   },
});

// Attach storage to the virtual machine.
const ebsAtt = new aws.ec2.VolumeAttachment("ebsAtt", {
   deviceName: "/dev/sdh",
   instanceId: server.id,
   volumeId: ebsvolume.id,
});
```

Now we have a virtual machine that can receive HTTP and HTTPS requests and allows outbound network traffic so that we can update and install software via the package manager.

## Provisioning with Dynamic Providers

Provisioning a VM when it's created by running user-supplied scripts is relatively straightforward. For example, AWS EC2 instances have a userData parameter that allows you to specify an inline script that runs when the instance starts. But what if you need to copy and execute scripts on the virtual machine without replacing the instance?

This where you can use Pulumi’s [dynamic provider]({{< relref "/docs/intro/concepts/programming-model#dynamicproviders" >}}) to provision existing instances. Dynamic providers enable creating custom resource types, such as provisioners, within the source code of your Pulumi program. They let you execute arbitrary code during the deployment process. Dynamic provisioners run during resource provisioning, and enable adding custom logic to a deployment workflow during the create, read, update, or delete steps of a Pulumi program.

Let's look at the code which creates a dynamic provisioner. In the code below, if Pulumi doesn't find the resource, it creates the resource. However, if you run `pulumi up` again and the resource is already running, Pulumi uses the diff method to replace the resource.

```ts
// Provisioner lets a custom action run the first time a resource has been created. It takes as input
// a dependent property. Anytime its value changes, the resource is replaced and will re-run its logic.
export class Provisioner<T, U> extends pulumi.dynamic.Resource {
   dep: pulumi.Output<T>;
   result: pulumi.Output<U>;
   constructor(name: string, props: ProvisionerProperties<T, U>, opts?: pulumi.CustomResourceOptions) {
       const provider: pulumi.dynamic.ResourceProvider = {
           diff: async (id: pulumi.ID, olds: State<T, U>, news: State<T, U>) => {
               const replace = JSON.stringify(olds.dep) !== JSON.stringify(news.dep);
               return {
                   changes: replace,
                   replaces: replace ? ["dep"] : undefined,
                   deleteBeforeReplace: true,
               };
           },
           create: async (inputs: State<T, U>) => {
               const result = await props.onCreate(inputs.dep);
               if (result !== undefined) {
                   inputs.result = result;
               }
               return { id: uuid.v4(), outs: inputs };
           },
       };
       super(provider, name, { dep: props.dep, result: null }, opts);
   }
}

export interface ProvisionerProperties<T, U> {
   dep: pulumi.Input<T>;
   onCreate: (dep: pulumi.Unwrap<T>) => Promise<pulumi.Unwrap<U>>;
}

interface State<T, U> {
   dep: pulumi.Unwrap<T>;
   result: pulumi.Unwrap<U>;
}
```

This example creates two interfaces using the provisioner. The first is a `copyFile` function that lets us copy the configuration files to the virtual machine. The second interface is the `runCommand` function, which runs commands on the virtual machine. Underlying both functions is the 'connToSsh2' function that opens the ssh connection to copy files via scp and to execute commands. When you run `pulumi up` the example writes a small configuration file on the virtual machine then runs 'cat' to print the configuration file to stdout.

## Installing PostgreSQL

Let's modify the example to install and configure PostgreSQL. First, create a directory to hold the installation script and configuration files.

```bash
$ mkdir ./postgres
```

Add the following files to the postgres directory. The postgres.conf file is a bare-bones configuration file the allows PostgreSQL to allow connections from any IP address on port 5432. The pg_hba.conf file permits authentication for connections with a password.

```bash
# postgres.conf

# -----------------------------
# PostgreSQL configuration file
# -----------------------------
#

#------------------------------------------------------------------------------
# CONNECTIONS AND AUTHENTICATION
#------------------------------------------------------------------------------

# - Connection Settings -

listen_addresses = '*'      # what IP address(es) to listen on;
                   # comma-separated list of addresses;
                   # defaults to 'localhost'; use '*' for all
                   # (change requires restart)
port = 5432             # (change requires restart)
```

```bash
# pg_hba.conf

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     trust
# IPv4 local connections:
host    all             all             127.0.0.1/32            trust
# IPv6 local connections:
host    all             all             ::1/128                 trust

```

Finally, the postgres_install.sh is a bash script that installs Postgres with the yum package manager. It initializes the database, replaces the configuration scripts, and starts the database.

```bash
#!/bin/bash

# This script installs and configures PostgreSQL
sudo yum -y install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs
sudo postgresql-setup initdb

# Copy configuration files
sudo cp -f ./pg_hba.conf /var/lib/pgsql/data/pg_hba.conf
sudo cp -f ./postgresql.conf /var/lib/pgsql/data/postgresql.conf

# Start postgres
sudo service postgresql start
```

To provision the EC2 instance we'll use the provisioner interface to copy the `./postgres` directory to the instance. Next, we'll make postgres_install.sh executable then run the script to install postgres and start it up.

```ts
// Copy a config file to our server.
const cpConf = new provisioners.CopyFile("postgres_conf", {
   conn,
   src: "./postgres/",
   dest: "./",
}, { dependsOn: server });

// Execute a basic command on our server.
const chmodInstall = new provisioners.RemoteExec("chmod-install", {
   conn,
   command: "chmod 755 postgres_install.sh ",
}, { dependsOn: cpConf });

// Execute a basic command on our server.
const installPgsql = new provisioners.RemoteExec("pg_install", {
   conn,
   command: "./postgres_install.sh ",
}, { dependsOn: chmodInstall });

export const publicIp = server.publicIp;
export const publicHostName = server.publicDns;
```

Note that the `dependsOn` parameter determines the sequence of deployment steps. This ensures that each part is available to the provisioner at that step. To deploy PostgreSQL on your virtual machine, run `pulumi up`. You can check the install by logging into the virtual machine and use psql to log into the database and list the tables.

```bash
$ ssh -i rsa ec2-user@$(pulumi stack output publicHostName)

# In the virtual machine
$ sudo su - postgres
-bash-4.2$ psql -U postgres
psql (9.2.24)
Type "help" for help.

postgres=# \dS
 pg_catalog | pg_aggregate                    | table | postgres
 pg_catalog | pg_am                           | table | postgres
 pg_catalog | pg_amop                         | table | postgres
 pg_catalog | pg_amproc                       | table | postgres
 pg_catalog | pg_attrdef                      | table | postgres
 pg_catalog | pg_attribute                    | table | postgres
 pg_catalog | pg_auth_members                 | table | postgres
 pg_catalog | pg_authid                       | table | postgres
...

postgres=# \q
-bash-4.2$ logout
```

## Conclusion

We can deploy and configure virtual machines programmatically using scripts and a CLI. However, updating existing instances can be onerous because it would require logging into each instance to update them. With Pulumi, we can use a dynamic provider to create a provisioner that can provision and configure an existing virtual machine. In this post, we walked through how to create a virtual machine with storage, starting from an [example on Github](https://github.com/pulumi/examples/tree/master/aws-ts-ec2-provisioners). We then installed PostgreSQL using a provisioner that copied configuration files, and an installation script then ran the script, all without creating a new virtual machine.

We have more virtual machine examples for other cloud providers. Check out:

- [Azure VM Scale Sets](https://github.com/pulumi/examples/tree/master/azure-py-vm-scaleset)
- [Pulumi DigitalOcean Droplets](https://github.com/pulumi/examples/tree/master/digitalocean-ts-loadbalanced-droplets)
- [GCP Nginx Server Using Compute Engine](https://github.com/pulumi/examples/tree/master/gcp-py-instance-nginx)
- [VSphere](https://github.com/pulumi/pulumi-vsphere/tree/master/examples/)

In our next installment, we'll go into detail about deploying applications on serverless infrastructure.
