---
title: Module iterable
---

<a href="../index.html">@pulumi/pulumi</a> &gt; iterable

<h2 class="pdoc-module-header">Index</h2>

* <a href="#groupBy">function groupBy</a>
* <a href="#toObject">function toObject</a>

<a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/iterable/index.ts">iterable/index.ts</a> 


<h2 class="pdoc-module-header" id="groupBy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/iterable/index.ts#L61">function groupBy</a>
</h2>

```typescript
groupBy<T,V>(iter: Input<Input<T>[]>, selector: { ... }): Output<{ ... }>
```


groupBy takes an array of T values, and a selector that prduces key/value pairs from those inputs,
and converts this array into an output object, with those keys, and where each property is an array of values,
in the case that the same key shows up multiple times in the input.

For instance, given an array as follows

    [{ s: "a", n: 1 }, { s: "a", n: 2 }, { s: "b", n: 1 }]

and whose selector is roughly `(e) => [e.s, e.n]`, the resulting object will be

    { "a": [1, 2], "b": [1] }


<h2 class="pdoc-module-header" id="toObject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/iterable/index.ts#L30">function toObject</a>
</h2>

```typescript
toObject<T,V>(iter: Input<Input<T>[]>, selector: { ... }): Output<{ ... }>
```


toObject takes an array of T values, and a selector that produces key/value pairs from those inputs,
and converts this array into an output object with those keys and values.

For instance, given an array as follows

    [{ s: "a", n: 1 }, { s: "b", n: 2 }, { s: "c", n: 3 }]

and whose selector is roughly `(e) => [e.s, e.n]`, the resulting object will be

    { "a": 1, "b": 2, "c": 3 }


