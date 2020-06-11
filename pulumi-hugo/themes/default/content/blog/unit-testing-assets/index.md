---
title: "Unit Testing Assets"
date: 2020-06-10T11:08:26-07:00
draft: false
meta_desc: "Learn how unit testing your infrastructure assets can help ensure correctness of your deployments."
meta_image: meta.png
authors:
    - lee-zen
tags:
    - Testing
    - Infrastructure
---

When deploying infrastructure, we want to ensure that what we're deploying matches our expectations.
One way to do so is via [unit testing]({{< relref "/docs/guides/testing/unit" >}}).
We've talked about this concept in previous posts such as [in this overview]({{< relref "/blog/unit-test-infrastructure" >}})
and [in this post on deployments with .NET]({{< relref "/blog/unit-testing-cloud-deployments-with-dotnet" >}}).

Often, when we're creating cloud resources, we want to ensure that a resource's underlying assets match certain properties.
For example, the entrypoint or handler for a cloud function should be an executable function.
Similarly, objects we'll serve as static assets on a website should not exceed a certain size.
We can use Pulumi's unit testing framework along with language-specific constructs such as introspection or filesystem calls
to ensure this type of correctness. We'll walk through some examples to show just how easy it is to do so.

<!--more-->

The examples below are in Python, but you can easily achieve the same types of tests using introspection/reflection in Node, .NET, and Go.

## Check that Functions are Executable

When creating a Lambda function, we're expected to pass in a function handler that gets called upon invocation.
Typically, the value is something like `mod.handler` where `mod` is the module name and `handler` is a function.
A basic check would be to make sure that the module actually exists and that the function is callable.

We can easily construct this unit test like so:

**test_infra.py**:

```python
import unittest
import pulumi

class MyMocks(pulumi.runtime.Mocks):
    def new_resource(self, type_, name, inputs, provider, id_):
        return [name + '_id', inputs]
    def call(self, token, args, provider):
        return {}

pulumi.runtime.set_mocks(MyMocks())

import infra

class TestInfrastructure(unittest.TestCase):

    # Test that the function entrypoint is actually an executable function.
    @pulumi.runtime.test
    def test_function_handler_callable(self):
        def check_entrypoint(handler):
            import importlib
            from types import ModuleType
            from inspect import signature, Parameter

            # The handler should be of the form <module_name>.<function>
            module_name, function_handler = handler.split('.', 1)

            # Check that we can load the module.
            module = importlib.import_module(module_name)
            self.assertIsInstance(module, ModuleType)

            # Check that the function handler is actually callable.
            fn = getattr(module, function_handler)
            self.assertTrue(callable(fn))

            # Check that it has two parameters: event and context
            sig = signature(fn)
            self.assertListEqual(['event', 'context'], list(sig.parameters.keys()))

        return infra.lambda_function.handler.apply(check_entrypoint)
```

Here, we use Python's introspection capabilities to import a module based on a string that we obtain from the Lambda function definition.
Similarly, after we import the module, we can verify that the function is callable and has the appropriate arguments for a Lambda function.
At this point, we've verified that we've correctly "wired in" a function handler.
Separately, we would expect another set of unit tests that verifies the correctness of the handler itself.

Here's the corresponding infrastructure code to make the test pass,
assuming there's also a file called `lambda_function.py` which contains a function `handler(event, context)`.:

**infra.py**:

```python
import pulumi
import pulumi_aws as aws

lambda_role = aws.iam.Role('example-role', assume_role_policy=f"""{{
    "Version":"2012-10-17",
    "Statement":[{{
        "Effect": "Allow",
        "Principal":{{
                        "Service": "lambda.amazonaws.com"
                    }},
        "Action": "sts:AssumeRole"
    }}]
}}
""")

attach_lambda_role_execution = aws.iam.RolePolicyAttachment('example-attach-execute',
    policy_arn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole',
    role=lambda_role.name)

module_name = 'lambda_function'
module_file = f'{module_name}.py'
lambda_function = aws.lambda_.Function('example-function',
    handler=f'{module_name}.handler',
    role=lambda_role.arn,
    runtime='python3.7',
    code=pulumi.AssetArchive({
        module_file: pulumi.FileAsset(module_file)
    })
)
```

If for whatever reason `lambda_function.py` doesn't exist or there's no function `handler` within that module, the test will fail.

## File Assets

Another example of checking for underlying asset correctness is when providing files to a resource.
For example, we might want to check that the content type we provide to an object actually matches that of the resource:

**test_infra.py**:

```python
# Test that the bucket object matches the correct mimetype
@pulumi.runtime.test
def test_bucket_object_content_type(self):
    def check_filetype(args):
        source, mimetype = args
        import filetype
        kind = filetype.guess(source.path)
        self.assertEqual(kind.mime, mimetype)

    return pulumi.Output.all(infra.bucket_obj.source, infra.bucket_obj.content_type).apply(check_filetype)
```

Here, we use the `filetype` module to guess at the type based on reading the file itself.
We then check that the mime type specified on the bucket object actually matches.

For example, if the file represented by `image.png` isn't actually a PNG, then this test would fail:

**infra.py**:

```python
bucket = aws.s3.Bucket('my-bucket')

bucket_obj = aws.s3.BucketObject('my-bucket-obj',
    bucket=bucket,
    content_type='image/png',
    source=pulumi.FileAsset('image.png'))
```

## Secrets

When working with secrets, we want to ensure that provided values are secret and that corresponding outputs are secret.
This helps ensure that our state never contains plaintext values that are meant to be secret. We can write a simple test
to check this:

**test_infra.py**:

```python
# Test that the secret input is marked as secret
@pulumi.runtime.test
def test_secret_input_and_output(self):
    self.assertTrue(infra.secret_password_v1.secret_string.is_secret().result())
```

If we try to write something like the following in our code, it'll fail this test:

**infra.py**:

```python
secret_password = aws.secretsmanager.Secret('example-secret')
secret_password_v1 = aws.secretsmanager.SecretVersion('example-secret-version',
    secret_id=secret_password,
    secret_string='example-string')
```

If we change `secret_string='example-string'` to `secret_string=pulumi.Output.secret('example-string')`
our test will pass.

## Conclusion

There are many other examples of resources where it's useful to check the underlying properties of the input assets.
For example, checking the validity of certificates, keys, files, and container images are all assets
that benefit from making sure we're wiring in resources correctly to our cloud infrastructure.
We hope you take this opportunity to use Pulumi's unit testing framework to check your infrastructure's underlying assets for correctness.
