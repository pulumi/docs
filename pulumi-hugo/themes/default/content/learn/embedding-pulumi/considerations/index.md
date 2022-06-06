---
title: "Understanding Logging and Error Handling"
layout: topic
date: 2021-12-15
draft: false
description: |
    Explore why it's important to consider logging and error handling when using
    the Automation API.
meta_desc: |
    Explore why it's important to consider logging and error handling when using
    the Automation API.
index: 2
estimated_time: 10
meta_image: meta.png
authors:
    - laura-santamaria
tags:
    - learn
block_external_search_index: false
---

Now that we've got a bit of code, we need to consider how we're going to use this code. We're not going to be running it from our local console any longer, so we have some things to think about.

## Adding logging

Since we're running an API that could get called anywhere, it's always good to add some logging to our stack. Why? Well, you'll need those logs for debugging, and if someone were to try to access a system through, for example, your pipeline, the basic system logs are probably the first place they'll try to wipe out. Additional logging locations that are separate from the actual system means you can set up a write-only connection, ensuring that any compromise to that system can't affect the logs as they're written.

Pulumi has some built-in ability in the free tier to log with a call to `pulumi.<log-level>`. If you're needing audit logging (tracking which system or who triggered each action), that's on the Enterprise tier. We're going to use the built-in logs, however, to get us going.

If you're not familiar with logging libraries, the call is typically to the logging level as you'll find with the Pulumi logging functions (`pulumi.debug()`, `pulumi.info()`, `pulumi.error()`, etc.). Logging levels are important as they help anyone reviewing the logs tune to the level of details they need for their use case. Skipping logging levels to use one generic level often leads to others turning off logging to reduce noise, which goes counter to the actual use of logging.

In our case, all of the logging calls are in `infra/basic.py`. Let's explore a bit.

At the top of the file, we've imported the `log` call from the `pulumi` library, so then all logging is from the `log.<level>` call. This is a shift from `pulumi.<level>` for readability and a smaller program since we're trying to minimize the size for performance and cost reasons. On line 29, you'll find our first logging call: `log.info("Preparing a virtual environment...")`. Line 48 has the paired log for a successful run: `log.info("Successfully prepared virtual environment")`. Two lines down on line 50, you'll find an ERROR-level log: `log.error("Failure while preparing a virtual environment:")`. These logs appear in the console as you run an update. If you were to run your program (which we'll do soon!), you would get the following output:

```bash
info: Preparing a virtual environment...
info: Successfully prepared virtual environment
# ...
```

In this case, there were no errors, so the INFO levels are the only ones that appear. If you ran into an error on build, you'd get the ERROR log level. Without these logs, you wouldn't get any output---for example, here there's none of the virtual environment creation outputs that you'd find if you were running this with the CLI.

## Handling Exceptions

Good development practice is to handle exceptions gracefully. Any call to our custom API should do the same, and it should log the error. If we examine the code in `infra/basic.py`, we'll find exceptions being handled. As an example, here's lines 79-86:

```python
def refresh_stack(stackd):
    try:
        log.info("Refreshing stack...")
        stackd.refresh(on_output=print)
        log.info("Successfully refreshed stack")
    except Exception as e:
        log.error("Failure when trying to refresh stack:")
        raise e
```

Here, any issue that the refresh step encounters is passed as an exception to the error log. We don't have a specific need to keep the program running, so we are just adding to the log and raising the error without forcing a specific exception class. If we needed to clean up, such as if we spun up some test infrastructure for a test that failed and we need to tear it down, you would handle that clean up before raising the error (probably with a `try...except` clause of its own holding a chained exception and logging).

<br/>
<br/>

With all of this in mind, let's try running it. Onward!
