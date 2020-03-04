---
title: Kafka
meta_desc: This page provides an overview of the Kafka Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-kafka
    weight: 5
---

<img src="/logos/tech/kafka.png" align="right" class="h-16 px-8 pb-4">

The Kafka provider for Pulumi can be used to provision any of the resources available for Kafka.
The Kafka provider must be configured with credentials to deploy and update resources in Kafka.

See the [full API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/kafka" >}}) for complete details of the available Kafka provider APIs.

## Setup

The Kafka provider supports several options for providing access to Kafka credentials.  See the [Kafka setup page]({{< relref "setup" >}}) for details.

## Example

{{< langchoose csharp >}}

```javascript
const kafka = require("@pulumi/kafka")

const topic = new kafka.Topic("topic", {
  name: "sample-topic",
  replicationFactor: 1,
  partitions: 4,
});
```

```typescript
import * as kafka from "@pulumi/kafka";

const topic = new kafka.Topic("topic", {
  name: "sample-topic",
  replicationFactor: 1,
  partitions: 4,
});
```

```python
import pulumi_kafka as kafka

topic = kafka.Topic("topic",
  name="sample-topic",
  replication_factor=1,
  partitions=4,
)
```

```go
import (
  kafka "github.com/pulumi/pulumi-kafka/sdk/go/kafka"
)

topic, _ := kafka.NewTopic(ctx, "topic", &kafka.TopicArgs{
  Name: "sample-topic",
  ReplicationFactor: 1,
  Partitions: 4,
})
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Kafka;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var topic = new Topic("topic", new TopicArgs
            {
                Name = "sample-topic",
                ReplicationFactor = 1,
                Partitions = 4,
            });
        });
}
```

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/kafka`](https://www.npmjs.com/package/@pulumi/kafka)
* Python: [`pulumi-kafka`](https://pypi.org/project/pulumi-kafka/)
* Go: [`github.com/pulumi/pulumi-kafka/sdk/go/kafka`](https://github.com/pulumi/pulumi-kafka)
* .NET: [`Pulumi.Kafka`](https://www.nuget.org/packages/Pulumi.Kafka)

The Kafka provider is open source and available in the [pulumi/pulumi-kafka](https://github.com/pulumi/pulumi-kafka) repo.
