---
title: "GitOps Best Practices I Wish I Had Known Before"
date: 2026-02-08
draft: false

meta_desc: |
  Discover essential GitOps best practices I wish I had known earlier. Avoid common pitfalls, bridge IaC with GitOps, and streamline your Kubernetes deployments.

meta_image: meta.png

authors:
- engin-diri

tags:
- gitops
- kubernetes
- best-practices
- argocd
- devops

social:
  twitter: |
    GitOps Best Practices I Wish I Had Known Before — hard-won lessons from production, the IaC-to-GitOps bridge, and why pragmatism beats dogma every time.
    <link>
  linkedin: |
    GitOps Best Practices I Wish I Had Known Before

    Getting started with GitOps? It can feel like you're trying to herd cats through a YAML factory. After years of running GitOps in production across dozens of clusters, I've compiled the essential best practices that could save you from the mistakes I made.

    From repo structure to secret management, drift detection to the IaC-to-GitOps bridge — this is the curated cheat sheet I wish I'd had from Day 1.
    <link>
---

Getting started with GitOps can feel like trying to herd cats through a YAML factory while the factory is on fire. After years of running GitOps workflows in production across dozens of clusters, I've collected a list of best practices that could save you from the mistakes I made. Think of this as the GitOps cheat sheet I wish I'd had from Day 1.

<!--more-->

If you're not familiar with the formal definition, the [OpenGitOps](https://opengitops.dev/) project distills it into four principles: declarative desired state, versioned and immutable storage, automatic pulling, and continuous reconciliation. Those principles define the "what." This post is about the "how" — the practical lessons that make or break a GitOps implementation.

In this post, I'll walk you through the GitOps best practices I've picked up from production experience, community talks, and more than a few late-night incident calls. Whether you're just getting started with GitOps or looking to level up an existing setup, these tips should help you avoid the potholes.

1. [Git is your single source of truth (no, really)](/blog/gitops-best-practices-i-wish-i-had-known-before/#1-git-is-your-single-source-of-truth-no-really)
1. [Declarative over imperative, always](/blog/gitops-best-practices-i-wish-i-had-known-before/#2-declarative-over-imperative-always)
1. [Pull-based deployments are the way](/blog/gitops-best-practices-i-wish-i-had-known-before/#3-pull-based-deployments-are-the-way)
1. [Separate app code from deployment config](/blog/gitops-best-practices-i-wish-i-had-known-before/#4-separate-app-code-from-deployment-config)
1. [Use directories, not branches, for environments](/blog/gitops-best-practices-i-wish-i-had-known-before/#5-use-directories-not-branches-for-environments)
1. [Trunk-based development or bust](/blog/gitops-best-practices-i-wish-i-had-known-before/#6-trunk-based-development-or-bust)
1. [Every change gets a PR review (no exceptions)](/blog/gitops-best-practices-i-wish-i-had-known-before/#7-every-change-gets-a-pr-review-no-exceptions)
1. [Validate before you merge](/blog/gitops-best-practices-i-wish-i-had-known-before/#8-validate-before-you-merge)
1. [Tag with commit SHAs, not "latest"](/blog/gitops-best-practices-i-wish-i-had-known-before/#9-tag-with-commit-shas-not-latest)
1. [Automate drift detection and reconciliation](/blog/gitops-best-practices-i-wish-i-had-known-before/#10-automate-drift-detection-and-reconciliation)
1. [Progressive delivery: don't YOLO to production](/blog/gitops-best-practices-i-wish-i-had-known-before/#11-progressive-delivery-dont-yolo-to-production)
1. [Policy-as-code: your automated guardrails](/blog/gitops-best-practices-i-wish-i-had-known-before/#12-policy-as-code-your-automated-guardrails)
1. [Secrets don't belong in Git (ever)](/blog/gitops-best-practices-i-wish-i-had-known-before/#13-secrets-dont-belong-in-git-ever)
1. [Bridge your IaC and GitOps (don't choose one)](/blog/gitops-best-practices-i-wish-i-had-known-before/#14-bridge-your-iac-and-gitops-dont-choose-one)
1. [Be pragmatic, not dogmatic](/blog/gitops-best-practices-i-wish-i-had-known-before/#15-be-pragmatic-not-dogmatic)
1. [Invest in observability (GitOps doesn't replace monitoring)](/blog/gitops-best-practices-i-wish-i-had-known-before/#16-invest-in-observability-gitops-doesnt-replace-monitoring)
1. [Final thoughts](/blog/gitops-best-practices-i-wish-i-had-known-before/#final-thoughts)

## 1. Git is your single source of truth (no, really)

This is the foundational principle of GitOps, and yet it's the one people break first. Every piece of your environment's desired state lives in a Git repository. No exceptions. No "I'll just fix it real quick with `kubectl edit`." No "let me patch this configmap by hand because the PR process takes too long."

The moment you make a manual change to your cluster, you've created drift between what Git says the world should look like and what it actually looks like. Drift will quietly wreck your GitOps workflows if you let it.

- Put everything in Git: Kubernetes manifests, Helm values, Kustomize overlays, policy rules, even your GitOps tool configuration itself.
- No manual `kubectl` edits. If it's not in Git, it doesn't exist. Period. Train your team to treat direct cluster changes like touching a hot stove.
- You get an audit trail for free. Git gives you a complete history of who changed what, when, and why. That's your compliance audit trail baked right in.

{{% notes type="info" %}}
Pro Tip: Enable branch protection rules on your GitOps repos from Day 1. This prevents anyone from pushing directly to main and bypassing the review process. Future you will thank present you during the next audit.
{{% /notes %}}

## 2. Declarative over imperative, always

If you're still running sequences of `kubectl create`, `kubectl patch`, and `kubectl delete` commands to manage your cluster, you're doing GitOps on hard mode. Declarative means you define *what* you want the end state to look like, not the step-by-step instructions to get there.

Think of it like ordering at a restaurant. Imperative: "Go to the kitchen, grab flour, knead dough, preheat the oven to 200 degrees, shape the pizza, add sauce..." Declarative: "One margherita pizza, please." Let the system figure out how to make it happen.

- Your manifests describe the end result. The GitOps operator reconciles reality to match.
- It's idempotent by design. Apply the same manifest ten times, get the same result. No side effects, no surprises.
- Rollbacks are easier: just revert a commit. The operator sees the previous desired state and reconciles. A caveat though: this works cleanly for stateless, declarative resources. Database schema migrations, CRD version changes, persistent volume modifications, and rotated secrets don't revert by just reverting a manifest, so plan those rollback paths separately.

{{% notes type="info" %}}
Pro Tip: If you find yourself writing shell scripts that run a sequence of `kubectl` commands, stop and ask yourself: "Can I express this as a declarative manifest instead?" Nine times out of ten, the answer is yes.
{{% /notes %}}

## 3. Pull-based deployments are the way

Traditional CI/CD is push-based: your pipeline builds an artifact and then pushes it to the cluster. GitOps flips this. An agent running inside your cluster continuously polls a Git repository and pulls changes when it detects them.

Why does this matter? With push-based deployments, your CI system needs credentials to access your cluster. That's a wide attack surface. With pull-based, the agent already lives inside the cluster and only needs read access to your Git repo.

- Tools like [ArgoCD](https://argoproj.github.io/cd/) and [FluxCD](https://fluxcd.io/) run controllers inside your cluster that watch your Git repos.
- Your CI pipeline never needs `kubeconfig` access. The agent handles deployment.
- The agent doesn't just deploy once; it continuously ensures the cluster matches the desired state in Git.

{{% notes type="info" %}}
Pro Tip: Set your reconciliation interval to something aggressive like 1 minute. A team running FluxCD in production for a German automotive manufacturer found that a 1-minute interval meant they always had confidence in exactly which version was deployed. A word of caution at scale: with 200+ applications polling every minute, you can blow through GitHub's API rate limits (5,000 requests/hour for authenticated users) and put pressure on the Kubernetes API server. Consider tiering intervals by environment, such as 1 minute for production and 5 minutes for dev/staging.
{{% /notes %}}

{{< related-posts >}}

## 4. Separate app code from deployment config

I see this mistake all the time: storing your Kubernetes manifests right next to your application source code in the same repo. It seems convenient at first, but it turns into a real headache as you scale.

Application code and deployment configuration have completely different lifecycles. You might update a Helm values file to bump resource limits without touching a single line of app code. Or you might refactor your entire codebase without changing a single deployment parameter. Coupling them means every config tweak triggers your full CI pipeline, and every code change touches your deployment repo.

- App code has its own release cadence. Deployment config changes on its own schedule. Keep them separate so config tweaks don't fire your full CI pipeline.
- Your deployment repo might contain sensitive environment-specific values. Not everyone who can push app code should see or modify those.
- Your app CI builds and tests code. Your GitOps repo triggers deployments. Clean separation, clean pipelines.

{{% notes type="info" %}}
Pro Tip: A common pattern is three repos: one for application source code, one for deployment configuration (Helm charts, Kustomize bases), and one for environment-specific overrides. This maps cleanly to the "fleet repo, infra repo, apps repo" model recommended by the FluxCD maintainers. To make this pattern practical, pair it with image update automation (Flux Image Automation Controller or ArgoCD Image Updater) so image tag bumps across repos don't become manual toil.
{{% /notes %}}

## 5. Use directories, not branches, for environments

This is the number one anti-pattern I encounter in the wild. Teams create a `dev` branch, a `staging` branch, and a `prod` branch, then cherry-pick or merge between them for promotions. It sounds logical, but it's a trap. And as Conway's Law reminds us, your repo structure will end up mirroring your org structure whether you plan for it or not, so it's worth being intentional about this from the start.

Branches diverge. Cherry-picks get missed. ConfigMaps and secrets meant for dev sneak into staging. Before you know it, your environments have drifted apart and you can't tell what's actually different between them.

- A folder structure like `environments/dev/`, `environments/staging/`, `environments/prod/` makes differences visible in a single `diff` command.
- Moving a change from dev to prod is just copying or updating files across directories, reviewed via a standard pull request.
- You'll never accidentally skip a commit or introduce an environment-specific change where it doesn't belong. No more cherry-pick roulette.

Here's what a clean directory structure looks like in practice:

```text
gitops-repo/
├── base/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── kustomization.yaml
├── environments/
│   ├── dev/
│   │   ├── kustomization.yaml   # replicas: 1, limits: 256Mi
│   │   └── patches/
│   ├── staging/
│   │   ├── kustomization.yaml   # replicas: 2, limits: 512Mi
│   │   └── patches/
│   └── prod/
│       ├── kustomization.yaml   # replicas: 3, limits: 1Gi
│       └── patches/
```

Each environment's `kustomization.yaml` references the shared base and applies only its overrides. Differences between environments are always one `diff` away.

{{% notes type="info" %}}
Pro Tip: Use Kustomize overlays to keep a shared base and per-environment patches. Your base directory holds the common manifests, and each environment directory contains only the differences. This minimizes duplication while keeping environment boundaries crystal clear. And in practice, it's not "Kustomize or Helm" — most teams use both in tandem. Kustomize patches work great when you know the values ahead of time (replicas, resource limits). Helm parameterization shines when values depend on the destination cluster and aren't known until deploy time, like an Ingress FQDN or a cloud-specific endpoint. Use Kustomize to keep things DRY, Helm to keep things flexible.
{{% /notes %}}

## 6. Trunk-based development or bust

Long-lived feature branches in a GitOps repo are a recipe for merge conflicts and stale configuration. Your GitOps repository should follow trunk-based development: one main branch, short-lived feature branches, and frequent merges.

The longer a branch lives, the further it drifts from reality. And in a GitOps context, "drifting from reality" means your environments are out of sync with what people think they look like. That's how incidents happen.

- Create a branch, make the change, open a PR, get it reviewed, merge. The whole cycle should take hours, not days or weeks.
- Avoid the `develop` / `release` / `main` branching model for GitOps repos. It adds complexity without value here.
- The more often you merge to main, the smaller each change is, and the easier it is to review and roll back.

{{% notes type="info" %}}
Pro Tip: If your GitOps repo has branches older than a week, treat it as a code smell. Set up automated reminders or CI checks that flag stale branches.
{{% /notes %}}

## 7. Every change gets a PR review (no exceptions)

A sobering stat from a production talk about running FluxCD at a German automotive manufacturer: the number one cause of failed deployments was missing PR reviews. Not bad YAML. Not misconfigured Helm charts. Missing reviews.

When someone pushes directly to main without review, there's no second pair of eyes to catch the typo in the resource limit, the missing namespace, or the wrong image tag. PR reviews are your last check before a change hits your cluster.

- Enable branch protection rules requiring at least one approval before merge.
- Assign specific teams or individuals as CODEOWNERS for critical paths in your GitOps repo.
- Pair human reviewers with CI checks (more on that in the next section).
- Beyond Git-level controls, use ArgoCD AppProjects to restrict which namespaces and clusters each team can target. A team should never be able to deploy to another team's namespace, even if they have push access to the repo. Flux achieves similar isolation through namespace-scoped Kustomization controllers and service account impersonation.

{{% notes type="info" %}}
Pro Tip: Make the review process lightweight so people don't try to bypass it. A clear PR template, automated linting, and fast CI checks reduce friction. If your review process takes two days, people will find ways around it.
{{% /notes %}}

## 8. Validate before you merge

Catching errors after they've been applied to your cluster is expensive. Catching them in CI before the merge is cheap. Shift left as hard as you can.

Your GitOps CI pipeline should validate everything it can before the change reaches your cluster: YAML syntax, Kubernetes schema validation, policy compliance, dry-run rendering.

- Tools like `yamllint` and `kubeval` catch syntax errors and schema violations before they become runtime failures.
- Run `helm template` or `kustomize build` in CI to verify that your templates render without errors.
- Use [OPA](https://www.openpolicyagent.org/)/[Conftest](https://www.conftest.dev/) or [Kyverno](https://kyverno.io/) to enforce organizational policies (no privileged containers, required labels, resource limits set) before merge.
- Consider the rendered manifests pattern. When your GitOps repo stores only "dry" sources (Helm charts, Kustomize overlays), the effects of a change aren't always obvious from the PR diff alone. A one-line Helm chart version bump might result in a thousand lines of manifest changes, but your PR only shows the version change. The [rendered manifests pattern](https://akuity.io/blog/the-rendered-manifests-pattern) solves this by rendering manifests in CI and storing the final, immutable YAML on environment-specific branches. You get truly transparent diffs, and ArgoCD applies manifests as-is without running Helm or Kustomize at sync time, which is a real performance win at scale. ArgoCD's built-in [source hydrator](https://argo-cd.readthedocs.io/en/latest/user-guide/source-hydrator/) can automate this natively. One caveat: this pattern doesn't work well with tools that render plaintext secrets (like SOPS), so use External Secrets Operator or similar reference-based approaches for secrets.

Here's a minimal GitHub Actions workflow that validates your GitOps manifests on every PR:

```yaml
name: Validate GitOps Manifests
on:
  pull_request:
    paths: ["environments/**"]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate YAML schemas
        run: kubeval --strict environments/**/*.yaml
      - name: Build and verify Kustomize output
        run: |
          for env in environments/*/; do
            kustomize build "$env" > /dev/null
          done
      - name: Diff against live cluster
        run: |
          kustomize build environments/staging/ | \
            kubectl diff -f - || true
```

{{% notes type="info" %}}
Pro Tip: Add a `kubectl diff` step in your CI pipeline that shows exactly what would change in the cluster if the PR were merged. This gives reviewers a concrete view of the impact, not just the YAML diff.
{{% /notes %}}

## 9. Tag with commit SHAs, not "latest"

Using `latest` as your image tag in a GitOps workflow is playing Russian roulette with your deployments. You have no idea what version is actually running, you can't reliably roll back, and your Git history becomes meaningless because the same manifest could deploy completely different code depending on when it was synced.

- Tag your container images with the Git commit SHA that produced them. This creates a direct link between your source code, your build, and your deployment.
- Once a tag is pushed, it should never be overwritten. No re-tagging, no "oops let me push a fix to the same tag."
- Need to roll back? Just revert the commit that updated the image tag. The previous SHA still points to the exact same image it always did.

{{% notes type="info" %}}
Pro Tip: Set up an admission controller or CI policy that rejects any manifest using `latest` or any other mutable tag. Make it impossible to deploy without a pinned version.
{{% /notes %}}

## 10. Automate drift detection and reconciliation

Drift is when your cluster's actual state doesn't match the desired state in Git. It happens when someone runs a manual `kubectl` command, when an autoscaler changes a replica count, or when a CRD controller modifies a resource behind your back.

The whole point of GitOps is continuous reconciliation. Your operator should constantly compare the live state against Git and bring things back in line. If you've disabled auto-sync or set your reconciliation interval to "once a day," you're missing the point.

- As mentioned earlier, a 1-minute reconciliation interval gives you high confidence that what's in Git is what's in your cluster.
- Configure your GitOps tool to automatically revert manual changes, but build your exclusion lists before you turn on auto-sync, not after. Controllers like Istio, cert-manager, and Crossplane legitimately modify resources, and auto-remediating those changes creates reconciliation loops that can destabilize a cluster. Start with a conservative exclusion list and tighten it over time.
- Even with auto-remediation, you want to know when drift happens. Set up alerts. It might indicate a process problem or a team member who needs coaching.

{{% notes type="info" %}}
Pro Tip: Be thoughtful about what you auto-remediate. HPAs, VPAs, cert-manager annotations, and external-dns records all legitimately modify resources. Use ignore rules to exclude fields that are intentionally dynamic. In ArgoCD, that looks like this:

```yaml
spec:
  ignoreDifferences:
    - group: apps
      kind: Deployment
      jsonPointers:
        - /spec/replicas
    - group: admissionregistration.k8s.io
      kind: MutatingWebhookConfiguration
      jqPathExpressions:
        - .webhooks[]?.clientConfig.caBundle
```

Also, don't overlook resource ordering. ArgoCD sync waves and Flux's `dependsOn` let you enforce that CRDs are applied before custom resources and namespaces before workloads. Getting ordering wrong is one of the most common causes of failed syncs in production.
{{% /notes %}}

## 11. Progressive delivery: don't YOLO to production

Pushing a change straight to production and hoping for the best is not a deployment strategy. Progressive delivery lets you gradually roll out changes, verify they're working, and automatically roll back if something goes wrong.

GitOps and progressive delivery fit well together. Your Git repo describes the desired rollout strategy, and controllers in the cluster execute it.

- Canary deployments: send a small percentage of traffic to the new version. If error rates spike, automatically roll back.
- Blue-green deployments: run two identical environments, switch traffic once the new one is verified healthy.
- [Argo Rollouts](https://argoproj.github.io/rollouts/) extends Kubernetes with canary, blue-green, and analysis-driven rollout strategies that integrate with ArgoCD.
- [Flagger](https://flagger.app/) is the Flux ecosystem equivalent, with automated canary analysis, A/B testing, and blue-green deployments using service mesh or ingress controllers.
- [Kargo](https://kargo.io/) takes it a step further by orchestrating promotions across multiple stages and environments. Instead of manually wiring up pipelines to move changes from dev to staging to prod, Kargo automates the entire promotion workflow on top of ArgoCD. I did a deep dive on GitOps promotion tools and why they belong in your toolkit:

{{< youtube "OhFdLTU5sAo?rel=0" >}}

{{% notes type="info" %}}
Pro Tip: Combine progressive delivery with automated analysis. Tools like Argo Rollouts can query Prometheus metrics during a canary and automatically promote or roll back based on error rates, latency percentiles, or custom metrics.
{{% /notes %}}

## 12. Policy-as-code: your automated guardrails

Reviews are great, but humans make mistakes. Policy-as-code adds an automated layer that enforces organizational rules before a change can land in your cluster. Think of it as guardrails on a mountain road: they don't slow you down, they just keep you from going over the edge.

- [OPA](https://www.openpolicyagent.org/)/Gatekeeper lets you define policies in Rego that the admission controller enforces at deploy time (e.g., no containers running as root, all deployments must have resource limits).
- [Kyverno](https://kyverno.io/) is a Kubernetes-native policy engine that uses familiar YAML to define and enforce policies, including mutation and generation.
- Starting with Kubernetes 1.26+, you can write CEL-based ValidatingAdmissionPolicies natively without any external tooling. A lightweight option if you don't need the full feature set of OPA or Kyverno.
- Run policy checks in your CI pipeline so violations are caught during the PR, not after deployment.

{{% notes type="info" %}}
Pro Tip: Start with a small set of high-impact policies (required labels, no privileged containers, resource limits) and expand over time. Trying to enforce 50 policies on Day 1 will create so much friction that teams will revolt.
{{% /notes %}}

## 13. Secrets don't belong in Git (ever)

Git history is forever. Once a secret is committed, it lives in the repository's history even if you delete it in a subsequent commit. And if your GitOps repo is your single source of truth, you need a strategy for secrets that doesn't involve committing them in plaintext.

This is one of the biggest pain points in GitOps. The good news: there are several solid solutions:

- [External Secrets Operator](https://external-secrets.io/) syncs secrets from external providers (AWS Secrets Manager, HashiCorp Vault, [Pulumi ESC](/docs/esc/)) into Kubernetes secrets.
- [Sealed Secrets](https://sealed-secrets.netlify.app/) encrypts secrets client-side so only the controller in your cluster can decrypt them. Safe to commit the encrypted version to Git.
- [Pulumi ESC](/docs/esc/) manages secrets and configuration across environments with fine-grained access controls, and integrates with [Kubernetes via the External Secrets Operator](/docs/esc/integrations/kubernetes/external-secrets-operator/) or the [Secret Store CSI Driver](/docs/esc/integrations/kubernetes/secret-store-csi-driver/).
- For a purely GitOps-native approach, [SOPS](https://github.com/getsops/sops) + age encrypts secret values in-place within your YAML files using `age` keys, so you can commit encrypted secrets directly to Git without a cluster-side operator. Widely used in the Flux ecosystem.

Here's what an ExternalSecret referencing a secret store looks like:

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-database-credentials
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: ClusterSecretStore
  target:
    name: db-credentials
  data:
    - secretKey: password
      remoteRef:
        key: prod/myapp/db-password
```

{{% notes type="info" %}}
Pro Tip: Run `git log --all --diff-filter=D -- '*.env' '*.secret' '*.key'` on your repos occasionally to check if anyone has ever committed and then deleted a secret file. If they have, consider the secret compromised and rotate it immediately.
{{% /notes %}}

## 14. Bridge your IaC and GitOps (don't choose one)

I hear this all the time: "We use Terraform for infrastructure and ArgoCD for deployments, and they live in completely separate worlds." Sound familiar? Most teams treat IaC and GitOps as independent workflows, but they're really two halves of the same story.

IaC handles "Day 0," creating the cloud resources your cluster depends on: VPCs, the Kubernetes cluster itself, IAM roles, databases, DNS zones. GitOps handles "Day 2," managing what runs inside the cluster: applications, addons, configurations. The gap between them is where things get messy. Your Helm charts need IAM role ARNs. Your GitOps-deployed addons need to know the cluster's OIDC provider endpoint. That metadata has to flow from the IaC layer to the GitOps layer somehow.

The [gitops-bridge](https://github.com/gitops-bridge-dev/gitops-bridge) pattern solves this cleanly: IaC provisions cloud resources and writes metadata (role ARNs, account IDs, endpoints) into resources that your GitOps tool can consume.

- Let each tool do what it's best at. Don't force Terraform's Helm provider to fight with ArgoCD over resource ownership.
- [Pulumi](/docs/get-started/) lets you define your cloud infrastructure in real programming languages (TypeScript, Python, Go), which makes it natural to compute and pass metadata to your GitOps layer. The [Pulumi Kubernetes Operator](/docs/iac/guides/continuous-delivery/pulumi-kubernetes-operator/) even lets ArgoCD reconcile Pulumi stacks via GitOps.
- Statsig went from "1-2 devs clicking around cloud consoles with SEVs left and right" to fully self-service by using [Pulumi to generate manifests and ArgoCD to deploy them](https://www.statsig.com/blog/scaling-infra-with-pulumi-argocd).
- As you grow beyond a handful of clusters, think multi-cluster from the start. Patterns like ArgoCD ApplicationSets with cluster generators and Flux's Kustomization targeting become important for fleet management. The gitops-bridge pattern works well here because your IaC layer can register new clusters and write their metadata into Git, and ApplicationSets automatically pick them up.

Here's how the gitops-bridge looks in practice. Pulumi provisions cloud resources and writes metadata into a ConfigMap that ArgoCD consumes:

```yaml
# ConfigMap written by Pulumi after provisioning cloud resources
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-metadata
  namespace: argocd
  labels:
    gitops-bridge: "true"
data:
  aws_account_id: "123456789012"
  cluster_name: "prod-us-east-1"
  iam_role_arn: "arn:aws:iam::123456789012:role/app-role"
  oidc_provider: "oidc.eks.us-east-1.amazonaws.com/id/EXAMPLE"
```

Your ArgoCD Applications or Helm values can then reference this ConfigMap, closing the loop between IaC and GitOps without hardcoding cloud-specific values.

{{% notes type="info" %}}
Pro Tip: If you're using Terraform today, the gitops-bridge pattern works there too. But if you're tired of wrangling HCL and want type-safe infrastructure code with real programming constructs, [give Pulumi a look](/docs/get-started/). The bridge from IaC to GitOps becomes much more natural when both sides speak a real programming language.
{{% /notes %}}

## 15. Be pragmatic, not dogmatic

Michael Crenshaw from Intuit gave a talk titled "How GitOps Should I Be?" at a CNCF conference. Intuit runs 45 ArgoCD instances managing 20,000 applications across 200 clusters. Their answer? "Be strategic, be pragmatic. GitOps most of the time."

That's right. One of the largest GitOps adopters in the world explicitly deviates from pure GitOps when the situation calls for it. Dogmatic adherence to principles that don't serve you is just another form of technical debt.

- Intuit found that GitHub's SLA of 20 minutes meant they couldn't rely on GitOps for region evacuation. Their solution? A `kubectl` cron job that bypasses Git for failover. Pragmatic.
- Massive Jenkins ecosystems don't get rewritten overnight. Intuit's compromise: the last step in the Jenkins pipeline calls `argocd app sync`. Push-based, but the source of truth stays in Git.
- Continuous reconciliation with self-heal (auto-reverting manual changes) is where most teams deviate. That's OK. Work toward it, but don't let perfect be the enemy of good.

{{% notes type="info" %}}
Pro Tip: Document your intentional deviations. Create an ADR (Architecture Decision Record) for each case where you've chosen not to follow pure GitOps, explaining why and what the plan is to close the gap (if ever). This turns exceptions into conscious decisions rather than accidental shortcuts.
{{% /notes %}}

## 16. Invest in observability (GitOps doesn't replace monitoring)

GitOps gives you a clean declarative workflow, but it doesn't tell you if your application is actually healthy. You still need observability. I'd argue you need it even more with GitOps, because with automated reconciliation happening continuously, you need to see what your GitOps operator is doing and whether deployments are succeeding.

- For ArgoCD, watch `argocd_app_sync_total`, `argocd_app_reconcile_count`, and `argocd_app_info` (which exposes sync status and health as labels). For Flux, track `gotk_reconcile_duration_seconds` and `gotk_reconcile_condition`. These tell you whether your GitOps pipeline is healthy before your users notice it isn't.
- Measure sync latency. The time between "commit merged" and "change live in cluster" is a metric most teams forget to track. If that number creeps above a few minutes, you have a bottleneck somewhere in your reconciliation pipeline.
- ArgoCD Notifications and Flux Notification Controller can push sync events, failures, and health changes to Slack, PagerDuty, or Teams. Don't rely on someone watching a dashboard. Wire up alerts so that an application stuck in OutOfSync for more than 15 minutes pages the right team automatically.
- [Prometheus](https://prometheus.io/) + [Grafana](https://grafana.com/) is the classic combination. Add dashboards for your GitOps tooling alongside your application dashboards.

{{% notes type="info" %}}
Pro Tip: Create a dedicated Grafana dashboard for your GitOps operator that shows sync status, reconciliation duration, error counts, and resource counts per application. A good starting point: alert on `argocd_app_info{sync_status="OutOfSync"}` persisting for more than 15 minutes in production, or `gotk_reconcile_condition{type="Ready", status="False"}` for Flux. These two alerts alone will catch the majority of silent GitOps failures.
{{% /notes %}}

## Final thoughts

GitOps isn't a silver bullet, but it's one of the best approaches we have for managing Kubernetes at scale. The practices in this list aren't theoretical. They're what I've learned from running GitOps in production, watching talks from teams at Intuit and Statsig, and making every mistake in the book at least once.

If I had to boil it all down to one sentence: **treat your GitOps repo like production code, because it is.**

Start with the basics (Git as source of truth, declarative config, pull-based delivery) and layer on the advanced practices as your team matures. Don't try to implement all 16 on Day 1. Pick the three that address your biggest pain points and iterate from there.

And remember, even the largest GitOps adopters in the world aren't doing it perfectly. They're being pragmatic. You should be too.

If you want to bridge the gap between your infrastructure and your GitOps workflow, here are some good starting points:

{{< blog/cta-button "Try Pulumi for Free" "/docs/get-started/" >}}
{{< blog/cta-button "Explore Pulumi ESC for Secrets" "/docs/esc/" >}}
{{< blog/cta-button "Pulumi Kubernetes Operator" "/docs/iac/guides/continuous-delivery/pulumi-kubernetes-operator/" >}}
