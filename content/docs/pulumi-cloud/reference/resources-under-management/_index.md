---
title: Resources Under Management
title_tag: "Pulumi Cloud REST API: Resources Under Management (RUM)"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for retrieving information about the volume and history of resources managed through Pulumi.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 16
---

Resources Under Management (RUM) provides information about the cloud resources managed by Pulumi across your organization. The RUM API allows you to track resource counts over time with various time aggregations.

## RUM Operations

The API provides endpoints for the following operations:

- Getting resource count summaries with different time granularities

## Get Resource Count Summary

Get a summary of resource counts over time with different aggregation options.

```plain
GET /orgs/{organization}/resources/summary
```

### Parameters

| Parameter       | Type           | In    | Description                                                                                |
|-----------------|----------------|-------|--------------------------------------------------------------------------------------------|
| `granularity`   | string         | query | How usage should be aggregated. Accepted values are: `hourly`, `daily`, `weekly`, `monthly`, or `yearly`.                                                                          |
| `lookbackDays`  | string         | query | **One of `lookbackDays` or `lookbackStart` is required, not both.** Returns usage for a period of `lookbackDays` x 24 hours, starting from now.    |
| `lookbackStart` | unix timestamp | query | **One of `lookbackDays` or `lookbackStart` is required, not both.**  Returns usage starting from the given timestamp.                          |

> Note: `lookbackDays` returns usage in 24-hour increments starting from the current time. This will truncate usage for the first day. To get complete usage for the first day, use `lookbackStart` to specify the start time.

### Example (hourly)

Note: If specifying `granularity=hourly`, the maximum `lookbackDays` you can set is `2`.

```bash
curl \
  -h "accept: application/vnd.pulumi+8" \
  -h "authorization: token $PULUMI_ACCESS_TOKEN" \
  --compressed \
  https://api.pulumi.com/api/orgs/{organization}/resources/summary?granularity=hourly&lookbackDays=1
```

### Default response (hourly)

```plain
Status: 200 OK
```

```json
{
  "summary": [
    {
      "year": 2022,
      "month": 8,
      "day": 31,
      "hour": 20,
      "resources": 27378
    },
    "..."
  ]
}
```

### Example (daily)

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --compressed \
  https://api.pulumi.com/api/orgs/{organization}/resources/summary?granularity=daily&lookbackDays=2
```

### Default response (daily)

```plain
Status: 200 OK
```

```json
{
  "summary": [
    {
      "year": 2022,
      "month": 8,
      "day": 30,
      "resources": 27379
    },
    "..."
  ]
}
```

### Example (weekly)

```bash
curl \
  -h "accept: application/vnd.pulumi+8" \
  -h "authorization: token $PULUMI_ACCESS_TOKEN" \
  --compressed \
  https://api.pulumi.com/api/orgs/{organization}/resources/summary?granularity=weekly&lookbackDays=28
```

### Default response (weekly)

```plain
Status: 200 OK
```

```json
{
  "summary": [
    {
      "year": 2022,
      "weekNumber": 31,
      "resources": 26432
    },
    "..."
  ]
}
```

### Example (monthly)

```bash
curl \
  -h "accept: application/vnd.pulumi+8" \
  -h "authorization: token $PULUMI_ACCESS_TOKEN" \
  --compressed \
  https://api.pulumi.com/api/orgs/{organization}/resources/summary?granularity=monthly&lookbackDays=90
```

### Default response (monthly)

```plain
Status: 200 OK
```

```json
{
  "summary": [
    {
      "year": 2022,
      "month": 6,
      "resources": 24520
    },
    "..."
  ]
}
```

### Example (yearly)

```bash
curl \
  -h "accept: application/vnd.pulumi+8" \
  -h "authorization: token $PULUMI_ACCESS_TOKEN" \
  --compressed \
  https://api.pulumi.com/api/orgs/{organization}/resources/summary?granularity=yearly&lookbackDays=730
```

### Default response (yearly)

```plain
Status: 200 OK
```

```json
{
  "summary": [
    {
      "year": 2022,
      "resources": 24380
    },
    "..."
  ]
}
```
