---
title_tag: "Environment Variables | Pulumi CLI"
meta_desc: A list of different environment variables the Pulumi CLI supports.
title: Environment variables
h1: Pulumi CLI environment variables
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    weight: 2
    parent: iac-cli
aliases:
  - /docs/reference/cli/environment-variables/
  - /docs/cli/environment-variables/
search:
  keywords:
    - environment
    - variables
    - environment variables
---

<dl class="tabular tabular-5-col break-words">
    <dt>
        <span class="font-mono">
            PULUMI_STACK
        </span>
    </dt>
    <dd>
        <p>
            Specifies the selected pulumi stack, overriding the stack selected with <a href="/docs/iac/cli/commands/pulumi_stack_select/"><code class="text-xs">pulumi stack select STACK</code></a>
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
            PULUMI_AI_SERVICE_ENDPOINT
        </span>
    </dt>
    <dd>
        <p>
            Specifies the endpoint for Pulumi AI service.
        </p>
        <pre><code class="text-xs">PULUMI_AI_SERVICE_ENDPOINT="https://www.pulumi.com/ai"</code></pre>
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
            PULUMI_BACKEND_URL
        </span>
    </dt>
    <dd>
        <p>
            Set this environment variable to use a specified backend instead of the default backend.  See <a href="/docs/concepts/state">State and Backends</a> for details on valid backend URLs.
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
            Sets <a href="/docs/concepts/config">configuration</a> for <a href="/docs/using-pulumi/testing/unit">unit testing</a>. Must be in JSON format.
        </p>
        <p>
            <strong>This environment variable is ignored during normal Pulumi operations -- e.g., <code>up</code>, <code>preview</code>, etc.</strong>
        </p>
        <pre><code class="text-xs">PULUMI_CONFIG="{'project:myTag':'val1','project:mySecret':'val2'}"</code></pre>
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
            and <a href="/docs/concepts/config">Configuration and Secrets</a> to learn more about Pulumi's configuration
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
            Use legacy refresh diff behaviour, in which only output changes are
            reported and changes against the desired state are not calculated.
        </p>
        <pre><code class="text-xs">PULUMI_ENABLE_LEGACY_REFRESH_DIFF=true</code></pre>
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
            Enables experimental options and commands.
        </p>
        <pre><code class="text-xs">PULUMI_EXPERIMENTAL=true</code></pre>
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
