---
title: "Kubernetes WordPress Helm Chart"
meta_desc: Learn how to deploy a Wordpress Helm Chart to a Kubernets cluster.
aliases: ["/docs/reference/tutorials/kubernetes/tutorial-wordpress-chart/"]
layout: how-to-guide
---

In this tutorial, we'll use the Helm API of `@pulumi/kubernetes` to deploy `v9.6.0` of the Wordpress
Helm Chart to a Kubernetes cluster. Pulumi will expand the Helm Chart and submit the expanded YAML to the cluster.

![wordpress](/images/docs/quickstart/kubernetes/wp-deploy.gif "Wordpress Helm Chart deployment")

## Running the App

Start by downloading the [example code](https://github.com/pulumi/examples/tree/master/kubernetes-ts-helm-wordpress).

If you haven't already, follow the steps in [Pulumi Installation and
Setup]({{< relref "/docs/get-started/install" >}}) and [Configuring Pulumi
Kubernetes]({{< relref "/registry/packages/kubernetes/installation-configuration" >}}) to get set up with
Pulumi and Kubernetes.

Now, install dependencies:

```sh
$ npm install
```

Create a new stack:

```sh
$ pulumi stack init
Enter a stack name: wordpress-dev
```

Preview the deployment of the application.

Preview the deployment of the application and then perform the deployment:

```sh
pulumi up
Previewing update (wordpress-dev)

View Live: https://app.pulumi.com/example/wordpress/wordpress-dev/previews/cc683bd2-1e19-49c9-8a88-792c44e3b020

     Type                                         Name                         Plan
 +   pulumi:pulumi:Stack                          wordpress-dev-wordpress      create
 +   └─ kubernetes:helm.sh:Chart                  wpdev                        create
 +      ├─ kubernetes:core:Secret                 default/wpdev-mariadb        create
 +      ├─ kubernetes:core:Secret                 wpdev-wordpress              create
 +      ├─ kubernetes:core:Service                default/wpdev-mariadb        create
 +      ├─ kubernetes:core:Service                wpdev-wordpress              create
 +      ├─ kubernetes:core:ConfigMap              default/wpdev-mariadb        create
 +      ├─ kubernetes:core:PersistentVolumeClaim  wpdev-wordpress              create
 +      ├─ kubernetes:apps:StatefulSet            default/wpdev-mariadb        create
 +      └─ kubernetes:apps:Deployment             wpdev-wordpress              create

Resources:
    + 10 to create

Do you want to perform this update? yes
Updating (ts-helm-wordpress)

View Live: https://app.pulumi.com/example/wordpress/ts-helm-wordpress/updates/7

     Type                                         Name                         Status
 +   pulumi:pulumi:Stack                          wordpress-dev-wordpress      create
 +   └─ kubernetes:helm.sh:Chart                  wpdev                        created
 +      ├─ kubernetes:core:Secret                 default/wpdev-mariadb        created
 +      ├─ kubernetes:core:Secret                 wpdev-wordpress              created
 +      ├─ kubernetes:core:PersistentVolumeClaim  wpdev-wordpress              created
 +      ├─ kubernetes:core:Service                wpdev-wordpress              created
 +      ├─ kubernetes:core:ConfigMap              default/wpdev-mariadb        created
 +      ├─ kubernetes:core:Service                default/wpdev-mariadb        created
 +      ├─ kubernetes:apps:StatefulSet            default/wpdev-mariadb        created
 +      └─ kubernetes:apps:Deployment             wpdev-wordpress              created

Outputs:
    frontendIp: "35.193.210.254"

Resources:
    + 10 created

Duration: 53s
```

We can see here in the `---outputs:---` section that Wordpress was allocated a public IP, in this
case `35.193.210.254`. It is exported with a stack output variable, `frontendIp`. We can use `curl`
and `grep` to retrieve the `<title>` of the site the proxy points at.

```sh
$ curl -sL $(pulumi stack output frontendIp):80 | grep "<title>"
<title>User&#039;s Blog! &#8211; Just another WordPress site</title>
```

You can also navigate to the site in a web browser.

When you're done, you can remove these resources with `pulumi destroy`:

```sh
pulumi destroy --skip-preview
Destroying (wordpress-dev)

View Live: https://app.pulumi.com/example/wordpress/wordpress-dev/updates/8

     Type                                         Name                         Status
 -   pulumi:pulumi:Stack                          wordpress-dev-wordpress      deleted
 -   └─ kubernetes:helm.sh:Chart                  wpdev                        deleted
 -      ├─ kubernetes:core:Secret                 wpdev-wordpress              deleted
 -      ├─ kubernetes:core:Secret                 default/wpdev-mariadb        deleted
 -      ├─ kubernetes:core:ConfigMap              default/wpdev-mariadb        deleted
 -      ├─ kubernetes:core:Service                default/wpdev-mariadb        deleted
 -      ├─ kubernetes:core:PersistentVolumeClaim  wpdev-wordpress              deleted
 -      ├─ kubernetes:core:Service                wpdev-wordpress              deleted
 -      ├─ kubernetes:apps:StatefulSet            default/wpdev-mariadb        deleted
 -      └─ kubernetes:apps:Deployment             wpdev-wordpress              deleted

Outputs:
  - frontendIp: "35.193.210.254"

Resources:
    - 10 deleted

Duration: 7s
```
