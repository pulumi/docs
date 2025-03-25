---
title: "Node.js Native Binary Compilation Using vercel/pkg"
date: 2022-09-13
updated: 2025-03-10
meta_desc: "Learn how to build standalone native binaries for Node.js apps using vercel/pkg.
  Package your Node.js project for easy distribution without dependencies."

authors:
  - daniel-bradley
tags:
  - engineering
  - nodejs
  - publishing
  - providers

meta_image: "meta.png"
search:
  keywords:
    - vercel
    - compilation
    - native
    - pkg
    - js
    - binary
    - node
---

In Pulumi's engineering department, we often build and distribute tools as native binaries to avoid the need for additional dependencies on user machines. Most of these tools are written in Go, which has good support for building self-contained binaries that target modern operating systems.

While other Pulumi-supported languages like Node.js, Python, and .NET require additional runtime dependencies, it's possible to bundle dependencies with the program. In this article, we'll show you how to do that for a Node.js program.

This is a problem that can be solved using [vercel/pkg](https://github.com/vercel/pkg) command line tool. Here's the summary from their readme.

> This command line interface enables you to package your Node.js project into an executable that can be run even on devices without Node.js installed.

Let's take a look at how to use `pkg` and some issues we encountered on the way.

## Setting up `pkg`

### 1 - Install

`pkg` is distributed as an npm package which can be installed into your “devDependencies” using:

```bash
npm install -D pkg
```

or

```bash
yarn add -D pkg
```

or run without installing with npx:

```bash
npx pkg [args]
```

### 2 - Set `bin` in `package.json`

`pkg` will use [the bin field from your package.json](https://docs.npmjs.com/cli/v6/configuring-npm/package-json#bin) to find the entry point so you just have to specify a path to the directory containing your `package.json`.

```json
{
    "name": "my-program"
    "bin": "bin/index.js",
    ...
}
```

If no target is specified, then a set of defaults will be chosen for you. If the output path is not specified, `pkg` will infer the name from the package.json “name” field and write to the current working directory.

### 3 - Execute

The main inputs that `pkg` needs is:

* The entry point to your program for packaging
* The target machine to build for
* The output path to write the finished binary

Here’s an example of building the project in the current directory using node v18 for macOS ARM architectures:

```bash
# pkg [options] <input>
# -t, --targets        comma-separated list of targets
# -o, --output         output file name or template for several files
pkg -t node18-macos-arm64 -o bin/my-program .
```

It's possible to specify multiple targets in a comma-separated list to build them all at the same time, but it does come with the limitation where the output file names follow a fixed pattern. Instead, we chose to just run the `pkg` command multiple times with different arguments from our makefile in parallel as this fits with our existing workflows well.

## Issues encountered

### “Inspector Not Available”

As soon as we started executing the provider we started seeing some interesting warnings printed to the console stating “Inspector is not available” (here’s our [tracking issue](https://github.com/pulumi/pulumi-awsx/issues/848) and some [`pkg` discussion](https://github.com/vercel/pkg/issues/93)). This is because we use the Node.js Inspector API as part of our automatic closure serialization, however this is not available by default when packaging with `pkg`.

`pkg` provides an option to fix this by building your own base image with custom Node.js flags set to enable debugging. However, on investigation, these issues were caused by the Pulumi Typescript SDK creating and caching an inspector instance at the point of being imported even though we never actually call this code in our plugin. Therefore, we opted to make this eager singleton creation to be lazy – only created on first use, as we’re not using in our providers at this time.

### Unrunnable MacOS ARM binaries

When trying to use the binaries produced by our CI, we found that [the binaries weren’t runnable on MacOS ARM architectures](https://github.com/pulumi/pulumi-awsx/issues/850) - and were forcibly killed by the operating system.

This led me down quite a bit of a rabbit hole investigating signing of binaries, but it was actually resolved by simply installing the ‘ldid’ tool on our linux CI environments. The ldid source is available via [git.saurik.com/ldid](git://git.saurik.com/ldid.git) and binaries are available from various sources. Our solution was to use the [“Install Ldid” GitHub Action](https://github.com/marketplace/actions/install-ldid) to install the ldid binary and add it to the PATH in our CI workflow. My learning here is that sometimes reading the warnings in logs more carefully can save you lots of time!

### Static Binaries

One adjustment to our configuration came from a [community contribution by @afreakk](https://github.com/pulumi/pulumi-awsx/pull/862) where the provider was being used in a nixos environment. Nixos adds the requirement for all binaries to be static rather than dynamic - so there’s no requirement for the operating system to dynamically map link functions from system libraries at runtime. Statically compiled programs sometimes result in a larger size, but avoid any possible issues with different versions of the libraries it depends on.

To resolve this issue, it’s as simple as changing the ‘linux’ targets to ‘linuxstatic’. E.g. `node18-linux-amd64` becomes `node18-linuxstatic-amd64`.

## Multi-platform builds with a makefile

We use makefiles to build our providers, so here's a brief outline of how we build for multiple platforms using GNU Make.

```make
# Set the correct pkg TARGET for each binary we build
# when building for linux-amd64, set the pkg target to node18-linuxstatic-x64
bin/linux-amd64/my-program: TARGET := node18-linuxstatic-x64
# output binary file ^      ^ variable ^ pkg target
bin/linux-arm64/my-program: TARGET := node18-linuxstatic-arm64
bin/darwin-amd64/my-program: TARGET := node18-macos-x64
bin/darwin-arm64/my-program: TARGET := node18-macos-arm64
bin/windows-amd64/my-program.exe: TARGET := node18-win-x64

# Wildcard rule to build any of binary outputs
# "To build any bin file, ensure node_modules are up to date..."
bin/%: node_modules
    # "... then run pkg for actual output name & target"
    yarn run pkg . --target ${TARGET} --output $@
    # "TARGET" is the variable defined above, depending on the output
    # "$@" is the current makefile target - e.g. 'bin/linux-amd64/my-program'

# Running `make bins` will build all the listed outputs
bins: bin/linux-amd64/my-program
bins: bin/linux-arm64/my-program
bins: bin/darwin-amd64/my-program
bins: bin/darwin-arm64/my-program
bins: bin/windows-amd64/my-program.exe

# Let Make know that `bins` doesn't really exist (is phony) - it's just a helpful shortcut
.PHONY: bins
```

In summary the above code does the following:

1. Define each output file we need
    * Set the correct `pkg` `TARGET` for each output
2. Define a rule for building any binary output:
    * Ensure module_modules are up-to-date (this is another make target not shown here).
    * Run `pkg` with the `$TARGET` set in (1) and the name of the current output (`$@`).
3. Define `bins` "phony target" which builds all listed bins.

{{< related-posts >}}

## Recap

I hope this gives you a good overview of the vercel/pkg tool and how you can use it to create standalone programs using Node.js.

### Historical Note

We used to do a similar process using the [nexe project](https://github.com/nexe/nexe), but there’s been no releases since 2017 and therefore no support for newer versions of Node.js and we therefore consider this package as unmaintained at this point in time.
