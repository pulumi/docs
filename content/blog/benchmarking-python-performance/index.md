---
title: "Benchmarking Python Performance"
date: 2023-09-28
meta_desc: "Benchmarking and improving the performance of Pulumi Python programs."
meta_image: meta.png

authors:
    - justin-vanpatten
    - robbie-mckinstry

tags:
    - performance
    - platform
    - engineering
---

This is the second post in a series about performance optimizations we've made
to the Pulumi CLI and SDKs. In this post, we'll go deep on a performance
improvement we made for Pulumi Python programs. You can read more
about Amazing Performance in
[the first post in the series](https://www.pulumi.com/blog/amazing-performance/).

<!--more-->

Late last year, we took a hard look at the performance of Python programs when we
realized they weren't performing up to our expectations. We uncovered a major
bug limiting Python performance, and we ran a number of rigorous experiments
to evaluate just how performant Pulumi Python programs are after the bug had
been repaired. The results indicate Pulumi Python programs are significantly
faster than they were, and now Pulumi Python has reached performance parity
with Pulumi Node.js!

## The Bug

When you execute a Pulumi program, Pulumi internally builds a dependency graph
between the resources in your program. In every Pulumi program, some resources
have all their input arguments available at the time of their construction.
In contrast, other resources may depend on `Outputs` from other resources.

For example, consider a sample program where we create two AWS S3 buckets, where
one bucket is used to store logs for the other bucket:

```python
import pulumi
import pulumi_aws as aws

log_bucket = aws.s3.Bucket("logBucket", acl="log-delivery-write")

bucket = aws.s3.Bucket("bucket",
    acl="private",
    loggings=[aws.s3.BucketLoggingArgs(
        target_bucket=log_bucket.id,
        target_prefix="log/",
    )])
```

Because `bucket` takes an `Output` from `log_bucket` as an input,
we can't create the `bucket` until after the `log_bucket`
is created. We have to create the `log_bucket` first to compute its ID,
which we can pass to `bucket`. This idea extends inductively for
arbitrary programs – before any resource can be run, we must resolve the
`Outputs` of all of its arguments. To do this, Pulumi builds a dependency graph
between all resources in your program. Then, it walks the graph topologically
to schedule provisioning operations.

Provisioning operations that are not dependent on each other can be executed
in parallel, and Pulumi defaults to unbounded parallelism, but users can
ratchet this down if they so desire. Consider this embarrassingly parallel
Python program:

```python
import pulumi
import pulumi_aws as aws

# SQS
for i in range(100):
	name = f'pulumi-{str(i).rjust(3, "0")}'
	aws.sqs.Queue(name)

# SNS
for i in range(100):
	name = f'pulumi-{str(i).rjust(3, "0")}'
	aws.sns.Topic(name)
```

In this program, we can create 200 resources in parallel because none of them
take inputs from other resources. This program should be entirely
network-bound because Pulumi can issue all 200 API calls in parallel and wait
for AWS to provision the instances.
[We discovered](https://github.com/pulumi/pulumi/issues/11116), however,
that it did not! Strangely, API calls were issued in an initial batch of 20;
as one completed, another would start.

## The Fix

The culprit was the Python default future executor,
[ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor).
We observed that benchmark was run on a four-core computer, and in Python 3.5
to Python 3.7, the number of max workers is five times the number of cores, or 20
(in Python 3.8, this number was changed to `min(32, os.cpu_count() + 4)`). We
realized we shouldn't be using the default `ThreadExecutor`, and instead we
should provide a `ThreadExecutor` with an adjusted number of `max_workers`
based on the configured parallelism value. That way, when users run
`pulumi up --parallel`, which issues an upper bound on parallel resource
construction, the `ThreadExecutor` will respect that bound. We
[merged a fix](https://github.com/pulumi/pulumi/pull/11122)
that would plumb the value of `--parallel` through to a custom `ThreadExecutor`
and measured the impact this change had on the performance of our benchmark.

## Experimental Setup

We designed and implemented two independent experiments to evaluate this change.
The first experiment measures how well the patched Python runtime stacks up
against the control group, Pulumi Python without the patch. The second experiment
compares Pulumi Python to Pulumi TypeScript using the same benchmark ported
to TypeScript. We used the awesome benchmarking tool
[hyperfine](https://github.com/sharkdp/hyperfine) to record wall clock time as
our indicator of performance.

The experiments ran overnight on a 2021 MacBook Pro with 32GB RAM, the M1 chip,
and 10 cores. Experimental code is
[available on GitHub](https://github.com/pulumi/python-concurrency-experiments/tags),
and release tags pin the version of the code used for each experiment.
We also made an effort to run the experiments on a quiet machine connected
to power. For all experiment groups, `--parallel` was unset, translating to
unbounded parallelism.

Before between samples, we ran `pulumi destroy –yes` to ensure a fresh
environment. Hyperfine measures shell startup time and subtracts the value
before final measurements are recorded to more precisely represent the true
cost of execution. All groups collected 20 samples each. We also discard
`stderr` and `stdout` to reduce noise associated with logging to a tty, but
we do record the status code of each command so can show they executed successfully.

## Python: Pre- and Post-patch

This experiment compares the performance of Pulumi Python before and after
the patch was applied. The control group used Pulumi v3.43.1, while the
experimental group used Pulumi v3.44.3. The primary difference between these
two groups is that a fix was introduced for a Python runtime concurrency bug
as part of v3.44.0. Both groups use the same benchmark program, which created
100 AWS SNS and 100 AWS SQS resources in parallel, as described earlier. Only
the version of the Pulumi CLI is different between groups.

### [Control vs. Fix](https://app.warp.dev/block/rk7fFf2jn2iKXYcIXwhZ8F)

| **Group**        | **Mean**  | **Standard Deviation** |
| ---------------- | --------- | ---------------------- |
| **Control**      | 222.232 s | 0.908 s                |
| **Experimental** | 70.189 s  | 1.497 s                |

**Summary:** The  **Experimental Group** ran 3.17 ± 0.07 times faster than the **Control Group**, accounting for a +300% speedup in performance. Running Welch T-Test indicated statical significance (p = 2.93e-59, α=0.05).

## Python vs. TypeScript

After seeing very promising results from the first experiment, we wanted to
determine just how promising these results were. We decided to compare Pulumi
Python to Pulumi TypeScript to see if this fix had narrowed the gap in
performance between the two runtimes. We ported the Python program to TypeScript:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// SQS
[...Array(100).map((_, i) => {
  const name = `pulumi-${i}`;
  new aws.sqs.Queue(name);
})];

// SQS
[...Array(100).map((_, i) => {
  const name = `pulumi-${i}`;
  new aws.sqs.Queue(name);
})];
```

For this experiment, we fixed the version of the CLI to v3.44.3, which included
the patch to the Python runtime. Here are the result.

### [TypeScript vs. Python](https://app.warp.dev/block/rk7fFf2jn2iKXYcIXwhZ8F)

| **Group**      | **Mean** | **Standard Deviation** |
| -------------- | -------- | ---------------------- |
| **Python**     | 70.975 s | 0.909 s                |
| **TypeScript** | 73.741 s | 1.574 s                |

**Summary:** The **Python Group** performed the best and ran 1.04 ± 0.03 times
faster than the **TypeScript Group**. This accounts for a 4% difference in
performance. A second T-Test indicated statical significance
(p = 1.4e-07, α=0.05). Not only did Python close the gap with TypeScript,
but it is also now marginally faster than its Node.js competitor.

## Conclusion

It's rare to have a small PR result in such a massive performance increase,
but when it happens, we want to shout it from the rooftops. This change, which
shipped last year in v3.44.3, does not require Python users to opt-in; their programs
are now faster. This patch has closed the gap with the Node.js runtime.
Users can now expect highly parallel Pulumi programs to run in a similar
amount of time between either language.

## Artifacts

You can check out the artifacts of the experiments
[on GitHub](https://github.com/pulumi/python-concurrency-experiments/tags),
including the source code.

Here are some useful links:

* [The GitHub repository](https://github.com/pulumi/python-concurrency-experiments/tags)
* [Artifacts from the first experiment](https://github.com/pulumi/python-concurrency-experiments/releases/tag/parallelism), "Control vs. Fix" or "Pre- and Post-patch".
* [More statistics](https://app.warp.dev/block/F6KkbWHvDVWLwtYFKq08Q2) about the first experiment.
* [Artifacts from the second experiment](https://github.com/pulumi/python-concurrency-experiments/releases/tag/TypeScript-vs-Python)
* [More statistics](https://app.warp.dev/block/gspCIKn10y9bEvZDMWHe4Q) about the second experiment.
* [Pulumi Internals](https://www.pulumi.com/docs/intro/concepts/how-pulumi-works/)
