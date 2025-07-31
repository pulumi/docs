---
title: "Introducing Approvals in Pulumi ESC"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-08-04T09:00:00-03:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Approvals enables effective change management by bringing governance and oversight directly into their environment configuration workflows.


# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - pablo-terradillos
    - claire-gaestel

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - esc


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

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Did you know that **80% of unplanned outages aren’t caused by hardware failures or cyberattacks, but by the very changes we make to improve our systems?**

Pulumi ESC already enables safer change management with [our innovative versioning capability](https://www.youtube.com/watch?v=HQN5KOY4asE) which **allows users to track and roll back environment revisions.**

Building on this foundation, we’re excited to announce the release of [**Approvals** in Pulumi ESC](/docs/esc/administration/approvals/)—a new feature that enables organizations to **bring governance and oversight directly into their environment configuration workflows.**

With Approvals, teams can require explicit review and sign-off before applying changes to ESC-managed environments, bringing the same rigor to configuration as they already have with infrastructure-as-code and application development.

---

## Enforce Change Management Without Slowing Teams Down

Pulumi ESC helps teams manage environment configurations—such as secrets and application settings—across services and environments, from development through production.

In fast-moving teams, managing these settings safely and consistently is critical. But as the number of contributors grows, so does the risk of accidental or unreviewed changes making it into critical environments.

That’s where Approvals come in.

With Approvals, any proposed change to an ESC environment—whether through the Pulumi Console or CLI—must go through a structured review process before it’s applied. Similar to submitting a Pull Request, contributors can propose changes that are reviewed and approved by designated team members.

This gives you a native, consistent workflow for gating configuration updates without needing external tools or manual oversight.

---

## How It Works

To get started, navigate to your environment’s **Settings → Approval Rulesets**, where you can define approval requirements such as:

- Number of required reviewers  
- Specific teams or individuals allowed to approve  
- Whether self-approval is permitted  
- Whether changes require reapproval if modified

![Pulumi Ruleset configuration](approvals-ruleset.png)

Once a ruleset is enabled, any environment update must go through a **change request** workflow. Instead of directly saving changes, contributors create a draft, which then must be reviewed and approved before being applied.

![Pulumi ESC Approvals Workflows](approvals-workflow.png)

Changes pending approval are clearly visible to your team, and reviewers can inspect the diff, leave feedback, or revise the request before approving.

Approvals are also fully supported in the [Pulumi ESC CLI](https://github.com/pulumi/esc), using the `--draft` flag:

```sh
$ esc env set --draft org/project/env FEATURE_X_ENABLED true
```

## Built for Collaboration and Compliance

Whether you’re enforcing separation of duties, complying with industry standards or regulations, or simply want better visibility into changes, Approvals helps bring process to how configuration flows through your systems.

It also integrates seamlessly into existing workflows—no need to reinvent how teams work. Just add governance where it matters most.

## What’s Next

Approvals in ESC is just the beginning. We're exploring how approval workflows can be extended to other areas of the Pulumi ecosystem to provide a consistent, governed experience across the entire software delivery lifecycle.

Our goal is to empower teams to move fast while staying secure and compliant—no matter where or how changes happen. We’re excited about what’s ahead and look forward to building it together with your feedback.

Happy building!
