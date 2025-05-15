---
title: Policy Results
title_tag: "Pulumi Cloud REST API: Policy Results"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for retrieving and analyzing policy evaluation results.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 13
---

Policy Results is a part of Pulumi Insights that provides information about policy violations detected during stack updates and resource scanning. The Policy Results API allows you to retrieve information about policy violations across your organization, enabling governance and compliance monitoring through the Pulumi Insights platform.

## Policy Results Operations

The API provides endpoints for the following operations:

- Listing policy violations across an organization

## List Policy Violations

Retrieve all policy violations for an organization.

```plain
GET /api/orgs/{organization}/policyresults/violationsv2
```

### Parameters

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | organization name                                                                                            |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/policyresults/violationsv2
```

### Default response

```plain
Status: 200 OK
```

```plain
{
    "policyViolations": [
        {
            "projectName": "pulumi-k8s-test",
            "stackName": "test",
            "stackVersion": 11,
            "policyPack": "kubernetes",
            "policyPackTag": "0.0.2",
            "policyName": "minimum-replica-count",
            "resourceURN": "urn:pulumi:test::pulumi-k8s-test::kubernetes:apps/v1:Deployment::nginx",
            "resourceType": "kubernetes:apps/v1:Deployment",
            "resourceName": "nginx",
            "message": "Checks that Kubernetes Deployments and ReplicaSets have at least three replicas.\nKubernetes Deployments should have at least three replicas.\n",
            "observedAt": "2025-01-16T23:44:13Z",
            "level": "advisory"
        },
        {
            "projectName": "test",
            "accountName": "us-west-1",
            "resourceVersion": 1,
            "policyPack": "aws-typescript",
            "policyPackTag": "0.0.1",
            "policyName": "s3-no-public-read",
            "resourceURN": "urn:insights:test/us-west-1::aws::aws:s3/bucket:Bucket::my-super-bucket-1234567890",
            "resourceType": "aws:s3/bucket:Bucket",
            "resourceName": "my-super-bucket-1234567890",
            "message": "Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.\nTest violation",
            "observedAt": "2025-01-16T23:08:28Z",
            "level": "advisory"
        }
    ],
    "continuationToken": ""
}
```
