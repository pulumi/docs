---
title: "Adding PostgreSQL State Backend Support to Pulumi: A Community Contribution Journey"
allow_long_title: true

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-06-19T14:46:07+03:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: "Learn about the community-driven journey to add PostgreSQL as a state backend option for Pulumi's DIY backend, enabling robust, scalable state management for self-hosted infrastructure."

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - matan-baruch

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - features
    - diy-backend
    - postgresql
    - state-management
    - community


# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

# Here are some examples of posts we have made in the past for inspiration:
# https://www.linkedin.com/feed/update/urn:li:activity:7171191945841561601
# https://www.linkedin.com/feed/update/urn:li:activity:7169021002394296320
# https://www.linkedin.com/feed/update/urn:li:activity:7155606616455737345
# https://twitter.com/PulumiCorp/status/1763265391042654623
# https://twitter.com/PulumiCorp/status/1762900472489185492
# https://twitter.com/PulumiCorp/status/1755637618631405655

social:
    twitter: "🎉 New PostgreSQL state backend support is now available in @PulumiCorp! Community contributor @matanbaruch shares the journey of adding robust database-backed state storage for DIY backends. #IaC #PostgreSQL #OpenSource"
    linkedin: "Excited to share how PostgreSQL state backend support came to Pulumi through community contribution! This new feature enables robust, transactional state management for self-hosted infrastructure. Read about the development journey and technical implementation."

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

When managing infrastructure as code at scale, reliable state storage is essential. Pulumi Cloud provides a fully managed, secure, and scalable solution out of the box. For teams that choose to build and maintain their own backend, Pulumi now offers support for PostgreSQL as a DIY state storage option—though this requires additional operational overhead and careful consideration around performance, security, and maintenance.

<!--more-->

## The Need for Database-Backed State Storage

Traditional DIY backends in Pulumi have relied on object storage systems like AWS S3, Google Cloud Storage, or Azure Blob Storage. While these work well for many use cases, they have limitations when it comes to handling very large state files, complex locking mechanisms, and transactional guarantees that some enterprise environments require.

PostgreSQL stood out as an excellent candidate for state storage due to its:

- **Large object support**: Ability to handle substantial state files without size constraints
- **ACID compliance**: Robust transactional guarantees for state consistency
- **Mature ecosystem**: Well-established tooling and operational practices
- **Scalability options**: From single instances to complex replication setups
- **Security features**: Comprehensive authentication and authorization capabilities

## The Community Contribution Process

This feature came to life through [PR #19581](https://github.com/pulumi/pulumi/pull/19581/files), which addressed a long-standing community request tracked in [issue #5632](https://github.com/pulumi/pulumi/issues/5632). The development process showcased the collaborative nature of open-source development, with multiple rounds of feedback, testing, and refinement.

### Key Technical Challenges

The implementation required several technical considerations:

**1. Integration with Go Cloud Development Kit (CDK)**

The PostgreSQL backend needed to integrate seamlessly with Pulumi's existing blob storage abstraction layer. This was achieved by implementing the `blob.BucketURLOpener` interface:

```go
// URLHandler is a URL opener for PostgreSQL URLs.
type URLHandler struct{}

// OpenBucketURL implements blob.BucketURLOpener.
func (p URLHandler) OpenBucketURL(ctx context.Context, u *url.URL) (*blob.Bucket, error) {
    pg, err := NewPostgresBucket(ctx, u)
    if err != nil {
        return nil, err
    }
    return pg.Bucket(), nil
}
```

**2. Database Schema Design**

The implementation uses a simple but effective schema for storing state data:

```sql
CREATE TABLE IF NOT EXISTS pulumi_state (
    key TEXT PRIMARY KEY,
    data JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

This design allows for efficient key-based lookups while leveraging PostgreSQL's native JSON support for flexible state data storage.

**3. Cross-Platform Testing**

One of the significant challenges was ensuring the implementation worked across different operating systems and CI environments. The solution involved using [testcontainers-go](https://golang.testcontainers.org/modules/postgres/) to spin up PostgreSQL instances during testing, with appropriate skip conditions for environments where Docker isn't available:

```go
func skipIfDockerNotAvailable(t *testing.T) {
    if runtime.GOOS == "windows" || runtime.GOOS == "darwin" {
        t.Skip("Skipping test: Docker not available on this platform in CI")
    }
    
    // Additional Docker availability checks...
}
```

## Performance and Limitations

### PostgreSQL wins over a plain S3 bucket

- **ACID transactions with row-level locking –** A postgres backend means strong consistency guarantees.

- **Faster for smaller state files –** Community benchmarks show improvements on S3 backend speed for smaller state files.

- **Point-in-time restore –** WAL-based backups allow for easier rollback.

- **Deep observability –** plug pg-metrics into Grafana/APM for real-time insight.

### Gaps you'll still close only with Pulumi Cloud

- **Server-side policy guardrails (CrossGuard) –** automatically enforced policies on every preview or deploy.

- **Always-on drift detection –** automatic scans catch out-of-band changes.

- **Managed Deployments –** fully managed runners, PR previews, and dependent stack updates.

- **Org-wide RBAC, SSO/SAML, immutable audit logs** – turnkey for teams and auditors.

- **Search & analytics across *all* cloud resources (Insights)** – not just those managed by Pulumi.

- **Enterprise Secrets & Configuration (ESC)** \- encrypted secrets and config with RBAC, versioning and audit trail.

- **SOC 2, high availability, and painless upgrades** – Pulumi operates the control plane so you don't have to.

## Getting Started

Using the PostgreSQL backend is straightforward:

1. **Login to your PostgreSQL backend:**
```bash
pulumi login postgres://pulumi_user:secure_password@localhost:5432/pulumi_state?sslmode=require
```

2. **Use Pulumi normally:**
```bash
pulumi up
# Your state is now stored in PostgreSQL!
```

## Community Impact

This contribution demonstrates the power of community-driven development in open source projects. It addresses a real need expressed by Pulumi users while maintaining the high quality standards expected from the project.

The implementation follows Pulumi's architectural patterns and coding standards, making it a seamless addition to the existing codebase. The comprehensive documentation and testing ensure that future maintainers can easily understand and modify the code.

## What's Next?

The PostgreSQL backend opens up several possibilities for future enhancements:

- **High Availability**: Support for PostgreSQL clustering and replication
- **Performance Optimizations**: Caching strategies and connection pooling
- **Advanced Features**: Custom backup strategies and state analytics
- **Multi-tenant Support**: Isolation patterns for multiple teams or environments

## Conclusion

The addition of PostgreSQL state backend support to Pulumi represents more than just a new feature—it's a testament to the collaborative nature of open source development and the power of community contributions. By providing enterprise-grade state storage options while maintaining the simplicity that makes Pulumi great, this feature enables organizations to adopt infrastructure as code with confidence.

Whether you're running a small startup or managing infrastructure for a large enterprise, having robust, reliable state storage options is crucial. The PostgreSQL backend provides an improved approach to Do-It-Yourself state management.

If you're interested in contributing to Pulumi or have ideas for new features, the community welcomes your contributions. This PR serves as an excellent example of how community members can make meaningful improvements to the project while learning from experienced maintainers and following established best practices.
