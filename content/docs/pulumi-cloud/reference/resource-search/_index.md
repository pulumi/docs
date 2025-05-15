---
title: Resource Search
title_tag: "Pulumi Cloud REST API: Resource Search"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for searching and querying resources managed by Pulumi across your organization.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 15
---

Resource Search provides powerful querying capabilities for resources managed by Pulumi. The Resource Search API allows you to find resources across your organization using various filters and criteria.

{{< notes >}}
The Resource Search API is currently in preview and subject to change.
{{< /notes >}}

## Resource Search Operations

The API provides endpoints for the following operations:

- Searching for resources across an organization with filtering, sorting, and pagination

## Search Resources

Search for resources belonging to the given organization.

```plain
GET /api/orgs/{org}/search/resourcesv2
```

### Parameters

| Parameter     | Type   | In    | Description                                                       |
|---------------|--------|-------|-------------------------------------------------------------------|
| `organization`| string | query | **Required.** The organization name to search resources for.      |
| `page`        | integer| query | **Optional.** Page number to retrieve results from. Default is 1.|
| `size`        | integer| query | **Optional.** Number of results to retrieve per page. Default is 50. |
| `sort`        | string | query | **Optional.** Sort by a property, such as `modified`. Default is `modified`. |
| `asc`         | boolean| query | **Optional.** Sort results in ascending order. Default is `false`. |
| `query`       | string | query | **Optional.** A search query to filter the results. |
| `properties`  | boolean| query | **Optional.** If `true`, includes the resource properties. Default is `false`. |
| `source`      | string | query | **Optional.** The source for resource search. |

### Detailed descriptions

**org**: Name of the organization to search.
The organization can belong to a team, enterprise, or an individual user.

The provided authorization token must have access to this organization.

**query**: The search query to execute. If omitted all resources are returned (subject to any pagination limits).

**sort**: Results are returned sorted by this field value.
If omitted, results are sorted according to their search relevance. If there is no query, results are sorted by their last modified time.

If specified more than once, the first parameter is the primary sort order and subsequent parameters control additional sorting criteria.

Allowed values: created, custom, delete, dependencies, id, modified, module, name, package, parentUrn, project, protected, providerUrn, stack, type, urn, managed, category

**asc**: Whether to return results in ascending or descending sort order.
Results are returned in descending order by default.

**size**: How many results to return at a time.

**page**: The page of results to return.
The `page` parameter can only be used to fetch up 10,000 resources. If a query matches more than 10,000 resources, the `cursor` parameter should be used instead.
Paginating with the `page` parameter is not transactional. The order of results can be impacted if a stack update completes while paginating.

**cursor**: A continuation token for pagination that allows fetching more than 10,000 resources.
Only available on Enterprise plans.
Paginating with the `cursor` parameter is not transactional. The order of results can be impacted if a stack update completes while paginating.

**properties**: Whether to include resource properties in results. Not supported for all subscriptions.

Attempting to set this on an unsupported subscription results in a 402 status code.

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+6" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/fizzbuzz/search/resourcesv2?page=1&size=50&sort=modified&asc=false&query=&properties=true&source=resource-search
```

### Example response

```json
{
  "total": 3,
  "resources": [
    {
      "created": "2025-02-10T19:33:09.6611691Z",
      "custom": false,
      "delete": false,
      "dependencies": [],
      "id": "i-12345abcde67890fg",
      "modified": "2025-02-10T19:33:09.6611691Z",
      "module": "aws",
      "name": "fizzbuzz-ec2-instance",
      "package": "aws",
      "parent.urn": "urn:fizzbuzz::example-stack::pulumi:pulumi:Stack::example-stack-fizzbuzz",
      "project": "example-stack",
      "protected": false,
      "provider.urn": "urn:fizzbuzz::example-stack::pulumi:providers:aws::default_4_16_7::ec2-1234abcde-5f6g-7h8i-9jklmno9876",
      "stack": "fizzbuzz",
      "type": "aws:ec2/instance:Instance",
      "urn": "urn:fizzbuzz::example-stack::aws:ec2/instance:Instance::fizzbuzz-ec2-instance",
      "properties": {
        "ami": "ami-0123456789abcdef0",
        "instanceType": "t2.micro",
        "keyName": "fizzbuzz-keypair",
        "securityGroups": ["fizzbuzz-sg"],
        "tags": {
          "Name": "fizzbuzz-ec2-instance"
        }
      },
      "metadata": {},
      "category": "compute",
      "managed": "Pulumi (discovered)"
    },
    {
      "created": "2025-02-10T19:33:09.406814916Z",
      "custom": false,
      "delete": false,
      "dependencies": [],
      "id": "db-12345xyz67890pq",
      "modified": "2025-02-10T19:33:09.406814916Z",
      "module": "aws",
      "name": "fizzbuzz-rds-instance",
      "package": "aws",
      "parent.urn": "urn:fizzbuzz::example-stack::pulumi:pulumi:Stack::example-stack-fizzbuzz",
      "project": "example-stack",
      "protected": false,
      "provider.urn": "urn:fizzbuzz::example-stack::pulumi:providers:aws::default_4_16_7::rds-xyzabc-1d2e-3f4g-5h6i7jklm8n9",
      "stack": "fizzbuzz",
      "type": "aws:rds/instance:Instance",
      "urn": "urn:fizzbuzz::example-stack::aws:rds/instance:Instance::fizzbuzz-rds-instance",
      "properties": {
        "allocatedStorage": 20,
        "engine": "mysql",
        "engineVersion": "8.0",
        "instanceClass": "db.t2.micro",
        "name": "fizzbuzz-db",
        "username": "[secret]",
        "password": "[secret]",
        "skipFinalSnapshot": true
      },
      "metadata": {},
      "category": "data",
      "managed": "Pulumi"
    },
    {
      "created": "2025-02-10T19:34:09.406814916Z",
      "custom": false,
      "delete": false,
      "dependencies": [],
      "id": "s3-12345xyz67890pq",
      "modified": "2025-02-10T19:34:09.406814916Z",
      "module": "aws",
      "name": "fizzbuzz-s3-bucket",
      "package": "aws",
      "parent.urn": "urn:fizzbuzz::example-stack::pulumi:pulumi:Stack::example-stack-fizzbuzz",
      "project": "example-stack",
      "protected": false,
      "provider.urn": "urn:fizzbuzz::example-stack::pulumi:providers:aws::default_4_16_7::s3-xyzabc-1d2e-3f4g-5h6i7jklm8n9",
      "stack": "fizzbuzz",
      "type": "aws:s3/bucket:Bucket",
      "urn": "urn:fizzbuzz::example-stack::aws:s3/bucket:Bucket::fizzbuzz-s3-bucket",
      "properties": {
        "bucket": "fizzbuzz-s3-bucket",
        "acl": "private",
        "tags": {
          "Name": "fizzbuzz-s3-bucket"
        }
      },
      "metadata": {},
      "category": "storage",
      "managed": "None"
    }
  ],
  "pagination": {
    "next": "https://api.pulumi.com/api/orgs/fizzbuzz/search/resources?page=2\u0026size=50\u0026sort=modified",
    "cursor": "https://api.pulumi.com/api/orgs/fizzbuzz/search/resources?cursor=H4sIAAAAAAAA_wTAwQ2AMAgF0Ltj9CwJX_gIsxgPpLX7j-B7cFtdoDtU9RzJqC9okhtTfLKkkZTIpbGb1svGe_wBAAD__3DHC1U3AAAA\u0026size=50\u0026sort=modified"
  }
}
```

### Response status codes

| Status | Description                                                                                     |
|--------|-------------------------------------------------------------------------------------------------|
| 200    | Successful search.                                                                              |
| 400    | Bad request. Not safe to retry.                                                                 |
| 402    | You attempted to use functionality not included in your Pulumi subscription. Not safe to retry. |
| 422    | Unprocessable query. Not safe to retry.                                                         |
| 500    | Server error. Safe to retry.                                                                    |

## Schema Definitions

This section documents the data schemas used by the Resource Search API. Understanding these schemas helps you interpret API responses and structure API requests correctly.

### ResourceSearchResult

The result of a Resource Search query.

```json
{
  "total": 10000,
  "resources": [
    {
      "created": "string",
      "custom": true,
      "delete": true,
      "dependencies": ["string"],
      "id": "string",
      "modified": "string",
      "module": "string",
      "name": "string",
      "package": "string",
      "parent.urn": "string",
      "pending": "creating",
      "project": "string",
      "properties": {},
      "protected": true,
      "provider.urn": "string",
      "stack": "string",
      "type": "string",
      "urn": "string"
    }
  ],
  "aggregations": {
    "others": 0,
    "results": [
      {
        "name": "string",
        "count": 0
      }
    ]
  },
  "pagination": {
    "previous": "string",
    "next": "string",
    "continue": "string"
  }
}
```

#### Properties

| Name         | Type                                | Description                                       |
|--------------|-------------------------------------|---------------------------------------------------|
| total        | integer(int64)\|null                | The total number of results matched by the query. |
| resources    | [[ResourceResult](#resourceresult)] | Resources matching the query.                     |
| aggregations | [Aggregations](#aggregations)       | The result of any aggregations requested.         |
| pagination   | [Pagination](#pagination)           | URIs for pagination, if appropriate.              |

### ResourceResult

An individual resource.

```json
{
  "created": "string",
  "custom": true,
  "delete": true,
  "dependencies": ["string"],
  "id": "string",
  "modified": "string",
  "module": "string",
  "name": "string",
  "package": "string",
  "parent.urn": "string",
  "pending": "creating",
  "project": "string",
  "properties": {},
  "protected": true,
  "provider.urn": "string",
  "stack": "string",
  "type": "string",
  "urn": "string"
}
```

#### Properties

| Name         | Type          | Description                                                                                                                                                                                                                                                                                                                                                                      |
|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| created      | string\|null  | The UTC time when the resource was created.<br><br>Resources created _or modified_ with CLI versions below 3.60 _do not_ have created set.                                                                                                                                                                                                                                       |
| custom       | boolean\|null | Whether the resource is a CustomResource.                                                                                                                                                                                                                                                                                                                                        |
| delete       | boolean\|null | Whether the resource is marked for deletion in the next update.<br><br> Typically indicates a resource that was not cleaned up due to an error.                                                                                                                                                                                                                                  |
| dependencies | [string]      | The URN of other resources this resource explicitly or implicitly [depends on](/docs/concepts/resources#dependson).                                                                                                                                                                                                                                                              |
| id           | string\|null  | The [physical name](/docs/concepts/resources/names/#physicalname) of the resource, as assigned by the resource's provider. May not be set if the resource is pending creation.                                                                                                                                                                                                   |
| modified     | string\|null  | The UTC time when the resource's state was last modified during an update, refresh or import. <br><br>Stacks modified with CLI versions below 3.60 record this for all resources as the time of the stack operation, regardless of whether the resource was modified. After CLI version 3.60 the resource's modified time is only updated when the resource's state is modified. |
| module       | string\|null  | The module component of the resource's type.<br><br>This is `s3` for a resource of type `aws:s3/bucketv2:BucketV2`.                                                                                                                                                                                                                                                              |
| name         | string\|null  | The logical name of the resource. <br><br>Typically the first parameter provided to the resource when it was instantiated.                                                                                                                                                                                                                                                       |
| package      | string\|null  | The package component of the resource's [type][types].<br><br>This is `aws` for a resource of type `aws:s3/bucketv2:BucketV2`                                                                                                                                                                                                                                                    |
| parent.urn   | string\|null  | The URN of the resource's parent, if it has one.                                                                                                                                                                                                                                                                                                                                 |
| pending      | string\|null  | The state of the resource if it is pending. <br><br>Typically indicates an operation that was interrupted due to an error, possibly needing manual intervention to resolve.<br><br>Allowed values: `creating`, `deleting`, `updating`, `reading`, `importing`.                                                                                                                   |
| project      | string\|null  | The project the resource belongs to.                                                                                                                                                                                                                                                                                                                                             |
| properties   | object\|null  | The resource's combined input and output values as recorded in Pulumi's state. Only available to certain Pulumi subscriptions.                                                                                                                                                                                                                                                   |
| protected    | boolean\|null | Whether the resource is [protected](/docs/concepts/options/protect] from deletion.                                                                                                                                                                                                                                                                                               |
| provider.urn | string\|null  | The URN of the resource's provider.                                                                                                                                                                                                                                                                                                                                              |
| stack        | string\|null  | The Stack the resource belongs to.                                                                                                                                                                                                                                                                                                                                               |
| type         | string\|null  | The type of the resource.                                                                                                                                                                                                                                                                                                                                                        |
| urn          | string\|null  | The URN of the resource.                                                                                                                                                                                                                                                                                                                                                         |

### Aggregations

A collection of aggregated values.

```json
{
  "others": 0,
  "results": [
    {
      "name": "string",
      "count": 0
    }
  ]
}
```

#### Properties

| Name    | Type                                      | Description                                                                                        |
|---------|-------------------------------------------|----------------------------------------------------------------------------------------------------|
| others  | integer(int64)\|null                      | The number of resources not counted in the top 5 results.                                          |
| results | [[AggregationResult](#aggregationresult)] | The top 5 values for the given aggregation, and the number of resources with each of those values. |

### AggregationResult

An aggregated value.

```json
{
  "name": "string",
  "count": 0
}
```

#### Properties

| Name  | Type                 | Description                          |
|-------|----------------------|--------------------------------------|
| name  | string\|null         | A value from the faceted dimension.  |
| count | integer(int64)\|null | How many resources share that value. |

### Pagination

URLs for fetching additional results.

If null, the request is invalid or does not permit pagination.

```json
{
  "previous": "string",
  "next": "string",
  "continue": "string"
}
```

#### Properties

| Name     | Type         | Description                                                                                                                                                                                                                                                                                                                                            |
|----------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| previous | string\|null | When non-null, this is a URI to fetch the previous page of results.                                                                                                                                                                                                                                                                                    |
| next     | string\|null | When non-null, this is a URI to fetch the next page of results.<br><br>This only allows paginating through the first 10,000 results of a query. <br><br>The `continue` parameter should be used to fetch more than 10,000 results.                                                                                                                     |
| continue | string\|null | When non-null, this is a URI to fetch the next page of results. <br><br>Unlike the `next` property, repeatedly following `continue` allows paginating through an unbounded number of results.<br><br>When paginating with `continue`, `next` and `previous` will always be `null`.<br><br>`continue` is only available to Pulumi Enterprise customers. |
