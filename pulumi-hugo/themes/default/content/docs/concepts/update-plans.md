---
title_tag: "Update Plans | Pulumi Concepts"
meta_desc: Learn about Pulumi update plans and how they can be used.
title: Update plans
h1: Update  plans
menu:
  concepts:
    weight: 10
aliases:
- /updateplans/
- /docs/intro/concepts/plans/
- /docs/intro/concepts/update-plans/
- /docs/intro/vs/
- /docs/concepts/plans/ 
---

{{% notes type="warning" %}}
Update plans are currently in experimental preview and will only show up in `--help` if the environment variable `PULUMI_EXPERIMENTAL` is set to `true`.
{{% /notes %}}

The result of previews can be saved to an _update plan_, this can then be used during a later update to
constrain the update only to the operations that were planned.

Constraining updates to plans may be useful in organizations with strict approval processes.

## Generate an update plan

To generate an update plan run `pulumi preview --save-plan=plan.json`. The plan will be written to the `plan.json` file.

## Use an update plan

To use an update plan run `pulumi up --plan=plan.json`, this will constrain the update to only the operations that were saved to the plan.

## Limitations

Update plans can only record information that is available at preview time. This means there are some program
constructs that while possible to run correctly at update time, can't be recorded at preview time.

The most common one is inputs set by the output of other resources that are being created. While the plan will
record that the program wants to set the input field, it can't record the value which it will be set with and
simply records `unknown`.

The next most common issue is creating resources inside an [`apply`
function](/docs/concepts/inputs-outputs/#apply). If the value for the apply is
unknown at preview time than the entire apply function will not run. This results in the plan not recording
anything for the resources created inside the apply and reporting an error at update time when they try to
create. This mostly comes up in the context of needing to create a resource for every item in an array, we
have [an issue on GitHub](https://github.com/pulumi/pulumi/issues/4834) tracking support for this.

The final issue is configuring explicit providers with unknown inputs. Providers configured with unknowns
currently do not do full checks and diffs of resources at preview time, this can result in the plan not
including information about default, or normalized values which then get set during the actual update.

The first limitation should not prevent the use of plans, it simply makes them a little harder to review and
not as strong a guarantee as to what the program will do. We will be looking at improving the precision here.

The other two are best worked around today by splitting your stacks up and using stack references to pass the
values forward. Stack reference values are never unknown (because the other stack must have run by the time
they're used).

## Format

The format of update plans is currently experimental and subject to change. The most up to date description of
the format is the [code](https://github.com/pulumi/pulumi/blob/master/sdk/go/common/apitype/plan.go).

Update plans as a feature will _not_ be deprecated, but the format of the JSON file could change.

## Example

Below is an example update plan file from previewing the creation of the [aws-typescript
template](https://github.com/pulumi/templates/tree/master/aws-typescript).

```json
{
    "manifest": {
        "time": "2022-11-15T11:38:20.7291898Z",
        "magic": "03503ad839446037795e489261c69ed98257c899e8d4e52abb8134db63afcdd3",
        "version": "3.46.2"
    },
    "config": {
        "aws:region": "us-east-1"
    },
    "resourcePlans": {
        "urn:pulumi:dev::examplets::aws:s3/bucket:Bucket::my-bucket": {
            "goal": {
                "type": "aws:s3/bucket:Bucket",
                "name": "my-bucket",
                "custom": true,
                "inputDiff": {
                    "adds": {
                        "__defaults": [
                            "acl",
                            "bucket",
                            "forceDestroy"
                        ],
                        "acl": "private",
                        "bucket": "my-bucket-6209a55",
                        "forceDestroy": false
                    }
                },
                "outputDiff": {},
                "parent": "urn:pulumi:dev::examplets::pulumi:pulumi:Stack::examplets-dev",
                "protect": false,
                "provider": "urn:pulumi:dev::examplets::pulumi:providers:aws::default_5_20_0::04da6b54-80e4-46f7-96ec-b56ff0331ba9",
                "customTimeouts": {}
            },
            "steps": [
                "create"
            ],
            "state": {
                "acl": "private",
                "bucket": "my-bucket-6209a55",
                "forceDestroy": false,
                "id": ""
            },
            "seed": "6PPrWjTx+PuWSaBVfirvdxH8JvVxKmUPPlvLirSDaFc="
        },
        "urn:pulumi:dev::examplets::pulumi:providers:aws::default_5_20_0": {
            "goal": {
                "type": "pulumi:providers:aws",
                "name": "default_5_20_0",
                "custom": true,
                "inputDiff": {
                    "adds": {
                        "region": "us-east-1",
                        "version": "5.20.0"
                    }
                },
                "outputDiff": {},
                "protect": false,
                "customTimeouts": {}
            },
            "steps": [
                "create"
            ],
            "state": {
                "region": "us-east-1",
                "version": "5.20.0"
            },
            "seed": "tunRRve9v1XHWU8kz/K22BpSx25+PZIUWSEvGdMlrB4="
        },
        "urn:pulumi:dev::examplets::pulumi:pulumi:Stack::examplets-dev": {
            "goal": {
                "type": "pulumi:pulumi:Stack",
                "name": "examplets-dev",
                "custom": false,
                "inputDiff": {},
                "outputDiff": {
                    "adds": {
                        "bucketName": "04da6b54-80e4-46f7-96ec-b56ff0331ba9"
                    }
                },
                "protect": false,
                "customTimeouts": {}
            },
            "steps": [
                "create"
            ],
            "state": {
                "bucketName": "04da6b54-80e4-46f7-96ec-b56ff0331ba9"
            },
            "seed": "H+gYmoW6MtpQibswnx9E8p4c3gMoGk2wJKtl9RDVKb0="
        }
    }
}
```

This is a textual representation of the goals, and operation steps that the program planned to take.

For the most part this should be readable without much internal knowledge of Pulumi, for example you can see
this plans on creating an `s3:Bucket` object called "my-bucket-6209a55". A lot of the other options correspond
directly to things you should be familiar with from Pulumi programs (such as parents, providers, custom or
 component resources).

 Some of the less obvious aspects of the above are the string `"04da6b54-80e4-46f7-96ec-b56ff0331ba9"` and the
 `"seed"` property. `"04da6b54-80e4-46f7-96ec-b56ff0331ba9"` is used to represent an unknown value, for
 example in the above the `bucketName` output didn't resolve to a concrete value at preview time, and so the
 plan recorded it as unknown. The `"seed"` property is used to ensure that when re-running with a plan set any
 "random" defaults (such as the "-6209a55" suffixed to the bucket name) are deterministic, when running an
 update with a plan the seeds from the plan will be used rather than new seeds being randomly generated.
