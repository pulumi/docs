---
title: Integration Testing
meta_desc: "Guide to integration testing of Pulumi programs with ephemeral environments."
weight: 3

menu:
  userguides:
    parent: testing
---

Integration testing focuses on black-box testing of Pulumi programs. An integration test runs the program in combination with the Pulumi CLI to deploy infrastructure to an ephemeral environment. It verifies the properties of the created resources and then destroys the infrastructure again.

By running a program through integration tests, you can ensure:

- Your project's code is syntactically well-formed and runs without errors.
- Your stack's configuration and secrets work and are interpreted correctly.
- Your project can be successfully deployed to your cloud provider of choice.
- Resources of the desired shape are successfully created.
- The infrastructure behaves as expected: for example, a health-check endpoint returns a valid HTML document, or a suite of application-level tests succeeds against the public API.
- Your project can be successfully updated from its starting state to other states.
- Your project can be successfully destroyed and removed from your cloud provider.

In principle, integration tests can be written in any general-purpose programming language. Tests do not interact with the program-under-test directly: instead, they shell out to the Pulumi CLI commands to create, update, and delete cloud infrastructure.

## Pulumi's Integration Test Framework

At Pulumi, we maintain an extensive suite of integration tests to validate the functionality of the core CLI and providers. Pulumi's integration test framework is written in Go.

This framework has been built to take a directory containing a full Pulumi program and drive various lifecycle operations against it: deploying a new stack from scratch, updating it with variations, and tearing it down afterwards, potentially multiple times. We run these tests for each pull request, regularly (such as nightly), and as stress tests.

While we don't currently provide first-party integration test frameworks for other languages, we encourage the community to do so. [Pitfall](https://github.com/bincyber/pitfall) is an example of a community-driven framework written in Python.

The rest of this guide shows you how to leverage the Pulumi integration test framework. You can use the Go test framework no matter the language your Pulumi program is written in.

### A Basic Integration Test

The following program is a simplified test of our example that provisions an [S3 bucket and objects in Pulumi](https://github.com/pulumi/examples/tree/master/aws-js-s3-folder):

**example_test.go:**

```go
package test

import (
    "os"
    "path"
    "testing"

    "github.com/pulumi/pulumi/pkg/v2/testing/integration"
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

This test runs through a basic lifecycle of stack creation, updating,
and destruction, for the `aws-js-s3-folder` example. It takes about a
minute or so to report success:

```
$ go test .
PASS
ok      ... 43.993s
```

There are many options to control the behavior of these tests. For a full set of options, see [the `ProgramTestOptions` data
structure](https://godoc.org/github.com/pulumi/pulumi/pkg/testing/integration#ProgramTestOptions). For instance, you can configure a Jaeger endpoint for tracing (`Tracing`), tell the harness to expect failure for negative testing (`ExpectFailure`), apply a series of "edits" to the program for a sequence of update state transitions (`EditDirs`), and more.

Let's see how to use the options to validate that the program deploys what we expect.

### Validating the Shape of Resources

The above integration test ensures that our program "works"&mdash;as in, it does not crash. But what if you want to validate the properties of the resulting stack? For example, that certain kinds of resources did (or did not) get provisioned, and that they have specific attributes.

The `ExtraRuntimeValidation` option for `ProgramTestOptions` allows you to look at the post-deployment state that Pulumi has captured, so that you can do extra validation on it. This includes a full snapshot of the resulting stack's state, including configuration, exported outputs, all resources and their property values, and all inter-resource dependencies.

To see a basic example of this, let's check that our program creates a single S3 Bucket:

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

Now when we run `go test`, it will not only run through the battery of lifecycle tests but will also, after successfully standing up the stack, perform the extra validation against the resulting state.

## Runtime Testing

The testing thus far has been about deployment behavior and the Pulumi resource model. You may also want to test that your provisioned infrastructure is actually working as expected. For example, that a VM is alive, an S3 bucket contains the files, and so on.

We can extend `ExtraRuntimeValidation` callback of `ProgramTestOptions` to perform such validation. When the callback triggers, it can run an arbitrary Go code with access to the full state of the program's resources. This state includes information such as VM IP addresses, URLs, and everything you need to interact with your resulting cloud applications and infrastructure to perform verification.

For instance, our test program exports the bucket's `websiteEndpoint` property as the stack output named `websiteUrl`, which is a full URL to fetch the bucket's index document:

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

Like our previous runtime validation checks, this will run in the harness right after the stack is stood up in response to a `go test` invocation.

## Ephemeral Environments

A very powerful capability is the ability to spin up ephemeral environments solely for purposes of acceptance testing. Pulumi's concept of [projects and stacks]({{< relref "/docs/intro/concepts/organizing-stacks-projects" >}}) is designed to make it easy to stand up entirely isolated and independent environments and to tear them down, including by using the integration testing framework.

If you are using GitHub, Pulumi offers a [GitHub App]({{< relref "/docs/guides/continuous-delivery/github-app" >}}) that helps to glue together your Pull Request workflow with this sort of acceptance testing run inside of your CI pipelines. Install the App into your GitHub repos, and Pulumi in your CI, and your Pull Requests will light up with infrastructure previews, updates, and test results:

![pr-comment](../pr-comment.png)

By leveraging Pulumi for your core acceptance test workflow, you'll
unlock new automation capabilities that improve your team's productivity and confidence in the quality of changes.

## Full Examples

A minimal example of using Pulumi's Go integration test framework is available in the examples repository: [Integration Testing in Go](https://github.com/pulumi/examples/tree/31056c3480cc445e5d4d3a8a0a86977adce2bc5e/testing-integration).

Our own [integration test suite](https://github.com/pulumi/examples/blob/31056c3480cc445e5d4d3a8a0a86977adce2bc5e/misc/test/examples_test.go) can be a source of further inspiration.
