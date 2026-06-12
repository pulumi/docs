---
title: Dynamic environment variables
title_tag: Dynamic environment variables | Pulumi ESC
h1: Running commands with environment variables
meta_desc: Pulumi ESC allows you to securely run commands with managed environment variables using the pulumi esc run command, without exporting them to your shell.
menu:
  esc:
    name: Dynamic environment variables
    identifier: esc-dynamic-environmeant-variables
    parent: esc-environments
    weight: 6
---

The Pulumi CLI includes a [`pulumi esc run` command](/docs/iac/cli/commands/pulumi_env_run/) that allows you to run commands with Pulumi ESC managed environment variables, without exporting them to your shell.

You can run `pulumi esc run` using an environment:

```bash
$ pulumi esc run <environment-name> <command>
```

For example, to list your S3 buckets with the AWS CLI using environment variables from the `myorg/test` environment:

```bash
$ pulumi esc run myorg/test aws s3 ls
2023-10-10 16:09:19 my-s3-bucket
```

If you need to pass one or more flags to the command, prefix the command with `--`:

```bash
$ pulumi esc run myorg/test -- aws s3 ls s3://my-s3-bucket --recursive --summarize
...
Total Objects: 5087
   Total Size: 2419123156
```

For additional options and details, see `pulumi esc run --help`.
