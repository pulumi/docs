---
title: "Building Pulumi HCL: Pair Programming With an Oracle"
date: 2026-07-30
draft: false
meta_desc: "How we built Pulumi HCL by testing against OpenTofu itself as an oracle, using an existing implementation to define correct behavior."
feature_image: feature.png
authors:
    - ian-wahbe
tags:
    - hcl
    - terraform
category: engineering
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Pulumi's HCL support requires that it is both a valid Pulumi language, and OpenTofu compatible.

        We've written up how we make sure it's both, and what properties we need to let LLMs hunt bugs unsupervised.
    linkedin: |
        Pulumi HCL (now in preview) has to satisfy two masters. A Terraform module used from Pulumi must behave exactly as it does under OpenTofu, and HCL must be a first-class Pulumi language alongside the other six.

        Those two goals get two very different test suites with very different properties. Our conformance tests are a hand-curated test suite built up over years of effort and shared across every Pulumi language. OpenTofu compatibility testing relies on our guarantee that for any valid program, tofu apply and pulumi up should do the same thing.

        That second property turns out to matter for AI. When tests are correct by construction, you can turn LLMs loose on finding failing tests without filtering false positives.

        Here's how both suites work & why the distinction matters.
    bluesky: |
        Pulumi's HCL support has to be two things at once: a valid Pulumi language, and OpenTofu compatible. Each half gets its own test suite, with very different properties.

        We've written up how both work, and which one lets us turn LLMs loose on bug hunting.
---

Typing out code has never been the hard part of programming, any more than my penmanship is what's stopping me from writing the next great American novel. The hard part is making sure what you wrote is correct. This is especially true for a project like adding HCL support to Pulumi (in preview now, try it at [pulumi-labs/pulumi-hcl](https://github.com/pulumi-labs/pulumi-hcl)). Users already know exactly what they want their [Terraform modules](https://developer.hashicorp.com/terraform/language/modules) to do, and when they start using those modules in their Pulumi programs the semantics are clear. Terraform modules consumed from Pulumi should do exactly the same thing as Terraform modules consumed from Terraform. At the same time, if Pulumi supports HCL then HCL needs to be fully incorporated into the Pulumi ecosystem, and we need to ensure we can correctly express [Pulumi concepts](https://www.pulumi.com/docs/iac/concepts/) in HCL. The way we do both is exhaustive testing, but the test strategy for *ensuring Pulumi HCL is OpenTofu compatible* is different from the one for *ensuring HCL is Pulumi native*, and I want to talk through each. Since this is a blog post in 2026, this will touch on AI. You have been warned.

<!--more-->

The key question with putting together any test suite over a complex program is where to source the test corpus from. Writing tests, much like writing code, is easy. Assembling an effective test corpus is much harder. I'd argue that a good test corpus has three properties: it's comprehensive, targeted, and correct:

### Comprehensive

Comprehensive means that your corpus covers your desired properties. When you change something by accident, a test will fail. If you have ever written a postmortem that ended with "not enough test coverage", this was your problem.

### Targeted

Targeted means that each test scenario is pointing towards a specific feature. A clear mapping between test cases and what broke is what allows you to see a broken test case and narrow that down to a bug. Consider this counterexample: building the [Linux kernel is a very broad test of a C compiler](https://www.anthropic.com/engineering/building-c-compiler), but if [it fails](https://github.com/anthropics/claudes-c-compiler/issues/1), that doesn't tell you what's broken in the compiler.

### Correct

Correct means that the test asserts the correct behavior. Incidental behavior should not be asserted on, since we don't want to update tests when something changes unless the desired behavior changes. [Snapshot testing](https://en.wikipedia.org/wiki/Characterization_test) has its place, but it's very easy to miss a regression in a 6,000-line snapshot diff. Naturally, the most important thing is that the test doesn't accidentally assert the wrong behavior.

## Pulumi language: Conformance testing

Pulumi supports six languages (seven with HCL), and each language needs to do the same thing. Our solution to this problem is **conformance tests**: a language-agnostic test suite that can validate a Pulumi language is compliant. Each test has three components:

- a PCL (Pulumi's internal codegen language) program
- a list of Pulumi providers
- an assertion on the result of applying Pulumi to that program against those providers

The set of tests is [centrally maintained in pulumi/pulumi](https://github.com/pulumi/pulumi/tree/94536e530d770753b42087931c3e5c0b3c5a51b7/pkg/testing/pulumi-test-language), and then [each](https://github.com/pulumi/pulumi/blob/94536e530d770753b42087931c3e5c0b3c5a51b7/sdk/go/pulumi-language-go/language_test.go) [language](https://github.com/pulumi/pulumi-dotnet/blob/534fc3f5d74051bf644a9abbc1eb4bb3d0659073/pulumi-language-dotnet/language_test.go) [runs](https://github.com/pulumi/pulumi/blob/94536e530d770753b42087931c3e5c0b3c5a51b7/sdk/pcl/cmd/pulumi-language-pcl/language_test.go) [them](https://github.com/pulumi-labs/pulumi-hcl/blob/571fedb720fe7cd7d8f37ce01990c7c2df384658/cmd/pulumi-language-hcl/language_test.go). Because the test suite is language-agnostic, the cost of maintaining the test suite is shared across all languages, and a new Pulumi language can immediately take advantage of conformance tests to bootstrap.

Let's walk through an example of a conformance test case to clarify what we mean. This is the `l2-resource-simple` test case, which verifies a language can define a resource with input properties:

```hcl
// PCL
resource "res" "simple:index:Resource" {
    value = true
}
```

Pulumi's HCL plugin translates that PCL into this HCL program:

```hcl
terraform {
  required_providers {
    simple = {
      source  = "pulumi/simple"
      version = "2.0.0"
    }
  }
}

resource "simple_resource" "res" {
  lifecycle {
    create_before_destroy = true
  }
  value = true
}
```

Pulumi's Python language plugin, in contrast, translates the same PCL into this program:

```python
import pulumi
import pulumi_simple as simple

res = simple.Resource("res", value=True)
```

Each language plugin knows how to generate code from PCL and can run the code they generate. This is the key to language-agnostic testing.

The [assertion on this test](https://github.com/pulumi/pulumi/blob/94536e530d770753b42087931c3e5c0b3c5a51b7/pkg/testing/pulumi-test-language/tests/l2_resource_simple.go) is:

```go
func init() {
	LanguageTests["l2-resource-simple"] = LanguageTest{
		Providers: []func() plugin.Provider{
			func() plugin.Provider { return &providers.SimpleProvider{} },
		},
		Runs: []TestRun{
			{
				Assert: func(l *L, res AssertArgs) {
					snap := res.Snap

					// Require the sdk folder to exist
					_, ok := res.SDKs["simple-2.0.0"]
					require.True(l, ok, "expected simple sdk in %v", res.SDKs)

					RequireStackResource(l, res.Err, res.Changes)

					// Check we have the one simple resource in the snapshot, its provider and the stack.
					require.Len(l, snap.Resources, 3, "expected 3 resources in snapshot")

					RequireSingleResource(l, snap.Resources, "pulumi:providers:simple")
					simple := RequireSingleResource(l, snap.Resources, "simple:index:Resource")

					want := resource.NewPropertyMapFromMap(map[string]any{"value": true})
					assert.Equal(l, want, simple.Inputs, "expected inputs to be {value: true}")
					assert.Equal(l, simple.Inputs, simple.Outputs, "expected inputs and outputs to match")
				},
			},
		},
	}
}
```

The `l2-resource-simple` test will only pass when we can generate a valid program that defines a resource in the language under test. The language has to be wired up correctly to send the resource registration to the Pulumi engine.

In general, we try to have a conformance test for every language property we care about. The goal is simple: a Pulumi language is conformant if and only if it passes all language tests. While we are still a long way from testing every property we care about, we are 167 tests deep, and that number grows week by week. It's not as *comprehensive* as we would like, but it's still a lot of coverage. The tests are *targeted* & *correct*. Each test checks one aspect of a Pulumi program, in the above case registering a resource. This property is maintained by careful code review of each test case. Pulumi's conformance test suite is a high-value, high-quality, expensive-to-build test corpus. Constructing it was and remains an active effort, but it keeps our language support bar high.

## OpenTofu compatible: tfcompat

Unlike the Pulumi conformance test suite, the tfcompat test suite does not need careful human decision-making to figure out the correct behavior for a given OpenTofu program. There is a clear oracle: for all valid OpenTofu programs, `tofu apply` and `pulumi up` should do the same thing. For our purposes, we define "same thing" to mean that the invoked Terraform providers witnessed the same inputs and the program returned the same output. That gives us the definition of a tfcompat test: a Terraform config and a set of providers. We take that Terraform config and use *the same .tf file* to define both a Pulumi project & an OpenTofu workspace, then we run `tofu apply` & `pulumi up` against a set of recorded in-memory Terraform providers. If the providers saw the same thing for both engines, and the stacks output the same result, then our behavior matches & the test passes. If the providers received different inputs, then Pulumi's HCL implementation did not match `tofu`, and the test fails.

Let's walk through an example of a tfcompat test to make this clearer. The real test for the built-in `sum` intrinsic looks like this:

```go
// TestL1Sum exercises the `sum` built-in: both paths must accumulate with
// arbitrary-precision numbers so large integers and decimal fractions stay
// exact rather than being rounded through float64.
func TestL1Sum(t *testing.T) {
	t.Parallel()
	tfcompat.RunCase(t, "l1_sum", tfcompat.Case{})
}
```

The `tfcompat.Case{}` doesn't need any extra assertions, since the test automatically asserts on the workspace/stack output matching. The test file referenced by `"l1_sum"` looks like this:

```hcl
output "big_ints" {
  value = sum([9007199254740993, 1])
}

output "decimals" {
  value = sum([0.1, 0.2])
}

output "mixed" {
  value = sum([1, 2, 3, 4])
}
```

Each test locks what it observes against OpenTofu's behavior, effectively making *correctness* a built-in property of the test framework. The challenge for tfcompat tests is *comprehensiveness* & *targetedness*. During development, we handle this by pairing each tfcompat bug fix & new feature with at least one tfcompat test. The test suite is not yet comprehensive, but we are getting there. Targetedness is, alas, left purely to human judgment, as it's a form of taste.

#### Building out the tfcompat test corpus

Because tests are correct by construction, we can ask our tireless LLM assistants to find failing tests. This is productive because we don't need to filter out false positives or negatives; the LLM can see if the test is correct or not. Here is my Claude prompt verbatim:

> I'd like you to do a pass trying to find bugs. You will prove each bug with a genuine failing tfcompat test. Start with 10 sub-agents. Bugs should not be duplicates and bugs should not reflect existing issues. Each failure should be stood up as a draft PR with just the failing test added. These PRs will fail CI. That is intentional. Don't try to fix the bugs you solved. Keep the sub-agents running until you have found 10 failures. You are responsible for validating that the bugs are real and ensuring that the sub-agents do not create duplicate bugs, so you should create the PRs directly.

This is supported by [a](https://github.com/pulumi-labs/pulumi-hcl/blob/571fedb720fe7cd7d8f37ce01990c7c2df384658/.claude/skills/find-tfcompat-bug/SKILL.md) [couple](https://github.com/pulumi-labs/pulumi-hcl/blob/571fedb720fe7cd7d8f37ce01990c7c2df384658/.claude/skills/swarm-tfcompat-bugs/SKILL.md) [of](https://github.com/pulumi-labs/pulumi-hcl/blob/2709fcb5d5825f69d1213c9d176f40d6bc52c98e/.claude/skills/farm-tfcompat-bugs/SKILL.md) [skills](https://github.com/pulumi-labs/pulumi-hcl/blob/571fedb720fe7cd7d8f37ce01990c7c2df384658/.claude/skills/fix-tfcompat-bug/SKILL.md), but this strategy does [genuinely](https://github.com/pulumi-labs/pulumi-hcl/pull/447) [find](https://github.com/pulumi-labs/pulumi-hcl/pull/397) [high-quality](https://github.com/pulumi-labs/pulumi-hcl/pull/411) [bugs](https://github.com/pulumi-labs/pulumi-hcl/pull/422). Each fix is locked in with a useful tfcompat test, expanding the test suite. I do the same thing when I find a bug while manually testing Pulumi HCL: I throw it to Claude to reproduce with a failing tfcompat test.

## Conclusion

The key takeaway is that your tests inherently re-encode the desired behavior of your program, and you need to be careful to ensure that the encoding is *comprehensive*, *targeted* & *correct*. If you can encode correctness into the test harness itself instead of manually into each test case, writing tests becomes easier and much less error-prone. Like everything else in software engineering, LLMs improve velocity but not quality. In the worst case, they add useless tests locking in current behavior without concern for correctness. In the best case, you approach [property-based testing](https://hypothesis.works/articles/what-is-property-based-testing/) with an LLM as both [generator](https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf) & [reducer](https://users.cs.utah.edu/~regehr/papers/pldi12-preprint.pdf). Tests that are *correct* by construction let you unleash LLMs to move towards *comprehensive* coverage.
