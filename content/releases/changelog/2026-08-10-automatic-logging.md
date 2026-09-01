---
title: "Automatic logging for faster, more secure debugging"
date: 2026-08-10
meta_desc: Pulumi now writes an encrypted log file for every operation automatically, so you can securely share exactly what happened with the Pulumi team for debugging.
authors:
    - christian-nunciato
---

Pulumi now writes a log file for every operation automatically, so when something goes wrong you no longer have to reproduce it just to capture logs for the Pulumi team. The details are already on disk, waiting for you.

Those logs are encrypted with your stack's secret manager and stored under `$PULUMI_HOME/logs`, and they're rotated out after seven days — or once they reach 500 MB — so they never fill up your disk. When you need a hand, [`pulumi logs share`](/docs/iac/cli/commands/pulumi_logs_share/) securely shares them with us, and [`pulumi logs decrypt`](/docs/iac/cli/commands/pulumi_logs_decrypt/) lets you inspect them yourself.

Automatic logging is available as of v3.254.0. Read the [announcement post](/blog/automatic-logging/) to learn more.
