---
title: CrossGuard Frequently Asked Questions
meta_desc: This page contains Frequently Asked Questions about Pulumi CrossGuard and Policy Packs.
linktitle: Frequently Asked Questions
weight: 4

menu:
  userguides:
    parent: crossguard
---

## Is CrossGuard open source?

The [Pulumi Policy SDK](https://github.com/pulumi/pulumi-policy) that allows you to express policies and using the local `--policy-pack` flag (as part of the Pulumi CLI) to enforce Policy Packs is also open source.

Enforcing Policy Packs across an organization and viewing Policy Pack results in the Pulumi Console are part of Pulumi CrossGuard and are available to [Pulumi Enterprise]({{< relref "/pricing" >}}) organizations.

## How do Policy Packs enforced by the service interact with Policy Packs specified by the local Policy Pack flag?

Policy Packs enforced by the Pulumi Console are always run by the Pulumi CLI.

Therefore, if a Policy Pack is specified locally using `--policy-pack`, the Pulumi CLI will run the local Policy Pack as well as the Policy Packs enforced by the Pulumi Console. A violation by any of the Policy Packs would halt an update.

## What happens if a stack belongs to multiple Policy Groups?

If a stack belongs to multiple Policy Groups, the Pulumi Service will aggregate all required Policy Packs from those Policy Groups. Only one of version of each Policy Pack will be run per update.

This means that if a stack belongs to multiple Policy Groups that specify different versions of a Policy Pack, only the newest version of that pack will be run. For example, if a stack `my-stack` belongs to Policy Group `production-stacks` that requires Policy Pack `aws-policies` version 2 and Policy Group `platform-stacks` that requires Policy Pack `aws-policies` version 4, only version 4 of `aws-policies` would be run. In the case that a stack has the same version of a Policy Pack with different configuration enabled, the most recently modified Policy Pack and configuration will be enforced.

Under a stack's "Settings" tab you can take a look at the Policy Packs that would be enforced on a `preview` or `update` as well as the Policy Groups that the stack belongs to.

![Stack Policy Settings](/images/docs/guides/crossguard/stack-policies.jpg)

## How does Policy as Code work during a stack import or refresh?

During `pulumi stack import`, Policy Packs are not run. This command does not modify any resources and simply allows you to make manual changes to the state file. During the next update, the resources and state file would be updated based on the stack's Pulumi program, which must be in compliance to succeed.

During `pulumi refresh`, no resources are modified. This command simply updates the state file with the current state of the resources. If there are out-of-compliance resources that get consumed into the state file during the `pulumi refresh` command, they will be updated during the next update to reflect the declared infrastructure from the stack's Pulumi program. The Pulumi program must be in compliance with the required Policy Packs for the update to be successful.

## What happens if I add a Policy Pack that causes an existing resource to become out-of-compliance?

The next preview or update of the stack with fail due to the policy violation. The stack will need to be fixed before it can be updated.

A stack with out-of-compliance resources can be destroyed.

## How do I version a Policy Pack?

Policy Packs that are published to the service require a version. The Policy Pack version is specified in the `package.json` file for TypeScript/JavaScript (Node.js) packs. The example below shows a Policy Pack version specified as `0.1.0`.

```json
{
    ...
    "version": "0.1.0",
    ...
}
```

For Python Policy Packs, the version is specified in the `PulumiPolicy.yaml` file.

```yaml
version: 0.1.0
```

A version can only be used one time and once published the version can never be used by that Policy Pack again.

## How are secrets handled in policies?

Encrypted [secrets]({{< relref "/docs/intro/concepts/secrets#secrets" >}}) are decrypted during previews and updates. Any policy that is run against a stack can access the values in plaintext. It is up to you to treat these values sensitively and only run policies that you trust.

## How are dependencies managed with Python Policy Packs?

As of Pulumi 2.4.0, new Python Policy Packs created with `pulumi policy new` will have a virtual environment created in a `venv` directory with required dependencies from `requirements.txt` installed in it, and Pulumi will automatically use this virtual environment when running the program.

This behavior is controlled by the following `virtualenv` `runtime` option in `PulumiPolicy.yaml`:

```yaml
runtime:
  name: python
  options:
    virtualenv: venv
```

`virtualenv` is the path to a virtual environment to use.

Existing Python Policy Packs can opt-in to using the built-in virtual environment support by setting the `virtualenv` option. To manually create a virtual environment and install dependencies, run the following commands in your Policy Pack directory:

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

```bash
$ python3 -m venv venv
$ venv/bin/pip install -r requirements.txt
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
$ python3 -m venv venv
$ venv/bin/pip install -r requirements.txt
```

{{% /choosable %}}

{{% choosable os windows %}}

```bat
> python -m venv venv
> venv\Scripts\pip install -r requirements.txt
```

{{% /choosable %}}

{{< /chooser >}}

If you prefer to manage the virtual environment on your own (for example, using tools like [Pipenv](https://github.com/pypa/pipenv)), you can delete the local `venv` directory and unset the `virtualenv` option in `PulumiPolicy.yaml`:

```yaml
runtime: python
```

When managing the virtual environment on your own and [running the Policy Pack locally]({{< relref "/docs/get-started/crossguard/authoring-a-policy-pack#running-locally" >}}) against a Pulumi program, you'll need to run any `pulumi` commands (such as `pulumi up`) from an activated virtual environment shell (or, if using a tool like [Pipenv](https://github.com/pypa/pipenv), prefix any `pulumi` commands with `pipenv run pulumi ...`). If the Pulumi program is also Python, both the Policy Pack and Pulumi program can use the same virtual environment.

Enforced Policy Packs that are published to the Pulumi Console will automatically create a virtual environment, install dependencies in the virtual environment, and use the virtual environment when running against a Pulumi stack.

### Adding a new dependency

To install a new dependency in the virtual environment, add an entry to `requirements.txt`, and run the following in your Policy Pack directory:

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

```bash
$ venv/bin/pip install -r requirements.txt
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
$ venv/bin/pip install -r requirements.txt
```

{{% /choosable %}}

{{% choosable os windows %}}

```bat
> python -m venv venv
> venv\Scripts\pip install -r requirements.txt
```

{{% /choosable %}}

{{< /chooser >}}
