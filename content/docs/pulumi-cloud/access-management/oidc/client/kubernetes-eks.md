---
title_tag: Configure OpenID Connect for Elastic Kubernetes Service (EKS) | OIDC
meta_desc: This page describes how to configure Pulumi to accept Elastic Kubernetes Service (EKS) OIDC tokens
title: Elastic Kubernetes Service (EKS) | OIDC
h1: Configuring OpenID Connect for Elastic Kubernetes Service (EKS)
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: AWS EKS
    parent: pulumi-cloud-access-management-oidc-client
    weight: 2
    identifier: pulumi-cloud-access-management-oidc-client-kubernetes-eks
  pulumicloud:
    parent: openid-connect-client
    weight: 1
aliases:
- /docs/pulumi-cloud/oidc/client/kubernetes-eks/
---

This document outlines the steps required to configure Pulumi to accept Elastic Kubernetes Service (EKS) id_tokens to be exchanged for a personal access token. With this configuration, Kubernetes pods authenticate to Pulumi Cloud using OIDC tokens issued by EKS.

## Prerequisites

* You must be an admin of your Pulumi organization.
* You must have a EKS cluster.
* You must [associate the EKS cluster with an OIDC provider](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html).

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the [Assign IAM roles to Kubernetes service accounts](https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html).
{{< /notes >}}

## Create and register an IAM role with a service account

1. Create an IAM Role for Service Accounts

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

    Create the IAM role using this trust policy and attach necessary permissions for your workload.

1. Associate the IAM Role with a Kubernetes Service Account.

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

## Register the OIDC issuer

1. Navigate to **OIDC Issuers** under your Organization's **Settings** and click on **Register a new issuer**.
1. Lookup your clusters OIDC Issuer url:

    ```bash
    aws eks describe-cluster --name <cluster-name> --query "cluster.identity.oidc.issuer" --output text
    ```

    This command returns the issuer URL, such as `https://oidc.eks.us-west-2.amazonaws.com/id/EXAMPLEDOCID`.

1. Name the issuer, set a max expiration (in seconds), and add the issuer url:
![Register EKS](../register-eks.png)
1. Submit the form

## Configure the Authorization Policies

1. Click on the issuer name.
1. Change the policy decision to `Allow`.
1. Change the token type to `Personal`. See this [page for other token types.](../#exchanging-oidc-tokens)
1. The user login should default to your login, but change if using a different login.
1. Add a new rule and configure it to verify namespace and the service name:

   ![kubernetes policy example](../eks-policy.png)

1. Click on **Save policies**

{{< notes type="info" >}}
   There are other attributes you can use to fine tune your policy, such as:

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

For example to reference the pod name, you would use `"kubernetes.io".pod.name` as the key path and the pod name (e.g. `busyboxplus` in this case) as the value.
{{< /notes >}}

## Sample

```typescript
// Pulumi program to run a bash script in a Kubernetes pod,
// mount a service account token with an appropriate audience,
// exchange the token for an ordinary Pulumi access token,
// then run `pulumi whoami`.

import * as kubernetes from "@pulumi/kubernetes";

const tokenParams = {
    "audience": "urn:pulumi:org:ORG_NAME",
    "token_type": "urn:pulumi:token-type:access_token:personal",
    "expiration": 2 * 60 * 60,
    "scope": "user:USER_LOGIN"
}

const script = new kubernetes.core.v1.ConfigMap("script", {
    data: {
        "entrypoint.sh": `#!/bin/bash
apt -qq install -y jq

# This is the location of the EKS id token
EKS_ID_TOKEN=$(cat /var/run/secrets/eks.amazonaws.com/serviceaccount/token)

echo "OIDC Token:"
echo $EKS_ID_TOKEN
export PULUMI_ACCESS_TOKEN=$(curl -sS -X POST  \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'audience=${tokenParams.audience}' \
    -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
    -d 'subject_token_type=urn:ietf:params:oauth:token-type:id_token' \
    -d 'requested_token_type=${tokenParams.token_type}' \
    -d 'expiration=${tokenParams.expiration}' \
    -d 'scope=${tokenParams.scope}' \
    -d "subject_token=$EKS_ID_TOKEN" \
    https://api.pulumi.com/api/oauth/token | jq -r '.access_token')
echo "Access Token:"
echo $PULUMI_ACCESS_TOKEN
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
                serviceAccountName: "pulumi-service-account"
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
