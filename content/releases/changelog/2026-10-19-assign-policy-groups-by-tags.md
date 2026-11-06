---
title: "Assign policy groups by stack and account tags"
date: 2026-10-19
meta_desc: Policy groups can now add stacks and cloud accounts by tag, so new infrastructure picks up the right policy coverage automatically as it's created.
authors:
    - christian-nunciato
---

Policy groups can now match stacks and cloud accounts by tag, instead of only by explicit assignment. Add a tag rule to a policy group, and any stack or account that carries a matching tag is covered automatically — including new ones created later, which pick up the right policies the moment they appear.

This keeps policy coverage from drifting as your environment grows: tag your infrastructure the way you already do, and the policies follow.

You can define tag rules in the Pulumi Cloud console or from the CLI with `pulumi policy group new` and `pulumi policy group edit`. To learn more, read the [announcement post](/blog/assign-policy-groups-by-tags/).
