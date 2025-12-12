---
title: Pulumi Platform Security Whitepaper
meta_desc: Technical whitepaper covering Pulumi platform architecture, cryptographic security, operational commitments, and SOC 2 Type II compliance.
---

Last updated: December 2025

## Executive Summary

The Pulumi Cloud platform represents a comprehensive infrastructure-as-code delivery system designed to enable
organizations to define, deploy, and manage cloud infrastructure through declarative programming interfaces. This
document provides a detailed technical overview of the platform's architecture, security mechanisms, and operational
commitments. It is intended for engineering and security audiences evaluating the system's design and security posture.

## High-Level Architecture

### Platform Overview

The Pulumi platform consists of two primary architectural components: a client-side command-line interface and a
multi-tenant cloud service infrastructure. These components work in concert to provide a complete infrastructure
management solution. The command-line interface serves as the primary interaction point for end users, while the cloud
service provides centralized state management, deployment orchestration, policy enforcement, and collaboration features.

On its core service layer the cloud service provides RESTful APIs for all platform operations, while specialized
components handle specific functional domains including deployment execution, resource discovery, policy evaluation,
workflow orchestration, and artificial intelligence-powered assistance. This separation of concerns allows each component
to scale independently based on demand patterns while maintaining service boundaries.

### Infrastructure Deployment Model

The platform's infrastructure is deployed using a container orchestration model on managed container services. Compute
resources are organized into clusters with auto-scaling capabilities, allowing the system to adapt to varying load
patterns. Services are distributed across multiple availability zones to ensure high availability, with load balancing
distributing incoming traffic across healthy service instances. The deployment model supports both fully managed cloud
deployments and self-hosted installation options for organizations with specific regulatory or operational requirements.

Network architecture follows a layered approach with distinct network zones for public-facing services, application
workloads, and data storage. External traffic enters through a content delivery network and load balancing layer that
provides distributed denial-of-service protection and request routing. Application services reside in private network
segments with no direct internet access, communicating through internal service discovery mechanisms. Database and
storage resources are further isolated in dedicated network zones with restrictive access controls allowing only
authorized application connections.

In fully managed cloud deployments, the platform is deployed into distinct cloud provider tenants and virtual private
networks.

### Core Service Components

The platform's API service forms the central hub for all platform operations, handling authentication, authorization,
resource management, and coordinating with specialized subsystems. This service maintains the primary data model
representing organizations, projects, stacks, deployment history, and configuration state. It implements comprehensive
role-based access control ensuring that all operations respect organizational access policies and user permissions.

Deployment orchestration represents a critical functional domain within the platform. When users initiate infrastructure
operations, requests are queued and subsequently processed by specialized execution components. These components operate
in isolated execution environments, pulling the latest infrastructure code, applying the requested changes against cloud
provider APIs, and capturing the resulting state. Execution environments are ephemeral, created for each operation and
destroyed upon completion, ensuring isolation between deployments and preventing state pollution across operations.

Resource discovery and policy compliance functions are handled by specialized scanning and evaluation services. The
scanning component connects to cloud provider APIs to inventory existing infrastructure resources, building a
comprehensive catalog of deployed assets. The evaluation component assesses these resources against organization-defined
policy packs, identifying compliance violations and generating reports. This architecture enables organizations to
maintain visibility into their infrastructure posture and enforce governance requirements across their cloud
environments.

Workflow integration provides continuous deployment capabilities by connecting to source control systems and executing
infrastructure operations in response to repository events. A pool management component maintains a fleet of execution
environments that can be rapidly allocated to handle workflow jobs. These environments are pre-configured with necessary
tooling and credentials, reducing job startup latency while maintaining isolation between executions.

### Data Storage Architecture

The platform employs a multi-layered data storage strategy optimized for different access patterns and data
characteristics. Structured operational data including user accounts, organizations, resource metadata, deployment
history, and access control policies resides in a managed relational database service. The platform deploys the database
in a highly available configuration with automatic failover capabilities and read replicas to scale query workloads. All
connections to the database utilize transport layer security with enforced minimum protocol versions, and the platform
encrypts data at rest using provider-managed encryption services.

The platform stores unstructured data including infrastructure state checkpoints, policy pack artifacts, and template
repositories in object storage services. State checkpoints represent the most critical data in the system, as they
contain the complete state of managed infrastructure including resource identifiers, configuration values, and
inter-resource dependencies. The platform stores these checkpoints with versioning enabled, allowing recovery from
accidental modifications or deletions. Cross-region replication ensures that checkpoint data remains available even in
the event of regional outages.

Caching infrastructure provides performance optimization for frequently accessed data and reduces load on backend
storage systems. The platform stores session information, metadata caches, and query results in managed cache clusters
with automatic scaling and failure detection. The caching layer implements appropriate cache invalidation strategies to
maintain consistency while maximizing hit rates.

Search functionality is provided through a managed search cluster that indexes resource metadata, enabling fast
full-text and structured queries across large infrastructure catalogs. Search indices are populated through event
streams that capture resource changes as they occur, ensuring that search results remain current with minimal latency.
The search infrastructure is deployed in a separate network environment with controlled access from application
services.

### Client Architecture

The command-line interface provides the primary user interface for interacting with infrastructure as code. The client
implements a plugin-based architecture where resource providers are loaded dynamically based on the resources defined in
user programs. When users execute infrastructure operations, the client coordinates between the user's program code,
loaded provider plugins, and the backend service to orchestrate the requested changes.

State management in the client supports multiple backend implementations, allowing users to choose between fully managed
cloud state storage and self-managed options including local filesystems, object storage services, or database systems.
Regardless of backend choice, the client implements consistent state locking mechanisms to prevent concurrent
modifications that could corrupt state data.

The client communicates with the cloud service through RESTful APIs, with all requests authenticated using access
tokens. Request compression reduces bandwidth consumption for large payloads, while retry logic handles transient network
failures. Distributed tracing headers are injected into requests, enabling end-to-end observability across the
client-service boundary.

## Cryptographic Architecture

### Encryption Key Hierarchy

The platform implements a sophisticated three-tier key hierarchy that separates key management responsibilities and
enables flexible key rotation without requiring re-encryption of all data. At the top of the hierarchy are key
encryption keys, which are never stored unencrypted within the platform's data stores. For cloud deployments, these keys
reside in external key management services operated by cloud infrastructure providers. For self-hosted deployments, they
reside in secure local key storage protected by operating system access controls and hardware security modules when
available.

Data encryption keys form the second tier of the hierarchy. These symmetric keys are generated using cryptographically
secure external key management services and are used for the actual encryption of content. Data encryption keys are
encrypted using key encryption keys before being stored in the platform's database. This envelope encryption pattern
ensures that key material is never persisted in plaintext, and that access to the database alone is insufficient to
decrypt protected content.

The third tier consists of the encrypted content itself, which includes user secrets, configuration values, and other
sensitive data. Each piece of content is encrypted using a data encryption key and a randomly generated initialization
vector, ensuring that identical plaintexts produce different ciphertexts. Authenticated encryption modes are used
throughout, providing both confidentiality and integrity protection.

### Encryption Implementation

All symmetric encryption operations utilize the Advanced Encryption Standard in Galois/Counter Mode with 256-bit keys.
This authenticated encryption algorithm provides both confidentiality of plaintext and integrity verification of
ciphertext, protecting against unauthorized modifications. Each encryption operation generates a unique initialization
vector using cryptographically secure random number generation, preventing key stream reuse and ensuring semantic
security.

Envelope structures encode the encryption format version, cryptographic binding tags, initialization vectors, and
authentication tags alongside the ciphertext. Format versioning enables cryptographic agility, allowing the system to
migrate to new encryption algorithms or parameters as security requirements evolve. Cryptographic tags bind encrypted
content to specific encryption keys, preventing key substitution attacks where an attacker might attempt to decrypt
content using a key they control.

For scenarios requiring asymmetric encryption, such as certain key management service integrations, the platform employs
optimal asymmetric encryption padding with secure hash algorithms. Digital signatures use probabilistic signature
schemes with secure hash functions to provide non-repudiation and integrity verification.

### Key Management Service Integration

The platform integrates with multiple key management services provided by major cloud infrastructure vendors, optionally
allowing organizations to maintain control over their own encryption keys while leveraging provider-operated security
infrastructure when using customer-managed keys. These integrations support standard key operations including data key
generation, key encryption, and key decryption.

When generating new encryption keys, the platform requests data keys from the key management service. The service
returns both plaintext and encrypted versions of the generated key. The platform uses the plaintext key immediately for
encryption operations, then securely erases it from memory. The encrypted key is persisted to the database, associated
with the encrypted content through cryptographic binding mechanisms.

Decryption operations retrieve encrypted data keys from the database and submit them to the key management service for
decryption. The service verifies that the requesting identity has appropriate permissions before returning the plaintext
key. This access control enforcement at the key management service level provides an additional security boundary beyond
the platform's own authorization mechanisms.

Integrations support multiple authentication methods including service credentials for platform-operated deployments and
federated identity tokens for customer-managed keys. When using federated authentication, the platform exchanges
temporary credentials with the key management service, following the principle of least privilege by requesting only the
minimum necessary permissions for each operation.

### Organizational Key Isolation

The platform supports both system-wide encryption keys managed by the platform operator and organization-specific keys
managed by individual customers. System-wide keys provide default encryption for organizations that have not configured
their own keys, ensuring that all sensitive data receives encryption at rest without requiring explicit customer action.
These keys are stored in the platform operator's key management service accounts with access restricted to platform
service identities.

Organizations requiring additional control over their encryption keys can provision organization-specific key encryption
keys in their own key management service accounts. The platform integrates with these customer-managed keys using
cross-account access mechanisms or federated identity flows. This bring-your-own-key model ensures that the platform
operator cannot decrypt organization data without explicit authorization from the customer's key management
infrastructure.

Each organization can maintain multiple key encryption keys simultaneously, with one designated as the default for new
encryption operations. This multi-key capability supports key rotation workflows where new data is encrypted with
updated keys while historical data remains encrypted with previous key versions. The platform tracks which data
encryption keys are encrypted by which key encryption keys, enabling systematic re-encryption during key rotation
operations.

### Key Rotation and Migration

Key rotation represents a critical operational capability for maintaining cryptographic hygiene and responding to
potential key compromise. The platform implements comprehensive key migration capabilities that allow systematic
re-encryption of data from one key encryption key to another without service interruption.

Migration operations enumerate all data encryption keys encrypted with a source key encryption key, decrypt each data
key using the source key, re-encrypt it with a destination key, and update the database records atomically. The
migration process maintains referential integrity between encrypted content, data encryption keys, and key encryption
keys throughout the operation. Migration state is tracked persistently, allowing interrupted migrations to be resumed
and providing audit trails of completed migrations.

During key rotation, both old and new keys remain accessible for a transition period. New encryption operations use the
updated default key while existing encrypted data continues to use its original key until explicitly migrated. This
approach eliminates the need for immediate re-encryption of large data volumes while ensuring forward progress toward
complete key transition.

### Transport Security

All network communication between platform components and with external clients utilizes transport layer security
protocols with enforced minimum protocol versions. Modern cipher suites providing forward secrecy are preferred,
ensuring that compromise of long-term keys does not enable decryption of historical traffic. Certificate validation is
enforced for all connections, with certificates issued by trusted certificate authorities.

The command-line interface enforces transport layer security by default for all communication with cloud services. While
an insecure mode exists to facilitate development and testing scenarios, users must explicitly opt into this mode, and
prominent warnings are displayed to discourage production usage.

### Secrets Management in State

Infrastructure state includes both public configuration values and sensitive secrets such as database passwords, API
keys, and encryption keys used by deployed infrastructure. The platform treats these secrets with additional protections
beyond general state encryption. Secrets are encrypted using the envelope encryption mechanism described previously,
with data encryption keys specific to the containing environment or stack.

When users define secrets in their infrastructure programs, the command-line interface encrypts secret values before
transmitting them to the backend service. This client-side encryption ensures that secrets remain protected during
transit and in the backend service's memory. Decryption occurs only when the infrastructure operation requires access to
the secret value, such as during resource provisioning.

The command-line interface provides multiple secrets manager implementations to accommodate different deployment models
and security requirements. Users can select backend service encryption, passphrase-based encryption for self-managed
deployments, cloud-native key management services for managed deployments, or custom secrets management backends for
integration with existing secrets infrastructure. Regardless of implementation choice, the user interface remains
consistent, allowing users to switch encryption backends without modifying their infrastructure code.

## Operational Commitments

### Audit Logging and Compliance

Comprehensive audit logging captures all significant operations performed within the platform, providing accountability
and enabling security monitoring, compliance reporting, and incident investigation. Audit events include user
authentication, authorization decisions, resource modifications, administrative actions, and configuration changes. Each
audit event records the acting user, timestamp, source network address, affected resources, and operation outcome.

Administrative operations receive special audit treatment due to their elevated privileges. A dedicated audit log
captures all administrator commands with detailed context including the authorization mechanism used, business
justification references, and affected accounts. This separated administrative audit trail ensures that privileged
operations receive appropriate scrutiny and that audit records cannot be modified by the same administrators whose
actions are being logged.

Organizations can configure automated export of their audit logs to external storage under their control. Export
functionality supports multiple destination types and configurable schedules, enabling organizations to integrate
platform audit events with their existing security information and event management systems. Exported audit logs include
cryptographic signatures when supported by the destination, providing non-repudiation guarantees.

### Monitoring and Observability

Comprehensive monitoring infrastructure provides real-time visibility into platform operations, enabling rapid detection
and response to performance degradations, service disruptions, and security incidents. The monitoring architecture
follows the three pillars of observability: metrics, logs, and distributed traces.

Metrics collection captures time-series data about service health, resource utilization, request rates, error rates, and
business-level indicators. Metrics are aggregated at multiple granularities, from individual service instance metrics to
cluster-wide and system-wide aggregates. Dimensional metrics enable sophisticated queries that slice data across
multiple attributes such as service version, deployment environment, customer organization, and request characteristics.
This metric data feeds real-time dashboards displayed to operations teams. It also powers automated alerting based on
threshold violations or anomaly detection.

Structured logging captures detailed information about service operations, errors, and security-relevant events. Log
aggregation collects logs from all service instances and indexes them for full-text search and analytical queries. Log
retention policies balance the value of historical logs for incident investigation against storage costs, with different
retention periods for various log categories based on their compliance and operational requirements.

Distributed tracing provides end-to-end visibility into request flows across service boundaries. When a request
enters the system, a unique trace identifier is generated and propagated through all service-to-service calls. Each
service records timing information and metadata about its request processing, creating trace spans that are assembled
into complete request traces. Trace sampling strategies balance the observability value of complete traces against the
performance overhead and cost of trace collection, with intelligent sampling that captures all errors and slow requests
while sampling only a fraction of successful fast requests.

### Incident Detection and Response

Automated alerting continuously monitors the health and security posture of the platform, detecting anomalies and
threshold violations that may indicate incidents. Alert definitions cover infrastructure health metrics, application
error rates, security events, and business-critical user experience indicators. Alerts are routed to on-call engineering
teams through integrated incident management systems that handle alert deduplication, escalation policies, and on-call
scheduling.

Alert sensitivity is tuned to balance rapid incident detection against alert fatigue from false positives. Statistical
anomaly detection complements threshold-based alerting, identifying unusual patterns that may not trigger static
thresholds. Alert context includes relevant metrics, recent deployments, and links to related dashboards and logs,
enabling responders to quickly assess incident severity and begin investigation.

Incident response follows documented procedures that guide responders through detection, assessment, containment,
remediation, and post-incident review phases. During active incidents, coordination occurs through dedicated
communication channels. Incident timelines are captured from communication channels, service logs, and operator actions,
providing comprehensive records for post-incident analysis.

Post-incident reviews analyze incident causes, evaluate response effectiveness, and identify improvement opportunities.
These reviews emphasize blameless culture, focusing on systemic factors rather than individual actions. Improvement
actions are tracked through completion, creating a continuous feedback loop that strengthens the platform's resilience
over time.

### Vulnerability Management

Security vulnerability management encompasses the entire lifecycle from vulnerability identification through remediation
and verification. The platform employs multiple mechanisms to identify potential vulnerabilities including automated
dependency scanning, security advisories monitoring, and periodic security assessments.

Dependency management automation continuously monitors third-party libraries and frameworks for known vulnerabilities,
automatically proposing updates when patches become available. Update proposals undergo testing in non-production
environments before production deployment, ensuring that security updates do not introduce functional regressions.
Dependency version constraints balance the desire for latest security patches against the stability benefits of
conservative update policies.

Container images undergo regular rebuilds to incorporate updated base images and system packages, ensuring that the
latest security patches are deployed even when application code has not changed. Image scanning occurs during the build
process and periodically for deployed images, identifying vulnerabilities in system packages and application
dependencies. Critical vulnerabilities trigger accelerated update processes that expedite patching outside normal
release cycles.

Security patch deployment follows risk-based prioritization, with critical vulnerabilities affecting internet-exposed
services receiving immediate attention while lower-severity issues are addressed through regular release processes.
Patch testing verifies both the security fix and continued system functionality before production deployment. Emergency
patches may be deployed with abbreviated testing when vulnerability severity and exploitability warrant urgent action.

### Backup and Recovery

Data durability and availability are ensured through comprehensive backup strategies that protect against hardware
failures, software defects, operational errors, and disaster scenarios. Backup architectures vary based on data
characteristics, with transactional databases, object storage, and operational state each employing appropriate
protection mechanisms.

Database backup includes both continuous replication and point-in-time snapshot mechanisms. Continuous replication
maintains synchronized copies of database contents across multiple data centers, enabling rapid failover in the event of
data center outages. Transaction logs are retained for extended periods, supporting point-in-time recovery to any moment
within the retention window. This combination of real-time replication and retained transaction logs protects against
both infrastructure failures and logical corruption scenarios.

Snapshot-based backups create periodic point-in-time copies of database contents that are stored separately from the
primary database infrastructure. Snapshots are copied to geographically distant regions, ensuring that regional
disasters do not impact backup availability. Snapshot retention follows a tiered schedule, with recent snapshots
retained for rapid recovery and older snapshots gradually aged out based on retention policies. Automated testing
validates that snapshots can be successfully restored, preventing scenarios where backup processes appear successful but
generate unrestorable backups.

Object storage protection leverages versioning and cross-region replication capabilities. Versioning preserves
historical versions of objects when they are modified or deleted, enabling recovery from accidental changes or malicious
modifications. Cross-region replication asynchronously copies objects to storage regions geographically separated from
primary storage, providing protection against regional failures. The combination of versioning and replication ensures
that data remains accessible even when facing multiple concurrent failure scenarios.

Recovery procedures are documented and regularly tested through disaster recovery exercises. These exercises validate
that documented procedures remain accurate, that backup data can be successfully restored, and that recovery objectives
can be achieved within acceptable timeframes. Lessons learned from exercises inform updates to recovery procedures and
backup configurations, maintaining the effectiveness of disaster recovery capabilities as the platform evolves.

### Business Continuity

High availability architecture eliminates single points of failure and enables the platform to continue operating
despite individual component failures. Critical services are deployed across multiple availability zones within cloud
regions, with automatic traffic routing directing requests away from unhealthy instances. Stateless application services
can be replaced rapidly when failures occur, with new instances joining the service pool within minutes.

Stateful components including databases employ multi-node clusters with automatic failover capabilities. When primary
database nodes fail, secondary nodes automatically promote to primary role and begin accepting write traffic. This
failover process completes within seconds to minutes depending on failure detection latency and failover coordination
time. Application services automatically reconnect to the new primary database node, requiring no manual intervention.

Load distribution across multiple instances enables graceful degradation during partial outages. When some service
instances fail, remaining healthy instances continue serving traffic at potentially reduced capacity. Auto-scaling
mechanisms detect increased load on remaining instances and provision additional capacity to maintain service levels.
This elastic capacity ensures that temporary increases in load or partial infrastructure failures do not result in
complete service unavailability.

Disaster recovery capabilities extend beyond individual component failures to address regional outages that affect
entire data centers. Cross-region backup replication enables recovery of critical data to alternative regions.
Infrastructure-as-code definitions allow rapid provisioning of complete platform infrastructure in alternative regions
when recovery in the primary region is not feasible. While regional failover represents a significant operational
undertaking, documented procedures and periodic testing ensure that this capability remains viable when needed.

## Conclusion

The Pulumi Cloud platform implements comprehensive security controls throughout its architecture, from cryptographic
protection of data at rest and in transit, through role-based access control and audit logging, to operational practices
supporting incident response, vulnerability management, and business continuity. The platform's security architecture
reflects defense-in-depth principles with multiple layers of protection, ensuring that no single control failure
compromises overall security posture.

The separation of key management responsibilities through hierarchical key architectures, support for customer-managed
encryption keys, and cryptographic binding between encryption layers demonstrates a mature approach to data protection.
Authentication and authorization mechanisms provide flexible integration with organizational identity providers while
maintaining strong security guarantees. Comprehensive audit logging and monitoring enable both real-time security event
detection and post-facto incident investigation.

Operational commitments around backup and recovery, and vulnerability management ensure that the platform maintains its
security posture over time despite evolving threats and changing requirements. The combination of technical security
controls and operational practices creates a robust foundation for organizations entrusting their infrastructure
management to the Pulumi platform.
