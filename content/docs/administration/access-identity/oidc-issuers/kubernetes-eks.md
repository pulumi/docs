---
title_tag: Configure OpenID Connect for Elastic Kubernetes Service (EKS) | OIDC
meta_desc: This page describes how to configure Pulumi Cloud to accept Elastic Kubernetes Service (EKS) OIDC tokens.
title: Elastic Kubernetes Service (EKS) | OIDC
h1: Configuring OpenID Connect for Elastic Kubernetes Service (EKS)
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: AWS EKS
    parent: administration-access-identity-oidc-issuers
    weight: 2
    identifier: pulumi-cloud-access-management-oidc-issuers-kubernetes-eks
  pulumicloud:
    parent: openid-connect-client
    weight: 1
aliases:
  - /docs/administration/access-identity/oidc-client/kubernetes-eks/
  - /docs/pulumi-cloud/access-management/oidc-client/kubernetes-eks/
  - /docs/pulumi-cloud/access-management/oidc/client/kubernetes-eks/
  - /docs/pulumi-cloud/oidc/client/kubernetes-eks/
---

This document outlines the steps required to configure Pulumi Cloud to accept Elastic Kubernetes Service (EKS) id_tokens and exchange them for a personal access token. With this configuration, Kubernetes pods authenticate to Pulumi Cloud using OIDC tokens issued by EKS.

## Common use cases

This integration is most often used to authenticate workloads that run Pulumi operations from inside an EKS cluster, without storing long-lived Pulumi access tokens. Two common scenarios:

- **[Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/)** — Run Pulumi stacks as Kubernetes custom resources. The operator's workspace pods authenticate to Pulumi Cloud using the cluster's OIDC tokens instead of a static `PULUMI_ACCESS_TOKEN`.
- **[Customer-managed deployment runners](/docs/deployments/deployments/runs/customer-managed-agents/)** — Run Pulumi Deployments inside your own EKS cluster. The workflow runner fetches a Pulumi Pool token dynamically using its OIDC identity.

{{< notes type="info" >}}
This guide walks through the Pulumi Cloud UI. You can also configure OIDC Issuers via the [REST API](/docs/reference/cloud-rest-api/oidc-issuers/) or the [`OidcIssuer`](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/oidcissuer/) resource in the Pulumi Service provider.
{{< /notes >}}

{{< notes type="info" >}}
This guide demonstrates using `personal` tokens. Depending on your [Pulumi edition](/docs/administration/access-identity/oidc-issuers/#token-types-by-edition), you can also use `organization` or `team` tokens by adjusting the token type in the authorization policies and the `pulumi login` parameters.
{{< /notes >}}

## Prerequisites

- You must be an admin of your Pulumi organization.
- You must have an EKS cluster.
- You must [associate the EKS cluster with an OIDC provider](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html).

{{< notes type="warning" >}}
This guide provides step-by-step instructions based on the official provider documentation, which is subject to change. For the most current information, refer to [Assign IAM roles to Kubernetes service accounts](https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html).
{{< /notes >}}

## Create and register an IAM role with a service account

1. Create an IAM Role for Service Accounts.

    Define a trust relationship between the IAM role and the OIDC provider for your EKS cluster. Here's an example trust policy:

    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Federated": "arn:aws:iam::<AWS_ACCOUNT_ID>:oidc-provider/<OIDC_PROVIDER_URL>"
          },
          "Action": "sts:AssumeRoleWithWebIdentity",
          "Condition": {
            "StringEquals": {
              "<OIDC_PROVIDER_URL>:sub": "system:serviceaccount:<namespace>:<service-account-name>"
            }
          }
        }
      ]
    }
    ```

    Replace `<AWS_ACCOUNT_ID>`, `<OIDC_PROVIDER_URL>`, `<namespace>`, and `<service-account-name>` with your values.

    Create the IAM role using this trust policy and attach the necessary permissions for your workload.

1. Associate the IAM role with a Kubernetes service account.

    Create a Kubernetes service account annotated with the IAM role ARN:

    ```yaml
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: pulumi-service-account
      namespace: default
      annotations:
        eks.amazonaws.com/role-arn: "arn:aws:iam::<AWS_ACCOUNT_ID>:role/<IAM_ROLE_NAME>"
    ```

    Replace `<AWS_ACCOUNT_ID>` and `<IAM_ROLE_NAME>` with the appropriate values.

1. Apply the service account to your Kubernetes cluster:

    ```bash
    kubectl apply -f pulumi-service-account.yaml
    ```

## Register the OIDC Issuer

1. Navigate to **Settings → Access Management → OIDC Issuers** and select **Register issuer**.
1. Look up your cluster's OIDC issuer URL:

    ```bash
    aws eks describe-cluster --name <cluster-name> --query "cluster.identity.oidc.issuer" --output text
    ```

    This command returns the issuer URL, such as `https://oidc.eks.us-west-2.amazonaws.com/id/EXAMPLEDOCID`.

1. Name the issuer, set a max expiration (in seconds), and enter the issuer URL.
1. Submit the form.

## Configure the authorization policies

1. Select the issuer name.
1. Set **Decision** to **Allow**.
1. Set **Token type** to **Personal**. See the [token types section](../#token-types-by-edition) for other options.
1. The user login should default to your login. Change it if you want to use a different login.
1. Add a new rule and configure it to verify the namespace and the service account name.
1. Select **Save policies**.

{{< notes type="info" >}}
There are other attributes you can use to fine-tune your policy, such as:

```json
   "kubernetes.io": {
    "namespace": "default",
    "node": {
      "name": "ip-10-10-4-26.us-west-2.compute.internal",
      "uid": "ffc5761d-939e-4256-8f82-a847d532a0fa"
    },
    "pod": {
      "name": "busyboxplus",
      "uid": "3227b947-e0c8-4bd2-95b9-a0d8f69b3110"
    },
    "serviceaccount": {
      "name": "pulumi-service-account",
      "uid": "bece172b-0180-48d5-b762-e3c4501de4e2"
    }
  }
```

For example, to reference the pod name, use `"kubernetes.io".pod.name` as the key path and the pod name (for example, `busyboxplus`) as the value.
{{< /notes >}}

## Sample

```typescript
// Pulumi program to run a bash script in a Kubernetes pod,
// mount a service account token with an appropriate audience,
// exchange the token for an ordinary Pulumi access token,
// then run `pulumi whoami`.

import * as kubernetes from "@pulumi/kubernetes";

const loginParams = {
    "org_name": "MY_ORG_NAME",
    "user_login": "MY_USER_LOGIN"
}

const script = new kubernetes.core.v1.ConfigMap("script", {
    data: {
        "entrypoint.sh": `#!/bin/bash
# This is the location of the EKS id token
EKS_ID_TOKEN=$(cat /var/run/secrets/eks.amazonaws.com/serviceaccount/token)

echo "OIDC Token:"
echo $EKS_ID_TOKEN
pulumi login --oidc-token $EKS_ID_TOKEN --oidc-org ${loginParams.org_name} --oidc-user ${loginParams.user_login}
pulumi whoami
`
    }
});

const job = new kubernetes.batch.v1.Job("runner", {
    metadata: {
    },
    spec: {
        template: {
            spec: {
                serviceAccountName: "pulumi-service-account",
                containers: [{
                    name: "runner",
                    image: "pulumi/pulumi:latest",
                    command: ["/bin/entrypoint.sh"],
                    volumeMounts: [
                        {
                            name: "script",
                            mountPath: "/bin/entrypoint.sh",
                            readOnly: true,
                            subPath: "entrypoint.sh",
                        },
                    ],
                }],
                restartPolicy: "Never",
                volumes: [
                    {
                        name: "script",
                        configMap: {
                            defaultMode: 0o700,
                            name: script.metadata.name,
                        },
                    },
                ],
            },
        },
        backoffLimit: 0,
    },
});

export const jobName = job.metadata.name;
```
