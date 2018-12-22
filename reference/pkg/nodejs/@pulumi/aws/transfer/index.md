---
title: Module transfer
---

<a href="../index.html">@pulumi/aws</a> &gt; transfer

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Server">class Server</a>
* <a href="#ServerArgs">interface ServerArgs</a>
* <a href="#ServerState">interface ServerState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts">transfer/server.ts</a> 


<h2 class="pdoc-module-header" id="Server">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L63">class Server</a>
</h2>

Provides a AWS Transfer Server resource.

```hcl
resource "aws_iam_role" "foo" {
	name = "tf-test-transfer-server-iam-role"

	assume_role_policy = <<EOF
{
	"Version": "2012-10-17",
	"Statement": [
		{
		"Effect": "Allow",
		"Principal": {
			"Service": "transfer.amazonaws.com"
		},
		"Action": "sts:AssumeRole"
		}
	]
}
EOF
}

resource "aws_iam_role_policy" "foo" {
	name = "tf-test-transfer-server-iam-policy-%s"
	role = "${aws_iam_role.foo.id}"
	policy = <<POLICY
{
	"Version": "2012-10-17",
	"Statement": [
		{
		"Sid": "AllowFullAccesstoCloudWatchLogs",
		"Effect": "Allow",
		"Action": [
			"logs:*"
		],
		"Resource": "*"
		}
	]
}
POLICY
}


resource "aws_transfer_server" "foo" {
  identity_provider_type = "SERVICE_MANAGED"
  logging_role = "${aws_iam_role.foo.arn}"

  tags {
	NAME   = "tf-acc-test-transfer-server"
	ENV    = "test"
  }
}
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L103">constructor</a>
</h3>

```typescript
new Server(name: string, args?: ServerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Server resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L72">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServerState, opts?: pulumi.CustomResourceOptions): Server
```


Get an existing Server resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L79">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of Transfer Server

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L83">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L87">property identityProviderType</a>
</h3>

```typescript
public identityProviderType: pulumi.Output<string | undefined>;
```


The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L91">property invocationRole</a>
</h3>

```typescript
public invocationRole: pulumi.Output<string | undefined>;
```


Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L95">property loggingRole</a>
</h3>

```typescript
public loggingRole: pulumi.Output<string | undefined>;
```


Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L99">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L103">property url</a>
</h3>

```typescript
public url: pulumi.Output<string | undefined>;
```


- URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ServerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L175">interface ServerArgs</a>
</h2>

The set of arguments for constructing a Server resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L179">property identityProviderType</a>
</h3>

```typescript
identityProviderType?: pulumi.Input<string>;
```


The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L183">property invocationRole</a>
</h3>

```typescript
invocationRole?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L187">property loggingRole</a>
</h3>

```typescript
loggingRole?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L191">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L195">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


- URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.

<h2 class="pdoc-module-header" id="ServerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L141">interface ServerState</a>
</h2>

Input properties used for looking up and filtering Server resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L145">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of Transfer Server

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L149">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L153">property identityProviderType</a>
</h3>

```typescript
identityProviderType?: pulumi.Input<string>;
```


The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L157">property invocationRole</a>
</h3>

```typescript
invocationRole?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L161">property loggingRole</a>
</h3>

```typescript
loggingRole?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L165">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/transfer/server.ts#L169">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


- URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.

