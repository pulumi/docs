---
title: "Concepts"
---

A **Pulumi program** is just an ordinary program in your language of choice (currently JavaScript, TypeScript or Python with more languages on the way).  This program may use **packages** from your language’s package manager, just like usual programs can; for instance, a JavaScript program can use packages from NPM, a Python program can use packages from Pip/PyPI, and so on.  A program must have a **project** file named Pulumi.yaml in its root; this tells Pulumi where and how to begin executing the program, and gives it a name.

A program may require **configuration**.  For instance, the region your program will run in, sizes of various aspects of scaling (storage, CPU and RAM, numbers of instances), and even **secrets**, like passwords and tokens for connecting to services that you’re integrating with. Configuration and secrets are all stored outside of your program text to make it easy to deploy multiple instances of your program with different values.

Each instance of a Pulumi program is a **stack**.  A stack has a name, a set of configuration values unique to the stack, and a record of its current state.  Each stack represents one of the  environments in which the program runs, such as `staging`, `production` or `dev-alice`.  Each environment, thanks to having different configuration values, may have extremely different attributes: some may run in AWS, others in Azure; some may run with massive scale numbers, and others with the minimum needed for development and testing.

Each Pulumi stack has a collection of associated **resources**.  A resource defines and tracks an externally managed cloud resource - such as an AWS Lambda Function, a Kubernetes Pod or an Azure Virtual Network.  Each resource is managed by a **resource provider** which defines how creation, update and delete of resources should be managed in the target cloud environment. Developers can create and use **components** which are themselves composed of many resources.  Components make it possible to create and share new abstractions on top of raw cloud infrastructure resources.

A program can be deployed into a stack to **update** the resources managed by the stack to the new and updated set of resources defined by the program.  The impact of deploying a program into a stack can be **previewed** to see what resources wil be created, updated and deleted as part of the update.

## Lifecycle of a Pulumi Stack

It is helpful to consider the lifetimes of the concepts just described. 

A stack exists from the time it is created (`pulumi stack init`) until it is deleted (`pulumi stack rm`). During that time, it can have a number of deployments (`pulumi update` or `pulumi destroy`).  

Each deployment runs the program to determine what the desired state is, and then creates, updates or deletes various resources to achieve that desired state.  As a result, at any given point in time, the stack has a set of resources associated with it.

Some of those resources may have runtime code associated with them, which can run continuously throughout the lifetime of the resource (in the case of containers or VMs), or on-demand (in the case of serverless functions).

![Object Lifetimes](../images/reference/object-lifetimes-diagram.png){:width="500px"}

