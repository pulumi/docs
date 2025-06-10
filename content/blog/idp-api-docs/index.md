---
title: "Introducing Auto-Generated API Documentation for Pulumi Components"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-06-17T11:06:40-06:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc:

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - idp-team

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - idp
    - iac
    - components
    - private-registry

---

We're excited to announce a major enhancement to Pulumi IDP that will transform how developers discover, understand, and use infrastructure components. Starting today, when you publish a component to Pulumi Private Registry, we automatically generate comprehensive API documentation across all supported languages.

<!--more-->

## What's New

Every component published to your Pulumi Private Registry now includes a dedicated **API Docs** tab that provides:

- **Complete constructor syntax** for each resource in TypeScript, Python, Go, C#, Java, and YAML
- **Detailed parameter documentation** with descriptions and types
- **Cross-language consistency** ensuring the same high-quality documentation experience regardless of your preferred language
- **Version-specific documentation** that tracks with each component release, so you can always reference the exact API for the version you're using

## Why This Matters

Until now, component authors had to manually create and maintain documentation across multiple languages—a time-consuming process that often led to inconsistent or incomplete docs. With auto-generated API documentation, we're solving several key challenges:

### For Component Authors

- **Zero maintenance overhead**: Documentation is generated automatically from your component's schema
- **Always up-to-date**: API docs are regenerated with every component version
- **Consistent quality**: Every component gets the same comprehensive documentation treatment
- **Version history**: Each component version maintains its own documentation, making it easy to track API changes over time

### For Component Users

- **Better discoverability**: Rich API documentation helps you understand what a component can do
- **Faster adoption**: Clear examples and parameter descriptions reduce time-to-productivity
- **Language flexibility**: Switch between languages while maintaining the same level of documentation quality
- **Version confidence**: Access documentation for the exact version you're using, with clear visibility into what's available in each release

## See It in Action

The new API documentation provides everything you need to get started with a component, with full version tracking:

**Version-Specific Documentation**: Each component version gets its own complete API documentation, so you can reference the exact interface for the version you're using

**Constructor Syntax**: See exactly how to instantiate resources with proper typing information

```typescript

public Trail(string name, TrailArgs? args = null, ComponentResourceOptions? opts = null)

```

**Parameter Details**: Understand what each parameter does and what values are expected

- `name`: The unique name of the resource
- `args`: The arguments to resource properties

**Real Examples**: Copy working code that demonstrates common usage patterns across all supported languages.

## Available Now

This feature is rolling out automatically to all Pulumi IDP customers. If you have existing components in your Private Registry, they'll receive auto-generated API documentation the next time you publish an update.

## Getting Started

Ready to experience the new API documentation? 

1. **Publish a component** to your Pulumi Private Registry using `pulumi package add`
2. **Navigate to your component page** in the Pulumi console
3. **Click the API Docs tab** to explore the auto-generated documentation

The feature works with all existing Pulumi component types and supports the full range of Pulumi's language ecosystem.

## What's Next

This is just the beginning of our efforts to make infrastructure components more accessible and developer-friendly. We're continuing to invest in documentation tooling and component discoverability features.

Have feedback on the new API documentation? We'd love to hear from you. Reach out to our team or share your thoughts in the Pulumi Community Slack.