---
title_tag: "Troubleshooting | Self-Hosting Pulumi"
meta_desc: Symptoms, causes, and fixes for common self-hosted Pulumi Cloud problems — failed migrations, garbled state, TLS errors, and search issues.
title: Troubleshooting
h1: Troubleshooting Self-Hosted Pulumi Cloud
menu:
  administration:
    name: Troubleshooting
    parent: administration-self-hosting
    weight: 9
    identifier: administration-self-hosting-troubleshooting
pulumi_cloud_feature: self-hosting
---

{{< self-hosting-trial-note />}}

Problems that come up often enough to be worth naming, with the symptom first so you can find yours by searching the error text.

## Migrations fail with `ALGORITHM=INPLACE is not supported`

**Symptom.** The migrations container exits with an error containing `ALGORITHM=INPLACE is not supported. Try ALGORITHM=COPY`.

**Cause.** The database's `sql_mode` does not include `STRICT_TRANS_TABLES`. Aurora MySQL 8.0 does not set it by default.

**Fix.** Set `STRICT_TRANS_TABLES` in the parameter group or server configuration and restart, then re-run migrations. See [Required sql_mode settings](/docs/administration/self-hosting/operations/database/#required-sql_mode-settings).

## The Docker Compose stack exits immediately

**Symptom.** `run-ee.sh` prints a message about contacting sales and exits before any container starts.

**Cause.** `PULUMI_LICENSE_KEY` is unset. The script hard-fails rather than starting a service that cannot run.

**Fix.** Export the license key before running the script. See the [Docker Compose quickstart](/docs/administration/self-hosting/deployment-options/quickstart-docker-compose/).

## Stack state or policy packs download garbled

**Symptom.** The CLI reports corrupt or unreadable state, or policy packs fail to load, against an S3-compatible object store.

**Cause.** The API stores objects gzip-compressed. Something between the store and the client — the store itself, a reverse proxy, or an ingress controller — is stripping the `Content-Encoding: gzip` response header.

**Fix.** Configure the store and every intermediary to preserve that header.

## Connection failures to a bring-your-own MySQL server

**Symptom.** The installer cannot reach a MySQL server that is otherwise up and accepting connections.

**Cause.** Inbound ICMP is disabled on the database server. The installer's connectivity check uses it.

**Fix.** Allow inbound ICMP from the cluster to the database server.

## S3-compatible object storage is not reachable

**Symptom.** The API fails to read or write objects against a non-AWS S3-compatible store.

**Cause.** The endpoint is missing the query parameters the storage client needs to address a non-AWS endpoint.

**Fix.** Append `endpoint=IP:PORT` and `s3ForcePathStyle=true` to the storage endpoint. See [System requirements](/docs/administration/self-hosting/system-requirements/#object-storage).

## TLS verification fails when connecting to MySQL

**Symptom.** The API or migrations container fails TLS verification against the database.

**Cause.** `DATABASE_CA_CERTIFICATE` is set to a file path rather than the PEM contents, or the certificate does not match the hostname the service connects to.

**Fix.** Set the variable to the PEM value itself and connect using a hostname the certificate covers. See [Encrypting connections with TLS](/docs/administration/self-hosting/operations/database/#encrypting-connections-with-tls).

## Duplicate or failed migrations across multiple Docker hosts

**Symptom.** Running the containers on more than one host produces migration errors or repeated migration attempts.

**Cause.** Every host is trying to run migrations against the shared database.

**Fix.** Set `disableDbMigrations` on every host except the one that owns migrations. See the [Docker Engine guide](/docs/administration/self-hosting/deployment-options/local-docker/).

## An unexpected account owns SAML administration

**Symptom.** After enabling SAML SSO, the administrator is an account nobody intended.

**Cause.** On a fresh installation the first user to sign up becomes the administrator, and setting `samlEnabled: true` does not by itself block email and password signup.

**Fix.** Create the intended administrator account first, before sharing the console URL. To stop further email signups, set `PULUMI_DISABLE_EMAIL_SIGNUP` on the API container — hiding the option on the console with `PULUMI_HIDE_EMAIL_SIGNUP` does not disable the underlying handler.

## Stacks are missing from the Resources page

**Symptom.** Resource search returns nothing, or is missing recently updated stacks.

**Cause.** The OpenSearch index is stale or was built while the cluster was unavailable.

**Fix.** Reindex from **Settings → Self-hosted** in the console. Search reindexes automatically each week, and search is never in the critical path for stack updates. See [Search](/docs/administration/self-hosting/components/search/).

## Still stuck?

Contact [Pulumi support](/support/) with your installer, its version, and the failing container's logs.
