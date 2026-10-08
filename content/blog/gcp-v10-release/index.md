---
title: "Pulumi Google Cloud Provider Version 10.0.0"
date: 2026-10-06T08:00:00-07:00
draft: false
meta_desc: "Release of the v10 version of the Pulumi Provider for Google Cloud, with a migration guide and an agent skill to help you upgrade."
feature_image: feature.png
authors:
    - alberto-pose
tags:
    - google-cloud
    - releases
    - features
category: product
schema_type: auto
social:
    twitter:
    linkedin:
    bluesky:
---

**TL;DR: we are releasing a new major version of the Google Cloud provider. To migrate, ask Neo or your coding agent to run the Pulumi `provider-upgrade` skill ([how to use it](#use-an-agent-to-assist-with-your-upgrade)) or follow the [v10 migration guide](/registry/packages/gcp/how-to-guides/10-0-migration/).**

We are happy to announce the next major version of the Pulumi Google Cloud provider. This release is based on the new [v8 major version of terraform-provider-google](https://github.com/hashicorp/terraform-provider-google/releases/tag/v8.0.0) (see also the [upstream v8 upgrade guide](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/guides/version_8_upgrade)). It ships with a [migration guide](/registry/packages/gcp/how-to-guides/10-0-migration/) that covers every breaking change in depth.

<!--more-->

Here are a few links to help you get started if you are new to Pulumi:

- [Getting Started](/docs/iac/get-started/gcp/): a guided walkthrough for creating your first project
- [Setup & Install](/registry/packages/gcp/installation-configuration/): how to install the Google Cloud provider
- [How-to guides](/registry/packages/gcp/how-to-guides/): how to provision specific resources with the Google Cloud provider
- [Pulumi Neo](/product/neo/): ask Pulumi Neo to help you with your project

### Upgrading

The [migration guide](/registry/packages/gcp/how-to-guides/10-0-migration/) accounts for every resource, type and function that changed in the new version. For the most popular resources, it gives a description of the change, a risk and impact section, a way to check whether you are affected, and step by step migration snippets.

### Use an agent to assist with your upgrade

We have updated the `provider-upgrade` skill in [Pulumi Agent Skills](/blog/pulumi-agent-skills/) to cover the upgrade from v9. You can use it from [Pulumi Neo](/docs/ai/neo/) or from any popular coding agent. Before it bumps the provider, it scans your stack and code for the changes that affect you, and it stops to ask before anything that would replace or delete live infrastructure. Then it upgrades the dependency, runs `pulumi preview` until the diff is explained, and leaves `pulumi up` to you.

In Neo, ask: "Upgrade this project to pulumi-gcp v10." Neo picks the `provider-upgrade` skill for you; there is nothing to install or name.

![Neo task prompt asking to upgrade the project to pulumi-gcp v10, with the stack and repository attached](/blog/gcp-v10-release/migration-prompt.png)

Neo plans the upgrade, starting with a scan of your stack while it is still on v9.

![Neo's plan: verify the v9 baseline and scan state, bump pulumi-gcp to v10, fix SecretVersion, typecheck and preview, create a pull request](/blog/gcp-v10-release/neo-plan.png)

Before it edits any code, it tells you which resources are affected and what could be replaced, and waits for your answer.

![Neo reporting that only SecretVersion is affected, with the fix for each resource, and asking to proceed](/blog/gcp-v10-release/neo-risk-gate.png)

Finally, Neo opens a pull request with the changes and the preview results. You review it and run `pulumi up` when you are ready.

![Pull request opened by Neo changing secretDataWoVersion to a string and bumping @pulumi/gcp to 10.0.0](/blog/gcp-v10-release/neo-pr.png)

In Claude Code, add the Pulumi marketplace and install the `pulumi` plugin:

```bash
/plugin marketplace add pulumi/agent-skills
/plugin install pulumi
```

Then ask: "Upgrade this project to pulumi-gcp v10." You can also run `/provider-upgrade` directly.

In OpenAI Codex, register the marketplace:

```bash
codex plugin marketplace add pulumi/agent-skills
```

Then run `codex`, open `/plugins`, and install `pulumi`. Ask Codex to upgrade the provider to v10, or invoke the skill with `$provider-upgrade`.

In Pi, and in any other agent that supports the [Agent Skills](https://agentskills.io) standard, install the skill with the universal installer:

```bash
npx skills add pulumi/agent-skills/pulumi --skill provider-upgrade -a pi
```

Then ask Pi to upgrade the provider to v10, or trigger the skill with `/skill:provider-upgrade`.

### Why upgrade

Moving to the latest version means you keep getting the latest updates from Google Cloud. GCP is covered by our [provider support policy](/docs/support/provider-support-policy/): with this release, v9 receives security updates for up to 12 months (or until v11 ships), while new features, bug fixes, and upstream updates land only in v10.

Staying on the latest version also means you keep getting new features. Google Cloud offers capabilities you will not find on other clouds, such as TPUs, accelerators Google designed for training and serving AI models. For example, here is how you could create a [Cloud TPU v6e (Trillium)](https://docs.cloud.google.com/tpu/docs/v6e) slice with the new major version, using [`gcp.tpu.V2Vm`](/registry/packages/gcp/api-docs/tpu/v2vm/):

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as gcp from "@pulumi/gcp";

// A Cloud TPU v6e (Trillium) slice with 8 chips, on Spot capacity.
const tpu = new gcp.tpu.V2Vm("trillium", {
    zone: "us-east1-d",
    runtimeVersion: "v2-alpha-tpuv6e",
    acceleratorConfig: {
        type: "V6E",
        topology: "2x4",
    },
    schedulingConfig: {
        spot: true,
    },
    labels: {
        workload: "training",
    },
});

export const tpuName = tpu.name;
export const tpuWorkers = tpu.networkEndpoints.apply(eps => eps.map(ep => ep.ipAddress));
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_gcp as gcp

# A Cloud TPU v6e (Trillium) slice with 8 chips, on Spot capacity.
tpu = gcp.tpu.V2Vm(
    "trillium",
    zone="us-east1-d",
    runtime_version="v2-alpha-tpuv6e",
    accelerator_config={
        "type": "V6E",
        "topology": "2x4",
    },
    scheduling_config={
        "spot": True,
    },
    labels={
        "workload": "training",
    },
)

pulumi.export("tpu_name", tpu.name)
pulumi.export(
    "tpu_workers",
    tpu.network_endpoints.apply(lambda eps: [ep.ip_address for ep in eps]),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-gcp/sdk/v10/go/gcp/tpu"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// A Cloud TPU v6e (Trillium) slice with 8 chips, on Spot capacity.
		vm, err := tpu.NewV2Vm(ctx, "trillium", &tpu.V2VmArgs{
			Zone:           pulumi.String("us-east1-d"),
			RuntimeVersion: pulumi.String("v2-alpha-tpuv6e"),
			AcceleratorConfig: &tpu.V2VmAcceleratorConfigArgs{
				Type:     pulumi.String("V6E"),
				Topology: pulumi.String("2x4"),
			},
			SchedulingConfig: &tpu.V2VmSchedulingConfigArgs{
				Spot: pulumi.Bool(true),
			},
			Labels: pulumi.StringMap{
				"workload": pulumi.String("training"),
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("tpuName", vm.Name)
		ctx.Export("tpuWorkers", vm.NetworkEndpoints.ApplyT(func(eps []tpu.V2VmNetworkEndpoint) []string {
			ips := make([]string, len(eps))
			for i, ep := range eps {
				ips[i] = *ep.IpAddress
			}
			return ips
		}).(pulumi.StringArrayOutput))
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Gcp = Pulumi.Gcp;

return await Deployment.RunAsync(() =>
{
    // A Cloud TPU v6e (Trillium) slice with 8 chips, on Spot capacity.
    var tpu = new Gcp.Tpu.V2Vm("trillium", new()
    {
        Zone = "us-east1-d",
        RuntimeVersion = "v2-alpha-tpuv6e",
        AcceleratorConfig = new Gcp.Tpu.Inputs.V2VmAcceleratorConfigArgs
        {
            Type = "V6E",
            Topology = "2x4",
        },
        SchedulingConfig = new Gcp.Tpu.Inputs.V2VmSchedulingConfigArgs
        {
            Spot = true,
        },
        Labels =
        {
            { "workload", "training" },
        },
    });

    return new Dictionary<string, object?>
    {
        ["tpuName"] = tpu.Name,
        ["tpuWorkers"] = tpu.NetworkEndpoints.Apply(eps => eps.Select(ep => ep.IpAddress).ToList()),
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.gcp.tpu.V2Vm;
import com.pulumi.gcp.tpu.V2VmArgs;
import com.pulumi.gcp.tpu.inputs.V2VmAcceleratorConfigArgs;
import com.pulumi.gcp.tpu.inputs.V2VmSchedulingConfigArgs;
import java.util.Map;
import java.util.stream.Collectors;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // A Cloud TPU v6e (Trillium) slice with 8 chips, on Spot capacity.
            var tpu = new V2Vm("trillium", V2VmArgs.builder()
                .zone("us-east1-d")
                .runtimeVersion("v2-alpha-tpuv6e")
                .acceleratorConfig(V2VmAcceleratorConfigArgs.builder()
                    .type("V6E")
                    .topology("2x4")
                    .build())
                .schedulingConfig(V2VmSchedulingConfigArgs.builder()
                    .spot(true)
                    .build())
                .labels(Map.of("workload", "training"))
                .build());

            ctx.export("tpuName", tpu.name());
            ctx.export("tpuWorkers", tpu.networkEndpoints().applyValue(eps -> eps.stream()
                .map(ep -> ep.ipAddress().orElse(null))
                .collect(Collectors.toList())));
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  # A Cloud TPU v6e (Trillium) slice with 8 chips, on Spot capacity.
  trillium:
    type: gcp:tpu:V2Vm
    properties:
      zone: us-east1-d
      runtimeVersion: v2-alpha-tpuv6e
      acceleratorConfig:
        type: V6E
        topology: 2x4
      schedulingConfig:
        spot: true
      labels:
        workload: training

outputs:
  tpuName: ${trillium.name}
  tpuWorkers: ${trillium.networkEndpoints}
```

{{% /choosable %}}

{{< /chooser >}}

[Gemini Enterprise Agent Platform (formerly Vertex AI)](https://cloud.google.com/products/gemini-enterprise-agent-platform), Google's platform for building with Gemini models, also gets new resources. New in v10, [`gcp.vertex.AiRagCorpus`](/registry/packages/gcp/api-docs/vertex/airagcorpus/) brings its RAG Engine under Pulumi: declare the corpus that grounds your Gemini applications in your own documents, with its embedding model and vector store, in the same program as the rest of your infrastructure. It joins the [Agent Runtime](/registry/packages/gcp/api-docs/vertex/aireasoningengine/) and [Model Garden](/registry/packages/gcp/api-docs/vertex/aimodelgardenenablemodel/) resources added during v9. In the provider, these resources keep the `gcp.vertex` module name.

You can find more about this release in the [v10 release notes](https://github.com/pulumi/pulumi-gcp/releases/tag/v10.0.0). We hope your transition goes smoothly, and as always we are happy to hear your feedback in our [Community Slack](https://slack.pulumi.com/) or through [support](/support/) if you are a paying Pulumi customer. Happy hacking!
