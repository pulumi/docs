---
title_tag: Configure OpenID Connect for Google Kubernetes Engine | OIDC
meta_desc: This page describes how to configure Pulumi Cloud to accept Google Kubernetes Engine OIDC tokens.
title: Google Kubernetes Engine
h1: Configuring OpenID Connect for Google Kubernetes Engine
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Google GKE
    parent: administration-access-identity-oidc-issuers
    weight: 2
    identifier: pulumi-cloud-access-management-oidc-issuers-kubernetes-gke
aliases:
- /docs/administration/access-identity/oidc-client/kubernetes-gke/
- /docs/pulumi-cloud/oidc/client/kubernetes-gke/
- /docs/pulumi-cloud/access-management/oidc-client/kubernetes-gke/
---

This document outlines the steps required to configure Pulumi Cloud to accept Google Kubernetes Engine id_tokens and exchange them for organization access tokens. With this configuration, Kubernetes pods authenticate to Pulumi Cloud using OIDC tokens issued by GKE.

See ["Bound Tokens"](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-bound-service-account-tokens) for more background.

## Common use cases

This integration is most often used to authenticate workloads that run Pulumi operations from inside a GKE cluster, without storing long-lived Pulumi access tokens. Two common scenarios:

- **[Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/)** — Run Pulumi stacks as Kubernetes custom resources. The operator's workspace pods authenticate to Pulumi Cloud using the cluster's OIDC tokens instead of a static `PULUMI_ACCESS_TOKEN`.
- **[Customer-managed deployment runners](/docs/deployments/deployments/runners/)** — Run Pulumi Deployments inside your own GKE cluster. The workflow runner fetches a Pulumi Pool token dynamically using its OIDC identity.

{{< notes type="info" >}}
This guide walks through the Pulumi Cloud UI. You can also configure OIDC Issuers via the [REST API](/docs/reference/cloud-rest-api/oidc-issuers/) or the [`OidcIssuer`](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/oidcissuer/) resource in the Pulumi Service provider.
{{< /notes >}}

{{< notes type="info" >}}
This guide demonstrates using `organization` tokens. Depending on your [Pulumi edition](/docs/administration/access-identity/oidc-issuers/#token-types-by-edition), you can also use `personal` or `team` tokens by adjusting the token type in the authorization policies and the `pulumi login` parameters.
{{< /notes >}}

## Prerequisites

- You must be an admin of your Pulumi organization.
- You must have a GKE cluster.

{{< notes type="warning" >}}
This guide provides step-by-step instructions based on the official provider documentation, which is subject to change. For the most current information, refer to the [official Bound Service Account Tokens documentation](https://kubernetes.io/docs/concepts/storage/projected-volumes/#serviceaccounttoken).
{{< /notes >}}

## Register the OIDC Issuer

1. Navigate to **Settings → Access Management → OIDC Issuers** and select **Register issuer**.
1. Name the issuer and set the issuer URL to `https://container.googleapis.com/v1/projects/PROJECT_NAME/locations/LOCATION/clusters/CLUSTER_NAME/`.
1. Submit the form.

## Configure the authorization policies

1. Select the issuer name.
1. Set **Decision** to **Allow**.
1. Set **Token type** to **Organization**.
1. Add a new rule and configure it to verify the namespace and the service name.
1. Select **Save policies**.

## Sample

```typescript
// Pulumi program to run a bash script in a Kubernetes pod,
// mount a service account token with an appropriate audience,
// exchange the token for an ordinary Pulumi access token,
// then run `pulumi whoami`.

import * as kubernetes from "@pulumi/kubernetes";

const loginParams = {
    "org_name": "MY_ORG_NAME",
}

const script = new kubernetes.core.v1.ConfigMap("script", {
    data: {
        "entrypoint.sh": `#!/bin/bash
OIDC_GKE_TOKEN=$(</var/run/secrets/pulumi/token)
echo "OIDC Token:"
echo $OIDC_GKE_TOKEN
pulumi login --oidc-token $OIDC_GKE_TOKEN --oidc-org ${loginParams.org_name}
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
                containers: [{
                    name: "runner",
                    image: "pulumi/pulumi:latest",
                    command: ["/bin/entrypoint.sh"],
                    volumeMounts: [
                        {
                            name: "pulumi-serviceaccounttoken",
                            mountPath: "/var/run/secrets/pulumi",
                        },
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
                        name: "pulumi-serviceaccounttoken",
                        projected: {
                            sources: [
                                {
                                    serviceAccountToken: {
                                        audience: "urn:pulumi:org:MY_ORG_NAME",
                                        expirationSeconds: 3600,
                                        path: "token",
                                    },
                                },
                            ],
                        },
                    },
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
