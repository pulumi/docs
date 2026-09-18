# Onboard to Pulumi

Get a new user from nothing to their first real Pulumi result in their own
cloud, built as a Pulumi project and saved to a Pulumi Cloud account they can
claim afterward. Follow these steps in order. Where you have a shell, do the
work yourself; otherwise give the user the exact commands to run. Explain each
key Pulumi concept briefly the first time it comes up, so the user learns as
they go.

## 1. Install the CLI and put it on the PATH

The user should be able to run `pulumi` now and in new shells, so onboarding
must leave a real CLI on their PATH — not just a per-session `npx` shim. First
check whether it is already installed: `pulumi version` (this does not touch
Pulumi Cloud). If that works, continue.

If `pulumi` is not found, install it for the user's platform:

- macOS or Linux — the install script, which installs to `$HOME/.pulumi/bin`
  but does not modify the PATH:

      curl -fsSL https://get.pulumi.com | sh

- Windows — prefer a package manager, which also puts `pulumi` on the PATH.
  Pass the non-interactive flags so the install runs unattended (the MSI
  installer is a GUI wizard and won't work in an agent session):
  `winget install pulumi --accept-package-agreements --accept-source-agreements`
  (winget ships with current Windows) or `choco install pulumi -y` (Chocolatey).
  If neither is available, run the PowerShell install script, which installs to
  `%USERPROFILE%\.pulumi\bin` and, like the macOS/Linux script, does not modify
  the PATH:

      iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))

When the install did not put `pulumi` on the PATH — the macOS/Linux script or
the Windows PowerShell script (confirm the install directory from the
installer's output) — a fresh shell won't find it yet. Put it on the PATH:

- For now: export it for the session — `export PATH="$HOME/.pulumi/bin:$PATH"`
  (macOS/Linux) or `$env:Path += ";$HOME\.pulumi\bin"` (PowerShell) — or use the
  full path.
- Permanently: offer to add that directory to the PATH — the user's shell
  profile on macOS/Linux, or their user PATH on Windows. Shells and profiles
  vary, so detect the user's shell (e.g. via `$SHELL`) and use the matching
  target and syntax rather than assuming zsh. Never edit it automatically —
  only with the user's go-ahead. If they decline or you can't write it, give
  them a copyable command that names the install location — for zsh:

      # The Pulumi CLI is installed at $HOME/.pulumi/bin
      echo 'export PATH="$HOME/.pulumi/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc

Only if no installer can run (say, a restricted environment) and Node is
available, fall back to `npx pulumi` for this session — but tell the user
plainly that `pulumi` won't be available in new shells until they install it
natively, and point them at the installers above. Whichever form you use, use
it for every `pulumi` command below, and don't continue until `pulumi version`
succeeds.

## 2. Install the Pulumi skills

This prompt hands the real work to Pulumi's `pulumi-overview` skill.
Install the Pulumi skills now so the steps below have them:

    npx skills add pulumi/agent-skills/pulumi --skill '*'

Follow the `pulumi-overview` skill for the work below, not any stub `pulumi`
skill that shipped with the CLI. If the install fails, don't stop or ask the
user to fix their machine — continue with the CLI directly (`pulumi new`,
`pulumi up`, each command's `--help`), which is enough to reach a first result.

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
`static-website-aws-typescript`). github.com/pulumi/templates is the source of
truth for what exists — always use it, and never `pulumi template list` or
Pulumi Cloud org templates, which the user may not have. `pulumi new` resolves
these bare names from that repo; if one is missing, offer a neighboring
template rather than stopping.

If the user would rather describe their own infrastructure than pick a
template, take that custom path: ask which cloud (AWS, Azure, GCP, or another
provider) and what to build. Don't push a template on someone who has asked to
build something specific.

If the user wants to migrate existing infrastructure code from Terraform,
CloudFormation, CDK, ARM, or Bicep, install the migration skills before
continuing:

    npx skills add pulumi/agent-skills/migration --skill '*'

If the migration skill install does not succeed, continue with
`pulumi-overview` and the Pulumi CLI rather than stopping.

## 4. Ask how to authenticate to the cloud

Pulumi deploys to the user's own cloud account, using credentials separate from
Pulumi Cloud. Ask how they authenticate to the target cloud — a named profile,
environment variables, an SSO session, an authenticated CLI, or a service
account key — and which to use if they have several. If they have none, help
them set some up. Always ask before using credentials rather than detecting and
choosing them yourself.

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
- Migration: point `pulumi-overview` at where the existing code lives and let
  it drive; it covers the source formats above and routes from there.

Teach as you build — when each concept first appears, explain it in a sentence
or two and share its docs link so the user can open the page while you work,
then move on:

- Project: the user's program — a collection of related cloud resources defined
  in code (the files `pulumi new` just created).
  pulumi.com/docs/iac/concepts/projects/
- Stack: `pulumi new` also creates a stack, an isolated, independently
  configurable instance of that program (here, `dev`); a project can have as
  many as you need, such as dev, staging, and production.
  pulumi.com/docs/iac/concepts/stacks/
- Configuration: per-stack key-value settings saved in `Pulumi.<stack>.yaml`,
  so stacks can differ without code changes.
  pulumi.com/docs/iac/concepts/config/
- Preview: the change plan `pulumi preview` (and the prompt before `pulumi up`)
  shows before anything is created — nothing changes until the user approves.
  pulumi.com/docs/iac/cli/commands/pulumi_preview/
- Update: `pulumi up` applies that plan once confirmed, creating or changing
  only what differs from the current state.
  pulumi.com/docs/iac/cli/commands/pulumi_up/

Do not use `pulumi do` in this onboarding flow. Everything runs as a real
Pulumi project with state, so even a single resource is a small project. Always
run `preview` before `up`, and confirm with the user before creating anything.

## 6. Save the work: surface the claim link

The first time Pulumi contacts Pulumi Cloud without saved credentials, it
provisions a free ephemeral account and prints a claim block to stderr — a
claim URL and how long the account stays usable. Read those from what the CLI
printed rather than assuming them.

Surface the claim URL right after the first success, framed as saving their
work: claiming transfers the project, stack, and state to their account and
unlocks the rest of Pulumi Cloud, including Neo. Relay how long they have, and
tell them to claim after you finish, since it briefly locks the organization.
If you're working on the user's behalf rather than beside them, include the
link in your response.

## 7. Point to the next step

Ask the user what they want to do next. Useful directions are more resources in
the project, credentials and secrets in ESC (`pulumi-overview` Level 3), or the
provider catalog at pulumi.com/registry.

Also make sure they can remove what you created, so trying Pulumi out doesn't
leave billable cloud resources behind. If they want to keep the work, they
claim it (step 6) and can tear it down later from their own account with
`pulumi destroy`. If they were only experimenting, offer to run `pulumi
destroy` now — it deletes all the resources in the stack
(pulumi.com/docs/iac/cli/commands/pulumi_destroy/) — confirming before you
destroy, as with any create.
