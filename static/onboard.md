# Onboard to Pulumi

Get a new user from nothing to their first real Pulumi result in their own
cloud, built as a Pulumi project, with the work saved to a Pulumi Cloud account
they can claim afterward. Follow these steps in order. Where you have a shell,
do the work yourself; where you cannot run commands, give the user the exact
commands to run.

## 1. Confirm the CLI is available

Run `npx pulumi version` to confirm the CLI is reachable; it does not touch
Pulumi Cloud. On first run this downloads a current Pulumi CLI, so allow a
moment. If `npx` or Node.js is missing, install the CLI with the native
installer, then re-check. Do not continue until the version command succeeds.

    curl -fsSL https://get.pulumi.com | sh

## 2. Install the Pulumi skills

This prompt hands the real work to Pulumi's `pulumi-overview` skill.
Install the Pulumi skills now so the steps below have them:

    npx skills add pulumi/agent-skills/pulumi --skill '*'

Follow the `pulumi-overview` skill for the work below, not any stub `pulumi`
skill that shipped with the CLI. If the install does not succeed, do not stop
and do not ask the user to repair their machine. Continue with the Pulumi CLI
directly (`pulumi new`, `pulumi up`, and each command's `--help`), which is
enough to reach a first result.

## 3. Ask what the user wants to do

Default to a template — it is the surest route to a clean first result. Walk
the user through three choices, in this order, and do not guess any of them
silently:

1. Cloud: AWS, Azure, or GCP.
2. What to build. Lead with the minimal starter; offer the richer
   architectures after it:
   - Minimal starter (recommended) — the quickest way to see Pulumi work: a
     single-resource project (a storage bucket on AWS and GCP, a storage
     account on Azure).
   - Static website
   - Serverless app
   - Container service
3. Language: TypeScript, Python, Go, C#, YAML, or HCL. Java is available only
   for the minimal starter — offer it only if the user asks, never for an
   architecture template.

The template name is the minimal starter `<cloud>-<language>` (for example,
`aws-typescript`) or an architecture `<use-case>-<cloud>-<language>` where
`<use-case>` is `static-website`, `serverless`, or `container` (for example,
`static-website-aws-typescript`), all from github.com/pulumi/templates. Confirm
the chosen template resolves before continuing; if a combination is missing,
offer a neighboring one rather than stopping.

If the user would rather describe their own infrastructure than pick a
template, take that custom path instead: ask which cloud (AWS, Azure, GCP, or
another provider) and what they want to build. Do not push a template on a user
who has asked to build something specific.

If the user wants to migrate existing infrastructure code from Terraform,
CloudFormation, CDK, ARM, or Bicep, install the migration skills before
continuing:

    npx skills add pulumi/agent-skills/migration --skill '*'

If the migration skill install does not succeed, continue with
`pulumi-overview` and the Pulumi CLI rather than stopping.

## 4. Ask how to authenticate to the cloud

Pulumi creates resources in the user's own cloud account, with credentials
separate from Pulumi Cloud. Ask the user whether they already have credentials
for the target cloud and how they are set up, since it varies: a named profile,
environment variables, an SSO session, authenticated CLI, or a service account key. If they have
more than one, ask which to use; if they have none, help them set up
credentials for that provider. Ask before using credentials rather than
detecting and choosing them yourself.

## 5. Build the first result as a project

Follow the `pulumi-overview` skill from step 2. Fill in any remaining specifics
for the path the user chose:

- Template: scaffold with the resolved name — the minimal starter
  `pulumi new <cloud>-<language>` (for example, `pulumi new aws-typescript`) or
  an architecture `pulumi new <use-case>-<cloud>-<language>` (for example,
  `pulumi new static-website-gcp-python`). This produces a complete,
  working project — the template is the result, so do not add resources unless
  the user asks. Walk the user through what it creates.
- Custom: confirm the language (TypeScript, Python, Go, C#, Java, YAML, or
  HCL), then use `pulumi-overview`, Level 2. Scaffold with
  `pulumi new <cloud>-<language>`, then add the resources they asked for,
  whether that is one or several. Keep it minimal if they only want one.
- Migration: hand it to `pulumi-overview`, which covers migrating from
  Terraform, CloudFormation, CDK, ARM, or Bicep and routes it from there. Point
  it at where the existing code lives and let it drive.

Do not use `pulumi do` in this onboarding flow. Everything runs as a real
Pulumi project with state, so even a single resource is a small project. Always
run `preview` before `up`, and confirm with the user before creating anything.

## 6. Save the work: surface the claim link

The first time Pulumi contacts Pulumi Cloud in an agent context without saved
credentials, it provisions a free ephemeral agent account and prints a claim
block to stderr. The block carries a claim URL, how long the account stays
usable, and an instruction to pass along. Read those values from what the CLI
printed rather than assuming them.

Surface the claim URL to the user right after the first success, framed as
saving their work: claiming transfers the project, stack, and state to their
account and unlocks the rest of Pulumi Cloud, including Neo. Relay how long they
have from the block, and tell them to claim after you finish, since claiming
locks the organization during the claim process. If you are working on behalf
of the user rather than beside them, relay the link in your response.

## 7. Point to the next step

Ask the user what they want to do next. Useful directions are more resources in
the project, credentials and secrets in ESC (`pulumi-overview` Level 3), or the
provider catalog at pulumi.com/registry.
