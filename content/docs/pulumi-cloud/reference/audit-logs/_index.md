---
title: Audit Logs
title_tag: "Pulumi Cloud REST API: Audit Logs"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for retrieving and exporting audit log events.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 2
---

Audit Logs provide a record of user actions and system events within Pulumi Cloud. The Audit Logs API allows you to retrieve and export audit log entries for compliance, security, and monitoring purposes.

## Audit Log Operations

The API provides endpoints for the following operations:

- Retrieving audit log events in JSON format
- Exporting audit log events in CSV or CEF formats

## Get Audit Log Events (JSON)

Retrieve audit log events in JSON format.

```plain
GET /api/orgs/{organization}/auditlogs
```

### Parameters

| Parameter           | Type           | In    | Description                                                                                                  |
|---------------------|----------------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string         | path  | organization name                                                                                            |
| `startTime`         | unix timestamp | query | return audit log entries that occurred before (i.e., are older) than this timestamp                          |
| `userFilter`        | string         | query | **Optional.** username (e.g. `user1`) to filter results by                                                   |
| `continuationToken` | string         | query | **Optional.** the continuation token to use for retrieving the next set of results if results were truncated |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token pul-abcdefghijklmnopqrstuvwxyz" \
  --compressed \
  https://api.pulumi.com/api/orgs/{organization}/auditlogs?startTime=1615872240
```

### Default response

```plain
Status: 200 OK
```

```plain
{
    "continuationToken": "1615413365",
    "auditLogEvents": [
        {
            "timestamp": 1615413432,
            "sourceIP": "10.0.0.1",
            "event": "Stack Update Started",
            "description": "Started update \"6f93fd86-b972-4402-9952-264c81639794\" for stack \"project1/dev\"",
            "user": {
                "name": "First Last",
                "githubLogin": "user1",
                "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
            }
        },
        {
            "timestamp": 1615413365,
            "sourceIP": "10.0.0.1",
            "event": "Stack Exported",
            "description": "Exported stack project1/dev",
            "user": {
                "name": "First Last",
                "githubLogin": "user1",
                "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
            }
        },
        {
            "timestamp": 1615413365,
            "sourceIP": "10.0.0.1",
            "event": "Stack Update Started",
            "description": "Started update \"da85cf90-4c7b-4dc4-9286-6ca58b4196e3\" for stack \"project1/dev\"",
            "user": {
                "name": "First Last",
                "githubLogin": "user1",
                "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
            }
        }
    ]
}
```

## Export Audit Log Events (CSV or CEF)

Export audit log events in CSV or Common Event Format (CEF).

{{< notes >}}
This API endpoint differs from other endpoints in the following ways:

- The response data is _always_ gzip compressed.
- The `Content-Type: application/json` header is omitted.
{{< /notes >}}

```plain
GET /api/orgs/{organization}/auditlogs/export
```

### Parameters

| Parameter      | Type           | In    | Description                                                                                |
|----------------|----------------|-------|--------------------------------------------------------------------------------------------|
| `organization` | string         | path  | organization name                                                                          |
| `startTime`    | unix timestamp | query | return audit log entries that occurred before (i.e., are older) than this timestamp        |
| `userFilter`   | string         | query | **Optional.** username (e.g. `user1`) to filter results by                                 |
| `format`       | string         | query | **Optional.** the response format to return - possible values are `cef` or `csv` (default) |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --compressed \
  https://api.pulumi.com/api/orgs/{organization}/auditlogs/export?startTime=1615872240&format=cef
```

### Default response

```plain
Status: 200 OK
```

```plain
Timestamp,Name,Login,Event,Description,SourceIP,RequireOrgAdmin,RequireStackAdmin,AuthenticationFailure
2021-04-11T23:51:45Z,First Last,user1,Member Role Changed,"Changed organization role for ""user2"" to admin",192.168.10.11,true,false,false
2021-04-11T23:09:36Z,First Last,user1,Member Role Changed,"Changed organization role for ""user2"" to admin",192.168.10.11,true,false,false
2021-04-11T23:09:25Z,First Last,user1,Member Role Changed,"Changed organization role for ""user3"" to admin",192.168.10.11,true,false,false
2021-04-11T21:09:52Z,First Last,user1,Secret Decrypted,"Decrypted secret value for stack ""demo-aws-ts-webserver/dev-user1"" (cipher text suffix: ""tbpiX4c="")",192.168.10.11,false,false,false
```
