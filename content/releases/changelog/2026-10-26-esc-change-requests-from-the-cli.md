---
title: "Manage Pulumi ESC change requests from the CLI"
date: 2026-10-26
meta_desc: The new pulumi env change-request commands let you review, approve, and apply Pulumi ESC change requests without leaving the terminal.
authors:
    - christian-nunciato
---

You can now work with Pulumi ESC [change requests](/docs/esc/concepts/approvals/) directly from the CLI. The new [`pulumi env change-request`](/docs/iac/cli/commands/pulumi_env_change-request/) commands let you open a change request, review its diff, comment, approve or unapprove, and apply it — all without leaving your terminal.

```bash
# List open change requests for an environment
pulumi env change-request list myorg/myproject/myenv

# Review the proposed diff
pulumi env change-request diff <id>

# Approve and apply it
pulumi env change-request approve <id>
pulumi env change-request apply <id>
```

To learn more, read the [announcement post](/blog/esc-change-requests-cli/) or the [`pulumi env change-request` documentation](/docs/iac/cli/commands/pulumi_env_change-request/).
