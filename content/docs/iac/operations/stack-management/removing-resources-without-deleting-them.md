---
title_tag: "Removing resources from a stack without deleting them | Pulumi Operations"
meta_desc: "Stop Pulumi from managing a resource without deleting the underlying cloud infrastructure, using pulumi state delete or retainOnDelete."
title: Removing resources without deleting them
h1: Removing resources without deleting them
menu:
    iac:
        name: Removing resources without deleting them
        parent: iac-operations-stack-management
        weight: 32
---

Deleting a resource from a Pulumi program normally deletes the underlying cloud infrastructure too: that is the whole point of the desired-state model. But sometimes you want the opposite outcome: stop Pulumi from managing something while leaving the real resource untouched. Common reasons include handing a resource off to another team's stack, undoing a [`pulumi import`](/docs/iac/guides/migration/import/) that turned out to be premature, or decommissioning a project while a database or DNS zone it created keeps serving traffic elsewhere.

Pulumi supports this with two complementary tools: [`pulumi state delete`](/docs/iac/cli/commands/pulumi_state_remove/) for a one-time, interactive removal, and the [`retainOnDelete`](/docs/iac/concepts/resources/options/retainOnDelete/) resource option for a change you want to make part of your program and repeat safely in CI. Both leave the cloud resource exactly as it is; they only change what Pulumi tracks.

{{% notes type="info" %}}
This is the reverse of [importing a resource](/docs/iac/guides/migration/import/), which brings existing infrastructure under Pulumi's management. It is also different from an out-of-band deletion, where a resource was removed outside of Pulumi and you need to reconcile state with reality; for that case see [Detecting and reconciling drift](/docs/iac/operations/stack-management/drift/) and `pulumi refresh`.
{{% /notes %}}

## Remove a resource with `pulumi state delete`

To remove a single resource from a stack's state right now, from the command line, find its URN and pass it to `pulumi state delete`:

```bash
$ pulumi stack --show-urns
$ pulumi state delete 'urn:pulumi:prod::my-project::aws:s3/bucket:Bucket::my-bucket'
```

`pulumi state delete` only edits the state file. It does not call the resource provider, so the bucket keeps existing in AWS; Pulumi forgets about it. Once the delete completes, remove the corresponding resource declaration from your program as well, so a later `pulumi up` doesn't try to recreate it.

Two safeguards apply by default:

* **Dependent resources.** Pulumi refuses to delete a resource that other resources depend on or are parented to, since doing so would leave those dependents referencing a resource that state no longer tracks:

  ```
  error: urn:...::demo-pet can't be safely deleted because the following resources depend on it:
   * "demo-password" (urn:...::demo-password)

  Delete those resources first or pass --target-dependents.
  ```

  Pass `--target-dependents` to remove the resource and everything that depends on it in one operation, or delete the dependents individually first if you want to keep them under management.

* **Protected resources.** A resource with the [`protect`](/docs/iac/concepts/resources/options/protect/) option set can't be removed from state without an explicit override, the same way it can't be deleted by `pulumi up`:

  ```
  error: urn:...::demo-protected can't be safely deleted because it is protected. Re-run this command with --force to force deletion
  ```

  Either pass `--force`, or run [`pulumi state unprotect`](/docs/iac/cli/commands/pulumi_state_unprotect/) first and then delete normally. Running `pulumi state unprotect` is the better choice when you also want to remove the `protect: true` line from your program, since it leaves an explicit trail of the change.

`pulumi state delete` also accepts multiple URNs in a single invocation and an `--all` flag to clear every resource in the stack, which is useful when retiring a whole stack whose resources should live on outside Pulumi's management.

## Remove a resource declaratively with `retainOnDelete`

`pulumi state delete` is well suited to a one-time cleanup you run by hand, but it isn't something you want a CI pipeline invoking on your behalf: a mistyped URN or a stale pipeline run could remove the wrong resource from state with nobody watching. When the removal should happen as a normal part of `pulumi up`, set the [`retainOnDelete`](/docs/iac/concepts/resources/options/retainOnDelete/) resource option instead:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const bucket = new aws.s3.Bucket("my-bucket", {}, { retainOnDelete: true });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
bucket = aws.s3.Bucket("my-bucket", opts=pulumi.ResourceOptions(retain_on_delete=True))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
bucket, _ := s3.NewBucket(ctx, "my-bucket", &s3.BucketArgs{}, pulumi.RetainOnDelete(true))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var bucket = new Aws.S3.Bucket("my-bucket", new Aws.S3.BucketArgs(),
    new CustomResourceOptions { RetainOnDelete = true });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var bucket = new Bucket("my-bucket",
    BucketArgs.Empty,
    CustomResourceOptions.builder()
        .retainOnDelete(true)
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  bucket:
    type: aws:s3:Bucket
    options:
      retainOnDelete: true
```

{{% /choosable %}}

{{< /chooser >}}

With `retainOnDelete` set, remove the resource's declaration from your program and run `pulumi up`. Pulumi's preview reports the resource as a retained delete, and the update drops it from state without ever calling the provider's delete operation:

```
 -  aws:s3:Bucket  my-bucket  delete[retain]
```

Because the whole change lives in your program, it goes through the same review, preview, and CI process as any other update, which makes it the safer choice whenever more than one person might touch the resource or the removal needs to happen unattended.

Once a retained resource has been dropped from state this way, there's nothing left in your program or state to toggle `retainOnDelete` back on: the resource declaration is gone and Pulumi no longer tracks it. If you later decide the resource really should be deleted from the cloud provider, either delete it directly through the provider's own console or CLI, or [import it back into Pulumi](/docs/iac/guides/migration/import/) to bring it under management again, set `retainOnDelete` to `false`, and then remove the declaration and run `pulumi up` to delete it through Pulumi.

If instead you want to keep the resource under Pulumi's management but stop retaining it on a future delete, set `retainOnDelete: false` while the resource is still declared in your program and run `pulumi up`; this clears the retained flag without deleting anything, so a later removal of the resource's declaration deletes it from the cloud provider as usual.

## Choosing between the two

Use `pulumi state delete` for a one-off, interactive cleanup where you're at the keyboard and want the result immediately: undoing an accidental import, or removing a handful of resources while reorganizing a stack. Use `retainOnDelete` when the removal is driven by a code change that should go through your normal review and deployment process, especially in CI, or when you want the intent to remain visible in your program's history rather than living only in a one-off command you ran once.

## For Terraform users

Pulumi's equivalent of `terraform state rm` is `pulumi state delete`: both remove a resource from the tool's state while leaving the underlying infrastructure alone. Pulumi additionally lets you express the same intent as a resource option, `retainOnDelete`, so the removal travels through your program's normal review and deployment path.

## Related pages

* [Editing state files](/docs/iac/operations/stack-management/editing-state-files/) covers the full range of `pulumi state` subcommands, along with when hand-editing a state file is appropriate.
* [Importing resources](/docs/iac/guides/migration/import/) is the inverse operation: bringing existing infrastructure under Pulumi's management.
* [Protecting against undesired changes](/docs/iac/operations/stack-management/protecting-against-undesired-changes/) covers the `protect` option and other production safeguards referenced above.
* [Moving resources between stacks](/docs/iac/operations/stack-management/moving-resources-between-stacks/) uses `pulumi state move` to transfer a resource's state to a different stack instead of removing it outright.
