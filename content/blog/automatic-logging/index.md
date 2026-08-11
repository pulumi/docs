---
title: "Automatic Logging for Faster, Secure Debugging"
date: 2026-08-10
draft: false
meta_desc: "Pulumi now writes encrypted logs for every operation automatically"
feature_image: feature.png
authors:
    - thomas-gummerer
tags:
    - logging
    - observability
    - features
category: product
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        When Pulumi hits an error, the fastest fix needs a log. Usually you had to reproduce the error by hand to capture one. Pulumi v3.254.0 changes that: every operation is now logged automatically, encrypted on disk, and safe to share.

        Here's how it works.
    linkedin: |
        You hit an unexpected Pulumi error. To debug it, someone needs the logs, but logging wasn't on, so now you're re-running the command trying to reproduce it. Sometimes it won't reproduce. Sometimes the state Pulumi was in is already gone.

        And even when you do capture a log, there's no safe way to hand it over. These files still contain secrets.

        Pulumi v3.254.0 fixes both. Every operation is now logged to an encrypted file automatically, and a new command re-encrypts and redacts it so you can share it over any channel, even a public GitHub issue.

        We wrote up how it works.
    bluesky: |
        Debugging a Pulumi error usually meant reproducing it by hand just to capture a log, then finding a safe way to share a file full of secrets. Pulumi v3.254.0 makes logs automatic and encrypted, safe to share even on a public GitHub issue.

        Here's what changed.
---

Pulumi v3.254.0 introduces automatic logging: every operation is logged in an encrypted log file that can optionally be shared with the Pulumi team for inspection. No more re-running commands just to get logs to the Pulumi team for debugging; instead you can share existing logs securely.

<!--more-->

You might have been in a situation where pulumi hit an error for an unexpected reason, or did something that was not quite right. Currently the process for trying to resolve that is to try and reproduce the error, ideally now with logging enabled. Sometimes the error doesn't reproduce, or the state pulumi was in at the time of the error doesn't exist anymore. And even if the issue reproduces it's a bit of a hassle to do all this again, just to get logs to Pulumi employees who can do something with them. There's also no great mechanism to send the potentially sensitive log file.

## How it works

From pulumi v3.254.0 onward, we automatically produce log files for every operation and store them in `$PULUMI_HOME/logs`. These log files are encrypted on disk, using the relevant stack's secret manager, whenever it is available, as they still contain secrets at this point. The final file consists of gzip'd chunks that are encrypted using AES256-GCM.  Log files are gzip'd when no secrets manager is available, as no secrets from property values can be in the log at that point.

Note that the logs are rotated out after 7 days, or after the log directory has reached 500 MB, removing the oldest logs first. This way logs will never fill up your disk, but will still be available after running pulumi commands. These defaults can be overridden with the `PULUMI_LOG_ROTATION_MAX_AGE_DAYS` and `PULUMI_LOG_ROTATION_MAX_TOTAL_MB` environment variables.

Locally these logs can be decrypted using [`pulumi logs decrypt`](/docs/iac/cli/commands/pulumi_logs_decrypt/). For this to work the same stack's secret manager as was used for the command needs to be available.

## Sharing logs

Previously there was no good way to securely share the logs with us. Users were always forced to find a way to send the logs to us on their own. With the latest pulumi version, we introduce the [`pulumi logs share`](/docs/iac/cli/commands/pulumi_logs_share/) command. This will automatically create a key, safely stored on the server side, and re-encrypt the log with that key, redacting all the secrets by default.

This key can then be accessed by Pulumi employees and Pulumi employees only via an internal tool to decrypt the log. Again we encrypt the log using AES256-GCM. Given this encryption the log can be shared over unsafe channels, and still be secure, even if it's posted on a GitHub issue.

And while we strive to keep the Pulumi experience as issue free as possible, this should drastically simplify the debugging experience when it is still necessary.
