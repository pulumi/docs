---
title: JavaScript and TypeScript Infrastructure as Code
meta_desc: "Define cloud infrastructure as code in TypeScript or JavaScript: real types, npm packages, IDE tooling, and Jest tests for VPCs and clusters."

type: what-is
page_title: "JavaScript and TypeScript Infrastructure as Code"

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - ware2go
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - skai
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro
authors: ["pablo-seibelt"]
---

**JavaScript and TypeScript can be used to define [infrastructure as code](/what-is/what-is-infrastructure-as-code/) the same way they're used to build web applications: real programs, real types, real package management, real tests, real IDE tooling.** Instead of describing cloud resources in a custom DSL like HCL or in YAML, you write a Node.js program whose API calls describe a VPC, a Kubernetes cluster, or an S3 bucket. An IaC engine then reconciles your declared state with what's running in the cloud.

For teams already running on Node.js, this collapses the gap between the application layer and the platform under it. The same TypeScript types, the same `npm install` workflow, the same Jest test setup, the same VS Code experience, and the same code review process apply to the infrastructure your app runs on. Pulumi treats TypeScript and JavaScript as first-class IaC languages alongside Python, Go, .NET, Java, and YAML; this page covers why JavaScript and TypeScript are a strong fit for IaC, what the tradeoffs look like, and how to set up a JS/TS IaC project well.

In this article, we'll cover the key questions about JavaScript and infrastructure as code:

* Why use JavaScript or TypeScript for infrastructure as code?
* Should I use JavaScript or TypeScript?
* What does JS/TS offer that an IaC DSL doesn't?
* What does TypeScript infrastructure as code look like?
* How does writing IaC in JS/TS compare to HCL or YAML?
* What ecosystem tools come with JavaScript IaC?
* What patterns and pitfalls should I know about?
* How does Pulumi support JavaScript and TypeScript?
* Frequently asked questions about JavaScript and infrastructure as code

## Why use JavaScript or TypeScript for infrastructure as code?

A few practical reasons drive most adoptions:

* **The team already knows it.** Most full-stack and frontend-heavy organizations already run Node.js in production. Using the same language for IaC means no new training, no new style guides, no new package manager.
* **The npm ecosystem is huge.** Thousands of utility libraries, validators, AWS/GCP/Azure SDK clients, retry helpers, schema validators, and logging libraries are already published, tested, and vetted at scale.
* **Real abstractions, not text templates.** Functions, classes, modules, generics. A repeating VPC pattern becomes a Pulumi component you import and parameterize, rather than a module you copy and edit.
* **Real testing tools.** Jest, Vitest, ts-mocha, supertest. Unit tests for IaC use the same runners you already configured for the application code.
* **Real IDE support.** Autocomplete, jump-to-definition, refactoring, inline error squiggles. The same VS Code or WebStorm experience that helps with app code helps with cloud APIs that have hundreds of optional properties.

## Should I use JavaScript or TypeScript?

TypeScript, in almost every case. Modern infrastructure has hundreds of optional properties per resource (a single AWS RDS instance has 50+ configuration fields), and the cost of a typo or a missing required field is a failed deploy or a security incident. TypeScript catches both at compile time.

| Aspect | JavaScript | TypeScript |
|---|---|---|
| Typing | None at compile time | Full static types, including for cloud resource shapes |
| IDE experience | Decent | Excellent (autocomplete, jump-to-definition, refactor) |
| Catches typos before deploy | No | Yes |
| Setup overhead | None | A `tsconfig.json` + a build step |
| Learning curve from JS | Same | A few hours to get productive; gradual adoption supported |

Pulumi templates generate TypeScript projects by default for this reason. The runtime cost of TypeScript is zero (it compiles to plain JavaScript); the development-time payoff for IaC is high.

## What does JS/TS offer that an IaC DSL doesn't?

DSLs like HCL or CloudFormation YAML keep their surface area small on purpose. They favor a constrained, declarative model, and general-purpose languages trade that simplicity for functions, richer loops, and a type system. JS/TS gives you those when you want them:

* **Loops and conditionals that compose.** A subnet per availability zone, a Lambda per region, or a Kubernetes namespace per tenant, all expressed as familiar `.map()` and `for` loops rather than DSL-specific iteration features.
* **Abstractions you actually own.** A Pulumi component is just a TypeScript class. It can take typed inputs, build any combination of underlying resources, and expose typed outputs. You can publish it to npm, version it semantically, and depend on it from many stacks.
* **Sharing through npm.** Internal Pulumi packages live in a private npm registry next to your other internal libraries. Public packages live on npm.
* **Real types over cloud APIs.** Every AWS, Azure, Google Cloud, and Kubernetes resource has a generated TypeScript type. The compiler knows what fields exist, which are required, and what types they take.
* **Standard testing infrastructure.** Jest tests for IaC live next to Jest tests for the app, run in the same CI step, and use the same mocking patterns.

## What does TypeScript infrastructure as code look like?

A complete Pulumi program that creates a versioned, tagged S3 bucket:

```typescript
import * as aws from "@pulumi/aws";

export const assets = new aws.s3.BucketV2("app-assets", {
    tags: { team: "platform", env: "prod" },
});

new aws.s3.BucketVersioningV2("app-assets-versioning", {
    bucket: assets.id,
    versioningConfiguration: { status: "Enabled" },
});

export const bucketName = assets.bucket;
```

Every property is typed. Misspell `versioningConfiguration`, pass a number where a string belongs, or omit a required field, and the program fails at compile time with a precise error, not halfway through a deploy. The same compiler that protects the application protects the infrastructure.

Because it's ordinary TypeScript, it's testable with the Jest setup the app already uses. Pulumi's mocks replace cloud calls so the test runs entirely in memory:

```typescript
import * as pulumi from "@pulumi/pulumi";

pulumi.runtime.setMocks({
    newResource: (args) => ({ id: `${args.name}-id`, state: args.inputs }),
    call: (args) => args.inputs,
});

test("buckets are tagged with an owning team", async () => {
    const { assets } = await import("./index");
    const tags = await new Promise((resolve) => assets.tags.apply(resolve));
    expect(tags).toMatchObject({ team: "platform" });
});
```

Getting a project running is three commands:

1. **Create a project.** `pulumi new aws-typescript` scaffolds `package.json`, `tsconfig.json`, and a starter program.
1. **Preview the change.** `pulumi preview` compiles the program and shows the planned resources before anything is created.
1. **Deploy.** `pulumi up` applies the plan and prints the stack outputs, like `bucketName` above.

See the [unit testing guide](/docs/iac/guides/testing/unit/) for the full mock API and patterns for testing components.

## How does writing IaC in JS/TS compare to HCL or YAML?

| Dimension | HCL (Terraform / OpenTofu) | YAML (CloudFormation, raw K8s) | JS / TS (Pulumi) |
|---|---|---|---|
| Language model | Domain-specific | Markup with macros | General-purpose |
| Loops & conditionals | Limited (`for_each`, `count`) | None (manual templating) | Full language constructs |
| Types | Limited | None | Full TypeScript types |
| Package ecosystem | Terraform registry | None | npm |
| IDE support | Good | OK | Excellent |
| Testing | Terratest, limited unit | Limited | Jest/Vitest, mocks, full TDD |
| Sharing modules | Registry modules | Nested stacks / Helm | npm packages, Pulumi components |
| Onboarding for JS devs | Steep | Easy | Trivial |

The right choice depends on what your team already knows and what skills you want to scale. Teams with deep JS/TS expertise tend to find Pulumi's TS workflow more natural; teams that have invested heavily in Terraform sometimes prefer to stay on HCL.

## What ecosystem tools come with JavaScript IaC?

JavaScript and TypeScript IaC plugs straight into the toolchain your application code already uses:

| Tool category | Representative tools |
|---|---|
| Package management | npm, yarn, pnpm |
| Testing | Jest, Vitest, Mocha + Chai, supertest |
| Linting / formatting | ESLint, Prettier, Biome |
| TypeScript build | `tsc`, esbuild, swc |
| IDE | VS Code, WebStorm, Neovim with `tsserver` |
| Static analysis | Knip, ts-prune, `noImplicitAny`, `strict` |
| CI/CD | GitHub Actions, GitLab CI, CircleCI, anything that runs `npm` |
| Bundling (where needed) | esbuild, webpack |
| Cloud SDKs | AWS SDK v3, Azure SDK for JS, Google Cloud client libraries (used directly from Pulumi programs when needed) |
| Schema validation | Zod, Yup, JSON Schema validators |

Combined with Pulumi's typed resource SDK, this means every workflow that exists for JavaScript apps (PR review, type checking, formatting, dependency updates via Dependabot or Renovate, deploy pipelines) applies unchanged to your infrastructure.

## What patterns and pitfalls should I know about?

A few patterns that hold up in production Node.js + Pulumi codebases:

* **Use TypeScript with `strict` enabled.** Strict mode catches the entire class of "undefined is not a function" issues at compile time. Worth setting on day one.
* **Don't import the cloud SDKs to "do something real time" inside a Pulumi program.** Pulumi programs describe desired state; they don't execute imperative calls against the cloud at apply time. Use Pulumi resources for declared state and `pulumi.runtime.runInPulumiStack` only for the small set of advanced cases that genuinely need it.
* **Don't put secrets in source.** Use [Pulumi ESC](/product/esc/) or another secrets store and pull them at runtime. Configuration stays in code; secret material doesn't.
* **Write components for any pattern you repeat.** If you copy-paste a VPC three times, the fourth time it should be `new MyVpc()`. Components version like any other npm package.
* **Treat `package-lock.json` (or `pnpm-lock.yaml`) as part of your IaC.** Lock files make `pulumi up` reproducible. Without them, a new transitive dependency can break a deploy.
* **Pin Pulumi providers explicitly.** Like any other npm dependency, Pulumi provider packages can release breaking changes. Pin major versions and upgrade deliberately.
* **Run `pulumi preview` on every PR.** Show the planned change as a comment so the reviewer doesn't have to guess what your TypeScript program is going to do.
* **Keep `async`/`await` and Pulumi outputs distinct.** Pulumi outputs (`Output<T>`) are not the same as JavaScript promises. Use `.apply()`, `pulumi.all`, and string interpolation helpers rather than awaiting them.

The most common pitfall: writing IaC like a script. JS/TS lets you do that, but you give up the strengths of declarative IaC if you do. Describe state; let Pulumi reconcile.

## How does Pulumi support JavaScript and TypeScript?

Pulumi treats Node.js as a first-class runtime alongside Python, Go, .NET, Java, and YAML.

* **Typed SDKs for every cloud.** AWS, Azure, Google Cloud, Kubernetes, Cloudflare, Snowflake, Datadog, and the rest of the [180+ providers in the Pulumi Registry](/registry/). Generated from each provider's API, so the types reflect the real cloud surface.
* **`pulumi new typescript`.** Creates a project with `tsconfig.json`, `package.json`, and a starter program in seconds. See the [JavaScript / TypeScript language guide](/docs/languages-sdks/javascript/) and [the get-started flow](/docs/get-started/).
* **Component model.** Write reusable [Pulumi components](/docs/iac/concepts/components/) as TypeScript classes. Publish them to npm (private or public) and depend on them across teams.
* **Crosswalk for AWS.** The [`@pulumi/awsx`](https://github.com/pulumi/pulumi-awsx) package wraps common AWS patterns (VPCs, ECS services, ECR registries, load balancers) in higher-level TypeScript classes with sensible defaults.
* **Unit testing with mocks.** Pulumi's [TypeScript test mocks](/docs/iac/guides/testing/unit/) replace cloud calls with canned responses, so Jest tests run in milliseconds.
* **Automation API.** The [automation API](/docs/iac/packages-and-automation/automation-api/) lets you run Pulumi programs from inside another Node.js application. Build CLIs, self-service portals, or CI jobs that drive `pulumi up` and `pulumi destroy` from typed JS.
* **Policy as code in TypeScript.** [Pulumi policies](/docs/insights/policy/) can be written in the same language as the IaC, with the same typing over the resource model.
* **Pulumi ESC for secrets.** [Pulumi ESC](/product/esc/) pulls secrets at runtime into Node.js programs, CI jobs, and applications, with audit trails.

[Get started with Pulumi and TypeScript](/docs/get-started/) to provision cloud infrastructure with the same tools you already use for application code.

## Frequently asked questions about JavaScript and infrastructure as code

### Can I use Node.js to manage infrastructure on every cloud?

Yes. Pulumi's TypeScript SDK covers AWS, Azure, Google Cloud, Kubernetes, and 180+ providers in total, with a uniform programming model across them. The same Pulumi program can mix providers (an AWS VPC, a Cloudflare DNS record, a Datadog monitor) without leaving the language.

### Is TypeScript meaningfully better than JavaScript for IaC?

Yes. Cloud resources have large, complex shapes; the compiler catching a missing required property or a typo before deploy is a continuous productivity win. The runtime is the same Node.js you'd get with plain JS, and the build step is unobtrusive.

### How does JS/TS compare to HCL for IaC?

HCL is a domain-specific language built for IaC; TypeScript is a general-purpose language used for IaC. HCL is simpler if you're starting from scratch and the team doesn't have a JS background. TypeScript wins on abstraction, testing, IDE support, and team familiarity once you're already in the npm ecosystem. See the comparison table above.

### Do I have to use Node.js to use Pulumi?

No. Pulumi supports Python, Go, .NET (C#, F#, VB), Java, and YAML alongside Node.js (JavaScript / TypeScript). Pick whichever language your team already uses.

### Can I write Pulumi infrastructure tests with Jest?

Yes. Jest is the most common choice for unit testing Pulumi TypeScript programs. Pulumi provides mocks that replace cloud calls so the tests run entirely in memory. See the [unit testing guide](/docs/iac/guides/testing/unit/).

### Can I publish a Pulumi component to npm?

Yes. A Pulumi component is just a TypeScript class. Compile it, publish it to npm (public or private), and depend on it from any number of stacks. Many platform teams maintain an internal npm registry of opinionated components for the rest of the company.

### What's the difference between an Output and a Promise?

A Pulumi `Output<T>` represents a value that's resolved during deploy time, often with dependencies on other resources. JavaScript `Promise<T>` is a generic asynchronous-value abstraction. Awaiting an `Output` directly doesn't work the way you'd expect; use `.apply()`, `pulumi.all([...])`, or string interpolation (`pulumi.interpolate`) to read or compose them.

### How do you handle secrets in a Node.js Pulumi program?

Use `pulumi.secret()` for values that should be encrypted in state, and pull anything sensitive from [Pulumi ESC](/product/esc/), AWS Secrets Manager, Azure Key Vault, or HashiCorp Vault at runtime. The Pulumi program references the secret; the secret material doesn't live in source.

### Can I migrate from Terraform / HCL to TypeScript?

Yes. Pulumi can import existing cloud resources with `pulumi import` and can interoperate with Terraform state via `pulumi convert` for the source code. Many teams do an incremental migration: new infrastructure in TypeScript, existing HCL stays put until it changes, eventually retiring HCL as resources move under Pulumi management.

### Does Pulumi's TypeScript SDK update when the cloud provider's API changes?

Yes. Pulumi regenerates the provider SDKs from each provider's source schema (either the upstream cloud API for native providers, or the Terraform provider schema for bridged providers) so new resource types and properties appear in the npm packages shortly after the provider ships them. Provider versions are pinned in `package.json` so you control when to adopt new releases.

## Learn more

Pulumi makes JavaScript and TypeScript a first-class option for infrastructure as code: typed SDKs for every major cloud, reusable components as npm packages, Jest tests with cloud mocks, and the same CI/CD and code review workflow you already use for the app. [Get started today](/docs/get-started/).

Related reading:

* [What is Infrastructure as Code (IaC)?](/what-is/what-is-infrastructure-as-code/)
* [Infrastructure as Code for DevOps](/what-is/infrastructure-as-code-for-devops/)
* [Infrastructure as Code for Kubernetes](/what-is/infrastructure-as-code-for-kubernetes/)
* [How to Step Up Cloud Infrastructure Testing](/what-is/how-to-step-up-cloud-infrastructure-testing/)
* [Python for DevOps](/what-is/python-for-devops/)
