---
title: "Introducing the Pulumi Azure Native Provider 3.0"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-01-30T14:12:54+01:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: "Introducing the Pulumi Azure Native Provider 3.0: expanded and more accurate"

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - thomas-kappler

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - azure
    - providers


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
    twitter:
    linkedin:

---

- We are thrilled to announce ...
- The Azure Native provider offers the most complete support for Azure possible - with same day access to the entire surface area of the Azure features from Azure Resource Manager.

<!--more-->

## List the major features introduced during v2

- Intro: We minimize major versions to avoid disruption

- Custom resources (phrase differently)
  - WebApp slots
  - Key Vault access policies
  - Blob container legal holds
  - Fileshare support in Recovery Services
- Windows binaries are now signed
- Maintain nested resources which are also settable on the parent resource #2755
- Better diffs through support for "keyed arrays" (sets) #2968
- Large investments in end-to-end testing, in particular for all authentication methods. (Does it look bad to call out that we _didn't_ have coverage before this?)
- Retry Conflicts for AnotherOperationInProgress #3653

## SDK size

Reduced by roughly 45%.

## Refreshed default API versions

## Improved correctness

- "Force new from subtypes" #3006
- De-duplicating resources by API path
- Skip flattening when properties clash #3195
- Up to date module naming: Network, CosmosDB

## Migrating from 2.x to 3.x

- All 2.x default API versions are preserved
- **Clearly** point to the migration guide
