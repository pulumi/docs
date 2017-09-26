---
layout: default
nav_section: "install"
---

# Installation and Setup

Follow these instructions to install the Pulumi Cloud SDK on your development or build machine.

For detailed instructions on using Pulumi, please refer to the <a href="/quickstart">Quickstart</a>.  For any
feedback or questions, please do not hesitate to [contact us](/contact) -- we'd love to hear from you!

## Download the SDK

The first step is to download a binary release suitable for your system.

### Featured Downloads

The current version of Pulumi's SDK is <b>0.6.1</b> (pre-release) and is available for these systems:

<div class="little-jumbotron">
    <div class="container">
        <h4 class="f4 title">Pulumi Cloud SDK</h4>
        <p>
            <a class="[ btn btn-lg ] [ white hover-white bg-brand hover-bg-accent2 no-underline ]"
                    style="padding-left: 12px; padding-right: 20px; padding-top: 8px; padding-bottom: 8px"
                    href="#" role="button">
                {% octicon cloud-download height:24 %} macOS x64
            </a>
            <a class="[ btn btn-lg ] [ white hover-white bg-brand hover-bg-accent2 no-underline ]"
                    style="padding-left: 12px; padding-right: 20px; padding-top: 8px; padding-bottom: 8px"
                    href="#" role="button">
                {% octicon cloud-download height:24 %} Windows x64
            </a>
            <a class="[ btn btn-lg ] [ white hover-white bg-brand hover-bg-accent2 no-underline ]"
                    style="padding-left: 12px; padding-right: 20px; padding-top: 8px; padding-bottom: 8px"
                    href="#" role="button">
                {% octicon cloud-download height:24 %} Linux x64
            </a>
        </p>
    </div>
</div>

We currently only provide pre-built binaries for x64 architectures on the following OS versions:

<ul>
    <li>macOS (f.k.a. OS X): Sierra</li>
    <li>Windows: 8 and 10</li>
    <li>Linux: Ubuntu Trusty 14.04 LTS</li>
</ul>

The binaries are likely to work on alternative versions and we are happy to provide builds for alternative
architectures (like x86) or OS versions as necessary.  Please [contact us for details](/contact).

## Installation and Setup

### Prerequisites

Before installing and using Pulumi's SDK, you'll need Node.js and an NPM package management client.

#### Node.js 6.10.2 (LTS)

First, install Node.js 6.10.2 (LTS).  This can be done by downloading and installing a package from the
[Node.js release page](https://nodejs.org/download/release/v6.10.2/), or by using the [Node Version Manager (nvm)](
https://github.com/creationix/nvm).  Links are included below for convenience.

<div class="little-jumbotron">
    <div class="container">
        <h4 class="f4 title">Node.js 6.10.2 (LTS)</h4>
        <p>
            <a class="[ btn btn-lg ] [ white hover-white bg-brand hover-bg-accent2 no-underline ]"
                    style="padding-left: 12px; padding-right: 20px; padding-top: 8px; padding-bottom: 8px"
                    href="https://nodejs.org/dist/v6.10.2/node-v6.10.2.pkg" role="button">
                {% octicon cloud-download height:24 %} macOS x64
            </a>
            <a class="[ btn btn-lg ] [ white hover-white bg-brand hover-bg-accent2 no-underline ]"
                    style="padding-left: 12px; padding-right: 20px; padding-top: 8px; padding-bottom: 8px"
                    href="https://nodejs.org/dist/v6.10.2/node-v6.10.2-x64.msi" role="button">
                {% octicon cloud-download height:24 %} Windows x64
            </a>
            <a class="[ btn btn-lg ] [ white hover-white bg-brand hover-bg-accent2 no-underline ]"
                    style="padding-left: 12px; padding-right: 20px; padding-top: 8px; padding-bottom: 8px"
                    href="https://nodejs.org/dist/v6.10.2/node-v6.10.2-linux-x64.tar.gz" role="button">
                {% octicon cloud-download height:24 %} Linux x64
            </a>
        </p>
    </div>
</div>

**Please note**: Pulumi *requires* Node.js 6.10.2 (LTS).  This ensures the environment that you are using locally
matches the version of the Node.js runtime used by AWS Lambda.  In the future, Pulumi intends to support additional
Node.js versions.  Please [let us know](/contact) if you need a specific version for your applications.

#### NPM or Yarn

Next, install an NPM client.  Either NPM itself or Yarn are fine choices, and you only need one:

* NPM comes with Node.js, so if this is your client of choice, you're done!  If you need to update or check your
  installation, please follow the [instructions](https://docs.npmjs.com/getting-started/installing-node) to do so.

* To install Yarn, a slightly faster client thanks to improved caching, follow the [installation instructions](
  https://yarnpkg.com/lang/en/docs/install/) and run `yarn --version` afterwards to ensure that it worked.

### Install the Pulumi Tools

First download the Pulumi SDK release for your operating system per the above instructions.

Next, choose an installation location and extract the release into it:

* On macOS and Linux, extract the `pulumi-v0.6.1-darwin-x64.tar.gz` or `pulumi-v0.6.1-linux-x64.tar.gz` tarball to the
  installation target and run `install.sh`.  We recommend `/opt/pulumi`.  For example:

```bash
$ tar -C /opt/pulumi -xzf pulumi-$VERSION-$OS-$ARCH.tar.gz
$ /opt/pulumi/install.sh
```

* On Windows, extract `pulumi-v0.6.1-windows-x64.zip` to the installation target and run  `install.cmd` from either a
  CMD or PowerShell shell.  We recommend `%SystemRoot%\Program Files\Pulumi`.

Afterwards, you'll need to add the installation's `bin` directory to you `PATH`.  This makes running `pulumi` CLI easy
and also ensures that dynamically loaded language and resource providers can be found:

* On macOS and Linux, add a line to your profile: `echo "export PATH=\$PATH:/opt/pulumi/bin" >> ~/.profile`.
* On Windows, add `%SystemRoot%\Program Files\Pulumi` to your `PATH` environment variable underneath system settings.

After doing this, the `pulumi` CLI will be available for creating, configuring, and deploying applications.  To verify
you have the tools installed and available on your `PATH`, try running `pulumi version`.  You should see:

```bash
$ pulumi version
Pulumi version 0.6.1
```

We're almost done, but not quite: Pulumi still needs to be told exactly how to talk with your favorite cloud provider.

### Configure AWS Credentials

Pulumi currently only supports AWS as a deployment target.  As a result, you will need to configure your system
so that Pulumi can communicate with AWS.  Pulumi does not store this information anywhere, and these credentials
must include sufficient IAM rights to deploy and manage resources in your AWS account.

The easiest way to configure your AWS credentials is to simply set the `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY` environment variables to the values given to you in the IAM console.  For example,
on macOS or Linux:

```bash
$ export AWS_ACCESS_KEY_ID=AK**************WORA
$ export AWS_SECRET_ACCESS_KEY=7n******************************6eLEKd8G
```

Of course the `**` strings should be replaced with your own credentials.

Alternatively, you can install the [AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) and use
it to configure yyour IAM credentials locally on your machine.  These will be stored and cached in your home directory:

```bash
$ aws configure
AWS Access Key ID [AK**************WORA]:
AWS Secret Access Key [7n******************************6eLEKd8G]:
Default region name [us-west-2]:
Default output format [None]:
```

In general, you can use any of the other configuration options documented on the [AWS SDK website](
http://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html).

### We're Done

And that's it -- you're done!

Now that we're finished installing, head on over to the [Quickstart](/quickstart) to to write our first Pulumi program!

