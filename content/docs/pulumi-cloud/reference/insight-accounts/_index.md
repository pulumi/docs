---
title: Insights Accounts
title_tag: "Pulumi Cloud REST API: Insights Accounts"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing Pulumi Insights accounts and integrations with cloud providers.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 6
---

Pulumi Insights enables visibility into cloud resources and compliance monitoring. The Insights Accounts API allows you to create, list, and manage accounts for various cloud providers.

## Insights Operations

The API provides endpoints for the following operations:

- Creating new Insights accounts
- Listing available Insights accounts
- Getting details for specific accounts

## Create Account

Creates a new account for use with Pulumi Insights.

```
POST /api/preview/insights/pulumi/accounts/{accountName}
```

### Parameters

| Parameter        | Type   | In    | Description                                                                                           |
|------------------|--------|-------|-------------------------------------------------------------------------------------------------------|
| `provider`       | string | body  | The cloud provider for the account (e.g., `aws`, `azure`, `oci`)                               |
| `environment`    | string | body  | The environment reference for the account, such as `insights/pulumi-staging@2`                         |
| `cron`           | string | body  | The cron expression defining when the account scan is scheduled (e.g., `0 0 * * *`)                    |
| `providerConfig` | object | body  | The configuration specific to the provider, such as regions for `aws` (e.g., `["us-east-1", "us-east-2"]`) |

### Example

```bash
curl \
  -X POST \
  -H "Accept: application/vnd.pulumi+6" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  -d '{
    "provider": "aws",
    "environment": "insights/pulumi-staging@2",
    "cron": "0 0 * * *",
    "providerConfig": {
      "regions": ["us-east-1", "us-east-2", "us-west-2"]
    }
  }' \
  https://api.pulumi.com/api/preview/insights/pulumi/accounts/FizzBuzz%20AWS%20Staging
```

### Default response

```
Status: 200 OK
```

```
{
  "message": "Account FizzBuzz AWS Staging created successfully."
}
```

## List Accounts

Lists Insight Accounts available to the authenticated user.

```
GET /api/preview/insights/pulumi/accounts
```

### Parameters

| Parameter             | Type   | In    | Description                                                                                          |
|-----------------------|--------|-------|------------------------------------------------------------------------------------------------------|
| `count`               | integer| query | **Optional.** the number of results to return (default is 100)                                        |
| `continuationToken`   | string | query | **Optional.** the continuation token to use for retrieving the next set of results if results were truncated |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/preview/insights/pulumi/accounts?count=1000
```

### Default response

```
Status: 200 OK
```

```
{
  "accounts": [
    {
      "name": "FizzBuzz Aws Prod",
      "provider": "aws",
      "providerEnvRef": "fizzbuzz/insights-pulumi-prod@4",
      "scheduledScanEnabled": false,
      "scanStatus": {
        "id": "",
        "orgId": "",
        "userId": "",
        "status": "",
        "startedAt": "2025-01-01T00:00:00Z",
        "finishedAt": null,
        "lastUpdatedAt": "2025-01-01T00:00:00Z",
        "jobTimeout": "2025-01-01T00:00:00Z"
      }
    },
    {
      "name": "FizzBuzz Aws Staging",
      "provider": "aws",
      "providerEnvRef": "fizzbuzz/insights-pulumi-staging@2",
      "scheduledScanEnabled": true,
      "scanStatus": {
        "id": "",
        "orgId": "",
        "userId": "",
        "status": "succeeded",
        "startedAt": "2025-02-03T12:01:00.000Z",
        "finishedAt": "2025-02-03T12:05:00.000Z",
        "lastUpdatedAt": "2025-02-03T12:05:00.000Z",
        "resourceCount": 250
      }
    }
  ]
}
```

## Get Account

Gets Insight Account details for the specific account.

```
GET /api/preview/insights/pulumi/accounts/{accountName}
```

### Parameters

| Parameter    | Type   | In    | Description                                            |
|--------------|--------|-------|--------------------------------------------------------|
| `accountName`| string | path  | The name of the account to retrieve details for.       |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+6" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/preview/insights/pulumi/accounts/FizzBuzz%20AWS%20Staging
```

### Default response

```
Status: 200 OK
```

```
{
  "name": "FizzBuzz AWS Staging",
  "provider": "aws",
  "providerEnvRef": "insights/pulumi-staging@2",
  "scheduledScanEnabled": true,
  "providerConfig": {
    "regions": [
      "us-east-1",
      "us-east-2",
      "us-west-2"
    ]
  },
  "scanStatus": {
    "id": "",
    "orgId": "",
    "userId": "",
    "status": "",
    "startedAt": "0001-01-01T00:00:00Z",
    "finishedAt": "0001-01-01T00:00:00Z",
    "lastUpdatedAt": "0001-01-01T00:00:00Z",
    "jobTimeout": "0001-01-01T00:00:00Z"
  }
}
```
