---
title: "Environment Variables"
meta_desc: A list of different environment variables the Pulumi CLI supports.
---

<dl class="tabular tabular-5-col">
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
            PULUMI_ENABLE_LEGACY_APPLY
        </span>
    </dt>
    <dd>
        <p>
            As of <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#100-beta1-2019-08-13"><code>1.0.0-beta1</code></a>,
            input properties are no longer propagated to missing output properties during a `pulumi preview`. If this causes issues
            in your Pulumi program, set this to `true` to enable the old behavior.
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
            provider. This change can expose bugs in the resource providers that lead to diffs being present even if the desired
            configuration matches the actual state of the resource. Set this to `1` or `true` to enable the old diff behavior.
        </p>
        <pre><code class="text-xs">PULUMI_ENABLE_LEGACY_DIFF=true</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_TEST_MODE
        </span>
    </dt>
    <dd>
        <p>
            As of <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#0177-2019-04-17"><code>v0.17.7</code></a>,
            you can enable a new "test mode" by setting this to `true` in either the Node.js or Python SDK. This mode allows you
            to unit test your Pulumi programs without needing to run them using the Pulumi CLI. Read the change log for details
            on limitations and other environment variables that must be set.
        </p>
        <pre><code class="text-xs">PULUMI_TEST_MODE=true</code></pre>
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
            using `AES-256-GCM`.
            Read <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#secrets-and-pluggable-encryption">the change log</a>
            and <a href="/docs/intro/concepts/config">Configuration and Secrets</a> to learn more about Pulumi's configuration
            and secrets management system.
        </p>
        <pre><code class="text-xs">PULUMI_CONFIG_PASSPHRASE="your-passphrase"</code></pre>
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
            PULUMI_PYTHON_CMD
        </span>
    </dt>
    <dd>
        <p>
            As of <a href="https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#0166-2018-11-28"><code>v0.16.6</code></a>,
            the Pulumi CLI uses `python3` instead of `python` when running a Python program. Set this environment variable to
            run a different Python binary.
        </p>
        <pre><code class="text-xs">PULUMI_PYTHON_CMD="python-version-binary"</code></pre>
    </dd>
    <dt>
        <span class="font-mono">
            PULUMI_ACCESS_TOKEN
        </span>
    </dt>
    <dd>
        <p>
            Set this environment variable to authenticate into the Pulumi Service backend and bypass the access
            token prompt when running `pulumi login`.
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
            Set this environment variable to use a specified backend instead of the default backend.  See <a href="/docs/intro/concepts/state">State and Backends</a> for details on valid backend URLs.
        </p>
        <pre><code class="text-xs">PULUMI_BACKEND_URL=s3://your-pulumi-state-bucket</code></pre>
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
            PULUMI_PREFER_YARN
        </span>
    </dt>
    <dd>
        <p>
            Set this environment variable to opt-in to using `yarn` instead of `npm` for installing Node.js dependencies.
        </p>
        <pre><code class="text-xs">PULUMI_PREFER_YARN=true</code></pre>
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
            PULUMI_CONSOLE_DOMAIN
        </span>
    </dt>
    <dd>
        <p>
            Overrides the domain used when generating links to the Pulumi Console.
        </p>
        <pre><code class="text-xs">PULUMI_CONSOLE_DOMAIN="yourhost.domain.com"</code></pre>
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
