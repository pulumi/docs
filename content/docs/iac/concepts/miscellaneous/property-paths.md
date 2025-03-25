---
title_tag: Property Paths
meta_desc: Property Paths are used to refer to elements in a configuration object.
title: Property Paths
h1: Property Paths
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    name: Property Paths
    parent: miscellaneous-concepts
    weight: 2
search:
  keywords:
    - paths
    - property
    - nest
    - notation
    - root
    - elements
    - array
---

Property paths represent a key or series of keys that one can use to refer to elements in an object or array.
The syntax, inspired by JavaScript, supports both dot notation and bracket notation.
For keys that contain special characters (i.e. `[`, `]`, `"`, or `.`) or begin with a digit,
bracket notation is required.

Below are some example property paths:

- `root`
- `root.nested`
- `root["nested"]`
- `root.double.nest`
- `root["double"].nest`
- `root["double"]["nest"]`
- `root.array[0]`
- `root.array[100]`
- `root.array[0].nested`
- `root.array[0][1].nested`
- `root.nested.array[0].double[1]`
- `root["key with \"escaped\" quotes"]`
- `root["key with a ."]`
- `["root key with \"escaped\" quotes"].nested`
- `["root key with a ."][100]`
- `root.array[*].field`
- `root.array["*"].field`
