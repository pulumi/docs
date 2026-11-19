---
title_tag: Pulumi Delivery stages and gates
meta_desc: Order promotion between environments with Pulumi Delivery stages, hold a release at a gate, pause or roll back a stage, and publish artifacts from a stage.
title: Stages and gates
h1: Stages and gates
menu:
  delivery:
    name: Stages and gates
    parent: delivery-concepts
    weight: 20
aliases: []
---

Stages give a pipeline its shape. Each stage is a step that a release moves through, commonly one environment such as `dev` or `prod`.

## Ordering stages with `from`

A stage with no `from` is an entry stage. Every other stage lists its upstream stages:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const dev = new delivery.Stage("dev", { pipeline });
const staging = new delivery.Stage("staging", { pipeline, from: [dev] });
const prod = new delivery.Stage("prod", { pipeline, from: [staging] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
dev = delivery.Stage("dev", pipeline=pipeline)
staging = delivery.Stage("staging", pipeline=pipeline, from_=[dev])
prod = delivery.Stage("prod", pipeline=pipeline, from_=[staging])
```

{{% /choosable %}}
{{% choosable language go %}}

```go
dev, err := delivery.NewStage(ctx, "dev", &delivery.StageArgs{Pipeline: pipeline})
if err != nil {
	return err
}
staging, err := delivery.NewStage(ctx, "staging", &delivery.StageArgs{Pipeline: pipeline, From: delivery.StageArray{dev}})
if err != nil {
	return err
}
prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{Pipeline: pipeline, From: delivery.StageArray{staging}})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var dev = new Stage("dev", new StageArgs { Pipeline = pipeline });
var staging = new Stage("staging", new StageArgs { Pipeline = pipeline, From = { dev } });
var prod = new Stage("prod", new StageArgs { Pipeline = pipeline, From = { staging } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var dev = new Stage("dev", StageArgs.builder().pipeline(pipeline).build());
var staging = new Stage("staging", StageArgs.builder().pipeline(pipeline).from(dev).build());
var prod = new Stage("prod", StageArgs.builder().pipeline(pipeline).from(staging).build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  dev:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
  staging:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
      from:
        - ${dev}
  prod:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
      from:
        - ${staging}
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_stage" "dev" {
  pipeline = delivery_pipeline.pipeline
}

resource "delivery_stage" "staging" {
  pipeline = delivery_pipeline.pipeline
  from     = [delivery_stage.dev]
}

resource "delivery_stage" "prod" {
  pipeline = delivery_pipeline.pipeline
  from     = [delivery_stage.staging]
}
```

{{% /choosable %}}

{{< /chooser >}}

A stage with several upstream stages waits until the same release has succeeded in each of them. Stage names must be unique within a pipeline.

A stage deploys one run at a time. When a newer run reaches a stage while an older run is still waiting for it, or waiting at its gate, the newer run takes its place. A run that has already entered the stage keeps it until it finishes.

<!-- TODO(launch): Say what happens to the older run when a newer one takes its place (canceled, or skips the stage). -->

{{% notes %}}
Pulumi Delivery doesn't detect cycles between stages. A run in a cycle waits until you cancel it.
{{% /notes %}}

## Gates

A gate is a rule on a stage that defines when a pipeline can progress. A release can't enter the stage until the rule passes.

Pulumi Delivery supports four kinds of gates, _manual_, _approval_, _decision_, and _HTTP_, and you can combine them into one rule. All of them are set in the stage's `when` property. Anyone with permission to approve the pipeline's runs can continue a manual gate. An approval gate names the people or teams who must approve and how many approvals it needs, shows them a preview of the changes, and lets them reject the release. A decision gate has TypeSafe's Jev model evaluate that preview against questions you write, and rejects the release if the risk is higher than you allow. An HTTP gate calls a URL until the response matches an expression you write, such as a health check that returns `"ok"`.

<!-- TODO(launch): Reconcile who can continue a manual gate: this paragraph says permission to approve runs, and the REST API section says write access to the pipeline stack. -->

### Manual gates

Manual gates pause the pipeline and wait for a person to continue them. You can use the gate's `description` property to help that person decide whether to do so:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.manual({ description: "Check the staging dashboards first." }),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
prod = delivery.Stage(
    "prod",
    pipeline=pipeline,
    from_=[staging],
    when=delivery.RuleArgs(kind="manual", description="Check the staging dashboards first."),
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{
	Pipeline: pipeline,
	From:     delivery.StageArray{staging},
	When: delivery.RuleArgs{
		Kind:        pulumi.String("manual"),
		Description: pulumi.String("Check the staging dashboards first."),
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var prod = new Stage("prod", new StageArgs
{
    Pipeline = pipeline,
    From = { staging },
    When = new RuleArgs { Kind = "manual", Description = "Check the staging dashboards first." },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var prod = new Stage("prod", StageArgs.builder()
    .pipeline(pipeline)
    .from(staging)
    .when(RuleArgs.builder()
        .kind("manual")
        .description("Check the staging dashboards first.")
        .build())
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  prod:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
      from:
        - ${staging}
      when:
        kind: manual
        description: Check the staging dashboards first.
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_stage" "prod" {
  pipeline = delivery_pipeline.pipeline
  from     = [delivery_stage.staging]
  when = {
    kind        = "manual"
    description = "Check the staging dashboards first."
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

Gates can be continued from the run page in the Pulumi Cloud console or with the REST API. See [Continuing a gate with the REST API](#continuing-a-gate-with-the-rest-api) for details.

### Approval gates

<!-- TODO(launch): Replace the next sentence with the pulumi-cloud shortcode for "delivery-approvals" once pulumi/marketing-web adds a hidden `delivery-approvals` feature (min_edition: pro). -->

Approval gates (available in the Pro and Enterprise editions) pause the pipeline until a set number of specified users or team members allow it to continue. List them in `approvers` as Pulumi usernames or team names, and set `count` to the number of approvals required (one by default):

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.approval({ approvers: ["platform-leads"], count: 2 }),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
prod = delivery.Stage(
    "prod",
    pipeline=pipeline,
    from_=[staging],
    when=delivery.RuleArgs(kind="approval", approvers=["platform-leads"], count=2),
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{
	Pipeline: pipeline,
	From:     delivery.StageArray{staging},
	When: delivery.RuleArgs{
		Kind:      pulumi.String("approval"),
		Approvers: pulumi.StringArray{pulumi.String("platform-leads")},
		Count:     pulumi.Int(2),
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var prod = new Stage("prod", new StageArgs
{
    Pipeline = pipeline,
    From = { staging },
    When = new RuleArgs { Kind = "approval", Approvers = { "platform-leads" }, Count = 2 },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var prod = new Stage("prod", StageArgs.builder()
    .pipeline(pipeline)
    .from(staging)
    .when(RuleArgs.builder()
        .kind("approval")
        .approvers("platform-leads")
        .count(2)
        .build())
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  prod:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
      from:
        - ${staging}
      when:
        kind: approval
        approvers:
          - platform-leads
        count: 2
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_stage" "prod" {
  pipeline = delivery_pipeline.pipeline
  from     = [delivery_stage.staging]
  when = {
    kind      = "approval"
    approvers = ["platform-leads"]
    count     = 2
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

Before approving, an approver sees a preview of the stack updates the stage will make. The preview doesn't cover jobs, because they run arbitrary commands. It can also be incomplete: a stack whose preview shows "Not available" might still change when the stage runs.

### Decision gates

{{< pulumi-cloud "pulumi-agents" />}}

A _decision gate_ evaluates whether a release can enter a stage based on the risk tolerance you define. It uses TypeSafe's Jev model to answer a set of yes-or-no questions about the stage's preview, and for each question, you set the highest risk you'll accept that the answer is yes. If any answer is riskier than you allow, the gate rejects the release and the run fails.

A decision gate evaluates only the preview of the stack updates the stage will make, so the stage needs at least one `Stacks` resource. Jobs, artifacts, and agent responses aren't part of the preview. Delivery gives the preview to Jev automatically.

For example, this gate stops a release if Jev thinks the `prod` stack updates delete a database:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.decision({
        questions: {
            dataLoss: {
                instructions: "Does the preview delete or replace a database or storage bucket?",
                maximumRisk: 0.05,
            },
        },
    }),
});

new delivery.Stacks("prodServices", {
    stage: prod,
    stacks: {
        api: { stack: "shop-api/prod", source: repo, directory: "api" },
    },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
prod = delivery.Stage(
    "prod",
    pipeline=pipeline,
    from_=[staging],
    when=delivery.RuleArgs(
        kind="decision",
        questions={
            "dataLoss": delivery.DecisionQuestionArgs(
                instructions="Does the preview delete or replace a database or storage bucket?",
                maximum_risk=0.05,
            ),
        },
    ),
)

delivery.Stacks(
    "prodServices",
    stage=prod,
    stacks={
        "api": {"stack": "shop-api/prod", "source": repo, "directory": "api"},
    },
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{
	Pipeline: pipeline,
	From:     delivery.StageArray{staging},
	When: delivery.RuleArgs{
		Kind: pulumi.String("decision"),
		Questions: delivery.DecisionQuestionMap{
			"dataLoss": delivery.DecisionQuestionArgs{
				Instructions: pulumi.String("Does the preview delete or replace a database or storage bucket?"),
				MaximumRisk:  pulumi.Float64(0.05),
			},
		},
	},
})
if err != nil {
	return err
}

_, err = delivery.NewStacks(ctx, "prodServices", &delivery.StacksArgs{
	Stage: prod,
	Stacks: delivery.StacksEntryMap{
		"api": delivery.StacksEntryArgs{Stack: pulumi.String("shop-api/prod"), Source: repo, Directory: pulumi.String("api")},
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var prod = new Stage("prod", new StageArgs
{
    Pipeline = pipeline,
    From = { staging },
    When = new RuleArgs
    {
        Kind = "decision",
        Questions =
        {
            ["dataLoss"] = new DecisionQuestionArgs
            {
                Instructions = "Does the preview delete or replace a database or storage bucket?",
                MaximumRisk = 0.05,
            },
        },
    },
});

new Stacks("prodServices", new StacksArgs
{
    Stage = prod,
    Stacks =
    {
        ["api"] = new StacksEntryArgs { Stack = "shop-api/prod", Source = repo, Directory = "api" },
    },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var prod = new Stage("prod", StageArgs.builder()
    .pipeline(pipeline)
    .from(staging)
    .when(RuleArgs.builder()
        .kind("decision")
        .questions(Map.of("dataLoss", DecisionQuestionArgs.builder()
            .instructions("Does the preview delete or replace a database or storage bucket?")
            .maximumRisk(0.05)
            .build()))
        .build())
    .build());

new Stacks("prodServices", StacksArgs.builder()
    .stage(prod)
    .stacks(Map.of(
        "api", StacksEntryArgs.builder().stack("shop-api/prod").source(repo).directory("api").build()))
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  prod:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
      from:
        - ${staging}
      when:
        kind: decision
        questions:
          dataLoss:
            instructions: Does the preview delete or replace a database or storage bucket?
            maximumRisk: 0.05
  prodServices:
    type: delivery:Stacks
    properties:
      stage: ${prod}
      stacks:
        api:
          stack: shop-api/prod
          source: ${repo}
          directory: api
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_stage" "prod" {
  pipeline = delivery_pipeline.pipeline
  from     = [delivery_stage.staging]
  when = {
    kind = "decision"
    questions = {
      dataLoss = {
        instructions = "Does the preview delete or replace a database or storage bucket?"
        maximum_risk = 0.05
      }
    }
  }
}

resource "delivery_stacks" "prodServices" {
  stage = delivery_stage.prod
  stacks = {
    api = {
      stack     = "shop-api/prod"
      source    = delivery_git_hub_source.repo
      directory = "api"
    }
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

For each question, Jev estimates the probability that the answer is yes. Delivery compares that estimate with the question's `maximumRisk`, a number from 0 to 1, and the gate passes only when every question is at or below its threshold.

{{% notes type="warning" %}}
If the stage's preview is larger than Jev's context window, the gate rejects the release and the run fails.
{{% /notes %}}

<!-- TODO(launch): Document recovery and diagnostics when the preview or the Jev evaluation is unavailable or fails. -->

### HTTP gates

An _HTTP gate_ holds a stage until an HTTP endpoint answers the way the pipeline expects. Use it with a health endpoint, a change-freeze calendar, an incident tool, or a feature-flag service. HTTP gates are available in every edition.

This gate holds `prod` until the health endpoint returns status 200 with `"ok"` in the body. Pulumi Cloud checks every five minutes, and the `Authorization` header comes from a secret in the pipeline's config:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const config = new pulumi.Config();
const healthToken = config.requireSecret("healthToken");

const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.httpOutput({
        url: "https://status.example.com/api/health",
        headers: { Authorization: pulumi.interpolate`Bearer ${healthToken}` },
        interval: "5m",
        successExpression: 'status == 200 && body.status == "ok"',
    }),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
config = pulumi.Config()
health_token = config.require_secret("healthToken")

prod = delivery.Stage(
    "prod",
    pipeline=pipeline,
    from_=[staging],
    when=delivery.RuleArgs(
        kind="http",
        url="https://status.example.com/api/health",
        headers={"Authorization": pulumi.Output.format("Bearer {0}", health_token)},
        interval="5m",
        success_expression='status == 200 && body.status == "ok"',
    ),
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
cfg := config.New(ctx, "")
healthToken := cfg.RequireSecret("healthToken")

prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{
	Pipeline: pipeline,
	From:     delivery.StageArray{staging},
	When: delivery.RuleArgs{
		Kind: pulumi.String("http"),
		Url:  pulumi.String("https://status.example.com/api/health"),
		Headers: pulumi.StringMap{
			"Authorization": pulumi.Sprintf("Bearer %s", healthToken),
		},
		Interval:          pulumi.String("5m"),
		SuccessExpression: pulumi.String(`status == 200 && body.status == "ok"`),
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var config = new Config();
var healthToken = config.RequireSecret("healthToken");

var prod = new Stage("prod", new StageArgs
{
    Pipeline = pipeline,
    From = { staging },
    When = new RuleArgs
    {
        Kind = "http",
        Url = "https://status.example.com/api/health",
        Headers =
        {
            ["Authorization"] = Output.Format($"Bearer {healthToken}"),
        },
        Interval = "5m",
        SuccessExpression = "status == 200 && body.status == \"ok\"",
    },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var config = ctx.config();

var prod = new Stage("prod", StageArgs.builder()
    .pipeline(pipeline)
    .from(staging)
    .when(RuleArgs.builder()
        .kind("http")
        .url("https://status.example.com/api/health")
        .headers(config.requireSecret("healthToken").applyValue(healthToken -> Map.of(
            "Authorization", "Bearer " + healthToken)))
        .interval("5m")
        .successExpression("status == 200 && body.status == \"ok\"")
        .build())
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
config:
  healthToken:
    type: string
    secret: true

resources:
  prod:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
      from:
        - ${staging}
      when:
        kind: http
        url: https://status.example.com/api/health
        headers:
          Authorization: Bearer ${healthToken}
        interval: 5m
        successExpression: status == 200 && body.status == "ok"
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
variable "healthToken" {
  type      = string
  sensitive = true
}

resource "delivery_stage" "prod" {
  pipeline = delivery_pipeline.pipeline
  from     = [delivery_stage.staging]
  when = {
    kind = "http"
    url  = "https://status.example.com/api/health"
    headers = {
      Authorization = "Bearer ${var.healthToken}"
    }
    interval           = "5m"
    success_expression = "status == 200 && body.status == \"ok\""
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

An HTTP rule takes these arguments:

- `url` (required): The address to call. It must use `https` and can't contain credentials. Pulumi Cloud calls only public addresses, so private, loopback, link-local, and cloud-metadata addresses are refused. Redirects aren't followed.
- `successExpression` (required): A [CEL](https://cel.dev) expression that returns a boolean. The gate passes when it's true. See [The success expression](#the-success-expression).
- `method`: `GET` (the default), `POST`, `PUT`, `PATCH`, or `HEAD`.
- `headers`: Request headers, up to 50. Values can be secret, which suits an `Authorization` header. You can't set headers that the HTTP client sets itself, such as `Host` and `Content-Length`.
- `body`: The request body, up to 16 KiB. It can be secret.
- `interval`: The time between checks, in whole seconds from `60s` to `1h`. The default is `1m`.
- `timeout`: The time allowed for one request, in whole seconds from `1s` to `20s`. The default is `10s`.
- `name` and `description`: Text for the console, as for other rules.

#### The success expression

The expression can use three variables:

- `status`: The HTTP status code, as an integer.
- `headers`: The response headers, as a map from lower-case header name to value.
- `body`: The parsed JSON if the response body is valid JSON, otherwise the body as a string. A response body larger than 64 KiB is an error.

An expression can be up to 1,024 bytes. Some examples:

| Expression | Passes when |
| --- | --- |
| `status == 200` | The endpoint returns 200. |
| `status in [200, 204]` | The status is 200 or 204. |
| `status == 200 && body.status == "ok"` | The status is 200 and the JSON field `status` is `"ok"`. |
| `body.checks.all(c, c.status == "ok")` | Every item in `checks` has the status `"ok"`. |
| `!body.checks.exists(c, c.status != "ok")` | No item in `checks` has another status. |
| `size(body.items) >= 3` | The `items` list has at least three entries. |
| `double(body.errors) / double(body.total) < 0.01` | The error rate is below 1 percent. |
| `headers["content-type"].contains("json")` | The response is JSON. |

Expressions support field and index access (`body.items[0]`, `headers["content-type"]`), `has()`, the `all` and `exists` macros, `&&`, `||`, `!`, the conditional `a ? b : c`, comparisons, `in` with a list of constants, `size()`, `contains()`, `startsWith()`, `endsWith()`, the conversions `int()`, `uint()`, `double()`, `bool()`, and `string()`, and arithmetic on numbers.

Expressions don't support `map`, `filter`, `exists_one`, `matches` (regular expressions), string or list concatenation, timestamps, or durations. A comparison needs a plain value on at least one side, so `body.status == "ok"` works but `body.a == body.b` doesn't. Arithmetic needs numbers, so convert response fields first, as in the error-rate example.

A field that's missing from the response makes the evaluation fail, and the gate keeps waiting. Guard optional fields with `has()`, as in `has(body.status) && body.status == "ok"`.

Numbers in a JSON body are read as floating point. Integers above 2^53 lose precision, so return such values as strings and compare them as strings.

#### How an HTTP gate behaves

Pulumi Cloud calls the URL every `interval` until a check passes. A check that doesn't pass never fails the run. The stage keeps waiting, and you cancel the run to stop waiting. A request can be repeated, so the endpoint must be safe to call more than once.

In the Pulumi Cloud console, the gate shows the result of the last check: the status code and whether the check passed, or the reason it failed, such as a timeout or an address that isn't allowed. The console never shows the URL, headers, body, or expression. The rule's `name` and `description` are visible, so don't put secrets in them. If a header or the body is secret, the whole rule is a secret value, but its name and description stay visible.

### Combining rules

You can also build composite rules that combine manual, approval, decision, and HTTP gates. In the following example, the pipeline is paused until `<your-colleague>` approves _and_ someone continues the `dashboards` check:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.allOfOutput({
        rules: [
            delivery.approvalOutput({ approvers: ["<your-colleague>"] }),
            delivery.manualOutput({ name: "dashboards", description: "Check the dashboards first." }),
        ],
    }),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
prod = delivery.Stage(
    "prod",
    pipeline=pipeline,
    from_=[staging],
    when=delivery.RuleArgs(
        kind="all",
        rules=[
            delivery.RuleArgs(kind="approval", approvers=["<your-colleague>"]),
            delivery.RuleArgs(kind="manual", name="dashboards", description="Check the dashboards first."),
        ],
    ),
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{
	Pipeline: pipeline,
	From:     delivery.StageArray{staging},
	When: delivery.RuleArgs{
		Kind: pulumi.String("all"),
		Rules: delivery.RuleArray{
			delivery.RuleArgs{
				Kind:      pulumi.String("approval"),
				Approvers: pulumi.StringArray{pulumi.String("<your-colleague>")},
			},
			delivery.RuleArgs{
				Kind:        pulumi.String("manual"),
				Name:        pulumi.String("dashboards"),
				Description: pulumi.String("Check the dashboards first."),
			},
		},
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var prod = new Stage("prod", new StageArgs
{
    Pipeline = pipeline,
    From = { staging },
    When = new RuleArgs
    {
        Kind = "all",
        Rules =
        {
            new RuleArgs { Kind = "approval", Approvers = { "<your-colleague>" } },
            new RuleArgs { Kind = "manual", Name = "dashboards", Description = "Check the dashboards first." },
        },
    },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var prod = new Stage("prod", StageArgs.builder()
    .pipeline(pipeline)
    .from(staging)
    .when(RuleArgs.builder()
        .kind("all")
        .rules(
            RuleArgs.builder()
                .kind("approval")
                .approvers("<your-colleague>")
                .build(),
            RuleArgs.builder()
                .kind("manual")
                .name("dashboards")
                .description("Check the dashboards first.")
                .build())
        .build())
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  prod:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
      from:
        - ${staging}
      when:
        kind: all
        rules:
          - kind: approval
            approvers:
              - <your-colleague>
          - kind: manual
            name: dashboards
            description: Check the dashboards first.
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_stage" "prod" {
  pipeline = delivery_pipeline.pipeline
  from     = [delivery_stage.staging]
  when = {
    kind = "all"
    rules = [
      {
        kind      = "approval"
        approvers = ["<your-colleague>"]
      },
      {
        kind        = "manual"
        name        = "dashboards"
        description = "Check the dashboards first."
      },
    ]
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

Composite rules can be of type `all` or `any`. `all`-type rules require that every rule in the rules list be satisfied, as in the previous example. `any`-type rules require at least one of them to be. You can nest rules up to three levels deep, counting the rules themselves: an `all` rule that contains an `any` rule that contains an approval is the deepest a gate can go.

Every rule takes an optional `name`, and names must be unique within a gate. An approval rule's name defaults to `approval` and a manual rule's to `manual`, so name each rule when a gate has two of the same kind.

## Continuing a gate with the REST API

Any credential with write access to the pipeline stack can continue a manual gate. To do it from another system, such as a deployment hook:

1. Read the run with `GET /api/preview/stacks/<org>/<project>/<stack>/delivery/runs/<run-number>`.
1. In `stages`, find the stage. If `stages[].gate.status` is `open`, note `stages[].gate.id`.
1. Send `POST .../delivery/runs/<run-number>/gates/<gate-id>/continue` with a JSON body:

    ```bash
    curl -X POST \
        -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{}' \
        https://api.pulumi.com/api/preview/stacks/acme/shop-delivery/main/delivery/runs/<run-number>/gates/<gate-id>/continue
    ```

A gate with one manual rule takes an empty JSON object. For a gate with several manual rules, pass the rule's name in `condition`, as in `{"condition": "dashboards"}`.

<!-- TODO(launch): Once the Delivery REST API is publicly documented, link this example to its API reference page. -->

## Stage actions

A stage normally takes whichever release reaches it next. Stage actions let you intervene when you need to, such as rolling back changes or pausing updates to that stage. You'll find them in the **Actions** menu on a stage's page in the Pulumi Cloud console or available via API.

Stage actions use your permissions rather than the service principal that deploys the pipeline. To do them, you need write access to the pipeline stack.

### Pausing and resuming a stage

Pause a stage when you need it to stay on its current release, for example while you investigate a problem in `prod`. No release enters a paused stage until someone resumes it. A run that's already deploying to the stage finishes, and runs that reach the stage while it's paused wait in its queue.

When you resume the stage, the newest waiting release enters it, as it would have if the stage hadn't been paused.

<!-- TODO: Pausing and resuming aren't in the audit log yet (DLV-392). Once they are, say so here and in the rollback item. -->

### Rolling back, redeploying, and force-promoting

Roll back, redeploy, and force-promote each start a new run that deploys one release to this one stage. The new run reuses the program commit, source commits, and recorded values of the run that first deployed that release, so it repeats what that release did rather than picking up anything newer. It skips the stage's gate and takes priority over other runs waiting for the stage.

- **Roll back** deploys a release that's older than the one the stage has now and that the stage already deployed successfully. A rollback also pauses the stage, so the newer release you rolled back from doesn't deploy over it. Resume the stage once you're ready for new releases. Keep in mind that a rollback restores everything in the older release, including any bugs that later releases fixed.
- **Redeploy** runs the stage's current release again, with the same commits and values as the run that first deployed it.
- **Force-promote** moves a release into the stage without waiting for the stage's gate. The release must already have succeeded in every upstream stage, because the stage reads their outputs. Each force-promote is recorded in your organization's audit log.

You can't roll back to, redeploy, or force-promote a release that came from [a local run](/docs/delivery/concepts/#run-locally). When a stage's current release is local, the stage's page shows it as **Deployed now** with a **Local** label, alongside its **Last cloud release**. To replace a local release, roll back to or force-promote a cloud release.

<!-- TODO(launch): Link the pipeline:* stage-action permissions (pipeline:pause, pipeline:rollback, pipeline:redeploy, pipeline:force_promote) to the RBAC scope reference once the nightly scope sync adds them. -->
<!-- TODO(launch): Once the Delivery REST API is publicly documented, add a "Stage actions with the REST API" subsection (POST .../delivery/stages/<stage>/{pause,resume,rollback,redeploy,promote}; rollback and promote take {"releaseNumber": <n>}; the run-starting ones return {"runNumber": <n>}) and link it to the API reference page. -->

## Artifacts

Artifacts are to pipelines what stack outputs are to stacks. An _artifact_ is a named value that a stage publishes once the release reaches it, such as a cluster endpoint, a database ID, or a container image tag. Other pipelines in your organization read it with a [`PipelineSource`](/docs/delivery/concepts/sources-and-triggers/#pipeline-sources). Artifacts are how one pipeline hands values to another without either one reaching into the other's stacks.

### Publishing an artifact

An `Artifact` resource names the stage that publishes it:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
new delivery.Artifact("clusterEndpoint", {
    stage: prod,
    value: cluster.outputs.apply(o => o["cluster"]["endpoint"]),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
delivery.Artifact(
    "clusterEndpoint",
    stage=prod,
    value=cluster.outputs.apply(lambda o: o["cluster"]["endpoint"]),
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
_, err = delivery.NewArtifact(ctx, "clusterEndpoint", &delivery.ArtifactArgs{
	Stage: prod,
	Value: cluster.Outputs.ApplyT(func(o map[string]map[string]interface{}) interface{} {
		return o["cluster"]["endpoint"]
	}),
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
new Artifact("clusterEndpoint", new ArtifactArgs
{
    Stage = prod,
    Value = cluster.Outputs.Apply(o => o["cluster"]["endpoint"]),
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
new Artifact("clusterEndpoint", ArtifactArgs.builder()
    .stage(prod)
    .value(cluster.outputs().applyValue(o -> (Object) o.get("cluster").get("endpoint")))
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  clusterEndpoint:
    type: delivery:Artifact
    properties:
      stage: ${prod}
      value: ${cluster.outputs["cluster"]["endpoint"]}
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_artifact" "clusterEndpoint" {
  stage = delivery_stage.prod
  value = delivery_stacks.cluster.outputs["cluster"]["endpoint"]
}
```

{{% /choosable %}}

{{< /chooser >}}

The value can be any structured value, such as a string, number, list, or map, and it can be secret. An artifact can't hold a file or binary data. It usually comes from the outputs of a stack update or a job in the same stage, as in this example, where `cluster` is a `Stacks` resource.

Other pipelines see an artifact once the release reaches its stage and the value is known. Because it belongs to a stage, a downstream pipeline that reads the `prod` stage only ever sees values from releases that `prod` deployed.

### Reading artifacts from other pipelines

A downstream pipeline can read an upstream pipeline's artifacts through a `PipelineSource`:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const platform = new delivery.PipelineSource("platform", {
    pipeline: "platform-delivery/main",
    stage: "prod",
    trigger: true,
});

const clusterEndpoint = platform.artifacts["clusterEndpoint"];
```

{{% /choosable %}}
{{% choosable language python %}}

```python
platform = delivery.PipelineSource(
    "platform",
    pipeline="platform-delivery/main",
    stage="prod",
    trigger=True,
)

cluster_endpoint = platform.artifacts["clusterEndpoint"]
```

{{% /choosable %}}
{{% choosable language go %}}

```go
platform, err := delivery.NewPipelineSource(ctx, "platform", &delivery.PipelineSourceArgs{
	Pipeline: pulumi.String("platform-delivery/main"),
	Stage:    pulumi.String("prod"),
	Trigger:  pulumi.Bool(true),
})
if err != nil {
	return err
}

clusterEndpoint := platform.Artifacts.MapIndex(pulumi.String("clusterEndpoint"))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var platform = new PipelineSource("platform", new PipelineSourceArgs
{
    Pipeline = "platform-delivery/main",
    Stage = "prod",
    Trigger = true,
});

var clusterEndpoint = platform.Artifacts.Apply(artifacts => artifacts["clusterEndpoint"]);
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var platform = new PipelineSource("platform", PipelineSourceArgs.builder()
    .pipeline("platform-delivery/main")
    .stage("prod")
    .trigger(true)
    .build());

var clusterEndpoint = platform.artifacts().applyValue(artifacts -> artifacts.get("clusterEndpoint"));
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  platform:
    type: delivery:PipelineSource
    properties:
      pipeline: platform-delivery/main
      stage: prod
      trigger: true

variables:
  clusterEndpoint: ${platform.artifacts["clusterEndpoint"]}
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_pipeline_source" "platform" {
  pipeline = "platform-delivery/main"
  stage    = "prod"
  trigger  = true
}

locals {
  cluster_endpoint = delivery_pipeline_source.platform.artifacts["clusterEndpoint"]
}
```

{{% /choosable %}}

{{< /chooser >}}

Pipeline sources return the artifacts of the latest release the specified stage deployed, including the artifacts that earlier stages published for that release.

### Secret artifacts

If any artifact is secret, the whole `artifacts` map is secret. A `Stacks` entry's `config` rejects secret values, so pass a secret artifact to a stack update or job in [`environment`](/docs/delivery/guides/cloud-credentials/#passing-credentials-through-the-pipeline) instead.

## Next steps

- Configure the [stacks and jobs](/docs/delivery/concepts/stacks-and-jobs/) each stage runs.
- Run a custom agent in a stage with an [`Agent`](/docs/delivery/concepts/agents/).
- Pass artifacts between pipelines in [Connecting pipelines](/docs/delivery/guides/multiple-pipelines/).
