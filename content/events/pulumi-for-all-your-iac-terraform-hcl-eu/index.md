---
# The EMEA sitting of this workshop used to be its own event page. It's now a
# session on the one event page, so this redirects to that session's tab rather
# than dropping people on the Americas date they didn't ask for.
#
# `redirect_to` rather than an `aliases:` entry on the surviving page: a Hugo
# alias can only point at a bare permalink, and scripts/translate-redirects.js
# turns any zero-delay meta refresh into a real S3 301 — fragment and all.
title: "Pulumi for All Your IaC: Including Terraform and HCL (EMEA)"
redirect_to: /events/pulumi-for-all-your-iac-terraform-hcl/#session-emea

# Keep it out of the events list, the homepage row, and the RSS feed: it's a
# redirect, not an event.
unlisted: true
---
