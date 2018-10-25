---
title: Module pinpoint
---

<a href="../index.html">@pulumi/aws</a> &gt; pinpoint

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AdmChannel">class AdmChannel</a>
* <a href="#ApnsChannel">class ApnsChannel</a>
* <a href="#App">class App</a>
* <a href="#BaiduChannel">class BaiduChannel</a>
* <a href="#EmailChannel">class EmailChannel</a>
* <a href="#EventStream">class EventStream</a>
* <a href="#GcmChannel">class GcmChannel</a>
* <a href="#SmsChannel">class SmsChannel</a>
* <a href="#AdmChannelArgs">interface AdmChannelArgs</a>
* <a href="#AdmChannelState">interface AdmChannelState</a>
* <a href="#ApnsChannelArgs">interface ApnsChannelArgs</a>
* <a href="#ApnsChannelState">interface ApnsChannelState</a>
* <a href="#AppArgs">interface AppArgs</a>
* <a href="#AppState">interface AppState</a>
* <a href="#BaiduChannelArgs">interface BaiduChannelArgs</a>
* <a href="#BaiduChannelState">interface BaiduChannelState</a>
* <a href="#EmailChannelArgs">interface EmailChannelArgs</a>
* <a href="#EmailChannelState">interface EmailChannelState</a>
* <a href="#EventStreamArgs">interface EventStreamArgs</a>
* <a href="#EventStreamState">interface EventStreamState</a>
* <a href="#GcmChannelArgs">interface GcmChannelArgs</a>
* <a href="#GcmChannelState">interface GcmChannelState</a>
* <a href="#SmsChannelArgs">interface SmsChannelArgs</a>
* <a href="#SmsChannelState">interface SmsChannelState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts">pinpoint/admChannel.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts">pinpoint/apnsChannel.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts">pinpoint/app.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts">pinpoint/baiduChannel.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts">pinpoint/emailChannel.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts">pinpoint/eventStream.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts">pinpoint/gcmChannel.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts">pinpoint/smsChannel.ts</a> 


<h2 class="pdoc-module-header" id="AdmChannel">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L14">class AdmChannel</a>
</h2>

Provides a Pinpoint ADM (Amazon Device Messaging) Channel resource.

~> **Note:** All arguments including the Client ID and Client Secret will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).


<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L42">constructor</a>
</h3>

```typescript
new AdmChannel(name: string, args: AdmChannelArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AdmChannel resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AdmChannelState): AdmChannel
```


Get an existing AdmChannel resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L30">property applicationId</a>
</h3>

```typescript
public applicationId: pulumi.Output<string>;
```


The application ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L34">property clientId</a>
</h3>

```typescript
public clientId: pulumi.Output<string>;
```


Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L38">property clientSecret</a>
</h3>

```typescript
public clientSecret: pulumi.Output<string>;
```


Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L42">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Specifies whether to enable the channel. Defaults to `true`.

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

<h2 class="pdoc-module-header" id="ApnsChannel">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L7">class ApnsChannel</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L28">constructor</a>
</h3>

```typescript
new ApnsChannel(name: string, args: ApnsChannelArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ApnsChannel resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L16">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApnsChannelState): ApnsChannel
```


Get an existing ApnsChannel resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L20">property applicationId</a>
</h3>

```typescript
public applicationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L21">property bundleId</a>
</h3>

```typescript
public bundleId: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L22">property certificate</a>
</h3>

```typescript
public certificate: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L23">property defaultAuthenticationMethod</a>
</h3>

```typescript
public defaultAuthenticationMethod: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L24">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L25">property privateKey</a>
</h3>

```typescript
public privateKey: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L26">property teamId</a>
</h3>

```typescript
public teamId: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L27">property tokenKey</a>
</h3>

```typescript
public tokenKey: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L28">property tokenKeyId</a>
</h3>

```typescript
public tokenKeyId: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="App">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L10">class App</a>
</h2>

Provides a Pinpoint App resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L46">constructor</a>
</h3>

```typescript
new App(name: string, args?: AppArgs, opts?: pulumi.CustomResourceOptions)
```


Create a App resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AppState): App
```


Get an existing App resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L26">property applicationId</a>
</h3>

```typescript
public applicationId: pulumi.Output<string>;
```


The Application ID of the Pinpoint App.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L30">property campaignHook</a>
</h3>

```typescript
public campaignHook: pulumi.Output<{ ... } | undefined>;
```


The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L34">property limits</a>
</h3>

```typescript
public limits: pulumi.Output<{ ... } | undefined>;
```


The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The application name. By default generated by Terraform

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L42">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


The name of the Pinpoint application. Conflicts with `name`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L46">property quietTime</a>
</h3>

```typescript
public quietTime: pulumi.Output<{ ... } | undefined>;
```


The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="BaiduChannel">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L14">class BaiduChannel</a>
</h2>

Provides a Pinpoint Baidu Channel resource.

~> **Note:** All arguments including the Api Key and Secret Key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).


<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L42">constructor</a>
</h3>

```typescript
new BaiduChannel(name: string, args: BaiduChannelArgs, opts?: pulumi.CustomResourceOptions)
```


Create a BaiduChannel resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BaiduChannelState): BaiduChannel
```


Get an existing BaiduChannel resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L30">property apiKey</a>
</h3>

```typescript
public apiKey: pulumi.Output<string>;
```


Platform credential API key from Baidu.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L34">property applicationId</a>
</h3>

```typescript
public applicationId: pulumi.Output<string>;
```


The application ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L38">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Specifies whether to enable the channel. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L42">property secretKey</a>
</h3>

```typescript
public secretKey: pulumi.Output<string>;
```


Platform credential Secret key from Baidu.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="EmailChannel">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L7">class EmailChannel</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L25">constructor</a>
</h3>

```typescript
new EmailChannel(name: string, args: EmailChannelArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EmailChannel resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L16">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EmailChannelState): EmailChannel
```


Get an existing EmailChannel resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L20">property applicationId</a>
</h3>

```typescript
public applicationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L21">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L22">property fromAddress</a>
</h3>

```typescript
public fromAddress: pulumi.Output<string>;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L23">property identity</a>
</h3>

```typescript
public identity: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L24">property messagesPerSecond</a>
</h3>

```typescript
public messagesPerSecond: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L25">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="EventStream">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L7">class EventStream</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L22">constructor</a>
</h3>

```typescript
new EventStream(name: string, args: EventStreamArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventStream resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L16">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventStreamState): EventStream
```


Get an existing EventStream resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L20">property applicationId</a>
</h3>

```typescript
public applicationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L21">property destinationStreamArn</a>
</h3>

```typescript
public destinationStreamArn: pulumi.Output<string>;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L22">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="GcmChannel">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L7">class GcmChannel</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L22">constructor</a>
</h3>

```typescript
new GcmChannel(name: string, args: GcmChannelArgs, opts?: pulumi.CustomResourceOptions)
```


Create a GcmChannel resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L16">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GcmChannelState): GcmChannel
```


Get an existing GcmChannel resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L20">property apiKey</a>
</h3>

```typescript
public apiKey: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L21">property applicationId</a>
</h3>

```typescript
public applicationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L22">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SmsChannel">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L7">class SmsChannel</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L25">constructor</a>
</h3>

```typescript
new SmsChannel(name: string, args: SmsChannelArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SmsChannel resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L16">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SmsChannelState): SmsChannel
```


Get an existing SmsChannel resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L20">property applicationId</a>
</h3>

```typescript
public applicationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L21">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L22">property promotionalMessagesPerSecond</a>
</h3>

```typescript
public promotionalMessagesPerSecond: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L23">property senderId</a>
</h3>

```typescript
public senderId: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L24">property shortCode</a>
</h3>

```typescript
public shortCode: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L25">property transactionalMessagesPerSecond</a>
</h3>

```typescript
public transactionalMessagesPerSecond: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AdmChannelArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L105">interface AdmChannelArgs</a>
</h2>

The set of arguments for constructing a AdmChannel resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L109">property applicationId</a>
</h3>

```typescript
applicationId: pulumi.Input<string>;
```


The application ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L113">property clientId</a>
</h3>

```typescript
clientId: pulumi.Input<string>;
```


Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L117">property clientSecret</a>
</h3>

```typescript
clientSecret: pulumi.Input<string>;
```


Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L121">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether to enable the channel. Defaults to `true`.

<h2 class="pdoc-module-header" id="AdmChannelState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L83">interface AdmChannelState</a>
</h2>

Input properties used for looking up and filtering AdmChannel resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L87">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```


The application ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L91">property clientId</a>
</h3>

```typescript
clientId?: pulumi.Input<string>;
```


Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L95">property clientSecret</a>
</h3>

```typescript
clientSecret?: pulumi.Input<string>;
```


Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/admChannel.ts#L99">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether to enable the channel. Defaults to `true`.

<h2 class="pdoc-module-header" id="ApnsChannelArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L88">interface ApnsChannelArgs</a>
</h2>

The set of arguments for constructing a ApnsChannel resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L89">property applicationId</a>
</h3>

```typescript
applicationId: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L90">property bundleId</a>
</h3>

```typescript
bundleId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L91">property certificate</a>
</h3>

```typescript
certificate?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L92">property defaultAuthenticationMethod</a>
</h3>

```typescript
defaultAuthenticationMethod?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L93">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L94">property privateKey</a>
</h3>

```typescript
privateKey?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L95">property teamId</a>
</h3>

```typescript
teamId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L96">property tokenKey</a>
</h3>

```typescript
tokenKey?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L97">property tokenKeyId</a>
</h3>

```typescript
tokenKeyId?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="ApnsChannelState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L73">interface ApnsChannelState</a>
</h2>

Input properties used for looking up and filtering ApnsChannel resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L74">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L75">property bundleId</a>
</h3>

```typescript
bundleId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L76">property certificate</a>
</h3>

```typescript
certificate?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L77">property defaultAuthenticationMethod</a>
</h3>

```typescript
defaultAuthenticationMethod?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L78">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L79">property privateKey</a>
</h3>

```typescript
privateKey?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L80">property teamId</a>
</h3>

```typescript
teamId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L81">property tokenKey</a>
</h3>

```typescript
tokenKey?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/apnsChannel.ts#L82">property tokenKeyId</a>
</h3>

```typescript
tokenKeyId?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="AppArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L112">interface AppArgs</a>
</h2>

The set of arguments for constructing a App resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L116">property campaignHook</a>
</h3>

```typescript
campaignHook?: pulumi.Input<{ ... }>;
```


The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L120">property limits</a>
</h3>

```typescript
limits?: pulumi.Input<{ ... }>;
```


The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L124">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The application name. By default generated by Terraform

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L128">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The name of the Pinpoint application. Conflicts with `name`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L132">property quietTime</a>
</h3>

```typescript
quietTime?: pulumi.Input<{ ... }>;
```


The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own

<h2 class="pdoc-module-header" id="AppState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L82">interface AppState</a>
</h2>

Input properties used for looking up and filtering App resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L86">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```


The Application ID of the Pinpoint App.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L90">property campaignHook</a>
</h3>

```typescript
campaignHook?: pulumi.Input<{ ... }>;
```


The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L94">property limits</a>
</h3>

```typescript
limits?: pulumi.Input<{ ... }>;
```


The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The application name. By default generated by Terraform

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L102">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The name of the Pinpoint application. Conflicts with `name`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/app.ts#L106">property quietTime</a>
</h3>

```typescript
quietTime?: pulumi.Input<{ ... }>;
```


The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own

<h2 class="pdoc-module-header" id="BaiduChannelArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L105">interface BaiduChannelArgs</a>
</h2>

The set of arguments for constructing a BaiduChannel resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L109">property apiKey</a>
</h3>

```typescript
apiKey: pulumi.Input<string>;
```


Platform credential API key from Baidu.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L113">property applicationId</a>
</h3>

```typescript
applicationId: pulumi.Input<string>;
```


The application ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L117">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether to enable the channel. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L121">property secretKey</a>
</h3>

```typescript
secretKey: pulumi.Input<string>;
```


Platform credential Secret key from Baidu.

<h2 class="pdoc-module-header" id="BaiduChannelState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L83">interface BaiduChannelState</a>
</h2>

Input properties used for looking up and filtering BaiduChannel resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L87">property apiKey</a>
</h3>

```typescript
apiKey?: pulumi.Input<string>;
```


Platform credential API key from Baidu.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L91">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```


The application ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L95">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether to enable the channel. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/baiduChannel.ts#L99">property secretKey</a>
</h3>

```typescript
secretKey?: pulumi.Input<string>;
```


Platform credential Secret key from Baidu.

<h2 class="pdoc-module-header" id="EmailChannelArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L85">interface EmailChannelArgs</a>
</h2>

The set of arguments for constructing a EmailChannel resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L86">property applicationId</a>
</h3>

```typescript
applicationId: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L87">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L88">property fromAddress</a>
</h3>

```typescript
fromAddress: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L89">property identity</a>
</h3>

```typescript
identity: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L90">property roleArn</a>
</h3>

```typescript
roleArn: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="EmailChannelState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L73">interface EmailChannelState</a>
</h2>

Input properties used for looking up and filtering EmailChannel resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L74">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L75">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L76">property fromAddress</a>
</h3>

```typescript
fromAddress?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L77">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L78">property messagesPerSecond</a>
</h3>

```typescript
messagesPerSecond?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/emailChannel.ts#L79">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="EventStreamArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L70">interface EventStreamArgs</a>
</h2>

The set of arguments for constructing a EventStream resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L71">property applicationId</a>
</h3>

```typescript
applicationId: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L72">property destinationStreamArn</a>
</h3>

```typescript
destinationStreamArn: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L73">property roleArn</a>
</h3>

```typescript
roleArn: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="EventStreamState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L61">interface EventStreamState</a>
</h2>

Input properties used for looking up and filtering EventStream resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L62">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L63">property destinationStreamArn</a>
</h3>

```typescript
destinationStreamArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/eventStream.ts#L64">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="GcmChannelArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L67">interface GcmChannelArgs</a>
</h2>

The set of arguments for constructing a GcmChannel resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L68">property apiKey</a>
</h3>

```typescript
apiKey: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L69">property applicationId</a>
</h3>

```typescript
applicationId: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L70">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h2 class="pdoc-module-header" id="GcmChannelState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L58">interface GcmChannelState</a>
</h2>

Input properties used for looking up and filtering GcmChannel resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L59">property apiKey</a>
</h3>

```typescript
apiKey?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L60">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/gcmChannel.ts#L61">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h2 class="pdoc-module-header" id="SmsChannelArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L76">interface SmsChannelArgs</a>
</h2>

The set of arguments for constructing a SmsChannel resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L77">property applicationId</a>
</h3>

```typescript
applicationId: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L78">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L79">property senderId</a>
</h3>

```typescript
senderId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L80">property shortCode</a>
</h3>

```typescript
shortCode?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="SmsChannelState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L64">interface SmsChannelState</a>
</h2>

Input properties used for looking up and filtering SmsChannel resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L65">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L66">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L67">property promotionalMessagesPerSecond</a>
</h3>

```typescript
promotionalMessagesPerSecond?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L68">property senderId</a>
</h3>

```typescript
senderId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L69">property shortCode</a>
</h3>

```typescript
shortCode?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pinpoint/smsChannel.ts#L70">property transactionalMessagesPerSecond</a>
</h3>

```typescript
transactionalMessagesPerSecond?: pulumi.Input<number>;
```

