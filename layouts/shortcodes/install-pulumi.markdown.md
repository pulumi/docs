<!-- chooser: os -->

<!-- option: macos -->

```bash
$ brew install pulumi/tap/pulumi
```

<!-- /option -->

<!-- option: linux -->

```bash
$ curl -fsSL https://get.pulumi.com | sh
```

<!-- /option -->

<!-- option: windows -->
{{ .Inner }}
```bat
> choco install pulumi
```

<!-- /option -->

<!-- /chooser -->

> **Note:** Other installation options [are available](/docs/install/).

Test your new installation by running the `pulumi version` command:

<!-- chooser: os -->

<!-- option: macos -->

```bash
$ pulumi version
v{{ readFile "static/latest-version" }}
```

If this doesn't work, you may need to restart your terminal to ensure the directory containing
the `pulumi` command is on your `PATH`.

<!-- /option -->

<!-- option: linux -->

```bash
$ pulumi version
v{{ readFile "static/latest-version" }}
```

If this doesn't work, you may need to restart your terminal to ensure the directory containing
the `pulumi` command is on your `PATH`.

<!-- /option -->

<!-- option: windows -->

```bat
> pulumi version
v{{ readFile "static/latest-version" }}
```

If this doesn't work, you may need to restart your terminal to ensure the directory containing
the `pulumi.exe` command is on your `PATH`.

<!-- /option -->

<!-- /chooser -->
