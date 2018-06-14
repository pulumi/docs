---
title: Module serverless
---

<a href="../index.html">@pulumi/aws</a> &gt; serverless

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Function">class Function</a>
* <a href="#lambdaRolePolicy">const lambdaRolePolicy</a>
* <a href="#addPackageAndDependenciesToSet">function addPackageAndDependenciesToSet</a>
* <a href="#allFoldersForPackages">function allFoldersForPackages</a>
* <a href="#computeCodePaths">function computeCodePaths</a>
* <a href="#findDependency">function findDependency</a>
* <a href="#removeBuiltins">function removeBuiltins</a>
* <a href="#sha1hash">function sha1hash</a>
* <a href="#Context">interface Context</a>
* <a href="#FunctionOptions">interface FunctionOptions</a>
* <a href="#Package">interface Package</a>
* <a href="#Handler">type Handler</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts">serverless/function.ts</a> 


<h2 class="pdoc-module-header" id="Function">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L101">class Function</a>
</h2>

Function is a higher-level API for creating and managing AWS Lambda Function resources implemented
by a Lumi lambda expression and with a set of attached policies.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L104">constructor</a>
</h3>

```typescript
new Function(name: string, options: FunctionOptions, func: Handler, opts?: pulumi.ResourceOptions, serialize?: { ... })
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L100">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L103">property lambda</a>
</h3>

```typescript
public lambda: lambda.Function;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L102">property options</a>
</h3>

```typescript
public options: FunctionOptions;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L104">property role</a>
</h3>

```typescript
public role: Role;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="lambdaRolePolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L223">const lambdaRolePolicy</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L225">let Statement</a>
</h3>

```typescript
let Statement: { ... }[] =  [
        {
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "lambda.amazonaws.com",
            },
            "Effect": "Allow",
            "Sid": "",
        },
    ];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L224">let Version</a>
</h3>

```typescript
let Version: string = "2012-10-17";
```

<h2 class="pdoc-module-header" id="addPackageAndDependenciesToSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L294">function addPackageAndDependenciesToSet</a>
</h2>

```typescript
addPackageAndDependenciesToSet(s: Set<string>, root: Package, pkg: string): void
```

<h2 class="pdoc-module-header" id="allFoldersForPackages">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L257">function allFoldersForPackages</a>
</h2>

```typescript
allFoldersForPackages(path: string, packages: string[]): Promise<Set<string>>
```

<h2 class="pdoc-module-header" id="computeCodePaths">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L174">function computeCodePaths</a>
</h2>

```typescript
computeCodePaths(closure: Promise<pulumi.runtime.SerializedFunction>, serializedFileName: string, extraIncludePaths?: string[], extraPackages?: string[]): Promise<pulumi.asset.AssetMap>
```

<h2 class="pdoc-module-header" id="findDependency">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L311">function findDependency</a>
</h2>

```typescript
findDependency(root: Package, name: string): Package
```

<h2 class="pdoc-module-header" id="removeBuiltins">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L333">function removeBuiltins</a>
</h2>

```typescript
removeBuiltins(packages: Set<string>): Set<string>
```

<h2 class="pdoc-module-header" id="sha1hash">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L238">function sha1hash</a>
</h2>

```typescript
sha1hash(s: string): string
```

<h2 class="pdoc-module-header" id="Context">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L32">interface Context</a>
</h2>

Context is the shape of the context object passed to a Function callback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L43">method getRemainingTimeInMillis</a>
</h3>

```typescript
getRemainingTimeInMillis(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L38">property awsRequestId</a>
</h3>

```typescript
awsRequestId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L33">property callbackWaitsForEmptyEventLoop</a>
</h3>

```typescript
callbackWaitsForEmptyEventLoop: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L42">property clientContext</a>
</h3>

```typescript
clientContext: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L34">property functionName</a>
</h3>

```typescript
functionName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L35">property functionVersion</a>
</h3>

```typescript
functionVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L41">property identity</a>
</h3>

```typescript
identity: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L36">property invokedFunctionArn</a>
</h3>

```typescript
invokedFunctionArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L39">property logGroupName</a>
</h3>

```typescript
logGroupName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L40">property logStreamName</a>
</h3>

```typescript
logStreamName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L37">property memoryLimitInMB</a>
</h3>

```typescript
memoryLimitInMB: string;
```

<h2 class="pdoc-module-header" id="FunctionOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L54">interface FunctionOptions</a>
</h2>

FunctionOptions provides configuration options for the serverless Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L78">property deadLetterConfig</a>
</h3>

```typescript
deadLetterConfig?: { ... };
```


A dead letter target ARN to send function invocation failures to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L94">property includePackages</a>
</h3>

```typescript
includePackages?: string[];
```


The packages relative to the program folder to include in the Lambda upload.  The version of the package
installed in the program folder and it's dependencies will all be included. Default is `[]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L89">property includePaths</a>
</h3>

```typescript
includePaths?: string[];
```


The paths relative to the program folder to include in the Lambda upload.  Default is `[]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L70">property memorySize</a>
</h3>

```typescript
memorySize?: number;
```


The memory size limit to use for execution of the Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L58">property policies</a>
</h3>

```typescript
policies?: ARN[];
```


A list of IAM policy ARNs to attach to the Function.  Must provide either [policies] or [role].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L62">property role</a>
</h3>

```typescript
role?: Role;
```


A pre-created role to use for the Function.  Must provide either [policies] or [role].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L74">property runtime</a>
</h3>

```typescript
runtime?: lambda.Runtime;
```


The Lambda runtime to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L66">property timeout</a>
</h3>

```typescript
timeout?: number;
```


A timout, in seconds, to apply to the Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L82">property vpcConfig</a>
</h3>

```typescript
vpcConfig?: { ... };
```


Configuration for a VPC to run the Function within.

<h2 class="pdoc-module-header" id="Package">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L245">interface Package</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L252">property children</a>
</h3>

```typescript
children: Package[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L246">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L248">property package</a>
</h3>

```typescript
package: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L251">property parent</a>
</h3>

```typescript
parent?: Package;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L247">property path</a>
</h3>

```typescript
path: string;
```

<h2 class="pdoc-module-header" id="Handler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L49">type Handler</a>
</h2>

```typescript
type Handler = { ... };
```


Handler is the signature for a serverless function.

