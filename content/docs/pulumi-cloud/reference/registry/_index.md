---
title: Registry
title_tag: "Pulumi Cloud REST API: Registry"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for interacting with the Pulumi Registry to access and publish packages and templates.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 14
---

The Pulumi Registry hosts reusable packages and templates for infrastructure deployments. The Registry API allows you to list, retrieve, publish, and manage packages and templates in the Pulumi Registry.

## Registry Identifiers

Resources in the Registry are identified by a three-part identifier: `{source}/{publisher}/{name}`.

- **Source**: Indicates the package's origin. For example:
  - `pulumi`: Packages published directly to the public Pulumi registry
  - `opentofu`: OpenTofu packages bridged to Pulumi
  - `private`: Organization-specific private registry packages
- **Publisher**: The organization that owns the package
  - For private packages: Matches the organization's canonical name
  - For public packages: Managed by Registry Administrators
- **Name**: The unique identifier for the package within its source and publisher

## Registry Operations

The API provides endpoints for the following operations:

- Listing registry packages
- Retrieving package version metadata
- Publishing new package versions
- Deleting package versions
- Retrieving template information

## List Registry Packages

List all registry packages visible to the user.

```plain
GET /api/preview/registry/packages
```

### Parameters

| Parameter           | Type    | In    | Description                                                                                                  |
|---------------------|---------|-------|--------------------------------------------------------------------------------------------------------------|
| `name`              | string  | query | **Optional.** Filter results to packages with this specific name                                             |
| `orgLogin`          | string  | query | **Optional.** Filter results to packages owned by this organization                                          |
| `limit`             | integer | query | **Optional.** Number of results to retrieve per page. Default is 100                                         |
| `continuationToken` | string  | query | **Optional.** The continuation token to use for retrieving the next set of results if results were truncated |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/preview/registry/packages
```

### Default response

```plain
Status: 200 OK
```

```json
{
  "packages": [
    {
      "name": "aws",
      "publisher": "pulumi",
      "source": "pulumi",
      "version": "6.80.0",
      "title": "AWS",
      "description": "A Pulumi package for creating and managing Amazon Web Services (AWS) cloud resources.",
      "repoUrl": "https://github.com/pulumi/pulumi-aws",
      "category": "cloud",
      "isFeatured": false,
      "packageTypes": [
        "bridged"
      ],
      "packageStatus": "ga",
      "readmeURL": "https://artifacts.pulumi.com/providers/f5de3f9d-cde1-4be0-a6c4-12fb7aa20cb8/docs/index.md",
      "schemaURL": "https://artifacts.pulumi.com/providers/f5de3f9d-cde1-4be0-a6c4-12fb7aa20cb8/schema.json",
      "createdAt": "2025-05-07T04:25:34.582Z",
      "visibility": "public"
    }
  ]
}
```

## Get Registry Package Version

Retrieve metadata for a specific package version.

```plain
GET /api/preview/registry/packages/{source}/{publisher}/{name}/versions/{version}
```

### Parameters

| Parameter   | Type   | In   | Description                |
|-------------|--------|------|----------------------------|
| `source`    | string | path | Registry source            |
| `publisher` | string | path | Publisher name             |
| `name`      | string | path | Package name               |
| `version`   | string | path | Package version number (SemVer) or 'latest'  |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/preview/registry/packages/{source}/{publisher}/{name}/versions/{version}
```

## Publish Registry Package Version

Initiates the process of publishing a new version of a package to the registry.

```plain
POST /api/preview/registry/packages/{source}/{publisher}/{name}/versions
```

### Parameters

| Parameter   | Type   | In   | Description      |
|-------------|--------|------|------------------|
| `source`    | string | path | Registry source  |
| `publisher` | string | path | Publisher name   |
| `name`      | string | path | Package name     |
| `version`   | string | body | Version number (SemVer) of the package to publish |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  --request POST \
  --data '{"version":"6.0.0"}' \
  https://api.pulumi.com/api/preview/registry/packages/{source}/{publisher}/{name}/versions
```

### Default response

```plain
Status: 202 Accepted
```

```json
{
  "operationID": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "uploadURLs": {
    "schema": "https://s3.aws.amazon.com/...",
    "index": "https://s3.aws.amazon.com/...",
    "installationConfiguration": "https://s3.aws.amazon.com/..."
  }
}
```

## Complete Registry Package Publish

Complete the package publishing process after uploading all required files.

```plain
POST /api/preview/registry/packages/{source}/{publisher}/{name}/versions/{version}/complete
```

### Parameters

| Parameter   | Type   | In   | Description                |
|-------------|--------|------|----------------------------|
| `source`    | string | path | Registry source            |
| `publisher` | string | path | Publisher name             |
| `name`      | string | path | Package name               |
| `version`   | string | path | Package version identifier |
| `operationID`| string | body | The operation ID received from the publish initiation |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"operationID":"f47ac10b-58cc-4372-a567-0e02b2c3d479"}' \
  https://api.pulumi.com/api/preview/registry/packages/{source}/{publisher}/{name}/versions/{version}/complete
```

## Delete Registry Package Version

Delete a specific version of a package from the registry.

```plain
DELETE /api/preview/registry/packages/{source}/{publisher}/{name}/versions/{version}
```

### Parameters

| Parameter   | Type   | In   | Description                |
|-------------|--------|------|----------------------------|
| `source`    | string | path | Registry source            |
| `publisher` | string | path | Publisher name             |
| `name`      | string | path | Package name               |
| `version`   | string | path | Package version identifier |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/preview/registry/packages/{source}/{publisher}/{name}/versions/{version}
```

## Get Registry Template

Retrieve template information.

```plain
GET /api/preview/registry/templates/{source}/{publisher}/{name}/versions/{version}
```

### Parameters

| Parameter   | Type   | In   | Description      |
|-------------|--------|------|------------------|
| `source`    | string | path | Registry source  |
| `publisher` | string | path | Publisher name   |
| `name`      | string | path | Template name    |
| `version`   | string | path | Template version (SemVer) or 'latest' |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/preview/registry/templates/{source}/{publisher}/{name}/versions/{version}
```

### Default response

```plain
Status: 200 OK
```

```json
{
    "name": "pulumi/templates/static-website-aws-yaml",
    "publisher": "pulumi",
    "source": "github",
    "displayName": "static-website-aws-yaml",
    "description": "A Pulumi YAML program to deploy a static website on AWS",
    "language": "yaml",
    "templateURL": "https://github.com/pulumi/templates/static-website-aws-yaml",
    "readmeURL": "https://api.pulumi.com/api/orgs/pulumi/template/readme?url=https%3A%2F%2Fgithub.com%2Fpulumi%2Ftemplates%2Fstatic-website-aws-yaml",
    "repoSlug": "pulumi/templates",
    "visibility": "public",
    "updatedAt": "2025-05-12T20:53:05.016991943Z"
}
```
