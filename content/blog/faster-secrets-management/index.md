---
title: "Faster Stack Secrets"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-03-07T11:14:18Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

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
    - daniel-bradley

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - secrets
    - performance


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

# social:
#     twitter:
#     linkedin:

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Pulumi IaC's inbuilt support for keeping secrets secure in your stack file just got faster with enhanced performance when using Pulumi Cloud.

<!--more-->

Pulumi Cloud transmits and stores stack state securely, but Pulumi also encrypts individual _secrets_ within the stack for additional, fine-grained protection. Pulumi will also track transitive use of secrets to avoid the secret values being accidentally exposed - either within the stack state, in the CLI or in Pulumi Cloud.

When using Pulumi Cloud as your secrets provider, all encryption and decryption tasks are done server-side without transmitting the encryption key to the Pulumi program. Combined with Pulumi Cloud's user authorisation and SSO tools, this provides a robust framework for ensuring that only authorized parties can access sensitive information.

Performance is crucial for any developer tool as minimising wait times can maximise productivity and therefore we're always looking for how we can make gains without sacrificing security or reliability. Doing network requests for encryption and decryption operations can become slow as the number of secrets in a stack grow.

The first improvement we've made is to identify scenarios where there's no changes to any secrets within a stack. This allows us to completely bypass the work of re-encrypting all secrets when nothing has changed.

The second improvement is to reduce the number of network requests being made by batching the encryption work into a single batch encryption request to Pulumi Cloud instead of a separate encryption request for each secret.Depending on the number of secrets you have in stack state and your latency, you should see measurable impact of this change. For example, a stack with 25 secrets and a latency of 150ms would see a typical saving of 4 seconds per operation which updates the stack state.

Update to version 3.x of Pulumi IaC to get this improved performance with Pulumi Cloud secrets.
