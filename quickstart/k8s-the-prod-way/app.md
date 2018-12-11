---
title: Provisioning a Kubernetes Application
---

This lab assumes you have successfully completed [lab 1](./identity.html), and [lab
2](./infrastructure.html) the results of which are to have (1) successfully bootstrapped the
identity platform for CI/CD and teams, and (2) successfully created the Kubernetes cluster on which
we will deploy.

In this tutorial, we will use this identity to:

* Use the identity provisioned in lab 1 and the Kubernetes cluster provisioned in lab 2 to provision
  a Kubernetes app, Wordpress.

Inside the [Kubernetes the Prod Way repository][ktpw], the `services` directory contains the
Wordpress application and a collection of utility scripts for interacting with it.

## Prerequisites: Logging into cloud provider with CLI

In the first lab, we need to set up credentials using the CLI, so that Pulumi can authenticate
against the cloud provider of your choice. Make sure you're still logged in before continuing.

## Provisioning

Begin by `cd`'ing into the `services/wordpress` directory. From there, install the Pulumi toolchain:

```sh
yarn install
```

Like the second lab, the infrastructure stack comes with a script that will allow you to
authenticate using the CI/CD service account we defined in lab 1. This time, we will use the
Kubernetes application developer service account instead of the infrastructure admin account. As in
lab 2, we will later we will use this in CI/CD -- for now we will use it to provision the Kubernetes
application.

Assuming you have successfully finished lab 1, you'll need to specify the name of the identity stack
you've created. This was the argument you passed to `pulumi stack init`.

```sh
./scripts/login-to-ci-service-account.sh <identity-stack-name>
```

As it did in lab 2, this script obtains the client secret for that service account from the identity stack, and uses `gcloud` to authenticate with it.

```sh
pulumi stack output k8sAppDevCiClientSecret -s "$1" > k8s-app-dev-ci-client-secret.json
gcloud auth activate-service-account --key-file k8s-app-dev-ci-client-secret.json
rm k8s-app-dev-ci-client-secret.json
```

Similar to what we did in lab 2, we need to specify the name of the infrastructure stack (_not_ the
identity stack) so that this stack can configure itself to use the same project, zone, _etc_., and
so that it can retrieve the kubeconfig file.

```sh
pulumi stack init
pulumi config set infrastructureStackName <infrastructure-stack-name>
pulumi up
```

On success, this should look something like the following.

<img src="/images/k8s-the-prod-way/app.png">

As we can see, we've deployed a `Deployment` containing the WordPress application, along with a
`StatefulSet` for mariadb, `Secret`s for the passwords, and some `Pod`s that do end-to-end tests.

Looking inside the application file, we see:

```typescript
```

## Stack Outputs: Frontend IP

Much like labs 1 and 2, this stack produces output values that can be referenced in other stacks. If
we run `pulumi stack output`, we see one export value:

* `frontendIp`, public IP address allocated to Wordpress.

If you paste this IP address into a browser, it should take you to the Wordpress landing page.

## Next Steps

In the next lab, we will see how to use the identities defined in lab 1 to set up CI for all of
these stacks.

