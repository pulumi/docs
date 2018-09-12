---
title: Module lightsail
---

<a href="../index.html">@pulumi/aws</a> &gt; lightsail

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Domain">class Domain</a>
* <a href="#Instance">class Instance</a>
* <a href="#KeyPair">class KeyPair</a>
* <a href="#StaticIp">class StaticIp</a>
* <a href="#StaticIpAttachment">class StaticIpAttachment</a>
* <a href="#DomainArgs">interface DomainArgs</a>
* <a href="#DomainState">interface DomainState</a>
* <a href="#InstanceArgs">interface InstanceArgs</a>
* <a href="#InstanceState">interface InstanceState</a>
* <a href="#KeyPairArgs">interface KeyPairArgs</a>
* <a href="#KeyPairState">interface KeyPairState</a>
* <a href="#StaticIpArgs">interface StaticIpArgs</a>
* <a href="#StaticIpAttachmentArgs">interface StaticIpAttachmentArgs</a>
* <a href="#StaticIpAttachmentState">interface StaticIpAttachmentState</a>
* <a href="#StaticIpState">interface StaticIpState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/domain.ts">lightsail/domain.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts">lightsail/instance.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts">lightsail/keyPair.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts">lightsail/staticIp.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIpAttachment.ts">lightsail/staticIpAttachment.ts</a> 


<h2 class="pdoc-module-header" id="Domain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/domain.ts#L16">class Domain</a>
</h2>

Creates a domain resource for the specified domain (e.g., example.com).
You cannot register a new domain name using Lightsail. You must register
a domain name using Amazon Route 53 or another domain name registrar.
If you have already registered your domain, you can enter its name in
this parameter to manage the DNS records for that domain.

~> **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/domain.ts#L36">constructor</a>
</h3>

```typescript
new Domain(name: string, args: DomainArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Domain resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/domain.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainState): Domain
```


Get an existing Domain resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/domain.ts#L32">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the Lightsail domain

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/domain.ts#L36">property domainName</a>
</h3>

```typescript
public domainName: pulumi.Output<string>;
```


The name of the Lightsail domain to manage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Instance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L14">class Instance</a>
</h2>

Provides a Lightsail Instance. Amazon Lightsail is a service to provide easy virtual private servers
with custom software already setup. See [What is Amazon Lightsail?](https://lightsail.aws.amazon.com/ls/docs/getting-started/article/what-is-amazon-lightsail)
for more information.

~> **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L70">constructor</a>
</h3>

```typescript
new Instance(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Instance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState): Instance
```


Get an existing Instance resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L35">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the Lightsail instance (matches `id`).
* `availability_zone`
* `blueprint_id`
* `bundle_id`
* `key_pair_name`
* `user_data`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L40">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The Availability Zone in which to create your
instance. At this time, must be in `us-east-1`, `us-east-2`, `us-west-2`, `eu-west-1`, `eu-west-2`, `eu-central-1`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`, `ap-south-1` regions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L45">property blueprintId</a>
</h3>

```typescript
public blueprintId: pulumi.Output<string>;
```


The ID for a virtual private server image
(see list below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L49">property bundleId</a>
</h3>

```typescript
public bundleId: pulumi.Output<string>;
```


The bundle of specification information (see list below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L50">property cpuCount</a>
</h3>

```typescript
public cpuCount: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L51">property createdAt</a>
</h3>

```typescript
public createdAt: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L52">property ipv6Address</a>
</h3>

```typescript
public ipv6Address: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L53">property isStaticIp</a>
</h3>

```typescript
public isStaticIp: pulumi.Output<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L58">property keyPairName</a>
</h3>

```typescript
public keyPairName: pulumi.Output<string | undefined>;
```


The name of your key pair. Created in the
Lightsail console (cannot use `aws_key_pair` at this time)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L62">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Lightsail Instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L63">property privateIpAddress</a>
</h3>

```typescript
public privateIpAddress: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L64">property publicIpAddress</a>
</h3>

```typescript
public publicIpAddress: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L65">property ramSize</a>
</h3>

```typescript
public ramSize: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L69">property userData</a>
</h3>

```typescript
public userData: pulumi.Output<string | undefined>;
```


launch script to configure server with additional user data

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L70">property username</a>
</h3>

```typescript
public username: pulumi.Output<string>;
```

<h2 class="pdoc-module-header" id="KeyPair">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L14">class KeyPair</a>
</h2>

Provides a Lightsail Key Pair, for use with Lightsail Instances. These key pairs
are seperate from EC2 Key Pairs, and must be created or imported for use with
Lightsail.

~> **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L66">constructor</a>
</h3>

```typescript
new KeyPair(name: string, args?: KeyPairArgs, opts?: pulumi.CustomResourceOptions)
```


Create a KeyPair resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeyPairState): KeyPair
```


Get an existing KeyPair resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the Lightsail key pair

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L35">property encryptedFingerprint</a>
</h3>

```typescript
public encryptedFingerprint: pulumi.Output<string>;
```


The MD5 public key fingerprint for the encrypted
private key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L41">property encryptedPrivateKey</a>
</h3>

```typescript
public encryptedPrivateKey: pulumi.Output<string>;
```


the private key material, base 64 encoded and
encrypted with the given `pgp_key`. This is only populated when creating a new
key and `pgp_key` is supplied

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L45">property fingerprint</a>
</h3>

```typescript
public fingerprint: pulumi.Output<string>;
```


The MD5 public key fingerprint as specified in section 4 of RFC 4716.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Lightsail Key Pair. If omitted, a unique
name will be generated by Terraform

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L51">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L56">property pgpKey</a>
</h3>

```typescript
public pgpKey: pulumi.Output<string | undefined>;
```


An optional PGP key to encrypt the resulting private
key material. Only used when creating a new key pair

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L61">property privateKey</a>
</h3>

```typescript
public privateKey: pulumi.Output<string>;
```


the private key, base64 encoded. This is only populated
when creating a new key, and when no `pgp_key` is provided

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L66">property publicKey</a>
</h3>

```typescript
public publicKey: pulumi.Output<string>;
```


The public key material. This public key will be
imported into Lightsail

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="StaticIp">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L12">class StaticIp</a>
</h2>

Allocates a static IP address.

~> **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L40">constructor</a>
</h3>

```typescript
new StaticIp(name: string, args?: StaticIpArgs, opts?: pulumi.CustomResourceOptions)
```


Create a StaticIp resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StaticIpState): StaticIp
```


Get an existing StaticIp resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the Lightsail static IP

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L32">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string>;
```


The allocated static IP address

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name for the allocated static IP

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L40">property supportCode</a>
</h3>

```typescript
public supportCode: pulumi.Output<string>;
```


The support code.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="StaticIpAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIpAttachment.ts#L12">class StaticIpAttachment</a>
</h2>

Provides a static IP address attachment - relationship between a Lightsail static IP & Lightsail instance.

~> **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIpAttachment.ts#L32">constructor</a>
</h3>

```typescript
new StaticIpAttachment(name: string, args: StaticIpAttachmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a StaticIpAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIpAttachment.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StaticIpAttachmentState): StaticIpAttachment
```


Get an existing StaticIpAttachment resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIpAttachment.ts#L28">property instanceName</a>
</h3>

```typescript
public instanceName: pulumi.Output<string>;
```


The name of the Lightsail instance to attach the IP to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIpAttachment.ts#L32">property staticIpName</a>
</h3>

```typescript
public staticIpName: pulumi.Output<string>;
```


The name of the allocated static IP

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DomainArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/domain.ts#L81">interface DomainArgs</a>
</h2>

The set of arguments for constructing a Domain resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/domain.ts#L85">property domainName</a>
</h3>

```typescript
domainName: pulumi.Input<string>;
```


The name of the Lightsail domain to manage

<h2 class="pdoc-module-header" id="DomainState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/domain.ts#L67">interface DomainState</a>
</h2>

Input properties used for looking up and filtering Domain resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/domain.ts#L71">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the Lightsail domain

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/domain.ts#L75">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```


The name of the Lightsail domain to manage

<h2 class="pdoc-module-header" id="InstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L183">interface InstanceArgs</a>
</h2>

The set of arguments for constructing a Instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L188">property availabilityZone</a>
</h3>

```typescript
availabilityZone: pulumi.Input<string>;
```


The Availability Zone in which to create your
instance. At this time, must be in `us-east-1`, `us-east-2`, `us-west-2`, `eu-west-1`, `eu-west-2`, `eu-central-1`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`, `ap-south-1` regions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L193">property blueprintId</a>
</h3>

```typescript
blueprintId: pulumi.Input<string>;
```


The ID for a virtual private server image
(see list below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L197">property bundleId</a>
</h3>

```typescript
bundleId: pulumi.Input<string>;
```


The bundle of specification information (see list below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L202">property keyPairName</a>
</h3>

```typescript
keyPairName?: pulumi.Input<string>;
```


The name of your key pair. Created in the
Lightsail console (cannot use `aws_key_pair` at this time)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L206">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Lightsail Instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L210">property userData</a>
</h3>

```typescript
userData?: pulumi.Input<string>;
```


launch script to configure server with additional user data

<h2 class="pdoc-module-header" id="InstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L133">interface InstanceState</a>
</h2>

Input properties used for looking up and filtering Instance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L142">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the Lightsail instance (matches `id`).
* `availability_zone`
* `blueprint_id`
* `bundle_id`
* `key_pair_name`
* `user_data`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L147">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The Availability Zone in which to create your
instance. At this time, must be in `us-east-1`, `us-east-2`, `us-west-2`, `eu-west-1`, `eu-west-2`, `eu-central-1`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`, `ap-south-1` regions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L152">property blueprintId</a>
</h3>

```typescript
blueprintId?: pulumi.Input<string>;
```


The ID for a virtual private server image
(see list below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L156">property bundleId</a>
</h3>

```typescript
bundleId?: pulumi.Input<string>;
```


The bundle of specification information (see list below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L157">property cpuCount</a>
</h3>

```typescript
cpuCount?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L158">property createdAt</a>
</h3>

```typescript
createdAt?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L159">property ipv6Address</a>
</h3>

```typescript
ipv6Address?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L160">property isStaticIp</a>
</h3>

```typescript
isStaticIp?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L165">property keyPairName</a>
</h3>

```typescript
keyPairName?: pulumi.Input<string>;
```


The name of your key pair. Created in the
Lightsail console (cannot use `aws_key_pair` at this time)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L169">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Lightsail Instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L170">property privateIpAddress</a>
</h3>

```typescript
privateIpAddress?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L171">property publicIpAddress</a>
</h3>

```typescript
publicIpAddress?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L172">property ramSize</a>
</h3>

```typescript
ramSize?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L176">property userData</a>
</h3>

```typescript
userData?: pulumi.Input<string>;
```


launch script to configure server with additional user data

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/instance.ts#L177">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="KeyPairArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L154">interface KeyPairArgs</a>
</h2>

The set of arguments for constructing a KeyPair resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L159">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Lightsail Key Pair. If omitted, a unique
name will be generated by Terraform

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L160">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L165">property pgpKey</a>
</h3>

```typescript
pgpKey?: pulumi.Input<string>;
```


An optional PGP key to encrypt the resulting private
key material. Only used when creating a new key pair

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L170">property publicKey</a>
</h3>

```typescript
publicKey?: pulumi.Input<string>;
```


The public key material. This public key will be
imported into Lightsail

<h2 class="pdoc-module-header" id="KeyPairState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L108">interface KeyPairState</a>
</h2>

Input properties used for looking up and filtering KeyPair resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L112">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the Lightsail key pair

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L117">property encryptedFingerprint</a>
</h3>

```typescript
encryptedFingerprint?: pulumi.Input<string>;
```


The MD5 public key fingerprint for the encrypted
private key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L123">property encryptedPrivateKey</a>
</h3>

```typescript
encryptedPrivateKey?: pulumi.Input<string>;
```


the private key material, base 64 encoded and
encrypted with the given `pgp_key`. This is only populated when creating a new
key and `pgp_key` is supplied

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L127">property fingerprint</a>
</h3>

```typescript
fingerprint?: pulumi.Input<string>;
```


The MD5 public key fingerprint as specified in section 4 of RFC 4716.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L132">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Lightsail Key Pair. If omitted, a unique
name will be generated by Terraform

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L133">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L138">property pgpKey</a>
</h3>

```typescript
pgpKey?: pulumi.Input<string>;
```


An optional PGP key to encrypt the resulting private
key material. Only used when creating a new key pair

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L143">property privateKey</a>
</h3>

```typescript
privateKey?: pulumi.Input<string>;
```


the private key, base64 encoded. This is only populated
when creating a new key, and when no `pgp_key` is provided

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/keyPair.ts#L148">property publicKey</a>
</h3>

```typescript
publicKey?: pulumi.Input<string>;
```


The public key material. This public key will be
imported into Lightsail

<h2 class="pdoc-module-header" id="StaticIpArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L94">interface StaticIpArgs</a>
</h2>

The set of arguments for constructing a StaticIp resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name for the allocated static IP

<h2 class="pdoc-module-header" id="StaticIpAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIpAttachment.ts#L80">interface StaticIpAttachmentArgs</a>
</h2>

The set of arguments for constructing a StaticIpAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIpAttachment.ts#L84">property instanceName</a>
</h3>

```typescript
instanceName: pulumi.Input<string>;
```


The name of the Lightsail instance to attach the IP to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIpAttachment.ts#L88">property staticIpName</a>
</h3>

```typescript
staticIpName: pulumi.Input<string>;
```


The name of the allocated static IP

<h2 class="pdoc-module-header" id="StaticIpAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIpAttachment.ts#L66">interface StaticIpAttachmentState</a>
</h2>

Input properties used for looking up and filtering StaticIpAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIpAttachment.ts#L70">property instanceName</a>
</h3>

```typescript
instanceName?: pulumi.Input<string>;
```


The name of the Lightsail instance to attach the IP to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIpAttachment.ts#L74">property staticIpName</a>
</h3>

```typescript
staticIpName?: pulumi.Input<string>;
```


The name of the allocated static IP

<h2 class="pdoc-module-header" id="StaticIpState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L72">interface StaticIpState</a>
</h2>

Input properties used for looking up and filtering StaticIp resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L76">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the Lightsail static IP

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L80">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The allocated static IP address

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L84">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name for the allocated static IP

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lightsail/staticIp.ts#L88">property supportCode</a>
</h3>

```typescript
supportCode?: pulumi.Input<string>;
```


The support code.

