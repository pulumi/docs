---
title: "What a Good Infrastructure Pull Request Looks Like Now"
date: 2026-10-29
draft: false
meta_desc: A reviewable infrastructure pull request attaches preview output, states its blast radius, and hides no config drift, whoever wrote it.
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - infrastructure-as-code
    - ci-cd
    - ai-agents
    - best-practices
    - testing
category: best-practices
schema_type: auto
faq_schema: true
---

A good infrastructure pull request gives the reviewer four things: a diff they can read, a preview of what will change in the cloud, tests where tests are possible, and a description they can act on without reconstructing the context themselves. That was true when every pull request came from a person, and it is true now.

What has changed is the volume. A [2025 study of agent-authored pull requests](https://arxiv.org/abs/2507.15003) (Li, Zhang, and Hassan) collected over 456,000 pull requests from five coding agents across 61,000 repositories, and found that although agents often outperform humans in speed, their pull requests are accepted less frequently. One developer in the dataset submitted as many pull requests in three days as they had in three years. Any gap in a pull request now reaches a reviewer faster and more often, and reviewer attention is the input that does not scale.

<!--more-->

This post describes what to put in an infrastructure pull request so that a reviewer can approve it, or reject it, quickly and with confidence.

## Why is an infrastructure diff harder to review than application code?

An application diff shows intent. You read the changed lines and reason about what the program will do. An infrastructure diff shows a request, and the consequence lives in a cloud provider that the diff does not display. A one-line change to a property can force a stateful resource to be replaced. A renamed resource can read as a rename in the code and as a delete plus a create in the cloud.

The stakes are well documented. Google's SRE team reports that [roughly 70% of outages are due to changes in a live system](https://sre.google/sre-book/introduction/). Infrastructure changes are changes to a live system by definition, so the pull request is the last cheap place to catch the problem.

## What should every infrastructure pull request attach? The preview output

Attach the output of `pulumi preview`. The preview is the only artifact that answers the reviewer's first question: what will this do to real resources?

Pulumi's [continuous delivery guidance](/docs/iac/operations/continuous-delivery/) is direct about this: a CI/CD pipeline for infrastructure must run a preview on every pull request. The recommended flow has the pipeline run `pulumi preview` when the pull request opens and post the summary of proposed changes for review, and re-run the preview after each update to the branch. That last part matters more than it looks. A preview pasted into the description on Monday says nothing about the commit pushed on Tuesday. A stale preview is worse than none, because it looks like evidence.

A few details make the attachment useful:

- Use `pulumi preview --diff` for a rich diff of the overall change. It is easier to scan than the default view when a stack has many resources.
- Let the pipeline post the result. The [Pulumi GitHub App](/docs/integrations/version-control/github-app/) displays the results of stack update previews in pull requests, so the reviewer does not depend on the author remembering to paste it.
- Consider pinning the apply to the preview. [Update plans](/docs/iac/operations/stack-management/update-plans/), currently an experimental feature, let you save the operations a preview proposed with `--save-plan` and then run `pulumi up --plan=plan.json`, which constrains the update to the operations in the plan.

## How do you state the blast radius in plain words?

The preview is complete, but it is not a summary. Reviewers skim, so the author should write down what the preview means. A useful blast radius statement is short and specific:

- How many resources are created, updated, replaced, and deleted.
- Which of those are stateful (databases, buckets, volumes, queues), and whether any is replaced.
- Which stacks and environments the change touches.
- What protects the important resources. The [resource options](/docs/iac/concepts/resources/options/) are the vocabulary here: `protect` prevents accidental deletion, `deleteBeforeReplace` deletes the existing resource before creating its replacement, `replaceOnChanges` treats changes to specified properties as forcing a replacement, and `retainOnDelete` retains the resource in the cloud provider when Pulumi deletes it.

If an author cannot fill in that list, the pull request is not ready for review, and the author, human or agent, has learned something useful.

Size belongs here too. Google's engineering practices say that [the right size for a change is one self-contained change](https://google.github.io/eng-practices/review/developer/small-cls.html), that reviewers may reject a change outright for being too large, and that smaller changes are simpler to roll back. Rollback is the property infrastructure teams care about most. A pull request that mixes a network refactor, a new database, and a dependency bump gives the reviewer three decisions and gives the on-call engineer no clean revert.

## How do you keep config drift from slipping in silently?

Silent drift enters an infrastructure pull request in three ways.

**Stack configuration changes.** Stack configuration lives in files named `Pulumi.<stack-name>.yaml`, and the [configuration docs](/docs/iac/concepts/config/) say these files should be committed to version control. That makes config edits part of the diff, which is good, but a reviewer reading the code changes first can miss a changed instance size or region in a YAML file. The description should name every config value that changed and why.

**Options that mute the diff.** The `ignoreChanges` option ignores changes to specified properties during a diff. Adding it can be legitimate, and it also makes the preview quieter. A new `ignoreChanges` entry deserves a sentence of justification, because it removes information from the very output the reviewer relies on.

**Differences between state and reality.** If someone changed a resource in the console, the preview compares your code against stale state. Run `pulumi preview --refresh` to refresh the state of the stack's resources before previewing, or `pulumi refresh --preview-only` to see the drift without applying it. Pulumi Cloud treats a [preview of a refresh as a drift detection run](https://www.pulumi.com/docs/deployments/concepts/drift/).

There is a related check for refactoring pull requests. If the description claims "no infrastructure change," make the pipeline enforce it: `--expect-no-changes` returns an error if any changes are proposed by the preview. A claim that a machine can verify should be verified by the machine.

## Which tests belong in an infrastructure pull request?

The [testing guide](/docs/iac/guides/testing/) separates two kinds. Unit tests are fast in-memory tests that mock all external calls. Integration tests deploy ephemeral infrastructure and run external tests against it. Unit tests are cheap enough to run on every push, and they are the right place to assert rules such as "every bucket has encryption enabled" or "no security group opens port 22 to the world."

For changes whose risk is in how pieces fit together, [review stacks](/docs/deployments/concepts/review-stacks/) go further. A review stack is created automatically when a pull request is opened, updated on each new commit, and destroyed when the pull request is merged or closed, so the reviewer can look at a running environment instead of imagining one.

Not every change can be tested this way, and that is acceptable. What the reviewer needs is honesty. Write "unit tests pass; not deployed to a review stack because it needs the production VPC peering" and the reviewer knows where to spend their attention. Silence about testing reads as "tested," and that is how gaps get approved.

## How do you write the description for a reviewer who was not there?

Google's guidance on change descriptions applies without modification: "Fix bug" is an inadequate description, because it leaves out which bug and what you did to fix it. Reading the code may reveal what the software is doing, but it may not reveal why the change exists, and the description becomes a permanent part of version control history. An infrastructure pull request adds two more questions: how will we know it worked, and how do we undo it?

Here is a template that covers the ground:

```markdown
## What and why
One paragraph. The problem, and the change that addresses it.

## Preview
Link to the CI preview for the latest commit, or paste the summary:
2 to create, 1 to update, 0 to replace, 0 to delete.

## Blast radius
- Stacks: dev, staging
- Stateful resources touched: none
- Config changed: instanceType in Pulumi.staging.yaml (t3.small to t3.medium)
- New ignoreChanges or protect changes: none

## Testing
What ran, what did not, and why.

## Verification and rollback
How to confirm it worked after apply. How to revert if it did not.
```

None of this is exotic. It is the checklist that careful teams already follow, written down once so nobody has to remember it at 5 p.m. on a Friday.

## Does the standard change when an agent opens the pull request?

The checklist does not change. The pressure on it does, in two ways.

First, fluent prose is cheap now. An agent can produce a confident, well-organized description for any diff, including a diff that does something other than what the description says. So the description should be checked against the preview, and the preview is the source of truth. If the text says "adds a read replica" and the preview shows a replacement of the primary, the preview wins.

Second, the reviewer may be an agent too. An agent reviewing a pull request needs the same artifacts a person does: the diff, the preview, the blast radius, the test results. A pull request that gives a human reviewer everything needed to decide also gives an automated reviewer everything it needs, and a pull request that makes a human dig will make an automated reviewer guess.

For the author, whether person or agent, the practical consequence is to build the checklist into the pipeline instead of the habit. Preview on every push, posted as a comment. A description template the repository enforces. `--expect-no-changes` on refactors. Then the standard holds on a busy Tuesday, with any author.

## The short checklist

Before requesting review on an infrastructure pull request:

1. Preview output is attached and was generated from the latest commit.
2. Blast radius is stated: counts, stateful resources, stacks affected.
3. Config changes and new `ignoreChanges` entries are named and justified.
4. Drift was checked with `pulumi preview --refresh` when the stack may have changed out of band.
5. Tests are listed, along with what was not tested and why.
6. The description explains why, how to verify, and how to roll back.
7. The change is one self-contained change.

A pull request that meets these seven is quick to review for anyone, and quick review is what keeps infrastructure changes moving at the pace the rest of engineering expects. To set up the preview-on-every-pull-request workflow, start with the [continuous delivery guide](/docs/iac/operations/continuous-delivery/).
