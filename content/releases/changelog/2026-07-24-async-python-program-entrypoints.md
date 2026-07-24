---
title: "Async Python program entrypoints with pulumi.run"
date: 2026-07-24
meta_desc: Pulumi Python programs can now use an async entrypoint. Pass an async function to pulumi.run to await operations and return stack outputs directly.
authors:
    - julien-poissonnier
---

Pulumi Python programs can now use an async entrypoint. Pass a zero-argument async function to `pulumi.run` in your `__main__.py`, and the runtime awaits it on the program's event loop. This makes it easier to call async functions while retaining a linear program flow:

```python
import pulumi

async def main() -> pulumi.Inputs:
    value_a = await some_async_operation()
    value_b = await some_other_async_operation()
    return {"value_a": value_a, "value_b": value_b}

pulumi.run(main)
```

If the entrypoint returns a mapping, each entry is registered as a stack output, merging with any explicit `pulumi.export` calls using the normal export behavior. The entrypoint can also return `None` and call `pulumi.export` directly.

`pulumi.run` may be called only once per program, and existing synchronous programs keep working unchanged. For details, see the [async entrypoint documentation](/docs/iac/languages-sdks/python/#async-entrypoint).
