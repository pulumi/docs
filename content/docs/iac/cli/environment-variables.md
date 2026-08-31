---
title_tag: "Environment Variables | Pulumi CLI"
meta_desc: A list of different environment variables the Pulumi CLI supports.
title: Environment variables
h1: Pulumi CLI environment variables
menu:
  iac:
    weight: 2
    parent: iac-cli
aliases:
    - /docs/reference/cli/environment-variables/
    - /docs/cli/environment-variables/
---

<dl class="tabular tabular-5-col break-words">
    <dt>
        <span class="font-mono">
            PULUMI_STACK
        </span>
    </dt>
    <dd>
        <p>
            Specifies the selected pulumi stack, overriding the stack selected with <a href="/docs/iac/cli/commands/pulumi_stack_select/"><code class="text-xs">pulumi stack select STACK</code></a>.
            The priority is as follows:
            <ol>
                <li>The <code class="text-xs">--stack</code> command line flag</li>
                <li><span class="font-mono">PULUMI_STACK</span></li>
                <li>Stack selected with <code class="text-xs">pulumi stack select &ltSTACK&gt</code></li>
            </ol>
        </p>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_AUTOMATION_API_SKIP_VERSION_CHECK
        </span>
    </dt>
    <dd>
        <p>
            Skips the minimum CLI version check used by Automation API to ensure compatibility. We do not recommend using this variable as it may result in unexpected behavior or confusing error messages from Automation API.
        </p>
        <pre><code class="text-xs">PULUMI_AUTOMATION_API_SKIP_VERSION_CHECK=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_ACCESS_TOKEN
        </span>
    </dt>
    <dd>
        <p>
            Set this environment variable to authenticate into the Pulumi Cloud backend and bypass the access
            token prompt when running {{% md %}}`pulumi login`{{% /md %}}.
        </p>
        <pre><code class="text-xs">PULUMI_ACCESS_TOKEN="your-access-token"</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_API
        </span>
    </dt>
    <dd>
        <p>
            Overrides the URL of the Pulumi Cloud API that the CLI communicates with when using the Pulumi Cloud backend. Most users should set <span class="font-mono">PULUMI_BACKEND_URL</span> instead, which selects the backend itself; this variable is for advanced scenarios, such as pointing the CLI at a non-default Pulumi Cloud API endpoint.
        </p>
        <pre><code class="text-xs">PULUMI_API="https://api.pulumi.com"</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_BACKEND_URL
        </span>
    </dt>
    <dd>
        <p>
            Set this environment variable to use a specified backend instead of the default backend.  See <a href="/docs/iac/concepts/state-and-backends/">State and Backends</a> for details on valid backend URLs.
        </p>
        <pre><code class="text-xs">PULUMI_BACKEND_URL="s3://your-pulumi-state-bucket"</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_CONFIG
        </span>
    </dt>
    <dd>
        <p>
            Sets <a href="/docs/iac/concepts/config/">configuration</a> for <a href="/docs/iac/guides/testing/unit/">unit testing</a>. Must be in JSON format.
        </p>
        <p>
            <strong>This environment variable is ignored during normal Pulumi operations -- e.g., <code>up</code>, <code>preview</code>, etc. -- but must be valid JSON if present.</strong>
        </p>
        <pre><code class="text-xs">PULUMI_CONFIG='{"project:myTag":"val1","project:mySecret":"val2"}'</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_CONFIG_PASSPHRASE
        </span>
    </dt>
    <dd>
        <p>
            Set this as an environment variable to protect and unlock your configuration values and secrets. Your passphrase
            is used to generate a unique key for your stack, and configuration and encrypted state values are then encrypted
            using <code>AES-256-GCM</code>.
            Read <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#secrets-and-pluggable-encryption">the change log</a>
            and <a href="/docs/iac/concepts/config/">Configuration and Secrets</a> to learn more about Pulumi's configuration
            and secrets management system.
        </p>
        <pre><code class="text-xs">PULUMI_CONFIG_PASSPHRASE="your-passphrase"</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_CONFIG_PASSPHRASE_FILE
        </span>
    </dt>
    <dd>
        <p>
            An alternative method to providing <code>PULUMI_CONFIG_PASSPHRASE</code>. Set this to the path of a file that contains the passphrase value.
        </p>
        <pre><code class="text-xs">PULUMI_CONFIG_PASSPHRASE_FILE="/tmp/passphrase.txt"</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_CONSOLE_DOMAIN
        </span>
    </dt>
    <dd>
        <p>
            Overrides the domain used when generating links to the Pulumi Cloud.
        </p>
        <pre><code class="text-xs">PULUMI_CONSOLE_DOMAIN="yourhost.domain.com"</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_CONTINUE_ON_ERROR
        </span>
    </dt>
    <dd>
        <p>
            Continues to perform the update/destroy operation despite the occurrence of errors.
        </p>
        <pre><code class="text-xs">PULUMI_CONTINUE_ON_ERROR=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_CREDENTIAL_STORE
        </span>
    </dt>
    <dd>
        <p>
            Selects an opt-in store for CLI credentials, such as your Pulumi Cloud access token, that encrypts them at rest with a key
            protected by your operating system's credential manager (Keychain on macOS, Credential Manager on Windows, or a Secret
            Service provider such as GNOME Keyring on Linux) instead of writing them to disk in plaintext under
            <code class="text-xs">PULUMI_HOME</code>. Set to <code class="text-xs">os</code> to require the OS-native store, or <code class="text-xs">auto</code> to use it when available and fall back to plaintext. Set to <code class="text-xs">plaintext</code> to opt out.
        </p>
        <pre><code class="text-xs">PULUMI_CREDENTIAL_STORE=os</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DEBUG_COMMANDS
        </span>
    </dt>
    <dd>
        <p>
            List commands helpful for debugging Pulumi itself.
        </p>
        <pre><code class="text-xs">PULUMI_DEBUG_COMMANDS=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DEBUG_GRPC
        </span>
    </dt>
    <dd>
        <p>
            Enables debug tracing of Pulumi gRPC internals. The variable should be set to the log file to which gRPC debug traces will be sent.
        </p>
        <pre><code class="text-xs">PULUMI_DEBUG_GRPC="/path/to/grpc-debug.log"</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DEBUG_PROMISE_LEAKS
        </span>
    </dt>
    <dd>
        <p>
            As of <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#0166-2018-11-28"><code>v0.12.2</code></a>,
            the promise leak experience has been improved and shows a simple error message. Set this environment variable to
            get more verbose error messages when debugging promise leaks.
        </p>
        <pre><code class="text-xs">PULUMI_DEBUG_PROMISE_LEAKS=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DEFAULT_ORGANIZATION
        </span>
    </dt>
    <dd>
        <p>
            Sets the default organization to use when creating a new stack or resolving an unqualified stack name, similar to
            setting a default organization with
            <a href="/docs/iac/cli/commands/pulumi_org_set-default/"><code class="text-xs">pulumi org set-default</code></a>.
        </p>
        <pre><code class="text-xs">PULUMI_DEFAULT_ORGANIZATION=your-org</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DEV
        </span>
    </dt>
    <dd>
        <p>
            Enable features for hacking on Pulumi itself.
        </p>
        <pre><code class="text-xs">PULUMI_DEV=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DISABLE_AUTOMATIC_PLUGIN_ACQUISITION
        </span>
    </dt>
    <dd>
        <p>
            Disables the automatic installation of missing plugins.
        </p>
        <pre><code class="text-xs">PULUMI_DISABLE_AUTOMATIC_PLUGIN_ACQUISITION=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DISABLE_SECRET_CACHE
        </span>
    </dt>
    <dd>
        <p>
            Disables the caching encryption operations for unchanged stack secrets.
        </p>
        <pre><code class="text-xs">PULUMI_DISABLE_SECRET_CACHE=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DISABLE_PROVIDER_PREVIEW
        </span>
    </dt>
    <dd>
        <p>
            Disables provider preview and enables previous more conservative preview behavior.
        </p>
        <pre><code class="text-xs">PULUMI_DISABLE_PROVIDER_PREVIEW=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DISABLE_VALIDATION
        </span>
    </dt>
    <dd>
        <p>
            Disables format validation of system inputs. Currently, this disables validation of stack names.
        </p>
        <pre><code class="text-xs">PULUMI_DISABLE_VALIDATION=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DISABLE_REGISTRY_RESOLVE
        </span>
    </dt>
    <dd>
        <p>
            By default, <code class="text-xs">pulumi install</code> and related package-resolution commands use the
            <a href="/registry/">Pulumi Registry</a> to resolve package names. Set this to <code>true</code> to disable
            registry-based resolution and fall back to the CLI's other resolution mechanisms.
        </p>
        <pre><code class="text-xs">PULUMI_DISABLE_REGISTRY_RESOLVE=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DIY_BACKEND_DISABLE_CHECKPOINT_BACKUPS
        </span>
    </dt>
    <dd>
        <p>
            If set, checkpoint backups will not be written to the backup folder.
        </p>
        <pre><code class="text-xs">PULUMI_DIY_BACKEND_DISABLE_CHECKPOINT_BACKUPS=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DIY_BACKEND_GZIP
        </span>
    </dt>
    <dd>
        <p>
            Enables gzip compression when writing state files.
        </p>
        <pre><code class="text-xs">PULUMI_DIY_BACKEND_GZIP=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DIY_BACKEND_IGNORE_DEPRECATION_ERROR
        </span>
    </dt>
    <dd>
        <p>
            Using a self-managed (DIY) state backend, such as a local directory or an Amazon S3, Google Cloud Storage, or
            Azure Blob Storage bucket, in the legacy non-project-scoped stack layout is deprecated and due to be removed in
            a future release. The CLI now raises an error rather than a warning when it detects this layout. Set this to
            <code class="text-xs">true</code> to bypass the error and continue using the legacy layout. We recommend running
            <a href="/docs/iac/cli/commands/pulumi_state_upgrade/"><code class="text-xs">pulumi state upgrade</code></a>
            to move to project-scoped stacks instead, and consider moving to the
            <a href="/docs/iac/concepts/state-and-backends/#pulumi-cloud-backend">Pulumi Cloud backend</a> while you are at
            it, since it manages this state layout, locking, and encryption for you.
        </p>
        <pre><code class="text-xs">PULUMI_DIY_BACKEND_IGNORE_DEPRECATION_ERROR=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DIY_BACKEND_LEGACY_LAYOUT
        </span>
    </dt>
    <dd>
        <p>
            Uses the legacy layout for new buckets, which currently default to project-scoped stacks.
        </p>
        <pre><code class="text-xs">PULUMI_DIY_BACKEND_LEGACY_LAYOUT=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DIY_BACKEND_NO_LEGACY_WARNING
        </span>
    </dt>
    <dd>
        <p>
            Disables the warning about legacy stack files mixed with project-scoped stack files.
        </p>
        <pre><code class="text-xs">PULUMI_DIY_BACKEND_NO_LEGACY_WARNING=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DIY_BACKEND_PARALLEL
        </span>
    </dt>
    <dd>
        <p>
            Number of parallel operations when fetching stacks and resources from the DIY backend.
        </p>
        <pre><code class="text-xs">PULUMI_DIY_BACKEND_PARALLEL=NUMBER_OF_PARALLEL_OPERATIONS</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_DIY_BACKEND_RETAIN_CHECKPOINTS
        </span>
    </dt>
    <dd>
        <p>
            If set, every checkpoint will be duplicated to a timestamped file.
        </p>
        <pre><code class="text-xs">PULUMI_DIY_BACKEND_RETAIN_CHECKPOINTS=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_ENABLE_LEGACY_APPLY
        </span>
    </dt>
    <dd>
        <p>
            As of <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#100-beta1-2019-08-13"><code>1.0.0-beta1</code></a>,
            input properties are no longer propagated to missing output properties during a <code>pulumi preview</code>. If this causes issues
            in your Pulumi program, set this to <code>true</code> to enable the old behavior.
        </p>
        <pre><code class="text-xs">PULUMI_ENABLE_LEGACY_APPLY=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_ENABLE_LEGACY_DIFF
        </span>
    </dt>
    <dd>
        <p>
            As of <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#01723-2019-07-16"><code>v0.17.23</code></a>,
            the detection of differences between the actual and desired state of a resource is left entirely up to that resource's
            provider. This change can expose bugs in resource providers that lead to diffs being present even if the desired
            configuration matches the actual state of the resource. Set this to <code>1</code> or <code>true</code> to enable the old diff behavior.
        </p>
        <pre><code class="text-xs">PULUMI_ENABLE_LEGACY_DIFF=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_ENABLE_LEGACY_PLUGIN_SEARCH
        </span>
    </dt>
    <dd>
        <p>
            As of <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#01618-2019-03-01"><code>v0.16.18</code></a>,
            a fix has been released to prevent the Pulumi CLI from loading the newest plugin for a resource provider instead of
            the requested version. This has the potential to disrupt users that previously had working configurations. Set this
            environment variable to opt into the legacy plugin load behavior.
        </p>
        <pre><code class="text-xs">PULUMI_ENABLE_LEGACY_PLUGIN_SEARCH=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_ENABLE_LEGACY_REFRESH_DIFF
        </span>
    </dt>
    <dd>
        <p>
            Use legacy refresh diff behavior, in which only output changes are
            reported and changes against the desired state are not calculated.
        </p>
        <pre><code class="text-xs">PULUMI_ENABLE_LEGACY_REFRESH_DIFF=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_ENABLE_STREAMING_JSON_PREVIEW
        </span>
    </dt>
    <dd>
        <p>
            By default, <code class="text-xs">pulumi preview --json</code> emits a single <code>PreviewDigest</code> JSON
            object to stdout after the preview completes. Set this to <code>true</code> to instead stream JSON events to
            stdout as the preview runs, matching the behavior of <code class="text-xs">pulumi up|destroy|refresh --json</code>.
        </p>
        <pre><code class="text-xs">PULUMI_ENABLE_STREAMING_JSON_PREVIEW=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_ERROR_ON_DEPENDENCY_CYCLES
        </span>
    </dt>
    <dd>
        <p>
            Enables error reporting when dependency cycles are detected.
        </p>
        <pre><code class="text-xs">PULUMI_ERROR_ON_DEPENDENCY_CYCLES=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_ERROR_OUTPUT_STRING
        </span>
    </dt>
    <dd>
        <p>
            Throws an error instead of returning a string when attempting to convert an Output to a string.
        </p>
        <pre><code class="text-xs">PULUMI_ERROR_OUTPUT_STRING=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_EXPERIMENTAL
        </span>
    </dt>
    <dd>
        <p>
            Enables experimental options and commands. See <a href="/docs/support/faq/infrastructure/#what-does-experimental-mean">What does "experimental" mean?</a> for what to expect.
        </p>
        <pre><code class="text-xs">PULUMI_EXPERIMENTAL=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_FALLBACK_TO_STATE_SECRETS_MANAGER
        </span>
    </dt>
    <dd>
        <p>
            When set to "true", the secrets manager stored in the stack's state is used as a fallback when the stack configuration is missing or incomplete.
        </p>
        <pre><code class="text-xs">PULUMI_FALLBACK_TO_STATE_SECRETS_MANAGER=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_GITSSH_PASSPHRASE
        </span>
    </dt>
    <dd>
        <p>
            The passphrase to use with Git operations that use SSH.
        </p>
        <pre><code class="text-xs">PULUMI_GITSSH_PASSPHRASE="your passphrase"</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_HOME
        </span>
    </dt>
    <dd>
        <p>
            Overrides the folder where the Pulumi CLI stores its artifacts: plugins, workspaces, templates, and
            credentials file. By default, artifacts are stored next to Pulumi binaries in <code>~/.pulumi</code>.
        </p>
        <pre><code class="text-xs">PULUMI_HOME="/path/to/artifacts"</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_IGNORE_AMBIENT_PLUGINS
        </span>
    </dt>
    <dd>
        <p>
            Disables discovering additional plugins by examining $PATH.
        </p>
        <pre><code class="text-xs">PULUMI_IGNORE_AMBIENT_PLUGINS=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_LOG_ROTATION_MAX_AGE_DAYS
        </span>
    </dt>
    <dd>
        <p>
            Overrides how long automatic logs in <code>$PULUMI_HOME/logs</code> are kept before being
            rotated out. Defaults to <code>7</code> days.
        </p>
        <pre><code class="text-xs">PULUMI_LOG_ROTATION_MAX_AGE_DAYS=14</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_LOG_ROTATION_MAX_TOTAL_MB
        </span>
    </dt>
    <dd>
        <p>
            Overrides the maximum total size, in megabytes, of the automatic logs directory
            (<code>$PULUMI_HOME/logs</code>) before the oldest logs are rotated out. Defaults to
            <code>500</code>.
        </p>
        <pre><code class="text-xs">PULUMI_LOG_ROTATION_MAX_TOTAL_MB=1000</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_NEO
        </span>
    </dt>
    <dd>
        <p>
            Enables Neo help and links in the CLI output, regardless of the Neo settings for the given Pulumi organization. The legacy name <span class="font-mono">PULUMI_COPILOT</span> is still accepted as an alias.
        </p>
        <pre><code class="text-xs">PULUMI_NEO=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_PARALLEL
        </span>
    </dt>
    <dd>
        <p>
            Allow P resource operations to run in parallel at once (1 for no parallelism)
        </p>
        <pre><code class="text-xs">PULUMI_PARALLEL=NUMBER_OF_PARALLEL_OPERATIONS</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_PARALLEL_DIFF
        </span>
    </dt>
    <dd>
        <p>
            Enables running diff calculations in parallel.
        </p>
        <pre><code class="text-xs">PULUMI_PARALLEL_DIFF=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_PLUGIN_DOWNLOAD_URL_OVERRIDES
        </span>
    </dt>
    <dd>
        <p>
            Specifies overrides for plugin-download URLs. The expected format is <code>regexp=URL</code>, and multiple pairs can be specified separated by commas.
        </p>
        <pre><code class="text-xs">PULUMI_PLUGIN_DOWNLOAD_URL_OVERRIDES="^https://foo=https://bar,^github://=https://buzz"</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_PREFER_YARN
        </span>
    </dt>
    <dd>
        <p>
            Set this environment variable to opt-in to using <code>yarn</code> instead of <code>npm</code> for installing Node.js dependencies.
        </p>
        <pre><code class="text-xs">PULUMI_PREFER_YARN=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_PYTHON_CMD
        </span>
    </dt>
    <dd>
        <p>
            As of <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#0166-2018-11-28"><code>v0.16.6</code></a>,
            the Pulumi CLI uses <code>python3</code> instead of <code>python</code> when running a Python program. Set this environment variable to
            run a different Python binary.
        </p>
        <pre><code class="text-xs">PULUMI_PYTHON_CMD="python-version-binary"</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_RUN_PROGRAM
        </span>
    </dt>
    <dd>
        <p>
            Runs the Pulumi program for refresh and destroy operations. This is the same as passing '--run-program=true' to the CLI.
        </p>
        <pre><code class="text-xs">PULUMI_RUN_PROGRAM=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_SKIP_CHECKPOINTS
        </span>
    </dt>
    <dd>
        <p>
            As of <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#3401-2022-09-17"><code>v3.40.1</code></a>, you may skip saving state checkpoints and only save the final deployment. See <a href="https://github.com/pulumi/pulumi/issues/10668">#10668</a>. This is an experimental feature that also requires <code>PULUMI_EXPERIMENTAL=true</code> to be set for versions <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#31040-2024-01-31"><code>&gt;= v3.40.1, &lt; v3.104.0</code></a>.
        </p>
        <pre><code class="text-xs">PULUMI_SKIP_CHECKPOINTS=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_SKIP_CONFIRMATIONS
        </span>
    </dt>
    <dd>
        <p>
            As of <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#200-2020-04-16"><code>v2.0.0</code></a>,
            an explicit confirmation was required when running in non-interactive mode. Set this environment variable to
            make that explicit confirmation.
        </p>
        <pre><code class="text-xs">PULUMI_SKIP_CONFIRMATIONS=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_SKIP_UPDATE_CHECK
        </span>
    </dt>
    <dd>
        <p>
            As of <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#0179-2019-04-30"><code>v0.17.9</code></a>,
            you may skip the Pulumi version update check by setting this environment variable.
        </p>
        <pre><code class="text-xs">PULUMI_SKIP_UPDATE_CHECK=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_SUPPRESS_NEO_LINK
        </span>
    </dt>
    <dd>
        <p>
            Suppresses showing the 'explainFailure' link to Neo in the CLI output, regardless of the Neo settings for the given Pulumi organization. The legacy name <span class="font-mono">PULUMI_SUPPRESS_COPILOT_LINK</span> is still accepted as an alias.
        </p>
        <pre><code class="text-xs">PULUMI_SUPPRESS_NEO_LINK=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            NO_COLOR
        </span>
    </dt>
    <dd>
        <p>
            The presence of this environment variable (regardless of its value) strips color ANSI codes from text
            output to the terminal. See <a href="https://no-color.org/">https://no-color.org/</a> for more details.
            When used with Automation API, this environment variable will strip color directives from the event logs.
        </p>
        <pre><code class="text-xs">NO_COLOR</code></pre>
    </dd>
</dl>

## Setting CLI arguments with environment variables

As of v3.208.0, all Pulumi CLI arguments can be set via environment variables.

All CLI argument environment variables follow a predictable naming convention:
`PULUMI_OPTION_` followed by the capitalized snake case version of the argument
name. For example:

| CLI argument example                  | Environment variable example             |
| ------------------------------------- | ---------------------------------------- |
| `pulumi up --parallel 1`              | `PULUMI_OPTION_PARALLEL=1 pulumi up`     |
| `pulumi up --refresh`                 | `PULUMI_OPTION_REFRESH=true pulumi up`   |
| `pulumi up --yes`                     | `PULUMI_OPTION_YES=1 pulumi up`          |
| `pulumi up --target foo --target bar` | `PULUMI_OPTION_TARGET=foo,bar pulumi up` |

Note that you can specify boolean arguments either with `true` and `false` or
`1` and `0`. For more information, as well as some practical examples, see the
[release article](https://www.pulumi.com/blog/controlling-the-cli-through-environment-variables/).
