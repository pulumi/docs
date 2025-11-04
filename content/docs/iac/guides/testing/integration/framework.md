---
title_tag: "Pulumi Integration Testing Framework"
meta_desc: "Learn how to use Pulumi's Go-based integration testing framework to validate infrastructure deployments."
title: Integration testing framework
h1: Pulumi Integration Testing Framework
meta_image: /images/docs/meta-images/docs-meta.png
weight: 1
menu:
    iac:
        name: Integration testing framework
        parent: iac-guides-testing-integration
        weight: 1
---

Pulumi maintains an integration test framework written in Go which Pulumi uses internally to validate the functionality of the core CLI and providers. This framework takes a directory containing a full Pulumi program and drives various lifecycle operations against it: deploying a new stack from scratch, updating it with variations, and tearing it down afterwards.

You can use the Go test framework no matter what language your Pulumi program is written in.

## A basic integration test

The following program is a simplified test of an example that provisions an S3 bucket and objects in Pulumi:

```go
package test

import (
    "os"
    "path"
    "testing"

    "github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func TestExamples(t *testing.T) {
    awsRegion := os.Getenv("AWS_REGION")
    if awsRegion == "" {
        awsRegion = "us-west-1"
    }
    cwd, _ := os.Getwd()
    integration.ProgramTest(t, &integration.ProgramTestOptions{
        Quick:       true,
        SkipRefresh: true,
        Dir:         path.Join(cwd, "..", "..", "aws-js-s3-folder"),
        Config: map[string]string{
            "aws:region": awsRegion,
        },
    })
}
```

This test runs through a basic lifecycle of stack creation, updating, and destruction. It takes about a minute or so to report success:

```bash
$ go test .
PASS
ok      ... 43.993s
```

## Configuration options

There are many options to control the behavior of these tests. For a full set of options, see the [`ProgramTestOptions` data structure](https://pkg.go.dev/github.com/pulumi/pulumi/pkg/v3/testing/integration#ProgramTestOptions). For instance, you can:

- Configure a Jaeger endpoint for tracing (`Tracing`)
- Tell the harness to expect failure for negative testing (`ExpectFailure`)
- Apply a series of "edits" to the program for a sequence of update state transitions (`EditDirs`)

## Performing additional validation

The above integration test ensures that a program "works"—as in, it does not crash. To validate the properties of the resulting stack, you can use the `ExtraRuntimeValidation` option.

The `ExtraRuntimeValidation` option allows you to look at the post-deployment state that Pulumi has captured. This includes a full snapshot of the resulting stack's state, including configuration, exported outputs, all resources and their property values, and all inter-resource dependencies.

### Validating resource properties

Here's an example that checks that a program creates a single S3 bucket:

```go
integration.ProgramTest(t, &integration.ProgramTestOptions{
    // as before...
    ExtraRuntimeValidation: func(t *testing.T, stack integration.RuntimeValidationStackInfo) {
        var foundBuckets int
        for _, res := range stack.Deployment.Resources {
            if res.Type == "aws:s3/bucket:Bucket" {
                foundBuckets++
            }
        }
        assert.Equal(t, 1, foundBuckets, "Expected to find a single AWS S3 Bucket")
    },
})
```

When you run `go test`, it will run through the battery of lifecycle tests and perform the extra validation against the resulting state.

### Validating stack outputs

You may also want to test that your provisioned infrastructure is actually working as expected. For example, that a VM is alive, an S3 bucket contains files, and so on.

You can extend the `ExtraRuntimeValidation` callback to perform such validation. When the callback triggers, it can run arbitrary Go code with access to the full state of the program's resources. This state includes information such as VM IP addresses, URLs, and everything you need to interact with your resulting cloud applications and infrastructure.

For instance, a test program might export a bucket's `websiteEndpoint` property as a stack output named `websiteUrl`. You can fetch and validate this endpoint:

```go
integration.ProgramTest(t, &integration.ProgramTestOptions{
    // as before ...
    ExtraRuntimeValidation: func(t *testing.T, stack integration.RuntimeValidationStackInfo) {
        url := "http://" + stack.Outputs["websiteUrl"].(string)
        resp, err := http.Get(url)
        if !assert.NoError(t, err) {
            return
        }
        if !assert.Equal(t, 200, resp.StatusCode) {
            return
        }
        defer resp.Body.Close()
        body, err := ioutil.ReadAll(resp.Body)
        if !assert.NoError(t, err) {
            return
        }
        assert.Contains(t, string(body), "Hello, Pulumi!")
    },
})
```

This validation runs in the harness right after the stack is stood up in response to a `go test` invocation.

## Additional resources

- [Integration Testing in Go example](https://github.com/pulumi/examples/tree/master/testing-integration) - A minimal example using Pulumi's Go integration test framework
- [Pulumi AWS provider tests](https://github.com/pulumi/pulumi-aws/tree/master/examples) - Comprehensive examples of integration tests in the AWS provider
- [Pulumi examples test suite](https://github.com/pulumi/examples/blob/master/misc/test/examples_test.go) - Additional examples and patterns
