---
title: "How Pulumi Works"
---

When a Pulumi program is deployed via `pulumi up`, there are a few processes involved. The _language host_ launches Node or Python and observes the running program. The host interacts with the Pulumi _engine_, which is the part of the CLI that determines which resource changes to make (if any). Any resource changes are then executed via an underlying _provider_, such as [AWS](./aws.html), [Azure](./azure.html), [Kubernetes](./kubernetes.html), and so on. The engine connects to pulumi.com to retrieve the stack's _checkpoint_, which stores the last known state of provisioned resources. 

During program execution, whenever there is a resource creation statement (via `new Resource()` in JavaScript or `Resource(...)` in Python), the resource is registered with the engine. This does not necessarily mean that a new resource should be created, it simply means that the program intends for the resource to exist. Using the last state in the checkpoint stored on pulumi.com, the engine determines which requests it should make to the underlying _provider_ in order to create, delete, or replace the resource. At the end the program execution, if a particular resource _R_ is never registered, the engine will make a delete request to the resource provider. The following diagram illustrates the interaction between these parts of the system.

![Pulumi engine and providers](../images/reference/engine-block-diagram.png){:width="600px"}

For instance, suppose we have the following Pulumi program, which creates two S3 buckets:

```javascript
const bucket = new aws.s3.Bucket("media-bucket");
const bucket = new aws.s3.Bucket("content-bucket");
```

Now, we run `pulumi stack init mystack`. Since `mystack` is a new stack, the "last deployed state" has no resources. 

Next, we run `pulumi up`. When the program runs to completion, it runs the two `new aws.s3.Bucket()` statements. So, the language host registers two resources with the engine.

The engine consults the last deployed state on pulumi.com, and determines that these resources do not already exist. So, the engine calls the AWS resource provider, requesting that it create a security group. Once the operation succeeds, this state is written to the last-deployed checkpoint. So, the resource list will be similar to the following:

```
stack mystack
   - aws.s3.Bucket "media-bucket653a4"
   - aws.s3.Bucket "content-bucket125ce"
```

Now, suppose we rename `content-bucket` to `app-bucket`:

```javascript
const bucket = new aws.s3.Bucket("media-bucket");
const bucket = new aws.s3.Bucket("app-bucket"); // renamed bucket
```

This time, the engine will not create another `media-bucket`, since it exists in the checkpoint. Now, since an S3 bucket cannot be renamed in place, the engine makes a "replace" call to the AWS provider. The provider deletes the bucket `content-bucket125ce` and creates a new one. 

## Creation and Deletion Order

A needed resource will be created or updated once all of the Inputs it depends on are satisfied.

If a needed resource does not already exist it will be created.

If a resource needs to be updated, the new instance will be created and then the old instance deleted *unless* you manually specify `name`, in which case pulumi will delete the old one before creating the new one.
