---
layout: default
nav_section: "quickstart"
---

<p><a href="/quickstart">Quickstart</a> &gt; <b>Further Reading</b></p>

# Further Reading

This section contains some additional further reading on the following topics:

* [Pulumi CLI](#pulumi-cli)
* [Using Typescript](#using-typescript)
* [Next Steps](#next-steps)

## Pulumi CLI

The `pulumi` CLI supports creating, configuring and updating Pulumi stacks.

An __stack__ represents a running Pulumi program.  `pulumi stack init` creates a new Pulumi stack for the
program in the working directory. Multiple stacks can be managed in a single program directory, and you can
see all environments with `pulumi stack ls`.

Each environment has an associated set of __config__.  The config is a set of key value pairs which are available to
your Pulumi program.

The running application can be __updated__, combining the current config with the current version of the program in the
working directory and deploying those updates into the running application - updating any necessary infrastructure and
deploying any new code or resources into the application.

An update can be __previewed__, displaying a summary of the expected changes that will be made during an update
operation based on the current state of the program and config.  This preview is a conservative summary - it will
include updates which may not need to be made depending on the results of applying some of the changes to the target
infrastructure.

```
Usage:
  pulumi [command]

Available Commands:
  config      Manage configuration
  destroy     Destroy an existing stack and its resources
  help        Help about any command
  init        Initialize a new Pulumi repository
  login       Log into the Pulumi Cloud Console
  logout      Log out of the Pulumi CLI
  logs        Show aggregated logs for a project
  preview     Show a preview of updates to an stack's resources
  stack       Manage stacks
  update      Update the resources in an stack
  version     Print Pulumi's version number

Flags:
  -C, --cwd string       Run pulumi as if it had been started in another directory
  -h, --help             help for pulumi
      --logflow          Flow log settings to child processes (like plugins)
      --logtostderr      Log to stderr instead of to files
      --tracing string   Emit tracing to a Zipkin-compatible tracing endpoint
  -v, --verbose int      Enable verbose logging (e.g., v=3); anything >3 is very verbose

Use "pulumi [command] --help" for more information about a command.
```

__pulumi stack__

```
Manage stacks

An stack is a named update target, and a single project may have many of them.
Each stack has a configuration and update history associated with it, stored in
the workspace, in addition to a full checkpoint of the last known good update.

Usage:
  pulumi stack [flags]
  pulumi stack [command]

Available Commands:
  init        Create an empty stack with the given name, ready for updates
  ls          List all known stacks
  rm          Remove an stack and its configuration
  select      Switch the current workspace to the given stack

Flags:
  -h, --help        help for stack
  -i, --show-ids    Display each resource's provider-assigned unique ID
  -u, --show-urns   Display each resource's Pulumi-assigned globally unique URN

Global Flags:
  -C, --cwd string       Run pulumi as if it had been started in another directory
      --logflow          Flow log settings to child processes (like plugins)
      --logtostderr      Log to stderr instead of to files
      --tracing string   Emit tracing to a Zipkin-compatible tracing endpoint
  -v, --verbose int      Enable verbose logging (e.g., v=3); anything >3 is very verbose

Use "pulumi stack [command] --help" for more information about a command.
```

__pulumi config__

```
Lists all configuration values for a specific stack. To add a new configuration value, run
'pulumi config set', to remove and existing value run 'pulumi config rm'. To get the value of
for a specific configuration key, use 'pulumi config get <key-name>'.

Usage:
  pulumi config [flags]
  pulumi config [command]

Available Commands:
  get         Get a single configuration value
  rm          Remove configuration value
  set         Set configuration value

Flags:
  -h, --help           help for config
      --show-secrets   Show secret values when listing config instead of displaying blinded values
  -s, --stack string   Operate on a different stack than the currently selected stack

Global Flags:
  -C, --cwd string       Run pulumi as if it had been started in another directory
      --logflow          Flow log settings to child processes (like plugins)
      --logtostderr      Log to stderr instead of to files
      --tracing string   Emit tracing to a Zipkin-compatible tracing endpoint
  -v, --verbose int      Enable verbose logging (e.g., v=3); anything >3 is very verbose

Use "pulumi config [command] --help" for more information about a command.
```

__pulumi update__

```
Update the resources in an stack

This command updates an existing stack whose state is represented by the
existing snapshot file. The new desired state is computed by compiling and evaluating an
executable package, and extracting all resource allocations from its resulting object graph.
These allocations are then compared against the existing state to determine what operations
must take place to achieve the desired state. This command results in a full snapshot of the
stack's new resource state, so that it may be updated incrementally again later.

The package to execute is loaded from the current directory. Use the `-C` or `--cwd` flag to
use a different directory.

Usage:
  pulumi update [flags]

Aliases:
  update, up

Flags:
      --analyzer stringSlice     Run one or more analyzers as part of this update
  -d, --debug                    Print detailed debugging output during resource operations
  -h, --help                     help for update
  -p, --parallel int             Allow P resource operations to run in parallel at once (<=1 for no parallelism)
      --show-config              Show configuration keys and variables
      --show-replacement-steps   Show detailed resource replacement creates and deletes instead of a single step (default true)
      --show-sames               Show resources that needn't be updated because they haven't changed, alongside those that do
  -s, --stack string             Choose an stack other than the currently selected one
      --summary                  Only display summarization of resources and operations

Global Flags:
  -C, --cwd string       Run pulumi as if it had been started in another directory
      --logflow          Flow log settings to child processes (like plugins)
      --logtostderr      Log to stderr instead of to files
      --tracing string   Emit tracing to a Zipkin-compatible tracing endpoint
  -v, --verbose int      Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

__pulumi preview__

```
Show a preview of updates an stack's resources

This command displays a preview of the updates to an existing stack whose state is
represented by an existing snapshot file. The new desired state is computed by compiling
and evaluating an executable package, and extracting all resource allocations from its
resulting object graph. These allocations are then compared against the existing state to
determine what operations must take place to achieve the desired state. No changes to the
stack will actually take place.

The package to execute is loaded from the current directory. Use the `-C` or `--cwd` flag to
use a different directory.

Usage:
  pulumi preview [flags]

Aliases:
  preview, pre

Flags:
      --analyzer stringSlice     Run one or more analyzers as part of this preview
  -d, --debug                    Print detailed debugging output during resource operations
  -h, --help                     help for preview
  -p, --parallel int             Allow P resource operations to run in parallel at once (<=1 for no parallelism)
      --show-config              Show configuration keys and variables
      --show-replacement-steps   Show detailed resource replacement creates and deletes instead of a single step
      --show-sames               Show resources that needn't be updated because they haven't changed, alongside those that do
  -s, --stack string             Choose an stack other than the currently selected one
      --summary                  Only display summarization of resources and operations

Global Flags:
  -C, --cwd string       Run pulumi as if it had been started in another directory
      --logflow          Flow log settings to child processes (like plugins)
      --logtostderr      Log to stderr instead of to files
      --tracing string   Emit tracing to a Zipkin-compatible tracing endpoint
  -v, --verbose int      Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

## Using TypeScript

You can write Pulumi programs in TypeScript to get additional verification and tooling benefits.  To use TypeScript,
apply the following four steps to an existing project.

First, update your `package.json` to look like the following (with your own values for `name`, `version`, etc.).  This
is what tells Node.js and NPM what packages you depend on, where to find your code's entrypoints, and so on:

```json
{
    "name": "webserver",
    "version": "0.1",
    "main": "bin/index.js",
    "typings": "bin/index.d.ts",
    "scripts": {
        "build": "tsc"
    },
    "devDependencies": {
        "typescript": "^2.1.4"
    },
    "peerDependencies": {
        "@pulumi/aws": "*",
        "@pulumi/pulumi-fabric": "*"
    },
    "dependencies": {
        "@types/node": "^8.0.26"
    }
}
```

Feel free to customize this in any way you please, such as adding test scripts, dependencies on any NPM packages you'd
like to use in your Cloud Application, and so on.  For more information on `package.json`, please refer to [the NPM
documentation](https://docs.npmjs.com/files/package.json).

Second, run `yarn install` to install the dependencies to your `node_modules` directory.

Third, create a `tsconfig.json` file with the TypeScript compiler settings and a list of your program files:

```json
{
    "compilerOptions": {
        "outDir": "bin",
        "target": "es6",
        "module": "commonjs",
        "moduleResolution": "node",
        "declaration": true,
        "sourceMap": true,
        "stripInternal": true,
        "experimentalDecorators": true,
        "pretty": true,
        "noFallthroughCasesInSwitch": true,
        "noImplicitAny": true,
        "noImplicitReturns": true,
        "forceConsistentCasingInFileNames": true,
        "strictNullChecks": true
    },
    "files": [
        "index.ts"
    ]
}
```

Please feel free to customize this however you'd like, including the TypeScript settings that work for you.  For
additional information on what settings you can use, please refer to [the TypeScript documentation for `tsconfig.json`](
https://www.typescriptlang.org/docs/handbook/tsconfig-json.html.

And finally, run `yarn build` any time you want to update your program prior to running `pulumi preview` or
`pulumi update` (this is just a shortcut for invoking the TypeScript compiler, `tsc`, so feel free to do that instead).

You can now use tools like VS Code to get completion lists, live error reporting and inline documentation help.

![Pulumi TypeScript in VS Code](./vscode.png)

## Upcoming Features

Some major features we are hard at work on at Pulumi include the following:

* More cloud abstractions
    - Containers
    - SQL databases
    - Redis-style caches
* Additional programming languages
* Robust deployments and cluster management
* A local cloud emulator for quick inner loop development

If you'd like to request specific features or have questions about any of this, please [let us know](/contact)!

## Next Steps

Check out the [package](/packages) documentation for more details on the kinds of programs you can build with Pulumi.

If you have questions of feedback on anything related to Pulumi, please don't hesitate to [contact us](/contact)).
