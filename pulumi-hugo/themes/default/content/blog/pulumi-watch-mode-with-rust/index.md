---
title: "Enabling Rapid Pulumi Prototyping with Rust"
date: 2022-09-21

meta_desc: >
    Enabling Pulumi watch mode on Apple Silicon and solving Go cross-compilation by building on Rust
meta_image: meta.png
authors:
    - aaron-friel
tags:
    - features
    - watch
    - rust
---

Pulumi enables engineers to employ the best practices of their field to infrastructure as code. The
`pulumi watch` command is an example of this, enabling rapid prototyping and a "hot reload" style
developer experience for prototyping Pulumi programs. In this post you'll see what watch mode
enables, the challenges encountered in maintaining the feature, and how we were able to use Rust to
bring that feature to more of our users.

<!--more-->

When developing a web application, hot reload frameworks enable quickly iterating and confirming the
divs are centered. When implementing new features, a test runner with a watch mode makes test-driven
development a breeze. In languages with an interactive shell, it's natural to use that to experiment
with new APIs. In each of these cases, engineers find value in being able to focus on writing code,
not typing console commands.

That's why [pulumi watch mode](/blog/pulumi-watch-mode-fast-inner-loop-development-for-cloud-infrastructure/)
exists and is one of my favorite features, and it's why I was disappointed to learn this feature was
not available to users on Apple Silicon Macs. As a Windows and Linux user, I discovered this while
root causing a Pulumi provider's failing build to the library used to implement watch mode. Thus
began a deep dive into cgo, file-watching libraries in Go, operating system event APIs, and finding
a solution for our build issues and missing feature.

To close this feature gap for one of our most important platforms, Pulumi v3.39.0 includes a binary
built with Rust to implement file-watching. `pulumi watch` works as it
always has. And as the first component to use the Rust language, it validated Pulumi's approach to
engineering of using the best languages and tools available.

## But first, what is and why use watch mode?

Watch mode monitors a project folder and automatically runs an equivalent to `pulumi up` with the
appropriate flags to skip prompts and displays simplified output. To see how quickly this can work,
I wrote a Pulumi TypeScript program to deploy an S3 bucket and bucket object "test.txt" before
writing a timestamp to the same file. That allows me to measure the inner loop with `pulumi watch`
or using an external program to run `pulumi up`. On each deployment, the program changes one of the
files in the directory kicking off the next deployment:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as fs from 'fs/promises'

const bucket = new aws.s3.Bucket("my-bucket");

const bucketObject = new aws.s3.BucketObject("my-bucket-object", {
    bucket: bucket.id,
    key: "test.txt",
    source: new pulumi.asset.FileAsset("test.txt"),
});

bucketObject.content.apply(() => {
  fs.appendFile('test.txt', `${new Date().valueOf()}\n`);
});
```

On a laptop with this simple program, `pulumi watch` consistently completed up to 50% faster, at 2.1
seconds per iteration than when using an external tool. Watch mode was more consistent, too: the
standard deviation over 50 samples was reduced to 46ms from 216ms. It does this while being easier
to remember and therefore use correctly, and with more terse output tuned for the use case of
quickly iterating on changes to a stack.

Watch mode has changed how I write infrastructure as code, and it brings that benefit to everyone
without needing to install and learn third-party tools for file-watching.

## The sad state of Go file-watching

Returning to the cross-compilation issue, the team found builds failed after updating
the Pulumi library dependency. Root causing this, I found that through a chain of Go package
dependencies, the file-watching library became a compilation unit in provider binaries. That library
had several reported issues with cross-compilation, with users reporting that it required enabling
cgo and building on macOS to target macOS.

That raised two flags. First, [cgo is not Go](https://dave.cheney.net/2016/01/18/cgo-is-not-go).
Using cgo entails wide-ranging side effects and results in a more complex build, packaging, and
support lifecycle. Second, continuous integration tools that support macOS runners are limited and
typically much higher cost. It was unacceptable to allow unintentional changes in a provider or the
Pulumi repository to impose those requirements on providers.

Why did the [notify library](https://github.com/rjeczalik/notify) have these constraints? This
library depended on C library support for a macOS API called FSEvents, and its Go source files
required a complex set of build tags. While this didn't seem impossible to work around, the library
remains unmaintained and would require us to maintain a fork to address these deficiencies. With no
recent contributions to the library to address this or a path to removing the cgo dependency, I had
to find another library.

The strongest candidate was the [fsnotify library](https://github.com/fsnotify/fsnotify). This library supported
the platforms required, did not require cgo, and supported cross-compilation. It did lack recursive
directory watching, though the repository listed it as a planned feature. However, in August the
maintainer archived the repository and stepped down from maintenance. Though contributors stepped up
to take over ownership of the repo, it left the state of the project in doubt. Without features like
recursive file watching, the team would have to maintain a fork. The search continued.

The last candidate looked at was the [watcher library](https://github.com/radovskyb/watcher/), which supported
recursive file watching across all platforms without cgo. Was this a panacea? Unfortunately, no. It
did this by falling back to the simplest method of file-watching: polling. This method works well
enough that the library has not changed in four years. The downside to polling is substantially
higher CPU usage and battery drain. It would also require workarounds for projects that contain
large folders of dependencies, such as a node.js node_modules or python venv directory. In spiking
on this, I was unsurprised to see that watching a folder with vendored dependencies was orders of
magnitude slower.

The Go language ecosystem lacks libraries that meet our needs. It was possible to watch only one
directory, or only support one operating system, or to be insensitive to performance concerns. I
needed an option that didn't make any of these sacrifices and, ideally, was also actively
maintained.

## From library to binary and the carcinization of Pulumi

One doesn't have to look hard to find CLIs that tackle this problem, many of which were at the top
of search results while looking for libraries. Using one of these as a plugin and reading stdout for
events instead would avoid any link-time dependency for providers. With this in mind, I considered
building a one-off binary using the previous utilities but ruled them out. The team would become de
facto maintainers of a fork of a complex library, in addition to needing to solve the deficiencies
identified above. That wasn't an innovation token I could spend.

I evaluated the complexity of building on the [watchman service](https://github.com/facebook/watchman), an
excellent file-watching CLI open-sourced by Facebook. Unfortunately, it would be costly to maintain
a wrapper with watchman as a dependency. While C++ isn't inaccessible, it does impose a complex
build system and a higher barrier to entry for engineers to contribute to it. And as both a client
and server application, it wouldn't be as simple as packaging a single binary and shelling out to
it.

Finally, I spiked on a library written in Rust, using the library underpinning the
[watchexec CLI](https://github.com/watchexec/watchexec). All-in, this worked out to just over 100
lines of code to maintain on top of the actively maintained watchexec libraries, with a similarly
small patch to the Pulumi CLI. And importantly, building the binary is a simple `cargo build` command that
the team can run on any platform. The
[watchutil-rs implementation](https://github.com/pulumi/watchutil-rs) lives in GitHub and is packaged as
pulumi-watch, a single-purpose binary that logs on stdout when files change.

Pulumi's mission is to enable everyone to apply the best programming languages and tools to
infrastructure as code. Implementing watch mode in Rust applied that principle to watch mode while
maintaining performance, moving the feature to a well-maintained footing, and expanding support to
every platform Pulumi supports.

Give [`pulumi watch`](/docs/cli/commands/pulumi_watch) a try with our
[getting started guide](/docs/quickstart/)!
