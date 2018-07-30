### Converting JavaScript functions to an AWS Lambda.

Pulumi provides a core API for converting a JavaScript function into all the code and files necessary to then have that function run as an [AWS Lambda](https://aws.amazon.com/lambda/).  This includes producing both the primary index.js file defining the entry-point for the Lambda, as well as packaging up all the node_module directories necessary for the Lambda to execute properly at runtime.  The API that exposes this functionality can be found in @pulumi/aws-serverless and can be accessed directly like so:

```ts
import * as aws from "@pulumi/aws";
import * as serverless from "@pulumi/aws-serverless";

const lambda: aws.lambda.Function = serverless.function.createLambdaFunction("mylambda", 
    async (input: MyInputType) => {
        // your code here...
        return someOutput;
    });
```

This is a direct way to access the API, however there are many indirect ways this API is used.  Many other APIs will allow JavaScript functions to be passed that will be used to define the AWS Lambda that will end up responsible for the code at runtime.  For example:

```ts
import * as aws from "@pulumi/aws";
import * as serverless from "@pulumi/aws-serverless";

const bucket = new aws.s3.Bucket("mybucket", { serverSideEncryptionConfiguration: ... });

// Can provide a JS function here that will end up producing an AWS Lambda that will
// be triggered in the cloud whenever an aws.s3.Object is created inside our Bucket.
// This will create the lambda using the serverless.function.createLambdaFunction API.
serverless.s3.onObjectCreated("mytrigger", bucket, async (eventInfo) => {
   for (const record of eventInfo.Records) {
       // process each record we're notified about.
   }
});
```

This functionality provides a powerful and convenient way to create your AWS Lambdas, without needing to manually create the index.js file, package up all necessary node_modules directories, specify Roles or RolePolicyAttachments, upload s3 buckets, or do any of the normal work normally necessary.

### Determining the appropriate node_modules packages to include with an AWS Lambda

Because AWS Lambdas can now be defined using JavaScript functions, a Pulumi program now ends up defining two different regions of code.  Code that exists and will execute when the Pulumi itself runs (i.e. during a `pulumi preview` or `pulumi update` execution), and code that will be uploaded to the AWS cloud and will execute when the appropriate Lambda is invoked.  We call the former 'deployment time' code and the latter 'cloud runtime' code.  Because both of these exist within the same program, it is necessary for the program's `package.json` definition to specify all `dependencies` needed for both execution times.  In other words, `package.json`.  When `pulumi` then runs and produces an AWS Lambda from a user-provided function, it will transitively include all packages specified in the `dependencies` section of the application's `package.json` file.

Importantly:
1. It is optional to specify a reference to "aws-sdk" in your package.json.  AWS always includes this package with Lambdas, and so it is not necessary to explicitly include it yourself.
2. `pulumi` will not include `@pulumi` or any `@pulumi/...` packages with the Lambda.  These packages exist solely to provide 'deployment time' functionality, and do not contain any code that can work properly at 'cloud runtime'.  They are automatically stripped from a Lambda both to prevent accidently usage, as well as to help reduce the size of the uploaded Lambda.

### JavaScript function transformation

At a high-level, creating an AWS Lambda out of a JavaScript function involves several conceptual phases and transformation steps.  The first step is determining all the functions used by the function that is being converted.  For example, if the code was:

```ts
const lambda: aws.lambda.Function = serverless.function.createLambdaFunction("mylambda", 
    async (input: MyInputType) => {
        foo(input);
        bar(input);
    });

function foo(input: MyInputType) {
    quux(input)
}

function bar(input: MyInputType) {
}

function quux(input: MyInputType) {
}

function ztesch() {
}
```

The primary JavaScript function ends up calling both 'foo' and 'bar', so both these functions will be analyzed, transformed and included in the 'cloud runtime' code as well.  When 'foo' is transformed it will see that 'quux' is called, so that function will also be processed.  However, 'ztesch' is never called.  So it will not be included.  

### 'Capturing' values in a JavaScript function.

For most functions, the code of the function can simply be included practically 'as is' in the code file for the AWS lambda.  The important exception to this are functions that 'capture' values defined outside of the function itself.  For example:

```ts
const obj1 = { a: 1, b: 2 };
const obj2 = new aws.s3.Bucket("mybucket", { serverSideEncryptionConfiguration: /*...*/ });
const obj3 = SomeFunction();

const lambda: aws.lambda.Function = serverless.function.createLambdaFunction("mylambda", 
    async (input: MyInputType) => {
        foo(obj1);
        foo(obj2);
        foo(obj3);
    });

function foo(o) {
}
```

In this code, the JavaScript function ends up capturing both 'obj' and 'bucket' from outside the function. If the code `async (input: MyInputType) => { foo(obj); bar(bucket); }` was captured 'as-is' inside the AWS Lambda, then it would simply fail to work properly when triggered in the cloud because the values for 'obj' and 'bucket' would not exist.  In order to support this, `pulumi` will analyze these functions to determine what values are captured, and it will "serialize" them into a form that can then be retrieved and used at cloud-runtime for use by the actual Lambda.

The actual process of serialization is conceptually straightforward.  Because JavaScript itself allows unimpeded reflection over values, `pulumi` uses this to introspect the value and produce as close a replica as it can in the cloud-runtime code.  This includes capturing all properties of a value, the prototype-chain, functions, symbols, generators and even Promises.

Because of this, almost all JavaScript values can be serialized with very few exceptions.  Importantly, Pulumi Resources themselves are captured in this fashion, allowing cloud-runtime code to simply references the defined Resources of a Pulumi Application and to use them when a Lambda is triggered.  One notable limitation of this system is that native-functions are not capturable.

Importantly: 
1. Each time the AWS Lambda is triggered these values will be rehydrated.  This happens immediately before the code for the Lambda itself starts executing.
2. Any mutations made to those values will be seen across a single  invocation of that Lambda.  However, it will not be seen by subsequent invocations.  They will always start with the original value that was captured.  This behavior is similar to how a web-page works, where each client that visits the pages will get their own fresh copy of variables, and will not see mutations made by other clients on other machines.

### Size of captured values.

Pulumi will attempt to reduce the size of a serialized object by removing parts of it that it can prove are not used in a program.  For example:

```ts
const obj = { foo() { console.log("foo called"); } bar() { console.log("bar called") } };

const lambda: aws.lambda.Function = serverless.function.createLambdaFunction("mylambda", 
    async (input: MyInputType) => {
        obj.foo();
    });
```

In this code, only the 'foo' property is used from 'obj'.  So Pulumi will serialize a value equivalent to `{ foo() { console.log("foo called"); } }`.  However, if the code where:

```ts
const obj = { foo() { console.log("foo called"); this.bar(); } bar() { console.log("bar called") } };

const lambda: aws.lambda.Function = serverless.function.createLambdaFunction("mylambda", 
    async (input: MyInputType) => {
        obj.foo();
    });
```

Then this would need to serialize the entire object value (because 'bar' itself is used from 'foo').  This process happens conservatively. By default objects are serialized in their entirety, and they are only trimmed down when it can be proved that it is totally safe to do so.

### 'Capturing' modules in a JavaScript function.

While capturing of most JavaScript values works by reflecting over the value in order to produce a replica instance, the process works differently when dealing with a JavaScript module.  For example, consider the following code:

```ts
import * as fs from "fs";

const lambda: aws.lambda.Function = serverless.function.createLambdaFunction("mylambda", 
    async (input: MyInputType) => {
        await fs.writeFile("example.txt", "data");
    });
```

In this example the 'fs' module is needed inside the cloud-runtime code.  Because a module is just a normal JavaScript function, it would be possible to serialize this value just like any other object.  However, for several reasons this is not done.

1. It would generate an enormous amount of serialized code.  This code would then have quite an impact on the time necessary to execute the lambda each time.  
2. It would be redundant to have this code serialized out given that the equivalent code will exist in the node_modules directory for the Lambda.
3. It would fail on a native-code function.  These functions are relatively common in real-world modules, and would greatly limit the ability to use a module in practice.

Because of these reasons, Modules are captured in a special, but intuitive fashion.  When a module is captured in code, it is translated into a idiomatic `require` call in the serialized JavaScript code.  Using the above example, the code will then effectively contain:

```
var fs = require("fs");

// ...

await fs.writeFile("example.txt", "data")
```

This ensures that all modules can be referenced simply in application code, and then used simply in cloud-runtime code with expected semantics.

Importantly: this form of module capturing only applies to external modules that are referenced.  i.e. modules that are directly part of Node, or are in the node_modules directory.  The 'local' module (i.e. the module for the Pulumi Application) is not captured in this fashion.  That's because this code will not actually be part of the uploaded node_modules, and so would not be found.  The 'local' module is captured as if it was a normal 'value'.  This means, all its relevant variable and functions are serialized over in a uniform fashion to the Lambda, regardless of which actual file/module they are contained in.

### Pulumi execution order.

`pulumi` uses `node` to execute a pulumi-application.  During execution, when a call to `createLambdaFunction` is encountered, the function is converted to a Lambda at that point in execution.  That means that if the function captures any state, then the value that is captured will be whatever it was at the point in time.

For this reason, it is highly recommended that code not capture values which are also mutated in code.  It is much safer and easier to reason about immutable values that are captured in code.

For example consider the following two programs:

```ts
let obj = { a: 1, b: 2 };

const lambda: aws.lambda.Function = serverless.function.createLambdaFunction("mylambda", 
    async () => {
        console.log(obj);
    });

obj = { a: 3, b: 4 };
```


```ts
let obj = { a: 1, b: 2 };
obj = { a: 3, b: 4 };

const lambda: aws.lambda.Function = serverless.function.createLambdaFunction("mylambda", 
    async () => {
        console.log(obj);
    });
```

When `pulumi` starts executing `createLambdaFunction` it will analyze the JavaScript function code and will see that it uses the 'obj' value.  At that point in time it will use whatever the value is currently to serialize over.  So, in the first example, it will serialize the value `{ a: 1, b: 2 }`, even though right after executing createLambdaFunction the program code will update that value to `{ a: 3, b: 4}`.  In the second example, the code will see the `{ a: 3, b: 4 }` value and will serialize that into the cloud-runtime code.  

Importantly: there are subtleties here with Promise-like values.  When `pulumi` encounters a Promise value that it needs to serialize into the code for a Lambda, it will actually 'await' that Promise.  During that 'await', 'node' can then execute more of the program application code.  This means that later code may execute which then changes a value which is captured by the JavaScript function.  If `pulumi` then serialized that value after serializing the Promise, then it may see the mutated value.

So, in the following code:

```ts
let obj = { a: 1, b: 2 };
let pr = new Promise((resolve, reject) => { /*...*/ });

const lambda: aws.lambda.Function = serverless.function.createLambdaFunction("mylambda", 
    async () => {
        console.log(pr);
        console.log(obj);
    });

obj = { a: 3, b: 4 };
```

it may be the case that the value `{ a: 1, b: 2}` or `{ a: 3, b: 4}` is serialized depending on the order that things are serialized in.
