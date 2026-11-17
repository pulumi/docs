---
title_tag: Pulumi Delivery agents
meta_desc: Run a Pulumi custom agent as a step in a Pulumi Delivery stage, and use its structured response in later steps of the release.
title: Agents
h1: Agents
pulumi_cloud_feature: pulumi-agents
menu:
  delivery:
    name: Agents
    parent: delivery-concepts
    weight: 40
aliases: []
---

An `Agent` runs one of your [custom agents](/docs/ai/agents/custom/) as a step in a stage. Use it for work that needs judgment, such as summarizing what a release changes or reviewing it against a runbook. The agent returns a structured response that the rest of the pipeline can read.

To gate a stage on its preview, use a [decision gate](/docs/delivery/concepts/stages-and-gates/#decision-gates).

Each agent run counts toward your organization's Pulumi Agents usage and its [usage limits](/docs/ai/concepts/neo/usage-limits/).

## Adding an agent to a stage

An `Agent` names its `stage`, the custom agent to run, the `prompt` to send it, and a `responseSchema` that its final answer must match. This example asks a release-notes agent to summarize each release in `prod`, then publishes the summary as an [artifact](/docs/delivery/concepts/stages-and-gates/#artifacts):

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const notes = new delivery.Agent("releaseNotes", {
    stage: prod,
    agentDefinitionId: "<your-agent-id>",
    prompt: "Summarize the user-facing changes in this release.",
    responseSchema: {
        type: "object",
        properties: { summary: { type: "string" } },
        required: ["summary"],
    },
});

new delivery.Artifact("releaseSummary", {
    stage: prod,
    value: notes.response.apply(r => r["summary"]),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
notes = delivery.Agent(
    "releaseNotes",
    stage=prod,
    agent_definition_id="<your-agent-id>",
    prompt="Summarize the user-facing changes in this release.",
    response_schema={
        "type": "object",
        "properties": {"summary": {"type": "string"}},
        "required": ["summary"],
    },
)

delivery.Artifact(
    "releaseSummary",
    stage=prod,
    value=notes.response.apply(lambda r: r["summary"]),
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
notes, err := delivery.NewAgent(ctx, "releaseNotes", &delivery.AgentArgs{
	Stage:             prod,
	AgentDefinitionId: pulumi.String("<your-agent-id>"),
	Prompt:            pulumi.String("Summarize the user-facing changes in this release."),
	ResponseSchema: pulumi.Map{
		"type": pulumi.String("object"),
		"properties": pulumi.Map{
			"summary": pulumi.Map{"type": pulumi.String("string")},
		},
		"required": pulumi.StringArray{pulumi.String("summary")},
	},
})
if err != nil {
	return err
}

_, err = delivery.NewArtifact(ctx, "releaseSummary", &delivery.ArtifactArgs{
	Stage: prod,
	Value: notes.Response.ApplyT(func(r interface{}) interface{} {
		return r.(map[string]interface{})["summary"]
	}),
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var notes = new Agent("releaseNotes", new AgentArgs
{
    Stage = prod,
    AgentDefinitionId = "<your-agent-id>",
    Prompt = "Summarize the user-facing changes in this release.",
    ResponseSchema =
    {
        ["type"] = "object",
        ["properties"] = new Dictionary<string, object>
        {
            ["summary"] = new Dictionary<string, object> { ["type"] = "string" },
        },
        ["required"] = new[] { "summary" },
    },
});

new Artifact("releaseSummary", new ArtifactArgs
{
    Stage = prod,
    Value = notes.Response.Apply(r => ((ImmutableDictionary<string, object>)r)["summary"]),
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var notes = new Agent("releaseNotes", AgentArgs.builder()
    .stage(prod)
    .agentDefinitionId("<your-agent-id>")
    .prompt("Summarize the user-facing changes in this release.")
    .responseSchema(Map.of(
        "type", "object",
        "properties", Map.of("summary", Map.of("type", "string")),
        "required", List.of("summary")))
    .build());

new Artifact("releaseSummary", ArtifactArgs.builder()
    .stage(prod)
    .value(notes.response().applyValue(r -> ((Map<String, Object>) r).get("summary")))
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  releaseNotes:
    type: delivery:Agent
    properties:
      stage: ${prod}
      agentDefinitionId: <your-agent-id>
      prompt: Summarize the user-facing changes in this release.
      responseSchema:
        type: object
        properties:
          summary:
            type: string
        required:
          - summary
  releaseSummary:
    type: delivery:Artifact
    properties:
      stage: ${prod}
      value: ${releaseNotes.response["summary"]}
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_agent" "releaseNotes" {
  stage               = delivery_stage.prod
  agent_definition_id = "<your-agent-id>"
  prompt              = "Summarize the user-facing changes in this release."
  response_schema = {
    type = "object"
    properties = {
      summary = { type = "string" }
    }
    required = ["summary"]
  }
}

resource "delivery_artifact" "releaseSummary" {
  stage = delivery_stage.prod
  value = delivery_agent.releaseNotes.response["summary"]
}
```

{{% /choosable %}}

{{< /chooser >}}

The agent runs with the role, connected tools, and saved instructions of your custom agent. Its `prompt` can accept outputs from the stacks and jobs earlier in the pipeline run.

## How an agent runs

Delivery starts the agent after the release enters the stage and the outputs the agent depends on are ready. The agent's response is defined by `responseSchema` and returned as the `response` output. Downstream resources can use `response` the same way they use a job's `outputs`.

## Next steps

- Gate a stage on an evaluation of its preview with a [decision gate](/docs/delivery/concepts/stages-and-gates/#decision-gates).
- [Build a custom agent](/docs/ai/agents/custom/) for your pipeline to run.
