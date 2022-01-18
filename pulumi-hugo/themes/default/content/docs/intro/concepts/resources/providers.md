---
title: "Providers"
meta_desc: A resource provider handles communications with a cloud service to create, read, update, and delete the resources you define in your Pulumi programs.
menu:
  intro:
    parent: resources
    weight: 4
---

A resource provider handles communications with a cloud service to create, read, update, and delete the resources you define in your Pulumi programs. Pulumi passes your code to a language host such as Node.js, waits to be notified of resource registrations, assembles a model of your desired state, and calls on the resource provider to produce that state. The resource provider translates those requests into API calls to the cloud service.

A resource provider is tied to the language that you use to write your programs. For example, if your cloud provider is AWS, the following providers are available:

- JavaScript/TypeScript: `@pulumi/aws`
- Python: `pulumi-aws`
- Go: `github.com/pulumi/pulumi-aws/sdk/go/aws`
- .NET: `Pulumi.Aws`

Normally, since you declare the language and cloud provider you intend to use when you write a program, Pulumi installs the provider for you as a plugin, using the appropriate package manager, such as NPM for Typescript.

The resource provider for custom resources is determined based on its package name. For example, the `aws` package loads a plugin named `pulumi-resource-aws`, and the `kubernetes` package loads a plugin named `pulumi-resource-kubernetes`.

## Default Provider Configuration

By default, each provider uses its package’s global configuration settings, which are controlled by your stack’s configuration. You can set information such as your cloud provider credentials with environment variables and configuration files. If you store this data in standard locations, Pulumi knows how to retrieve them.

For example, suppose you run this CLI command:

```bash
$ pulumi config set aws:region us-west-2
```

Then, suppose you deploy the following Pulumi program:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

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

{{< /chooser >}}

It creates a single EC2 instance in the us-west-2 region.

## Explicit Provider Configuration

While the default provider configuration may be appropriate for the majority of Pulumi programs, some programs may have special requirements. One example is a program that needs to deploy to multiple AWS regions simultaneously. Another example is a program that needs to deploy to a Kubernetes cluster, created earlier in the program, which requires explicitly creating, configuring, and referencing providers. This is typically done by instantiating the relevant package’s `Provider` type and passing in the options for each `Resource` that needs to use it. For example, the following configuration and program creates an ACM certificate in the `us-east-1` region and a load balancer listener in the `us-west-2` region.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

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
    __opts__=pulumi.ResourceOptions(provider=useast1))

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
var cert = new Aws.Acm.Certificate("cert", new Aws.Acm.CertifiateArgs
{
    DomainName = "foo.com",
    ValidationMethod = "EMAIL",
}, new ResourceArgs { Provider = useast1 });

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

{{< /chooser >}}

```bash
$ pulumi config set aws:region us-west-2
```

Component resources also accept a set of providers to use with their child resources. For example, the EC2 instance parented to `myResource` in the program below is created in `us-east-1`, and the Kubernetes pod parented to myResource is created in the cluster targeted by the `test-ci` context.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

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
        instance = aws.ec2.Instance("instance", ..., __opts__=pulumi.ResourceOptions(parent=self))
        pod = kubernetes.core.v1.Pod("pod", ..., __opts__=pulumi.ResourceOptions(parent=self))

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

{{< /chooser >}}
