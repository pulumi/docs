---
title_tag: "Database Best Practices | Self-Hosting Pulumi"
meta_desc: Best practices for MySQL database configuration, high availability, sizing, and migrations for self-hosted Pulumi Cloud.
title: Database
h1: Database Best Practices
menu:
  administration:
    name: Database
    parent: administration-security-compliance-self-hosted-operations
    weight: 2
    identifier: administration-security-compliance-self-hosted-operations-database
---

{{< self-hosting-trial-note />}}

Pulumi Cloud uses MySQL 8.0 for metadata, stack state references, and user/organization data. This page covers best practices for database configuration in production self-hosted deployments.

## Use a managed MySQL service

Deploy MySQL 8.0 on a managed service rather than self-managing:

- **AWS**: Amazon Aurora MySQL (recommended) or RDS MySQL
- **Azure**: Azure Database for MySQL Flexible Server
- **GCP**: Cloud SQL for MySQL
- **On-prem**: MySQL 8.0 with InnoDB, configured for replication

## Required sql_mode settings

Pulumi Cloud database migrations use `ALGORITHM=INPLACE`, which MySQL only permits when strict mode is active. The server's `sql_mode` must include `STRICT_TRANS_TABLES`. Without it, migrations fail with:

```
ALGORITHM=INPLACE is not supported. Reason: cannot silently convert NULL values, as required in this SQL_MODE. Try ALGORITHM=COPY.
```

Stock MySQL 8.0 enables `STRICT_TRANS_TABLES` by default, but some managed and custom configurations do not — notably Amazon Aurora MySQL 8.0. If you bring your own database or customize a parameter group, configure `sql_mode` for your platform:

- **Amazon Aurora / RDS MySQL**: Set `sql_mode` (including `STRICT_TRANS_TABLES`) in the DB cluster parameter group (Aurora) or DB parameter group (RDS), then apply and reboot.
- **Azure Database for MySQL Flexible Server**: Set the `sql_mode` server parameter to include `STRICT_TRANS_TABLES`.
- **Google Cloud SQL for MySQL**: Add `sql_mode` as a database flag with a value that includes `STRICT_TRANS_TABLES`.
- **Self-managed MySQL**: Set `sql-mode` in `my.cnf` (for example, `sql-mode = "STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION"`) and restart, or run `SET GLOBAL sql_mode = '...';` at runtime.

{{% notes type="warning" %}}
If `sql_mode` does not include `STRICT_TRANS_TABLES`, database migrations during installation and upgrades will fail. This is a common source of failures on Amazon Aurora MySQL 8.0, which does not enable strict mode by default.
{{% /notes %}}

Verify the current setting by running:

```sql
SHOW VARIABLES LIKE 'sql_mode';
```

## High availability configuration

### Multi-AZ and read replicas

Deploy your database cluster across multiple availability zones with at least one read replica:

- **Aurora**: Use a cluster with a writer instance and one or more reader instances in separate AZs. Aurora handles automatic failover to a reader within approximately 30 seconds.
- **RDS**: Enable Multi-AZ deployment for automatic standby failover.
- **Cloud SQL / Azure MySQL**: Enable high-availability configuration (regional availability).

### Instance sizing

The self-hosted installers default to the following database instance types:

| Cloud | Default instance type | Notes |
| :-- | :-- | :-- |
| AWS | db.r5.large (16 GB RAM) | Memory-optimized, recommended for production |
| Azure | General Purpose D2ads_v5 or equivalent | 2 vCPU / 8 GB RAM |
| GCP | db-g1-small (1.7 GB RAM) | Minimal; upgrade for production use |

For production workloads, start with a memory-optimized instance with at least 16 GB RAM (db.r5.large, db.r6g.large, General Purpose D4s_v3, or equivalent) and scale based on monitoring. Burstable instances (db.t3.*) are acceptable for development and light workloads but may throttle under sustained load.

## Zero-downtime migrations

Pulumi Cloud runs database migrations as a separate task before deploying new application versions. For self-hosted deployments:

- Run migrations before updating service containers.
- The self-hosted installers handle this automatically via a dedicated migration task/job.
- If running migrations manually, ensure they complete before restarting services.

Migrations require strict mode. Confirm your database's `sql_mode` includes `STRICT_TRANS_TABLES` before upgrading — see [Required sql_mode settings](/docs/administration/self-hosting/operations/database/#required-sql_mode-settings).

See [Upgrades](/docs/administration/self-hosting/operations/upgrades/) for the full update process.

## Encrypting connections with TLS

Pulumi Cloud supports TLS-encrypted connections between the API service and MySQL. This encrypts data in transit between the service and database, which is a requirement for many compliance frameworks.

### MySQL server requirements

The MySQL server must be configured with:

- A **server certificate** and **private key** signed by a Certificate Authority (CA).
- The **CA certificate** used to sign the server certificate. This is what the Pulumi API service uses to verify the server's identity.

For managed database services, TLS is typically enabled by default:

- **Amazon Aurora / RDS**: TLS is enabled by default. Download the [RDS CA certificate bundle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) for your region.
- **Azure Database for MySQL**: TLS is enforced by default. Download the [DigiCert Global Root CA](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/how-to-connect-tls-ssl).
- **Google Cloud SQL**: TLS is enabled by default. Download the server CA from the Cloud SQL instance's **Connections** tab.

For self-managed MySQL, configure the server with the `--ssl-ca`, `--ssl-cert`, and `--ssl-key` options pointing to your certificate files. See the [MySQL encrypted connections documentation](https://dev.mysql.com/doc/refman/8.0/en/using-encrypted-connections.html) for details.

### Hostname verification

The API service verifies that the **hostname** in `PULUMI_DATABASE_ENDPOINT` matches the Common Name (CN) or a Subject Alternative Name (SAN) in the server certificate. If the hostname does not match, the connection will fail with a TLS verification error.

- Ensure the certificate includes the database hostname as a DNS SAN (e.g., `my-db.example.com`) or IP SAN (e.g., `10.0.1.50`).
- For managed services, the certificate typically already covers the service endpoint hostname.

### API service configuration

Set the following environment variables on the **API service** container. Both are required to enable TLS — if either is missing, the service connects without TLS.

| Variable Name            | Description                                                                                                                     |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| `DATABASE_CA_CERTIFICATE`  | The PEM-encoded CA certificate that signed the MySQL server's TLS certificate. Must be the certificate **value**, not a file path. |
| `DATABASE_MIN_TLS_VERSION` | The minimum TLS version to accept (e.g., `1.2` or `1.3`).                                                                       |

Example:

```bash
# Load the CA certificate into the environment variable
export DATABASE_CA_CERTIFICATE="$(cat /path/to/ca-cert.pem)"
export DATABASE_MIN_TLS_VERSION="1.2"
```

{{% notes type="warning" %}}
`DATABASE_CA_CERTIFICATE` must contain the **full PEM-encoded certificate text** (including the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` markers), not a file path. This is a common source of misconfiguration.
{{% /notes %}}

### Migrations container

The database migrations container also supports TLS. Set `DATABASE_CA_CERTIFICATE` on the migrations container with the same CA certificate value. See [API component — Migrations](/docs/administration/self-hosting/components/api/#database-connections) for the full list of migration environment variables.

### Verifying TLS is active

After configuring TLS, verify that connections are encrypted by running the following SQL query against your MySQL server:

```sql
SHOW STATUS LIKE 'Ssl_cipher';
```

A non-empty value (e.g., `TLS_AES_256_GCM_SHA384`) confirms the connection is using TLS. An empty value means the connection is unencrypted.

You can also check the TLS version:

```sql
SHOW STATUS LIKE 'Ssl_version';
```

### Requiring TLS on the MySQL server

To ensure **all** connections use TLS (not just the Pulumi API), configure MySQL to reject unencrypted connections:

```sql
-- Require TLS for a specific user
ALTER USER 'pulumi_service'@'%' REQUIRE SSL;

-- Or require TLS for all connections (MySQL 8.0+)
-- Set in my.cnf: require_secure_transport=ON
```
