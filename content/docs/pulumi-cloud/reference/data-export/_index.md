---
title: Data Export
title_tag: "Pulumi Cloud REST API: Data Export"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for exporting resource data for further analysis or integration.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 3
---

Data Export allows you to download resource data from Pulumi Cloud for offline analysis or integration with other systems. The Data Export API provides endpoints for exporting resource data in various formats.

{{< notes >}}
The Data Export API is only available to organizations using the Enterprise and Business Critical editions.

The Data Export API is currently in preview and subject to change.
{{< /notes >}}

## Data Export Operations

The API provides endpoints for the following operations:

- Exporting resources in CSV format to download and analyze

## Export Resources

Export resources matching a given query in CSV format.

```plain
GET /api/orgs/{org}/search/resources/export
```

### Parameters

| Name       | In    | Type          | Required | Description                                                         |
|------------|-------|---------------|----------|---------------------------------------------------------------------|
| org        | path  | string        | true     | Name of the organization to search.                                 |
| query      | query | string        | false    | The search query to execute. If omitted all resources are returned. |
| sort       | query | array[string] | false    | Results are returned sorted by this field value.                    |
| asc        | query | boolean       | false    | Whether to return results in ascending or descending sort order.    |
| properties | query | boolean       | false    | Whether to return properties with results.                          |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+6" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --output resources.csv \
  https://api.pulumi.com/api/orgs/{org}/search/resources/export?query=type:aws:s3/bucket:Bucket
```

### Example response

The response is a CSV file with resource information:

```plain
created,custom,delete,id,modified,module,name,package,parent_urn,pending,project,protected,provider_urn,stack,type,urn
2025-02-10T19:34:09.406814916Z,false,false,s3-12345xyz67890pq,2025-02-10T19:34:09.406814916Z,aws,fizzbuzz-s3-bucket,aws,urn:fizzbuzz::example-stack::pulumi:pulumi:Stack::example-stack-fizzbuzz,false,example-stack,false,urn:fizzbuzz::example-stack::pulumi:providers:aws::default_4_16_7::s3-xyzabc-1d2e-3f4g-5h6i7jklm8n9,fizzbuzz,aws:s3/bucket:Bucket,urn:fizzbuzz::example-stack::aws:s3/bucket:Bucket::fizzbuzz-s3-bucket
```

### Response status codes

| Status | Description                                                                                     |
|--------|-------------------------------------------------------------------------------------------------|
| 200    | Successful export.                                                                              |
| 400    | Bad request. Not safe to retry.                                                                 |
| 402    | You attempted to use functionality not included in your Pulumi subscription. Not safe to retry. |
| 422    | Unprocessable query. Not safe to retry.                                                         |
| 500    | Server error. Safe to retry.                                                                    |
