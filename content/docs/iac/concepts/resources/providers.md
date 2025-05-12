---
title_tag: "Resource Providers"
meta_desc: A resource provider handles communications with a cloud service to create, read, update, and delete the resources you define in your Pulumi programs.
title: Providers
h1: Resource providers
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Providers
        parent: iac-concepts-resources
        weight: 4
    concepts:
        parent: resources
        weight: 4
aliases:
- /docs/intro/concepts/resources/providers/
- /docs/concepts/resources/providers/
---

A resource provider handles communications with a cloud or SaaS service to create, read, update, and delete the resources you define in your Pulumi programs.

Providers are composed of two parts: an executable, which makes the actual call to the cloud provider's API, and an SDK, which allows you to consume the provider in the language of your Pulumi program. When you run your Pulumi program, Pulumi passes your code to a language host such as Node.js, waits to be notified of resource registrations, assembles a model of your desired state, and calls on the provider executable to produce that state. The resource provider translates those requests into API calls to the cloud service.

## Installing Providers

There are two methods for installing a provider and using it in your Pulumi program:

1. **Adding a reference to a provider's SDK using a package manager** in the language of your Pulumi program (e.g., npm in Node.js). This method is more common and is used for nearly all packages in the [Pulumi Registry](/registry).
1. **Using the [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) command**. This method is most commonly used for [parameterized providers](https://pulumi-developer-docs.readthedocs.io/latest/docs/architecture/providers/parameterized.html), such as the [Any Terraform Provider](/registry/packages/terraform-provider). The `pulumi package add` command generates a local SDK on disk (as opposed to downloading a pre-generated SDK from a package feed like npm) and allows you to consume any provider in the OpenTofu registry in you Pulumi program, even if there is no corresponding provider in the Pulumi Registry.

### Installing a Provider via a Package Manager

The most common method of installing a provider is to use your language's package management tool: npm in Node.js, PyPI in Python, etc. For example, the [AWS provider](/registry/packages/aws/installation-configuration) has the following SDKs available:

- JavaScript/TypeScript: `@pulumi/aws`
- Python: `pulumi-aws`
- Go: `github.com/pulumi/pulumi-aws/sdk/go/aws`
- .NET: `Pulumi.Aws`
- Java: `com.pulumi.aws`

After installing the provider using your package manager, you reference the provider in your Pulumi program to define the desired state of the resources for that provider. When you install the SDK for a provider (e.g., via `npm install <package_name>` in Node.js), the package manager (npm in this example) automatically downloads and installs the provider executable along with the SDK if the executable is not already cached on your system.

### Installing a Parameterized Provider via `pulumi package add`

Parameterized providers allow you to generate a local provider SDK in the language of your Pulumi program. This method of consuming a provider is most commonly applicable when a pre-built provider SDK does not exist for a given cloud provider, SaaS service, or on-prem device, but a provider does exist in [the OpenTofu registry](https://search.opentofu.org). The [Any Terraform Provider](/registry/packages/terraform-provider) is a parameterized provider that provides this capability.

For example, to generate a local SDK for the [`hashicorp/random` provider](https://search.opentofu.org/provider/hashicorp/random/latest):

```bash
pulumi package add terraform-provider hashicorp/random
```

This command does two things:

1. Generates a local SDK in the language of your Pulumi program
1. Automatically adds the package to your `Pulumi.yaml` file under the `packages` key

{{% notes type="tip" %}}
In order to make sure Pulumi users are aware of the Any Terraform Provider's capabilities, Pulumi has included select, popular providers that can be consumed in Pulumi via the Any Terraform Provider in the Pulumi Registry, such as [The Honeycomb provider](/registry/packages/honeycombio/).
{{% /notes %}}

The generated SDK will include a `.gitignore` so it can be safely committed to version control without including all of the SDK's dependencies. The SDK installation process also downloads the provider binary to a shared location on your local system outside of the working directory. The binary is cached, so it will not need to be downloaded more than once, and is not committed to version control.

#### About Provider Packages in the Project Configuration File

{{% notes type="info" %}}
When using `pulumi package add` with Pulumi version 3.157.0 or later, packages are automatically added to your project configuration file (`Pulumi.yaml`).
{{% /notes %}}

When you run `pulumi package add`, the package is automatically added to your Pulumi project configuration file under the [`packages`](/docs/iac/concepts/projects/project-file/#packages-options) key. For the example in the previous section, the following entry would be added to your `Pulumi.yaml`:

```yaml
packages:
  random:
    source: terraform-provider
    # The version of terraform-provider in the Pulumi registry.
    # This is automatically added by the `pulumi package add` command:
    version: 0.10.0
    parameters:
      - hashicorp/random
      # The version of hashicorp/random in the OpenTofu Registry.
      # This is not a required parameter, but you may wish to include
      # it at the command line or add it after the fact in Pulumi.yaml
      # in order to ensure consistent builds. If this value is not
      # specified, the provider will take the latest version of
      # the OpenTofu provider.
      - 3.7.1
```

You can install any packages tracked in the project configuration file with the [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) command:

```bash
$ pulumi install
Installing packages defined in Pulumi.yaml...
Installing package 'random'...
# ...
```

{{% notes type="warning" %}}
If you are using `pulumi install` to install packages defined in your project file, be sure to remove any generated SDK files from version control and `.gitignore` the SDK directory or the generated files will still be under version control!
{{% /notes %}}

## Default and Explicit Providers

Within a Pulumi program, there are two types of providers you can use to declare resources:

- **Default providers** are not declared in your Pulumi program, and use global configuration settings. Resources created with a default provider do not need the [`provider` option](/docs/iac/concepts/options/provider/) set in the [resource's options parameter](/docs/iac/concepts/options/). This is the simplest way to declare Pulumi resources.
- **Explicit providers** are explicitly declared in your Pulumi program, and use the configuration values you specify when you declare the provider. Resources created with explicit providers must have the `provider` option set in their resource options. The most common use case for explicit providers are multi-environment deployments of cloud infrastructure in a single stack. Explicit providers are themselves Pulumi resources, and their configuration values are [Pulumi inputs](/docs/iac/concepts/inputs-outputs/).

The following table summarizes the differences between default and explicit providers:

|                       | Default Providers                                                                                         | Explicit Providers                                                                                                                                    |
|-----------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Declaration           | Never declared in your Pulumi program                                                                     | Explicitly declared, are themselves Pulumi resources that take inputs as configuration values                                                         |
| Configuration         | Comes from system (e.g. environment variables) or well-known stack configuration keys (e.g. `aws:region`) | Explicitly configured when the provider is declared                                                                                                   |
| Assigned to resources | Automatically, if the `provider` resource option is not set                                               | Explicitly, via the `provider` resource option                                                                                                        |
| Can be disabled?      | Yes                                                                                                       | No                                                                                                                                                    |
| Best fit for          | Simpler use cases, where only a single provider is needed per cloud                                                                                         | Greater control, often required for deploying into multiple environments for the same cloud in the same Pulumi program (e.g. two or more AWS regions) |

{{% notes type="info" %}}
The choice (or necessity) to use explicit providers is on a per-cloud basis. For example, you may have a program that deploys primary and disaster recovery resources in the public cloud, which might require explicit providers, but the program also creates DNS entries in with your DNS vendor, which can use the default provider since there's only a single resource to update for DNS.
{{% /notes %}}

### Default Provider Configuration

A default provider's global configuration settings (like credentials, region, or tenancy configuration) can be set explicitly in your stack configuration (so its configuration will be the same no matter where your Pulumi program is run), or implicitly through methods like environment variables or well-known file locations (so its configuration will be dependent on the environment). The precise way a provider reads its implicit global settings depends on the particular provider. The provider's Installation and Configuration page ([example](/registry/packages/aws/installation-configuration/)) in the Pulumi Registry contains the details of how a provider will attempt to read configuration values if not explicitly specified in the stack configuration.

You may also specify default provider configuration in your [stack config](/docs/iac/concepts/config/). The configuration keys for default provider configuration follow the pattern `<provider name>:<config setting name>`. For example, to configure the `region` on the default AWS provider, you would run the following command:

```bash
pulumi config set aws:region us-east-1
```

{{% notes type="info" %}}
Default provider configuration in your stack config always takes precedence over implicit configuration like environment variables.
{{% /notes %}}

{{% notes type="info" %}}
When specifying default provider configuration, be sure to pay attention to whether a configuration setting is plain-text or a secret. Secret values must be set by passing the `--secret` flag to the [`pulumi config set`](/docs/iac/cli/commands/pulumi_config_set/) command.
{{% /notes %}}

#### Example: Setting the Region on the Default AWS Provider

To see how default provider configuration works, let's look at a detailed example. If you run this CLI command:

```bash
pulumi config set aws:region us-west-2
```

Then, you deploy the following Pulumi program:

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
let aws = require("@pulumi/aws");

let instance = new aws.ec2.Instance("myInstance", {
    instanceType: "t2.micro",
    ami: "myAMI",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let aws = require("@pulumi/aws");

let instance = new aws.ec2.Instance("myInstance", {
    instanceType: "t2.micro",
    ami: "myAMI",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi_aws import ec2

instance = ec2.Instance("myInstance", instance_type="t2.micro", ami="myAMI")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
vpc, err := ec2.NewInstance(ctx, "myInstance", &ec2.InstanceArgs{
    InstanceType: pulumi.String("t2.micro"),
    Ami:          pulumi.String("myAMI"),
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var instance = new Aws.Ec2.Instance("myInstance", new Aws.Ec2.InstanceArgs
{
    InstanceType = "t2.micro",
    Ami = "myAMI",
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var instance = new Instance("myInstance",
    InstanceArgs.builder()
        .instanceType("t2.micro")
        .ami("myAMI")
        .build());
```

{{% /choosable %}}

{{< /chooser >}}

It creates a single EC2 instance in the us-west-2 region, no matter what the `AWS_REGION` environment variable may be on your system.

### Explicit Provider Configuration

Explicit providers are Pulumi resources themselves and take Pulumi inputs as configuration values. This enables powerful scenarios that aren't possible with default providers. For example, you can create a Kubernetes cluster and then immediately deploy resources to that cluster in the same Pulumi program. This works because the kubeconfig of the newly created cluster (a Pulumi output) can be passed directly to the `kubeconfig` argument of an explicit Kubernetes provider (which accepts Pulumi inputs). The explicit provider can then be assigned to resources that should be deployed to the newly provisioned cluster. This scenario is _only_ possible by using explicit providers: We cannot use the default Kubernetes provider because we don't know what its kubeconfig should be until after the cluster is created.

While the default provider configuration may be appropriate for the majority of Pulumi programs, some programs may have special requirements. One example is a program that needs to deploy to multiple AWS regions simultaneously. Another example is a program that needs to deploy to a Kubernetes cluster, created earlier in the program, which requires explicitly creating, configuring, and referencing providers. This is typically done by instantiating the relevant package’s `Provider` type and passing in the options for each `Resource` that needs to use it. For example, the following configuration and program creates an ACM certificate in the `us-east-1` region and a load balancer listener in the `us-west-2` region.

{{% notes type="info" %}}
**Note:** This example for AWS does not apply to Azure which provides access to all regions regardless of the default region defined in your Pulumi program. That means you don't need to explicitly create and configure providers for each region when working with Azure. You can simply specify the region in the resource definition itself.
{{% /notes %}}

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
let pulumi = require("@pulumi/pulumi");
let aws = require("@pulumi/aws");

// Create an AWS provider for the us-east-1 region.
let useast1 = new aws.Provider("useast1", { region: "us-east-1" });

// Create an ACM certificate in us-east-1.
let cert = new aws.acm.Certificate("cert", {
    domainName: "foo.com",
    validationMethod: "EMAIL",
}, { provider: useast1 });

// Create an ALB listener in the default region that references the ACM certificate created above.
let listener = new aws.lb.Listener("listener", {
    loadBalancerArn: loadBalancerArn,
    port: 443,
    protocol: "HTTPS",
    sslPolicy: "ELBSecurityPolicy-2016-08",
    certificateArn: cert.arn,
    defaultAction: {
        targetGroupArn: targetGroupArn,
        type: "forward",
    },
})
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let pulumi = require("@pulumi/pulumi");
let aws = require("@pulumi/aws");

// Create an AWS provider for the us-east-1 region.
let useast1 = new aws.Provider("useast1", { region: "us-east-1" });

// Create an ACM certificate in us-east-1.
let cert = new aws.acm.Certificate("cert", {
    domainName: "foo.com",
    validationMethod: "EMAIL",
}, { provider: useast1 });

// Create an ALB listener in the default region that references the ACM certificate created above.
let listener = new aws.lb.Listener("listener", {
    loadBalancerArn: loadBalancerArn,
    port: 443,
    protocol: "HTTPS",
    sslPolicy: "ELBSecurityPolicy-2016-08",
    certificateArn: cert.arn,
    defaultAction: {
        targetGroupArn: targetGroupArn,
        type: "forward",
    },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

# Create an AWS provider for the us-east-1 region.
useast1 = aws.Provider("useast1", region="us-east-1")

# Create an ACM certificate in us-east-1.
cert = aws.acm.Certificate("cert",
    domain_name="foo.com",
    validation_method="EMAIL",
    opts=pulumi.ResourceOptions(provider=useast1))

# Create an ALB listener in the default region that references the ACM certificate created above.
listener = aws.lb.Listener("listener",
    load_balancer_arn=load_balancer_arn,
    port=443,
    protocol="HTTPS",
    ssl_policy="ELBSecurityPolicy-2016-08",
    certificate_arn=cert.arn,
    default_action={
        "target_group_arn": target_group_arn,
        "type": "forward",
    })
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Create an AWS provider for the us-east-1 region.
useast1, err := aws.NewProvider(ctx, "useast1", &aws.ProviderArgs{
    Region: pulumi.String("us-east-1"),
})
if err != nil {
    return err
}

// Create an ACM certificate in us-east-1.
cert, err := acm.NewCertificate(ctx, "myInstance", &acm.CertificateArgs{
    DomainName:       pulumi.String("foo.com"),
    ValidationMethod: pulumi.String("EMAIL"),
}, pulumi.Provider(useast1))
if err != nil {
    return err
}

// Create an ALB listener in the default region that references the ACM certificate created above.
listener, err := lb.NewListener(ctx, "myInstance", &lb.ListenerArgs{
    LoadBalancerArn: loadBalancerArn,
    Port:            pulumi.Int(443),
    Protocol:        pulumi.String("HTTPS"),
    SslPolicy:       pulumi.String("ELBSecurityPolicy-2016-08"),
    CertificateArn:  cert.Arn,
    DefaultActions: lb.ListenerDefaultActionArray{
        &lb.ListenerDefaultActionArgs{
            TargetGroupArn: targetGroupArn,
            Type:           pulumi.String("forward"),
        },
    },
})
if err != nil {
    return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Create an AWS provider for the us-east-1 region.
var useast1 = new Aws.Provider("useast1", new Aws.ProviderArgs { Region = "us-east-1" });

// Create an ACM certificate in us-east-1.
var cert = new Aws.Acm.Certificate("cert", new Aws.Acm.CertificateArgs
{
    DomainName = "foo.com",
    ValidationMethod = "EMAIL",
}, new CustomResourseOptions { Provider = useast1 });

// Create an ALB listener in the default region that references the ACM certificate created above.
var listener = new Aws.Lb.Listener("listener", new Aws.Lb.ListenerArgs
{
    LoadBalancerArn = loadBalancerArn,
    Port = 443,
    Protocol = "HTTPS",
    SslPolicy = "ELBSecurityPolicy-2016-08",
    CertificateArn = cert.arn,
    DefaultAction: new Aws.Lb.ListenerDefaultAction
    {
        TargetGroupArn = targetGroupArn,
        Type = "forward",
    },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// Create an AWS provider for the us-east-1 region.
var useast1 = new Provider("useast1",
        ProviderArgs.builder().region("us-east-1").build());

// Create an ACM certificate in us-east-1.
var cert = new Certificate("cert",
    CertificateArgs.builder()
        .domainName("foo.com")
        .validationMethod("EMAIL")
        .build(),
    CustomResourceOptions.builder()
            .provider(useast1)
            .build());

// Create an ALB listener in the default region that references the ACM certificate created above.
var listener = new Listener("listener",
        ListenerArgs.builder()
            .loadBalancerArn(loadBalancerArn)
            .port(443)
            .protocol("HTTPS")
            .sslPolicy("ELBSecurityPolicy-2016-08")
            .certificateArn(cert.arn())
            .defaultActions(ListenerDefaultActionArgs.builder()
                    .targetGroupArn(targetGroupArn)
                    .type("forward")
                    .build())
            .build());
```

{{% /choosable %}}

{{< /chooser >}}

```bash
pulumi config set aws:region us-west-2
```

Component resources also accept a set of providers to use with their child resources. For example, the EC2 instance parented to `myResource` in the program below is created in `us-east-1`, and the Kubernetes pod parented to myResource is created in the cluster targeted by the `test-ci` context.

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
class MyResource extends pulumi.ComponentResource {
    constructor(name, opts) {
        let instance = new aws.ec2.Instance("instance", { ... }, { parent: this });
        let pod = new kubernetes.core.v1.Pod("pod", { ... }, { parent: this });
    }
}

let useast1 = new aws.Provider("useast1", { region: "us-east-1" });
let myk8s = new kubernetes.Provider("myk8s", { context: "test-ci" });
let myResource = new MyResource("myResource", { providers: { aws: useast1, kubernetes: myk8s } });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
class MyResource extends pulumi.ComponentResource {
    constructor(name, opts) {
        let instance = new aws.ec2.Instance("instance", { ... }, { parent: this });
        let pod = new kubernetes.core.v1.Pod("pod", { ... }, { parent: this });
    }
}

let useast1 = new aws.Provider("useast1", { region: "us-east-1" });
let myk8s = new kubernetes.Provider("myk8s", { context: "test-ci" });
let myResource = new MyResource("myResource", { providers: { aws: useast1, kubernetes: myk8s } });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
class MyResource(pulumi.ComponentResource):
    def __init__(self, name, opts):
        instance = aws.ec2.Instance("instance", ..., opts=pulumi.ResourceOptions(parent=self))
        pod = kubernetes.core.v1.Pod("pod", ..., opts=pulumi.ResourceOptions(parent=self))

useast1 = aws.Provider("useast1", region="us-east-1")
myk8s = kubernetes.Provider("myk8s", context="test-ci")
my_resource = MyResource("myResource", pulumi.ResourceOptions(providers={
    "aws": useast1,
    "kubernetes": myk8s,
})
```

{{% /choosable %}}
{{% choosable language go %}}

```go
useast1, err := aws.NewProvider(ctx, "useast1", &aws.ProviderArgs{
    Region: pulumi.String("us-east-1"),
})
if err != nil {
    return err
}
myk8s, err := kubernetes.NewProvider(ctx, "myk8s", &kubernetes.ProviderArgs{
    Context: pulumi.String("test-ci"),
})
if err != nil {
    return err
}
myResource, err := NewMyResource(ctx, "myResource", pulumi.ProviderMap(map[string]pulumi.ProviderResource{
    "aws": useast1,
    "kubernetes": myk8s,
}))
if err != nil {
    return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Aws = Pulumi.Aws;
using Kubernetes = Pulumi.Kubernetes;

class MyResource : ComponentResource
{
    public MyResource(string name, ComponentResourceOptions opts)
        : base(name, opts)
    {
        var instance = new Aws.Ec2.Instance("instance", new Aws.Ec2.InstanceArgs { ... }, new CustomResourceOptions { Parent = this });
        var pod = new Kubernetes.Core.V1.Pod("pod", new Kubernetes.Core.V1.PodArgs { ... }, new CustomResourceOptions { Parent = this });
    }
}

class MyStack
{
    public MyStack()
    {
        var useast1 = new Aws.Provider("useast1",
            new Aws.ProviderArgs { Region = "us-east-1" });
        var myk8s = new Kubernetes.Provider("myk8s",
            new Kubernetes.ProviderArgs { Context = "test-ci" });
        var myResource = new MyResource("myResource",
            new ComponentResourceOptions { Providers = { useast1, myk8s } });
    }
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
final var usEast1 = new com.pulumi.aws.Provider("aws",
    com.pulumi.aws.ProviderArgs.builder()
        .region("us-east-1")
        .build());
final var myk8s = new com.pulumi.kubernetes.Provider("kubernetes",
    com.pulumi.kubernetes.ProviderArgs.builder()
        .kubeconfig(kubeconfig)
        .build());
final var myresource = new MyResource("myResource",
    ComponentResourceOptions.builder()
        .providers(usEast1, myk8s)
        .build());
```

{{% /choosable %}}

{{< /chooser >}}

## Disabling Default Providers

While default providers are enabled by default, they [can be disabled](/docs/concepts/config#special-configuration-options) on a per stack basis. Disabling default providers is a good idea if you want to ensure that your providers must be explicitly configured and should never use the default system configuration. (The meaning of "default system configuration" depends on the provider: it may be environment variables which can differ between environments, or a configuration file in a default location, and so on.)

{{% notes type="tip" %}}
Disabling explicit providers will help ensure that the [`provider` resource option](/docs/iac/concepts/options/provider) _must_ be set on all resources. If the `provider` resource option is not set (a common mistake) the resource will use the default provider, which can result in resources being deployed to the wrong environment.
{{% /notes %}}

For example, to disable the `aws` provider, you can run:

```sh
pulumi config set --path 'pulumi:disable-default-providers[0]' aws
```

If you wanted to also disable the `kubernetes` default provider, as well as the `aws` default provider, you could run:

```sh
pulumi config set --path 'pulumi:disable-default-providers[1]' kubernetes
```

This adds a new entry to the list `pulumi:disable-default-providers`. To disable all default providers, use `*` as the package name:

```sh
pulumi config set --path 'pulumi:disable-default-providers[0]' '*'
```
