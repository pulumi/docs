---
title_tag: "Provider Configuration"
meta_desc: "Learn how to declare configuration keys for a Pulumi provider, including secrets and environment variable defaults."
title: Provider Configuration
h1: Provider Configuration
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Provider Configuration
        parent: iac-guides-providers
        weight: 35
---

A Pulumi provider can declare its own configuration keys, which users set via `pulumi config`, [Pulumi ESC](/docs/esc/) environments, or environment variables. Declaring configuration in the provider schema (rather than reading it ad hoc inside resource methods) gives you typed access in every language SDK, automatic secret handling, and automatic fallback to environment variables.

This guide uses the [Pulumi Go Provider SDK](/docs/iac/guides/building-extending/providers/sdks/pulumi-go-provider-sdk/). For the underlying schema fields, see the [package schema reference](/docs/iac/guides/building-extending/packages/schema/#default).

## Declaring a config type

Define a struct whose fields are tagged with `pulumi:"<name>"`. Register it on the provider builder with `WithConfig`:

```go
import (
    "context"

    p "github.com/pulumi/pulumi-go-provider"
    "github.com/pulumi/pulumi-go-provider/infer"
)

type Config struct {
    ClientKey    string `pulumi:"clientKey"`
    ClientSecret string `pulumi:"clientSecret" provider:"secret"`
}

func provider() (p.Provider, error) {
    return infer.NewProviderBuilder().
        WithNamespace("examples").
        WithConfig(infer.Config(&Config{})).
        Build()
}
```

The `provider:"secret"` tag marks the value as a secret so Pulumi encrypts it in state and redacts it from logs and CLI output.

## Describing fields and defaults

Implement `Annotate` to attach descriptions, defaults, and environment variable fallbacks. The third (and subsequent) arguments to `SetDefault` are the names of environment variables to probe — Pulumi reads them in order and uses the first one that is set:

```go
func (c *Config) Annotate(a infer.Annotator) {
    a.Describe(&c.ClientKey, "The client key for the external system.")
    a.Describe(&c.ClientSecret, "The client secret for the external system.")
    a.SetDefault(&c.ClientKey, "", "EXAMPLE_CLIENT_KEY")
    a.SetDefault(&c.ClientSecret, "", "EXAMPLE_CLIENT_SECRET")
}
```

This emits the following into the generated package schema, which every language SDK consumes:

```json
"clientSecret": {
    "type": "string",
    "default": "",
    "defaultInfo": {
        "environment": ["EXAMPLE_CLIENT_SECRET"]
    },
    "secret": true
}
```

The resolution order at runtime is: explicit value passed to the provider constructor, then `pulumi config` value, then each environment variable in `defaultInfo.environment`, then the static `default`.

## Reacting to configuration

If you need to validate the config or build derived state (for example, an authenticated API client), implement `Configure`. It runs once after the user-supplied values are merged with defaults:

```go
func (c *Config) Configure(ctx context.Context) error {
    if c.ClientKey == "" {
        return fmt.Errorf("clientKey is required")
    }
    return nil
}
```

## Reading config from a resource

Use `infer.GetConfig` from any resource method to retrieve the populated config struct:

```go
func (w *Widget) Create(
    ctx context.Context,
    req infer.CreateRequest[WidgetArgs],
) (infer.CreateResponse[WidgetState], error) {
    cfg := infer.GetConfig[Config](ctx)
    // use cfg.ClientKey, cfg.ClientSecret, ...
}
```

## A complete example

The [`configurable`](https://github.com/pulumi/pulumi-go-provider/tree/main/examples/configurable) and [`credentials`](https://github.com/pulumi/pulumi-go-provider/tree/main/examples/credentials) examples in the `pulumi-go-provider` repository demonstrate the full pattern, including enums, optional fields, and post-processing in `Configure`.

## Bridged providers

Providers built with the Terraform bridge declare configuration through the upstream Terraform schema and the bridge's `ProviderInfo.Config` map rather than the mechanism shown here. See the [bridged provider documentation](/docs/iac/guides/building-extending/providers/implementers/) for details.
