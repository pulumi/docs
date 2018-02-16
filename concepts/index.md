---
title: "Overview"
---

## What is Placeholder?

Short, high-level summary of Placeholder.

## Programs and config

A Placeholder program is authored in JavaScript/TypeScript or Python, with more languages supported in the future. The configuration is defined in `Pulumi.yaml`, 

- Tiny AWS+Javascript example

- Link to AWS, Azure, Kubernetes.

A placeholder program has configuration, defined in `Pulumi.yaml`, which can be accessed within your code. Link to config.

## Stacks, deployments, and resources

A Placeholder program is **deployed** to a **stack**. A stack is a target in which programs will run and typically denotes an environment (such as "staging" or "production"). A program becomes a running application by **deploying** it through `pulumi update` [LINK]. A deployment may be previewed before it is executed, via `pulumi preview` [LINK].

A deployment results in the creation, update, or deletion of one or more **resources**. A resource is typically an infrastructure component, such as a virtual machine, network security group, or AWS IAM role. Essentially, a Placeholder program "runs" through these interconnected cloud resources. 

A Placeholder program can also define application runtime code in addition to deployment-time code, when it uses the  higher-level `@pulumi/cloud` programming model (LINK). This means that there is a mixing of *phases*, part of the program runs at deployment time, and part at runtime.

It is helpful to consider the lifetimes of the concepts just described. A stack exists for a particular duration, during which time it can have a number of deployments. Deployments create and delete resources, generally with an overlap between creation of a new resource and creation of a new one. The final line in the diagram illustrates the running "application code," which is part of the Placeholder program, but not the program itself. Application code is either deployed through a mechanism outside of Placeholder (such as creating a custom Amazon Machine Image) or using  `@pulumi/cloud` components such as `cloud.Service` and `cloud.HttpEndpoint`. 

In particular, a resource like `cloud.HttpEndpoint` is implemented as serverless functions (such as AWS Lambda). So, an individual execution could just be a part of the underlying resource lifetime, such as the Lambda function definition itself.

![Object Lifetimes](../images/concepts/object-lifetimes-diagram.png){:width="500px"}

## Placeholder components

Describe "Engine/CLI" 

