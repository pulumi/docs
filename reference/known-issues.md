---
title: "Known issues"
---

You should be aware of the following known issues and product limitations. The engineering team is actively working on fixing these issues. 

If you encounter an problem that's not on this list, please file a [GitHub issue](https://github.com/pulumi/pulumi/issues/new). <!-- validate the link once public -->

1.  **Errors after bypassing Pulumi for CloudFront resources.** When using AWS CloudFront resources with Pulumi, you can run into errors if you update the CloudFront resource directly through AWS, such as the AWS CLI or console. This known issue is anticipated to be solved in the v0.12.0 SDK, as part of implementing the fix [Perform a `Refresh` operation before each `Apply`. #57](https://github.com/pulumi/pulumi-terraform/issues/57).

    The CLI will show an error such as the following:

    ```
    rpc error: code 
      = Unknown desc = deleting urn:pulumi:stack::project::aws:cloudfront/distribution:Distribution::cdn-name: 
      PreconditionFailed: The request failed because it didn't meet the preconditions 
      in one or more request-header fields.
    ```

    This is because any CloudFront update operation (such as registering a new domain via Route53) rolls forward the [ETag](https://en.wikipedia.org/wiki/HTTP_ETag). Any future management operations must supply the latest ETag, or they will fail. Because Pulumi stores the last ETag in your stack checkpoint file, you must manually update the ETag value if you have managed CloudFront resources outside of Pulumi.

    You can update the ETag using the stack `import` and `export` operations:

    1.  Export the current stack checkpoint and copy to a new file:

        ```bash
        pulumi stack export > before.json # save current stack contents
        cp before.json after.json         # copy contents to a new file
        ```

    1.  Find the CloudFront distribution ID in `before.json`. 

    1.  Get the latest ETag for your CloudFront resource, using the distribution ID from the previous step:

        ```bash
        aws cloudfront get-distribution --id <ID> | grep -i etag
        ```
   
    1.  Edit `after.json` and replace the `"etag": "<OLD_VALUE>"` with the ETag you retrieved from the previous step.

    1.  To ensure the edit was performed correctly, perform a diff: `diff -c before.json after.json`. 

    1.  Import the new stack value via `pulumi stack import < after.json`. Now, future updates will be based on the correct ETag.

1.  **`pulumi destroy` uses current configuration, not previous** When performing a `pulumi destroy`, the current configuration (e.g. from `Pulumi.yaml`) is used, rather than the configuration at the time that the resources were created. To work around, roll back your config to the point where the resources were provisioned, then perform a `destroy` operation. See [Use old config when destroying resources #716](https://github.com/pulumi/pulumi/issues/716).

1.  **Cannot change project name in `Pulumi.yaml` when resources are provisioned**. The project name in `Pulumi.yaml` is assumed to be part of a stable identifier in identifying a stack (either a local or managed stack). Currently, renaming the project will result in all stack resources being orphaned. To work around this, run `pulumi destroy` before renaming the project. (If you have already changed the project name, simply change back to the old name and run `pulumi destroy`.) See [Changing `name` in Pulumi.yaml leads to assert #541](https://github.com/pulumi/pulumi/issues/541).