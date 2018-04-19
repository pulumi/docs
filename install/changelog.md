---
title: "Change log"
---

<!-- Common links -->
[`Output`]: https://docs.pulumi.com/packages/pulumi/classes/_resource_.output.html
[Python documentation]: ../reference/python.html
[Defining and setting stack settings]: ../reference/config.html#config-stack
[Configuration]: ../reference/config.html
[Pulumi npm packages]: ../reference/javascript.html#npm-packages
[Programming Model]: ../reference/programming-model.html
[Use Travis to continuously deploy Pulumi programs]: ../managed-cloud/cicd-with-travis.html
[Create and work with managed stacks]: ../managed-cloud/cloud-stack.html
[Using the Pulumi Console]: ../managed-cloud/console.html
<!-- End common links -->

## Available versions {#all-versions}

<table class="version-table">
    <thead>
        <tr>
            <th scope="col" width="25%">Version</th>
            <th scope="col" width="25%">Date</th>
            <th scope="col" width="50%">Downloads</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row"><a href="#v112">0.11.3</a></th>
            <td>2018/04/13</td>
            <td>{% include sdk-links.html version='0.11.3' %}</td>
        </tr>
        <tr>
            <th scope="row"><a href="#v10">0.10.0</a></th>
            <td>2018/02/27</td>
            <td>{% include sdk-links.html version='0.10.0' %}</td>
        </tr>
    </tbody>
</table>

> See [known issues](../reference/known-issues.html) for currently known issues and workarounds.

> **Note:** Versions of the Pulumi SDK prior to 0.11.3 have a strict dependency on Node.js 6.10.2.

## v0.11.3 {#v1113}

Released on April 13, 2018

### Added 

-  Add a static `get` method to all AWS resource classes. ([pulumi/pulumi-aws#189](https://github.com/pulumi/pulumi-aws/pull/189)). Each Pulumi resource class now has a static `get` method that construct an instance by reading existing resource state from your cloud provider.  For example, to read an existing EC2 VM, use `aws.ec2.Instance.get("vm", "i-01d7e1cddb70a2f0d")`. 

### Changed 

-  Switch to a resource-progress oriented view for pulumi preview, update, and destroy operations ([pulumi/pulumi#1116](https://github.com/pulumi/pulumi/pull/1116)). The operations `pulumi preview`, `update` and `destroy` have far simpler output by default, and show a progress view of ongoing operations. In addition, there is a structured component view, showing a parent operation as complete only when all child resources have been created.

-  Remove strict dependency on Node v6.10.x ([pulumi/pulumi#1139](https://github.com/pulumi/pulumi/pull/1139)). It is now no longer necessary to use a specific version of Node to run Pulumi programs. Node versions after 6.10.x are supported, as long as they are under **Active LTS** or are the **Current** stable release.

-  Use subnets instead of subnetMappings on LoadBalancer ([pulumi/pulumi-cloud#451](https://github.com/pulumi/pulumi-cloud/pull/451)). A change to how load balancers are configured for `cloud.Service` will mean that applications may see load balancers for non-HTTP services get replaced during updates.  This should not cause disruption to applications, but may change the DNS names of the load balancers where services are exposed.

### Fixed

-  Fix non-Fargate support for `cloud.Service` ([pulumi/pulumi-cloud#458](https://github.com/pulumi/pulumi-cloud/pull/458)). The issue in the 0.11.2 version of the SDK has now been fixed, and `cloud.Service` can either be used in the Fargate execution mode, or to target a cluster of EC2 instances (including the `cloud-aws:ecsAutoCluster` configuration setting).

## v0.11.2 {#v112}

Released on April 6, 2018

### Added

-  Add support for AWS Fargate ([pulumi/pulumi-cloud#411](https://github.com/pulumi/pulumi-cloud/pull/411)). Adds a `cloud-aws:useFargate` flag which causes container compute to run in Fargate. Also, when neither `cloud-aws:externalVpcId` nor `cloud-aws:usePrivateNetwork` are defined, `cloud.Service` uses the default VPC as the target network.

### Changed

-  (Breaking) Require `pulumi login` before commands that need a backend ([pulumi/pulumi#1114](https://github.com/pulumi/pulumi/pull/1114)). The `pulumi` CLI now requires you to log in to pulumi.com for most operations. 

### Fixed

-  Improve the error message arising from missing required configurations for resource providers ([pulumi/pulumi#1097](https://github.com/pulumi/pulumi/pull/1097)). The error message now prints all missing configuration keys, along with their descriptions.

## v0.11.1 {#v111}

Released on March 30, 2018

### Added

-  Initial support for a new `cloud.Bucket` component ([pulumi/pulumi-cloud#426](https://github.com/pulumi/pulumi-cloud/pull/426)).

### Fixed

-  When waiting for an ECS service to reach steady state, retry when ECS says the service can't be found ([pulumi/pulumi-cloud#443](https://github.com/pulumi/pulumi-cloud/pull/443)). This situation can occur when the ECS API performs a stale read of its datastore, so the workaround is to retry the operation.

## v0.11.0 {#v11}

Released on March 20, 2018

### Added

-  Add a `pulumi new` command to scaffold a project ([pulumi/pulumi#1008](https://github.com/pulumi/pulumi/pull/1008)). Usage is `pulumi new [templateName]`. If template name is not specified, the CLI will prompt with a list of templates. Currently, the templates `javascript`, `python` and `typescript` are available. Templates are defined in the GitHub repo [pulumi/templates](https://github.com/pulumi/templates) and contributions are welcome!

-  Python is now a supported language in Pulumi ([pulumi/pulumi#800](https://github.com/pulumi/pulumi/pull/800)). For more information, see [Python documentation].

-  Add ECS container definition JSON schemas ([pulumi/pulumi-aws#156](https://github.com/pulumi/pulumi-aws/pull/156)). Additionally, the Lambda runtime enum has been updated. The function `getLinuxAMI` has been removed from `ec2` and moved directly into example code.

-  Add link to documentation source in doc comments ([pulumi/pulumi-terraform#126](https://github.com/pulumi/pulumi-terraform/pull/126)). Adds a "Sourced from \<url\>" annotation to all generated doc comments, with links to Terraform resource provider source documentation.

### Changed

-  (Breaking) Change the way that configuration is stored ([pulumi/pulumi#986](https://github.com/pulumi/pulumi/pull/986)). To simplify the configuration model, there is no longer a separate notion of project and workspace settings, but only stack settings. The switches `--all` and `--save` are no longer supported; any common settings across stacks must be set on each stack directly. Settings for a stack are stored in a file that is a sibling to `Pulumi.yaml`, named `Pulumi.<stack-name>.yaml`. On first run `pulumi`, will migrate projects from the previous configuration format to the new one. The recommended practice is that developer stacks that are not shared between team members should be added to `.gitignore`, while stack setting files for shared stacks should be checked in to source control. For more information, see the section [Defining and setting stack settings].

-  (Breaking) Eliminate the superfluous `:config` part of configuration keys ([pulumi/pulumi#995](https://github.com/pulumi/pulumi/pull/995)). `pulumi` no longer requires configuration keys to have the string `:config` in them. Using the `:config` string in keys for the object `@pulumi/pulumi.Config` is deprecated and `preview` and `update` show warnings when it is used. Additionally, it is preferred to set keys in the form `aws:region` rather than `aws:config:region`. For compatibility, the old behavior is also supported, but will be removed in a future release. For more information, see the article [Configuration].

-  (Breaking) Require provider config and improve error message when provider not installed ([pulumi/pulumi-cloud#377](https://github.com/pulumi/pulumi-cloud/pull/377)). When using the JavaScript package `@pulumi/cloud`, you must first set the configuration value for `cloud:provider`. For instance, to target AWS, use `pulumi config set cloud:provider aws`.  Additionally, if the package `@pulumi/cloud-aws` is not included in the `dependencies` section of `package.json`, you'll see the following error message. For more information, see [Pulumi npm packages].

    ```
    Attempted to load the 'aws' implementation of '@pulumi/cloud',
    but no '@pulumi/cloud-aws' module is installed. Install it now
    or select another provider implementation with the "cloud:config:provider" setting.
    ```

-  (Breaking) Use plural names for array-typed values ([pulumi/pulumi-aws#146](https://github.com/pulumi/pulumi-aws/pull/146)) and ([pulumi/pulumi-terraform#123](https://github.com/pulumi/pulumi-terraform/pull/123)). API properties that are array-typed now have a plural name. For example, the property is `aws.cloudfront.Distribution.cacheBehaviors` (plural), rather than `cacheBehavior` (singular).

-  (Breaking) Project array with one element as nested struct instead of array ([pulumi/pulumi-terraform#122](https://github.com/pulumi/pulumi-terraform/pull/122)). The API is now improved for properties that were previously array typed but accepted exactly one value. These properties are now nested structs instead of an array. For example, the properties `clusterConfig`, `ebsOptions` and `snapshotOptions` in `aws.elasticsearch.Domain` are no longer array-typed.

-  (Breaking) Modules are treated as normal values when serialized ([pulumi/pulumi#1030](https://github.com/pulumi/pulumi/pull/1030)). If you need to use a module at runtime, consider either using `require` or `await import` at runtime, or pre-compute what you need and capture the resulting data or objects.

<!-- NOTE: the programming-model article below is still all todos. -->
-  (Breaking) Serialize resource registration after inputs resolve ([pulumi/pulumi#964](https://github.com/pulumi/pulumi/pull/964)). Previously, resources were most often created/updated in the order they were seen during the Pulumi program execution. In preparation for supporting parallel resource operations, these operations now run in an order that respects the dependencies between resources (via [`Output`]), but may not match the order of program execution. This is mostly transparent to Pulumi program authors, but does mean that any missing dependencies will cause your program to fail in unexpected ways. For more information on how such failures manifest and what to do about them, see the article [Programming Model].

-  Hide secrets from CLI output ([pulumi/pulumi#1002](https://github.com/pulumi/pulumi/pull/1002)). To prevent secret values from being accidentally disclosed in command output or logs, `pulumi` replaces secret values with the string `[secret]`. Inspired by the behavior of [Travis CI](https://travis-ci.org/).

-  Change default of where stacks are created ([pulumi/pulumi#971](https://github.com/pulumi/pulumi/pull/971)). If currently logged in to the Pulumi CLI, `stack init` creates a managed stack; otherwise, it creates a local stack. To force a local or remote stack, use the flags `--local` or `--remote`.

- Use the same load balancer port as exposed on the underlying `cloud.Service` ([pulumi/pulumi-cloud#395](https://github.com/pulumi/pulumi-cloud/pull/395)). By default, the port exposed by a `cloud.Service` load balancer is the same as the container port. There is also a new `target` port property which allows exposing a different port than the internal container port. Note that this may cause surprising resource updates or replacements upon your next update after adopting v0.11.0 of the SDK. Such updates should be handled transparently by Pulumi, with no downtime.

### Fixed

-  In `cloud.Service`, wait for ECS services to reach a steady state ([pulumi/pulumi-cloud#396](https://github.com/pulumi/pulumi-cloud/pull/396)). Previously, when a `cloud.Service` resource was updated (for example, to point to a new container image), the update operation did not wait for the underlying service to reach a new steady state, but only waited for the service update to start. Now, `pulumi update` waits for the service to reach a new steady state, ensuring that the service is in a healthy state before continuing to make further changes to your infrastructure.

-  Improve error messages output by the CLI ([pulumi/pulumi#1011](https://github.com/pulumi/pulumi/pull/1011)). RPC endpoint errors have been improved. Errors such as "catastrophic error" and "fatal error" are no longer duplicated in the output.

-  Produce better error messages when the main module is not found ([pulumi/pulumi#976](https://github.com/pulumi/pulumi/pull/976)). If you're running TypeScript but have not run `tsc` or your main JavaScript file does not exist, the CLI will print a helpful `info:` message that points to the possible source of the error.

## v0.10.0 {#v10}

Released on February 27, 2018

### Added

#### Pulumi CLI and SDK

-  Support "force" option when deleting a managed stack.

-  In `@pulumi/cloud`, support for creating a `Cluster` without EFS using the `cloud-aws:config:ecsAutoClusterUseEFS` config setting ([pulumi-cloud#175](https://github.com/pulumi/pulumi-cloud/issues/175))

-  Add a `pulumi history` command ([pulumi#636](https://github.com/pulumi/pulumi/issues/636)). For a managed stack, use the `pulumi history` to view deployments of that stack's resources.

#### Pulumi Console

-  Show deployment history for a stack in Pulumi Console.

-  Display AWS console links in the Pulumi Console.
   Deep links to the AWS console are now displayed for the following types of resources: API Gateway, CloudWatch (event targets, log groups, and log subscription filter), Dynamo DB tables, IAM roles and role policy attachments, Lambda functions, S3 buckets, and SNS topics and subscriptions.

### Changed {#v10-changed}

#### Pulumi CLI and SDK

-  (Breaking) Use `npm install` instead of `npm link` to reference the Pulumi SDK `@pulumi/aws`, `@pulumi/cloud`, `@pulumi/cloud-aws`. For more information, see [Pulumi npm packages].

-  (Breaking) Explicitly track resource dependencies via `Input` and `Output` types. This enables future improvements to the Pulumi development experience, such as parallel resource creation and enhanced dependency visualization. When a resource is created, all of its output properties are instances of a new type [`pulumi.Output<T>`][`Output`]. `Output<T>` contains both the value of the resource property and metadata that tracks resource dependencies. Inputs to a resource now accept `Output<T>` in addition to `T` and `Promise<T>`.

#### Pulumi Console

-  Show parent/child relationships for resource components in the UI.

-  Pulumi Console is stack-oriented, not repo-oriented. The Pulumi Console now displays a view of all stacks in a table, rather than displaying a hierarchy of organization, repo, project, and stack.

### Fixed

#### beta.pulumi.com service

-  Support for zero-downtime updates of the **beta.pulumi.com** service. Within a tenant, deployments are further isolated from each other so that concurrent deployments do not share compute resources. Requests to get stack logs, update logs, and stack history are now always responsive, regardless of whether are are active deployments.

#### Pulumi CLI and SDK

-  Make change detection more accurate for complex values ([pulumi-terraform#99](https://github.com/pulumi/pulumi-terraform/issues/99)).
-  In `@pulumi/cloud`, ensure `Deployment` is recreated on all changes to API body. ([pulumi-cloud#360](https://github.com/pulumi/pulumi-cloud/issues/360))
-  In `@pulumi/cloud`, `Task.run` does not throw an error when running the task fails ([pulumi-cloud#368](https://github.com/pulumi/pulumi-cloud/issues/368))
-  In `@pulumi/cloud`, when creating `Cluster`, sporadic failure to create requested number of EC2 instances ([pulumi-cloud#195](https://github.com/pulumi/pulumi-cloud/issues/195))
-  When using managed stacks, get an HTTP 500 error if you try to remove a non-empty stack ([pulumi-ppc#111](https://github.com/pulumi/pulumi-ppc/issues/111))
-  Managed stacks sometimes return a 500 error when requesting logs ([pulumi-service#662](https://github.com/pulumi/pulumi-service/issues/662))
-  Error when using `float64` attributes using SDK v0.9.9 ([pulumi-terraform#95](https://github.com/pulumi/pulumi-terraform/issues/95))
-  `pulumi logs` entries only return first line ([pulumi#857](https://github.com/pulumi/pulumi/issues/857))

## v0.9.13 {#v913}

Released on February 7, 2018

### Added

- Added the ability to control the upload context to the Pulumi Service. You may now set a `context` property in `Pulumi.yaml`, which is combined with the location of `Pulumi.yaml`. This new path is the root of what is uploaded and can be used during deployment. This allows you to, for example, share common code that is located in a folder in your source tree above the directory `Pulumi.yaml` for the project you are deploying.

- Added additional configuration for docker builds for a container. The `build` property of a container may now either be a string (which is treated as a path to the folder to do a `docker build` in) or an object with properties `context`, `dockerfile` and `args`, which are passed to `docker build`. If unset, `context` defaults to the current working directory, `dockerfile` defaults to `Dockerfile` and `args` default to no arguments.

## v0.9.11 {#v911}

Released on January 22, 2018

### Added

- Added the ability to import or export a stack's deployment in the Pulumi CLI. This command can be used for either local or managed stacks. There are two new verbs under the command `stack`:
   - `export` writes the current stack's latest deployment to stdout in JSON format.
   - `import` reads a new JSON deployment from stdin and applies it to the current stack.

- A basic progress spinner is displayed during deployment operations.
   - When the Pulumi CLI is run in interactive mode, it displays an animated ASCII spinner
   - When run in non-interactive mode, CLI prints a message that it is still working. For CI systems that kill jobs when there is no CLI output (such as TravisCI), this eliminates the need to create shell scripts that periodically print output.

- [@pulumi/cloud] Support for ACM certificates on HttpEndpoint. The AWS implementation of `HttpEndpoint#attachCustomDomain` accepts an ACM cert in place of raw certificate material, making it much easier to use `HttpEndpoint` with custom domains.

- [@pulumi/cloud] Added `HttpEndpoint#proxy` function to provide routes on an HTTP endpoint which redirect to a URL or `cloud.Endpoint`.

- [@pulumi/cloud] Added `Response#getHeader` function.

- [@pulumi/cloud-aws] Many new config settings have been added to enable overriding defaults for Network and Cluster configuration - both for auto clusters and for externally provided networks and clusters.

### Changed

- To make the behavior of local and managed stacks consistent, the Pulumi CLI uses a separate encryption key for each stack, rather than one shared for all stacks. You can now use a different passphrase for different stacks. Similar to managed stacks, you cannot copy and paste an encrypted value from one stack to another in `Pulumi.yaml`. Instead you must manage the value via `pulumi config`.

- The default behavior for `--color` is now `always`. To change this, specify `--color always` or `--color never`. Previously, the value was based on the presence of the flag `--debug`.

- The command `pulumi logs` now defaults to returning one hour of logs and outputs the start time that is  used.

- [pulumi-aws] Auto-name ElasticSearch domain name, following the naming restrictions documented in [Amazon Elasticsearch documentation for DomainName](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-configuration-api.html#es-configuration-api-datatypes-domainname).

- [pulumi-cloud] Header names are now normalized (using toLowerCase) for HttpEndpoint.

- [pulumi-cloud] For `cloud.Service`, the default permissions for cluster EC2 instances have been reduced.

- [pulumi-cloud] Pulumi now adds a `Name` tag onto instances launched into the ECS cluster.

- [pulumi-cloud] Expose additional AWS resources in `@pulumi/cloud-aws`: Topic, Timer, Table and HttpEndpoint.

### Fixed

- When a stack is removed, `pulumi` now deletes any configuration it had saved in either the `Pulumi.yaml` file or the workspace.

## v0.9.8

Released on December 28, 2017

### Added

#### Pulumi Console and managed stacks

New in this release is the [Pulumi Console](https://beta.pulumi.com) and stacks that are managed by Pulumi. This is the recommended way to safely deploy cloud applications.
- `pulumi stack init` now creates a Pulumi managed stack. For a local stack, use `--local`. To learn more, see the tutorial [Create and work with managed stacks].
- All Pulumi CLI commands now work with managed stacks. Login to Pulumi via `pulumi login`.
- The [Pulumi Console](https://beta.pulumi.com) provides a management experience for stacks. You can view the currently deployed resources (along with the AWS ARNs) and see logs from the last update operation.
For more information, see the documentation articles [Using the Pulumi Console] and [Use Travis to continuously deploy Pulumi programs].

#### Components and output properties

-  Support for component resources([pulumi #340](https://github.com/pulumi/pulumi/issues/340)), enabling grouping of resources into logical components. This provides an improved view of resources during `preview` and `update` operations in the CLI ([pulumi #417](https://github.com/pulumi/pulumi/issues/417)).

  ```
  + pulumi:pulumi:Stack: (create)
     [urn=urn:pulumi:donna-testing::url-shortener::pulumi:pulumi:Stack::url-shortener-donna-testing]
     + cloud:table:Table: (create)
        [urn=urn:pulumi:donna-testing::url-shortener::cloud:table:Table::urls]
        + aws:dynamodb/table:Table: (create)
              [urn=urn:pulumi:donna-testing::url-shortener::cloud:table:Table$aws:dynamodb/table:Table::urls]
  ```
- A stack can have *output properties*, defined as `export let varName = val`. You can view the last deployed value for the output property using `pulumi stack output varName` or in the Pulumi Console.

#### Resource naming

Resource naming is now more consistent, but there is a new file format for checkpoint files for both local and managed stacks.

> If you created stacks in the 0.8 release, you should destroy them with the 0.8 CLI, then recreate with the 0.9.x CLI.

#### Support for configuration secrets
- Store secrets securely in configuration via `pulumi config set --secret`. chris
- The verbs for `config` are now consistent, via `get`, `set`, and `rm`. See [Consistent config verbs #552](https://github.com/pulumi/pulumi/issues/552).

#### Logging

- [**experimental**] Support for the `pulumi logs` command ([pulumi #527](https://github.com/pulumi/pulumi/issues/527)). Unified logging is available in all of the `@pulumi/cloud` components ([pulumi-cloud #40](https://github.com/pulumi/pulumi-cloud/issues/40)). These features now work:
   - To see new logs as they arrive, use `--follow`
   - Use `--since` to limit to recent logs, such as `pulumi logs --since=1h`
   - Filter to specific resources with `--resource`. This filters to a particular component and its child resources (if any), such as `pulumi logs --resource examples-todoc57917fa --since 1h`

#### Other features

- Support for `.pulumiignore`, for files that should not be uploaded when deploying a managed stack through Pulumi. [pulumi-service \#122](https://github.com/pulumi/pulumi-service/issues/122)
- [Allow overriding a `Pulumi.yaml`'s entry point #575](https://github.com/pulumi/pulumi/issues/575). To specify the entry directory, specify `main` in `Pulumi.yaml`. For instance, `main: a/path/to/main/`.
- Support for *protected* resources. A resource can be marked as `protect: true`, which prevents deletion of the resource. For example, `let res = new MyResource("precious", { .. }, { protect: true });`. To "unprotect" the resource, change `protect: false` then run `pulumi update`. See [Allow resources to be flagged "protected" #689](https://github.com/pulumi/pulumi/issues/689).
- Changed defaults for workspace and stack configuration. See [Workspace configuration is error prone #714](https://github.com/pulumi/pulumi/issues/714).
- Allow configuring the number of availability zones in auto-cluster via the setting `cloud-aws:config:ecsAutoClusterNumberOfAZs`. See [Provide config for auto-cluster's number of availability zones #300](https://github.com/pulumi/pulumi-cloud/issues/300).
- [Save configuration under the stack by default](https://github.com/pulumi/pulumi/issues/693).
- [Create an endpoint for downloading the Pulumi SDK via beta.pulumi.com #372](https://github.com/pulumi/pulumi-service/issues/372).

### Fixed
- Improved SDK installer. It automatically creates directories as needed, configures node modules, and prints out friendly error messages. ([pulumi-home #49](https://github.com/pulumi/home/issues/49), [pulumi-home #52](https://github.com/pulumi/home/issues/52), [pulumi-home #53](https://github.com/pulumi/home/issues/53), [pulumi-home #54](https://github.com/pulumi/home/issues/54), [pulumi-home #69](https://github.com/pulumi/home/issues/69))
- [Switch to use \`\-\-password\-stdin\` on Docker CLI \#152](https://github.com/pulumi/pulumi-cloud/issues/152)
- [Better diffing in CLI output, especially for Lambdas \#454](https://github.com/pulumi/pulumi/issues/454)
- [Aggregate container logs into shared pulumi\-app\-log\-collector \#93](https://github.com/pulumi/pulumi-cloud/issues/93)
- [Implement strong read consistency on cloud.Table #44](https://github.com/pulumi/pulumi-cloud/issues/44)
- [Improved error when Docker is not running #309](https://github.com/pulumi/pulumi-service/issues/309)
- Add an HTTP cache for GitHub API requests for a user's organization membership. See [Exhausting GitHub rate limiting requests on behalf of users #413](https://github.com/pulumi/pulumi-service/issues/413).
- [`main` does not set working dir correctly for Lambda zip #667](https://github.com/pulumi/pulumi/issues/667)
- [Better error when invalid access token is used in `pulumi login` #640](https://github.com/pulumi/pulumi/issues/640)
- [Eliminate the top-level Stack from all URNs #647](https://github.com/pulumi/pulumi/issues/647)
- [Improve performance of "cold" requests to PPC #368](https://github.com/pulumi/pulumi-service/issues/368)
- [Store user account credentials safely #112](https://github.com/pulumi/pulumi-ppc/issues/112)
- [Service API for Encrypting and Decrypting secrets #221](https://github.com/pulumi/pulumi-service/issues/221)
- [Make CLI resilient to network flakiness #763](https://github.com/pulumi/pulumi/issues/763)
- [Some PPC messages aren't colorized #152](https://github.com/pulumi/pulumi-ppc/issues/152)
- [Support --since and --resource on `pulumi logs` when targeting the service #431](https://github.com/pulumi/pulumi-service/issues/431)
- [Pulumi unable to serialize non-integers #694](https://github.com/pulumi/pulumi/issues/694)
- [Stop buffering CLI output #660](https://github.com/pulumi/pulumi/issues/660)
