---
title: Best Practices
linktitle: Best Practices
meta_desc: An index of Pulumi's best-practices guidance across infrastructure as code, ESC, IDP, and policy, in one place.
h1: Best Practices
description: <p>Pulumi's best-practices guidance lives close to the capability it applies to. This page indexes it in one place, with a one-line pointer for when each pattern applies, so you and your AI assistant land on Pulumi's own guidance instead of generic advice from the open web.</p>
---

Pulumi publishes best-practices guidance throughout its documentation, close to the
capability each pattern applies to. That keeps each guide grounded in real APIs and
concrete examples, but it also means the guidance is easy to miss if you do not already
know which section to look in. This page collects it in one place.

Each entry below is a link to the authoritative guide, with a short note on when to
reach for it. This page does not duplicate that guidance or restate it in different
words; it exists so you (and any AI assistant working on your behalf) can find
Pulumi's own recommendations quickly, rather than falling back on generic
infrastructure-as-code advice that may not apply to Pulumi.

## Organizing code and projects

- [Organizing projects and stacks](/docs/iac/guides/basics/organizing-projects-stacks/) —
  reach for this when deciding how to split infrastructure across Pulumi projects and
  stacks as a codebase and a team grow.
- [Components](/docs/iac/concepts/components/) — reach for this when a group of
  resources is provisioned together repeatedly and deserves a single, reusable
  abstraction.
- [Building and extending Pulumi](/docs/iac/guides/building-extending/) — reach for
  this when you are packaging components, providers, or templates for others on your
  team, or for the wider community, to reuse.

## Secrets and configuration

- [Secrets handling](/docs/iac/concepts/secrets/) — reach for this when deciding how
  sensitive values flow through a Pulumi program and where they are stored at rest.
- [Configuration](/docs/iac/concepts/config/) — reach for this when structuring
  per-stack settings so the same program can run safely against dev, staging, and
  production.
- [ESC secrets-rotation best practices](/docs/esc/operations/rotation/best-practices/) —
  reach for this when defining who rotates a credential, how often, and how a rotation
  propagates to every environment that consumes it.
- [ESC environment composition patterns](/docs/esc/guides/environment-composition-patterns/) —
  reach for this when multiple environments need to share common configuration without
  duplicating it.

## Testing and delivery

- [Testing](/docs/iac/guides/testing/) — reach for this when deciding which layer to
  test at: unit tests against your program's logic, or integration tests against real
  provisioned resources.
- [Automation API](/docs/iac/concepts/automation-api/) — reach for this when a
  workflow needs to drive Pulumi programmatically instead of through the CLI, such as
  a self-service provisioning tool or a custom CI/CD pipeline.

## Governance and policy

- [Discovery & governance: policy get started](/docs/insights/policy/get-started/) —
  reach for this when you are ready to enforce organizational guardrails on
  infrastructure as code with Policy as Code.
- [Discovery & governance: policy CI/CD integration](/docs/insights/policy/ci-cd/) —
  reach for this when policy checks need to run automatically in a pull request or a
  deployment pipeline, before infrastructure changes are applied.

## Internal developer platforms

- [IDP best practices: the four factors](/docs/idp/guides/best-practices/) — reach for
  this when designing a platform team's paved paths: the templates, components,
  environments, and policies that give application teams safe self-service.
- [IDP patterns](/docs/idp/guides/best-practices/#patterns) — reach for this when you
  need a named, proven shape for a common platform problem, such as one ESC
  environment per service or team, or enforcing cost controls through constrained
  component inputs.

## Operating Pulumi at scale

- [Setting up for success](/docs/administration/get-started/setting-up-for-success/) —
  reach for this when standing up Pulumi for an organization for the first time and
  deciding how teams, projects, and access should be structured from day one.
- [Security hardening for self-hosted deployments](/docs/administration/self-hosting/operations/security-hardening/) —
  reach for this when running Pulumi's self-hosted deployment and hardening it for
  production use.

## A note on scope

This page indexes best-practices content that already exists elsewhere in Pulumi's
docs; it intentionally does not introduce new normative guidance of its own; that
guidance belongs in the guide for the capability it concerns, not duplicated here.
Its placement in the docs navigation is a separate, open question: see
[the tracking issue](https://github.com/pulumi/docs/issues/16455) for the discussion.
