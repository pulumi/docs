---
title: Data handling
title_tag: Neo data handling and model provenance | Pulumi Neo
h1: Neo data handling
meta_desc: Which models power Pulumi Neo, what data Neo can access, how prompts and task history are handled, and how secret values are redacted.
menu:
    ai:
        name: Data handling
        parent: ai-neo
        identifier: ai-data-handling
        weight: 13
---

This page collects, in one place, what's published about the models behind Pulumi Neo and how Neo handles the data it touches while it works. For the full breakdown of what Neo can access and act on within your organization, see the [permissions model](/docs/ai/neo/permissions/).

## Which models power Neo

Neo is Pulumi's own infrastructure agent, powered by Anthropic's Claude family of models, accessed through Amazon Bedrock rather than directly through Anthropic. Pulumi selects and updates the underlying model as the Claude family evolves; a specific model version isn't a permanent commitment, so treat "the Claude family via Amazon Bedrock" as the durable fact and specific version numbers announced on the [Pulumi blog](https://www.pulumi.com/blog/) as a point-in-time detail.

## What data Neo can access

Neo only sees what the invoking person or automation is authorized to see. Every Neo task runs under the RBAC permissions of the user or token that started it, scoped to the organization, projects, and stacks that identity can already reach. Neo doesn't have a standing credential or elevated access of its own. See the [permissions model](/docs/ai/neo/permissions/) for the full detail on scoping, MCP integration credentials, and how Neo interacts with your version control and cloud provider connections.

## How prompts, completions, and task history are handled

Because Neo's models run through Amazon Bedrock, Bedrock itself does not retain the prompts sent to it or the completions it returns. A Neo task's runtime session is torn down once it goes idle; the next turn in that task rebuilds its context from Pulumi's own stored, redacted task history rather than from anything held open in the model provider's infrastructure.

That stored history is also where Pulumi's own redaction runs. Task events are scanned for credential-shaped patterns before they're written to storage, and detected values are replaced with `[REDACTED]` so they never appear in task history, shared task views, or the Slack and pull request output Neo produces. See [handling of secret values](/docs/ai/neo/permissions/#handling-of-secret-values) in the permissions model for the specifics, including why that scan is defense in depth rather than a guarantee.

## Open questions we're tracking

Some questions we regularly hear from teams evaluating Neo aren't yet answered in public documentation, and we're not going to guess at answers here. If your organization needs a committed answer to any of the following ahead of what's published, contact your Pulumi account team:

- Whether IaC source code, stack state, resource metadata, prompts, or task transcripts are used to train or fine-tune the underlying models.
- How long Neo task transcripts and history are retained.
- Whether customers are notified in advance of a change to the underlying model.

## Learn more

- [Neo permissions model](/docs/ai/neo/permissions/)
- [Pulumi security](/security/)
- [Pulumi privacy policy](/privacy/)
