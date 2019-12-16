---
title: Serializing JavaScript Functions
meta_desc: Use Pulumi's Node.js SDK to serialize JavaScript functions into an artifact that can be used at runtime in the cloud.
keywords:
- javascript
- aws lambda
- function serialization
- pulumi sdk

aliases: ["/docs/reference/serializing-functions/"]
---

The Pulumi [Node.js SDK](https://github.com/pulumi/pulumi/tree/master/sdk/nodejs) provides a core API for converting a JavaScript function into all the code and files necessary to have that function be used at runtime within some cloud, like in an [AWS Lambda](https://aws.amazon.com/lambda/) for example.

There are many cases where a small piece of runtime functionality must be defined as part of a cloud application, and it makes sense to define that runtime functionality directly inline as part of the Pulumi program. This can augment, or even replace, using runtime code and binaries defined outside of Pulumi in Lambda ZIPs, Docker images, VM images, etc.

Pulumi makes this easy by allowing JavaScript callbacks written in a Pulumi program to be serialized down into an artifact that can be used at runtime. This function serialization feature moves code between stages of your application lifecycle &mdash; from _deployment time_ to _run time_. _Deployment time_ code runs during a `pulumi preview` or `pulumi up`, while _run time_ code runs when the corresponding cloud artifact is triggered. It is thus important to understand how this is done, and some of the restrictions placed on code in a Pulumi program that is intended to be invoked at _run time_.

For the purposes of this walkthrough and the examples, we will be using AWS Lambda. This information equally applies to all cloud providers, however. Additionally, we will use TypeScript to help provide type annotation for clarity &mdash; although it is not required &mdash; since all functionality is exposed entirely to JavaScript. The API that exposes this functionality for AWS can be found in `@pulumi/aws` and can be accessed directly like so:

```typescript
import * as aws from "@pulumi/aws";

const lambda = new aws.lambda.CallbackFunction("mylambda", {
  callback: async e => {
    // your code here ...
    return someOutput;
  }
});
```

There are also many indirect ways this API is used. Many Pulumi SDK APIs allow JavaScript functions to be passed that will be used to define the Lambda that will end up responsible for the code at _run time_. These APIs normally provide a strongly-typed definition that helps TypeScript users ensure their JavaScript functions are properly typed and will execute properly at _run time_. For example:

```typescript
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("mybucket", { serverSideEncryptionConfiguration: ... });

// Can provide a JS function here that will end up producing an Lambda that will
// be triggered in the cloud whenever an aws.s3.Object is created inside our Bucket.
// This will create the lambda using the aws.lambda.CallbackFunction API.
bucket.onObjectCreated("mytrigger", async (eventInfo) => {
   for (const record of eventInfo.Records) {
       // process each record we're notified about.
   }
});
```

This functionality provides a powerful and convenient way to create your Lambdas, without needing to manually create the `index.js` file, package up all necessary `node_modules` directories, specify Roles or RolePolicyAttachments, upload S3 buckets, or do any of the traditionally necessary work.

## JavaScript Function Transformation

At a high level, creating a Lambda out of a JavaScript function involves several conceptual phases and transformation steps. The first step is determining all the functions used by the function that is being converted. For example, if the code were:

```typescript
const lambda = new aws.lambda.CallbackFunction("mylambda", {
  callback: async e => {
    foo(input);
    bar(input);
  }
});

function foo(input: MyInputType) {
  quux(input);
}

function bar(input: MyInputType) {}

function quux(input: MyInputType) {}

function ztesch() {}
```

The primary JavaScript function ends up calling both `foo` and `bar`, so both these functions will be analyzed, transformed and included in the _run time_ code as well. When `foo` is transformed it will see that `quux` is called, so that function will also be processed. However, `ztesch` is never called and will therefore not be included.

All functions that are needed for _run time_ execution will then be included in the uploaded code for the Lambda. Generally speaking, this code is almost always included as originally written, ensuring that the serialized code behaves as close as possible to the original code definition. It is a primary goal of Pulumi to have the semantics of the _run time_ code match the semantics of the original program's code.

### Capturing values in a JavaScript function

For most functions, the code of the function can simply be included practically as is in the code file for the Lambda. The important exception to this are functions that ***capture*** values defined outside of the function itself. For example:

```typescript
const obj1 = { a: 1, b: 2 };
const obj2 = new aws.s3.Bucket("mybucket", { serverSideEncryptionConfiguration: /*...*/ });
const obj3 = SomeFunction();

const lambda = new aws.lambda.CallbackFunction("mylambda", {
    callback: async e => {
        foo(obj1);
        foo(obj2);
        foo(obj3);
    }
});

function foo(o) {
}
```

In this code, the JavaScript function ends up capturing `obj1`, `obj2`, and `obj3` from outside the function. If the code `async e => { foo(obj1); /*...*/ }` were captured as is inside the Lambda, then it would simply fail to work properly when triggered in the cloud because the values for `obj1` and the rest would not exist. In order to support this, `pulumi` will analyze these functions to determine what values are captured, and it will _serialize_ them into a form that can then be retrieved and used at _run time_ for use by the actual Lambda.

The actual process of serialization is conceptually straightforward. Because JavaScript itself allows unimpeded reflection over values, `pulumi` uses this to serialize the entire object graph for the referenced JavaScript value, including the prototype chain, properties, and methods on the object and any values those transitively reference.

Because of this, almost all JavaScript values can be serialized with very few exceptions. Importantly, Pulumi resources themselves are captured in this fashion, allowing _run time_ code to simply reference the defined resources of a Pulumi application and to use them when a Lambda is triggered.

> ### Notes
>
> * Native functions are not capturable. This impacts capturing any value that is either itself a native function or which _transitively_ references a native from being capturable.
> * Each time the cloud Lambda is triggered, these values will be rehydrated. This happens immediately before the code for the Lambda itself starts executing.
> * Any mutations made to those values will be seen across a single invocation of that Lambda. However, it will not be seen by subsequent invocations. They will always start with the original value that was captured. This behavior is similar to how a web page works, where each client visiting the pages gets its own fresh copy of variables, and will not see mutations made by other clients on other machines.

#### Size of captured values

Pulumi will attempt to reduce the size of a serialized object by removing parts of it that it can prove are not used in a program. For example:

```typescript
const obj = { foo() { console.log("foo called"); } bar() { console.log("bar called") } };

const lambda = new aws.lambda.CallbackFunction("mylambda", {
    callback: async e => {
        obj.foo();
    }
});
```

In this code, only the `foo` property is used from `obj`. So Pulumi will serialize a value equivalent to `{ foo() { console.log("foo called"); } }`. However, if the code were:

```typescript
const obj = { foo() { console.log("foo called"); this.bar(); } bar() { console.log("bar called") } };

const lambda = new aws.lambda.CallbackFunction("mylambda", {
    callback: async e => {
        obj.foo();
    }
});
```

Then Pulumi would need to serialize the entire object value, since `bar` itself is used from `foo`. This process happens conservatively. By default objects are serialized in their entirety, and they are only trimmed down when it can be proven that it is totally safe to do so.

### Capturing modules in a JavaScript function

Capturing of most JavaScript values normally works by serializing the entire object graph to produce a representation which can then be rehydated into a replica instance. However, this process works differently when the value being dealt with is a JavaScript module. For example, consider the following code:

```typescript
import * as fs from "fs";

const lambda = new aws.lambda.CallbackFunction("mylambda", {
  callback: async e => {
    await fs.writeFile("example.txt", "data");
  }
});
```

In this example, the `fs` module is needed inside the _run time_ code. Because a module is just a normal JavaScript value, it is possible to serialize it just like any other value. This is not done for several reasons:

1. It would generate an enormous amount of serialized code which would have quite an impact on the time necessary to execute the Lambda each time it was invoked.
2. It would be redundant to have this code serialized out given that the equivalent code will exist in the `node_modules` directory for the Lambda.
3. It would fail on a native code function. These functions are relatively common in real world modules, and would greatly limit the ability to use a module in practice.

For the reasons cited previously, modules are captured in a special but intuitive fashion. When a module is captured in code, it is translated into an idiomatic `require` call in the serialized JavaScript code. Using the above example, the code will then effectively contain:

```javascript
var fs = require("fs");

// ...

await fs.writeFile("example.txt", "data");
```

This ensures that all modules can be referenced simply in application code, and then used simply in _run time_ code with expected semantics.

> **Note:** This form of module capturing only applies to external modules that are referenced: modules that are directly part of Node, or are in the `node_modules` directory. The `local` module &mdash; the module for the Pulumi application itself &mdash; is not captured in this fashion. That is because this code will not actually be part of the uploaded `node_modules`, and so would not be found. The `local` module is captured as if it was a normal value. This means that all its relevant variable and functions are serialized over in a uniform fashion to the Lambda, regardless of which actual file or module they are contained in.

## Pulumi Execution Order

`pulumi` uses `node` to execute a Pulumi application. During execution, when a call to `new aws.lambda.CallbackFunction` is encountered, the function is converted to a Lambda at that point in execution. This means that if the function captures any state, then the value that is captured will be whatever it was at the point in time.

For this reason, it is highly recommended that code not capture values which are also mutated in code. It is much safer and easier to reason about immutable values that are captured in code. To see the problems this avoids in practice, consider the following two programs:

```typescript
let obj = { a: 1, b: 2 };

const lambda = new aws.lambda.CallbackFunction("mylambda", {
  callback: async () => {
    console.log(obj);
  }
});

obj = { a: 3, b: 4 };
```

```typescript
let obj = { a: 1, b: 2 };
obj = { a: 3, b: 4 };

const lambda = new aws.lambda.CallbackFunction("mylambda", {
  callback: async () => {
    console.log(obj);
  }
});
```

When `pulumi` starts executing `new aws.lambda.CallbackFunction`, it will analyze the JavaScript function code and will see that it uses the `obj` value. At that point in time, it will use whatever the current value is to serialize over. So, in the first example, it will serialize the value `{ a: 1, b: 2 }`, even though right after executing `new aws.lambda.CallbackFunction` the program code will update that value to `{ a: 3, b: 4}`. In the second example, the code will see the `{ a: 3, b: 4 }` value and will serialize that into the _run time_ code.

> **Note:** There are subtleties here with Promise-like values. When `pulumi` encounters a Promise value that it needs to serialize into the code for a Lambda, it will actually `await` that Promise. During that `await`, `node` can then execute more of the program application code. This means that later code may execute which then changes a value which is captured by the JavaScript function. If `pulumi` then serialized that value after serializing the Promise, then it may see the mutated value.

So, in the following code:

```typescript
let obj = { a: 1, b: 2 };
let pr = new Promise((resolve, reject) => {
  /*...*/
});

const lambda = new aws.lambda.CallbackFunction("mylambda", {
  callback: () => {
    console.log(pr);
    console.log(obj);
  }
});

obj = { a: 3, b: 4 };
```

It may be the case that the value `{ a: 1, b: 2}` or `{ a: 3, b: 4}` is serialized depending on the order that things are serialized in. As previously mentioned, it is highly recommended to not mutate values that are captured _especially_ in the presence of asynchronously executing code.

## Customizing the cloud Lambda produced from a JavaScript function

By default, Pulumi will generate a cloud Lambda for a given JavaScript function with reasonable defaults for many configurable properties. For example, values are picked to define the default roles and permissions for the Lambda, the timeout it should have, how much memory it can use, which version of the Node runtime to use, and so on and so forth. If these defaults are not desirable, any or all of them can be overridden by supplying desired values. For example:

```typescript
const lambda = new aws.lambda.CallbackFunction("mylambda", {
  callback: async e => {
    // your code here ...
    return someOutput;
  },
  // Only let this Lambda run for a minute before forcefully terminating it.
  timeout: 60
});
```

When calling APIs that allow callbacks to be passed in, you can provide customizations like so:

```typescript
bucket.onObjectCreated(
  "mytrigger",
  new aws.lambda.CallbackFunction("mylambda", {
    callback: async eventInfo => {
      for (const record of eventInfo.Records) {
        // process each record we're notified about.
      }
    },
    // Only let this Lambda run for a minute before forcefully terminating it.
    timeout: 60
  })
);
```

In other words, the Lambda will first be created with appropriate values overridden. Then that Lambda itself can be passed in as the code to run for the specific API.

## Determining the appropriate node_modules packages to include with a Lambda

Because a Pulumi application contains both _deployment time_ code and _run time_ code, it is necessary for the program's `package.json` definition to have a `dependencies` section which specifies all necessary packages needed for both execution times. When `pulumi` produces a Lambda from a user-provided function, it will transitively include all packages specified in that `dependencies` section in the final uploaded Lambda.

Note that `pulumi` will not include `@pulumi/...` packages with the Lambda. These packages exist solely to provide _deployment time_ functionality, and do not contain any code that can work properly at _run time_. They are automatically stripped from a Lambda both to prevent accidental usage and to help reduce the size of the uploaded Lambda.

> **Referencing `aws-sdk`**
>
> It is optional to specify a reference to "aws-sdk" in your `package.json`. AWS always includes this package with Lambdas, so it is not necessary to explicitly include it yourself.
