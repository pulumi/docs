---
title: "Managing Secrets with Pulumi"
date: "2019-05-17"
meta_desc: "Pulumi supports automatic tracking of secret values, and client-side encryption, giving you full control over secrets encryption and decryption."
authors: ["matt-ellis"]
tags: ["Features","Security"]
---

We've had a 1st class concept of encrypted secrets configuration ever
since first releasing Pulumi. Customers have told us they love having
such a simple and easy way to ensure safe management of tokens, database
passwords, and more. Since launching, however, we've also heard that
you'd like more control over encryption and to see this protection
expanded to cover not just configuration, but all of the secret data
within their Pulumi deployments.

To support this, we've added two new features to Pulumi in our latest
0.17.12 release:

- Automatic tracking of secret values throughout a Pulumi program to
  ensure that all such values are always encrypted in the resulting
  state, no matter how they are used.
- A new option to use custom client-side encryption, instead of the
  default of using the Pulumi backend for encryption, to have full
  control over the secrets encryption and decryption.

Together, these features provide you with complete control over how
secrets are managed within Pulumi deployments. We have worked with
customers with advanced security and compliance needs while developing
this feature, enabling them to use our online hosted SaaS with even
greater confidence.
<!--more-->

## Secrets and State

Like many infrastructure as code systems, Pulumi uses a state file to
describe the current state of your infrastructure. When you run
`pulumi up`, Pulumi takes your existing state file, runs your program to
compute a new desired state and compares the two states. It makes
updates to the current state so it matches the desired state and updates
its state file as it does so. As part of this, Pulumi needs to retain
all the input values passed to resources in the state file, so it can
detect if they have changed from run to run.

While Pulumi has allowed you to pass `--secret` to force configuration
values to be encrypted before being stored in a stack's configuration
file, if you used these configuration values as inputs to resources,
they would be stored in plain text in the state file. While the state
file itself is stored securely (we encrypt all state files in transit
and at rest), anyone with access to the state file itself would be able
to see the plain text for all of these secrets.

By adding first class support for secrets with Pulumi, we are now able
to automatically track secrets across your program's execution and
ensure that secret values are encrypted in the state file. This means
you can use secrets confidently without worrying about accidentally
leaking plain text values. Let's take a look at how it works!

## Output and Secrets

To start, let's talk a bit about `Output`, one of the centerpieces of
the Pulumi programming model. `Output<T>` ties together a value (which
may not be ready yet, since it could depend on some data from a cloud
resource that is still being created) and resources that the output
depends on. When you create a resource with Pulumi, the properties of
that resource are `Output`'s that you can pass to other resources.
Pulumi uses the information tracked by `Output` to understand
dependencies between different resources. For example when an
`Output<string>` is used to construct a resource, Pulumi knows this
resource depends on any resources that were used to generate that
output. The underlying value that the `Output` wraps is what we store in
the state file as an input for this new resource.

With 0.17.11 of Pulumi, we now have `Output<T>` track if it contains
secret data. If it does, we ensure that the data is encrypted before we
store it in the state file. There are few ways to create secret
`Output`s today:

By fetching values from the `Config` object in the JavaScript and Python
SDKs, using the newly added `getSecret` or `requireSecret` (JavaScript)
and `get_secret` or `require_secret` (Python), as well as some type
specific overloads. These methods fetch the requested value from the
configuration bag and then wrap it up in an `Output` which is marked as
a secret.
By using `pulumi.secret` (JavaScript) or `pulumi.Output.secret` (Python)
to take an existing value and wrap it up in an `Output` which is marked
as a secret. These behave the same way as `pulumi.output` (JavaScript)
and `pulumi.Output.from_input` (Python) except they also mark the
returned output as a secret.
By retrieving an output that is marked as a secret from a resource.

When constructing a resource that has one or more secret inputs for a
property, the entire corresponding output property of the resource is
marked as a secret as well. In addition, as you combine outputs
together, via `all` or `apply`, the resulting output is marked as a
secret if any of the inputs values where themselves secrets. This means
that just like dependency information, the "secret-ness" of an output
flow naturally as you combine it with other data.

Let's take a look at a small program which creates an AWS Systems
Manager parameter, based on a secret configuration value.

Here's the program we'll be using:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const cfg = new pulumi.Config();
const secretMessage = cfg.requireSecret("secretMessage");

const param = new aws.ssm.Parameter("secretParameter", {
    type: "SecureString",
    value: secretMessage.apply(s => s.toUpperCase())
});

export const paramId = param.id;
export const paramValue = param.value;
```

In the above code sample, we're using the new `requireSecret` method to
pull out a configuration value as a secret. In addition, we use an
`apply` to transform the string to all uppercase before creating our SSM
Parameter. Because `secretMessage` was marked as a secret, this new
value is also marked as a secret. It's important to note the function
that runs during the `apply` has access to the unencrypted value, so you
need to be sure that your code inside the apply does not cause the
secret to leak (for example, don't write it to a text file!)

For a demo, let's create a new stack, target `us-west-2` in AWS and set
a secret message:

    $ pulumi stack init dev
    $ pulumi config set aws:region us-west-2
    $ pulumi config set --secret secretMessage "it's a secret to everybody"

Now, when we run `pulumi up` after creating a new stack, we'll see the
following preview:

    Previewing update (dev):

         Type                  Name              Plan
     +   pulumi:pulumi:Stack   secrets-blog-dev  create
     +   └─ aws:ssm:Parameter  secretParameter   create

    Resources:
        + 2 to create

If we look at the details for this deployment (before actually running
the update), we can see that the value of this resource has been marked
as a secret:

    + pulumi:pulumi:Stack: (create)
        [urn=urn:pulumi:dev::secrets-blog::pulumi:pulumi:Stack::secrets-blog-dev]
        + aws:ssm/parameter:Parameter: (create)
            [urn=urn:pulumi:dev::secrets-blog::aws:ssm/parameter:Parameter::secretParameter]
            name      : "secretParameter-1d79dca"
            type      : "SecureString"
            value     : "[secret]"

Once we've deployed our program, we can use `pulumi stack export` to
look at the state file for our deployment, we see that the value is
encrypted there as well (I've removed some uninteresting fields here,
for clarity):

    {
        "urn": "urn:pulumi:dev::secrets-blog::aws:ssm/parameter:Parameter::secretParameter",
        ...snip...
        "inputs": {
            ...snip...
            "name": "secretParameter-56f0ffb",
            "type": "SecureString",
            "value": {
                "4dabf18193072939515e22adb298388d": "1b47061264138c4ac30d75fd1eb44270",
                "ciphertext": "AAABAMo1ZLFpKzoHxUkGPXsUMjLBANri5fkPiveYUrjuMzsqONi2U1LnZSPxsN1vvFTs50skEru+Ff6N"
            }
        },
        "outputs": {
            ...snip...
            "name": "secretParameter-56f0ffb",
            "type": "SecureString",
            "value": {
                "4dabf18193072939515e22adb298388d": "1b47061264138c4ac30d75fd1eb44270",
                "ciphertext": "AAABAOjpCFOLHMzP4G9OXc4r+mQs6/4DJv2aWO+vX0LyYHLjfawAHWFlRmv3dErda6Ip48pRB19bBL9t"
            }
        }
        ...snip...
    }

As you can see, the value is encrypted in the state file for this
resource! Also note that because the value was marked as a secret input,
the corresponding copy in the output section of the state file was also
marked as a secret. Pulumi ensures that any outputs with the same names
as inputs which had secret data are also considered secrets. If there
are additional outputs you want to set as secrets, you can pass the
`additionalSecretOutputs` (JavaScript) or `additional_secret_outputs`
(Python) resource option when constructing a resource to provide a list
of other property names you want treated as secrets including computed
output properties of a resource which might be sensitive, like generated
passwords or access credentials.

## Configuring your secrets provider

You might be wondering how these values are actually encrypted. We use
the same encryption that we have always used for our configuration
system. This means when storing state with
<app.pulumi.com>, we use a key managed by the <app.pulumi.com> service, specific to your stack, to
encrypt everything. Some users have asked for more control over what key
is used (and the ability to use a key not managed by Pulumi at all!)

When creating a new stack (via `pulumi stack init` or `pulumi new`), you
may now pass `--secrets-provider passphrase` to specify that both
configuration secrets and secrets stored in the state file should be
encrypted using a key derived from a passphrase (if you've used Pulumi's
local state storage mode, this will be familiar to you). When you use a
passphrase, we use [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) to
derive a 32 byte encryption key, which we then use with the AES-256-GCM
encryption algorithm to encrypt your value (using a random 12 byte nonce
per value encrypted). Let's run through deploying the same code but
using the passphrase secret provider:

First, I create a new stack, setting the secrets provider to passphrase:

    $ pulumi stack init dev --secrets-provider passphrase
    Enter your passphrase to protect config/secrets:
    Re-enter your passphrase to confirm:
    Created stack 'dev'

As part of creating the stack, I had to enter a passphrase, which I'll
have to use during future updates. This passphrase is used to derive the
key used for both configuration and state management. I can now
configure my stack as I please:

    $ pulumi config set aws:region us-west-2
    $ pulumi config set secretMessage --secret "it's a secret to everybody"
    Enter your passphrase to unlock config/secrets
        (set PULUMI_CONFIG_PASSPHRASE to remember):

Note that to set the secret value, I had to provide my passphrase (since
it is needed to generate the key that is used to encrypt the value).

Finally, I can run `pulumi up`, here I'm prompted to enter my passphrase
again. I could also set `PULUMI_CONFIG_PASSPHRASE` in my environment.
You might do this locally as part of your local development loop (so you
don't have to type your passphrase over and over) or in your CI system
(where you'd be unable to type your passphrase in interactively).

    $ pulumi up
    Enter your passphrase to unlock config/secrets
        (set PULUMI_CONFIG_PASSPHRASE to remember):

If we use `pulumi stack export` again to examine the state file, we can
see that the structure of the ciphertext has changed:

    "value": {
        "4dabf18193072939515e22adb298388d": "1b47061264138c4ac30d75fd1eb44270",
        "ciphertext": "v1:qdfpSdF8vCWRJIDa:4gPQAMRSXi+5ap0koiZBsSVRnqzbp79cSEyWnLYkD9M5S/oI8qhgy521IBA="
    }

The change is because we are no longer using the Pulumi service to
encrypt or decrypt this data, instead the encryption and decryption
happens locally, the data never leaves your machine. So while I get to
continue to use <app.pulumi.com> to store state for my
stack, I don't have to worry about my secrets being encrypted with a key
managed by a third party.

Support for changing the secrets provider for an existing stack is on
its way. To track progress on this feature, please see GitHub issue
[pulumi/pulumi#481](https://github.com/pulumi/pulumi/issues/481).

## What's Next

In addition to passphrase based encryption, we plan to add support for
encrypting using AWS KMS, Azure KeyVault and GCP KMS in the coming
weeks.

The whole team is super excited about this feature and we love how
nicely we were able to integrate it into our overall programming model.
With these two new features, Pulumi users gain full control over how
their secrets are managed, but without sacrificing usability and
productivity. We're excited for you all to start playing around with it!
Pulumi is open source, free to use, and works today with variety of
clouds. Try it today!
