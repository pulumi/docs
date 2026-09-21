# Onboard to Pulumi

Get a new user from nothing to their first real Pulumi result in their own
cloud, built as a Pulumi project and saved to a Pulumi Cloud account they can
claim afterward. Follow these steps in order. Where you have a shell, do the
work yourself; otherwise give the user the exact commands to run. Explain each
key Pulumi concept briefly the first time it comes up, so the user learns as
they go.

## 1. Install the CLI and put it on the PATH

The user must end up able to run `pulumi` in a brand-new shell — not only in
your session via `npx`, a one-off `export`, or the full path. So installing is
not enough: on macOS or Linux you must also actively offer to put it on their
PATH for good (see below), in this step, before moving on — don't leave it
session-only and let them discover later that `pulumi` isn't found. First check
whether it is already installed: `pulumi version` (this does not touch Pulumi
Cloud). If that works, continue.

If `pulumi` is not found, install it for the user's platform:

- macOS or Linux — the install script (installs to `$HOME/.pulumi/bin`). It
  does not modify the PATH, so set that up next:

      curl -fsSL https://get.pulumi.com | sh

- Windows — the PowerShell install script (installs to
  `%USERPROFILE%\.pulumi\bin`). It adds `pulumi` to the user's PATH for you and
  updates the current session, so there's nothing more to do — a newly opened
  shell may just need a restart to see it:

      iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))

On macOS or Linux, put the install directory (confirm it from the installer's
output) on the PATH:

- For now: export it for the session — `export PATH="$HOME/.pulumi/bin:$PATH"`
  — or use the full path.
- Permanently (do not skip, and do not wait to be asked): this is what makes
  `pulumi` available in the user's future shells — without it, the command won't
  be found the next time they open a terminal. Say that plainly, then offer to
  amend their PATH for them: on their go-ahead, add the install directory to the
  right shell config. Never edit it automatically — only with their go-ahead.
  Detect the shell (`$SHELL` names the login shell) and use its own target and
  syntax rather than assuming zsh:
  - zsh: add `export PATH="$HOME/.pulumi/bin:$PATH"` to `~/.zshrc`.
  - bash: the same line in `~/.bashrc` (Linux) or `~/.bash_profile` (macOS).
  - fish: run `fish_add_path $HOME/.pulumi/bin`.

  If they'd rather do it themselves, quote the exact command for their shell so
  they can run it later, and name the install location (`$HOME/.pulumi/bin`).

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
3. Language. Make clear when you ask that Pulumi supports general-purpose
   programming languages — TypeScript, Python, Go, and C# — and configuration
   languages — YAML and HashiCorp Configuration Language (HCL). If the UX fits
   only a few choices, offer TypeScript, Python, and a cloud-appropriate third
   (Go for AWS and GCP, C# for Azure), and make the rest available on request.
   Java is available only for the minimal starter — offer it only if the user
   asks, never for an architecture template.

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

Once the project is scaffolded, tell the user the exact directory it lives in
(an absolute path) and invite them to open it in their editor of choice to look
through the code — it's theirs to read and change.

Teach as you build — as each concept first appears, explain it to the user in a
sentence or two, then move on. Each time, show the user its "Learn more" link so
they can open the page while you work — present the URL to them in your reply;
don't just read it yourself:

- Project: the user's program — a collection of related cloud resources defined
  in code (the files `pulumi new` just created). Learn more:
  pulumi.com/docs/iac/concepts/projects/
- Stack: `pulumi new` also creates a stack, an isolated, independently
  configurable instance of that program (here, `dev`); a project can have as
  many as you need, such as dev, staging, and production. Learn more:
  pulumi.com/docs/iac/concepts/stacks/
- Configuration: per-stack key-value settings saved in `Pulumi.<stack>.yaml`,
  so stacks can differ without code changes. Learn more:
  pulumi.com/docs/iac/concepts/config/
- Preview: the change plan `pulumi preview` (and the prompt before `pulumi up`)
  shows before anything is created — nothing changes until the user approves.
  Learn more: pulumi.com/docs/iac/cli/commands/pulumi_preview/
- Update: `pulumi up` applies that plan once confirmed, creating or changing
  only what differs from the current state. Learn more:
  pulumi.com/docs/iac/cli/commands/pulumi_up/

Do not use `pulumi do` in this onboarding flow. Everything runs as a real
Pulumi project with state, so even a single resource is a small project. Always
run `preview` before `up`, and confirm with the user before creating anything.

After a successful `up`, confirm it works and show the user — run a check built
from a stack output (`pulumi stack output <name>`) yourself, since your session
is already authenticated. Match it to what was deployed: open a served URL
(`open $(pulumi stack output url)` for a static site or serverless app), hit an
API endpoint with `curl`, or list what a resource created
(`aws s3 ls $(pulumi stack output bucketName)`). You can hand the user the same
command to run on their own, but only after the save-your-work step below: if
the work is in an unclaimed ephemeral account, `pulumi` won't run in their shell
until they claim it and log in; if they're already on their own account, they
just need `pulumi login`.

## 6. Save the work: surface the claim link (only if one was printed)

The claim flow happens only when the user had no saved Pulumi Cloud
credentials: the first time Pulumi contacts Pulumi Cloud it provisions a free
ephemeral account and prints a claim block to stderr — a claim URL and how long
the account stays usable. If the user was already logged in to their own
account, there is no claim block; skip this step, since the work is already in
their account. (If their shell just isn't logged in, `pulumi login` is all they
need.)

When a claim block is printed, read the URL and expiry from it rather than
assuming them, and surface the URL right after the first success as saving
their work: claiming transfers the project, stack, and state to their account
and unlocks the rest of Pulumi Cloud, including Neo. Relay how long they have,
and tell them to claim after you finish, since it briefly locks the
organization. If you're working on the user's behalf rather than beside them,
include the link in your response.

While the work sits in an unclaimed ephemeral account, only your session can
reach it — so surface this step before inviting the user to run any `pulumi`
command themselves, and warn them that `pulumi` in their own shell (`stack
output`, `preview`, `up`, `destroy`) will fail until they claim the account and
then run `pulumi login`.

## 7. Suggest the next steps

Don't just ask "what next" — actively encourage the user to keep going, in this
order of importance:

1. Save the work to a Pulumi Cloud account — the single most important next
   step. If the CLI printed a claim link (step 6), urge them to claim now,
   before it expires, to move the project, stack, and state into their account
   and unlock the rest of Pulumi Cloud, including Neo. If they were already on
   their own account, there's nothing to claim — just confirm they're logged in.
2. Open the project in their editor and look around. Pulumi is agent-friendly,
   but it pays to understand how a project fits together — encourage them to
   read the code, make a small change (add a resource from the catalog at
   pulumi.com/registry, or set config and secrets with ESC via `pulumi-overview`
   Level 3), and deploy it with `pulumi up` from the project directory — which
   works once they can run `pulumi` themselves (claim first if the work is in an
   ephemeral account, then `pulumi login`).
3. Tear it down when they're done. If you already ran `pulumi destroy`, say so.
   Otherwise remind them they can remove everything anytime — by asking you
   later or, once they can run `pulumi` themselves (claim if needed, then
   `pulumi login`), running `pulumi destroy` from the project directory
   (pulumi.com/docs/iac/cli/commands/pulumi_destroy/) — so a trial run doesn't
   leave billable resources behind. Offer to run it now if they were only
   experimenting, confirming first as with any create.

Always close by inviting them to keep exploring:

- Docs — learn more at pulumi.com/docs/
- Blog — news, deep dives, and how-tos at pulumi.com/blog/
- Dev Center — tutorials, templates, and examples at pulumi.com/dev/
