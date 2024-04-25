---
title: "Extending Pulumi's Language Support via YAML"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-06-08T10:56:34-05:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: Learn how to use Pulumi YAML as a bridge for CUE, JSONNET, and Rust. This open interface provides support to many other programming languages for Pulumi.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - david-flanagan

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - languages

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---

It's a surprise to nobody that Pulumi's YAML support has me rather excited, even though I'm unlikely to use YAML itself for Pulumi. So why do I find it exciting? Well, because it's an open interface to provide support to many other programming languages for Pulumi.

Let's take a look at using YAML as a bridge for CUE, JSONNET, and Rust.

<!--more-->

## CUE

It's no surprised to anybody that I'm a rather large supporter of the CUE project. I worked hard on the YAML launch to ensure CUE was available, with our CTO Luke covering one of the examples in our release blog. More recently, I also dedicated a Modern Infrastructure to showing how to manage DNS records on Cloudflare with a CUE interface.

{{< youtube "YATPtKehD4o?rel=0" >}}

I believe that CUE could open up a whole world of possibilities for Pulumi and I'm excited to see what myself and others can come up with in this space in 2022.

To use CUE as a compiler for Pulumi YAML, you need to update the `Pulumi.yaml` file with the following compiler options:

```yaml
runtime:
  name: yaml
  options:
    compiler: cue export
```

Next, run `cue mod init` to create a new CUE module. From here, you can create any file with a `.cue` extension and it'll become part of your Pulumi YAML project.

Here's a small example:

```cue
package pulumi

resources:
  randomPassword: {
    type: "random:RandomPassword"
    properties: {
      length:          16
      special:         true
      overrideSpecial: "_%@"
    }
  }

outputs:
  password: "${randomPassword.result}"
```

## JSONNET

In much the same view as CUE, Pulumi YAML can actually be a compilation target for any YAML superset. Let's take a look at another popular option: JSONNET.

First, we need to configure the compiler options:

```yaml
runtime:
  name: yaml
  options:
    compiler: jsonnet index.jsonnet
```

Then we can provide the `index.jsonnet` file. Here's the same example as above, but in JSONNET.

```jsonnet
{
  resources: {
    randomPassword: {
        type: "random:RandomPassword",
        properties: {
        length:          16,
        special:         true,
        overrideSpecial: "_%@"
        }
    }
  }

  outputs: {
    password: "${randomPassword.result}"
  }
}
```

Now, this is actually just a plain JSON object and we've not taken advantage of any JSONNET features yet. So let's create a function for creating this random resource.

```jsonnet
local random_password(length=16, special=true, overrideSpecial="@") = {
  type: "random:RandomPassword",
  properties: {
    length: length,
    special: special,
    overrideSpecial: overrideSpecial,
  },
};


local first = random_password();
local second = random_password();

{
    resources: {
        first: first,
        second: second,
    },

    outputs: {
        "firstPassword": "first.result"
    }
}
```

Now we have a function for creating a resource, with default values. Nice.

## Rust

So, what if we wanted to do the same ... but with Rust? Let's see! First, our compiler options:

```yaml
runtime:
  name: yaml
  options:
    compiler: cargo run
```

Next, we need to generate some Rust types to represent our Pulumi resources. Instead of doing the random resource, like above, let's go with the Cloudflare resources from the YouTube video I recorded.

```rust
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
pub struct Zone {
    pub zone: String,
}

#[derive(Serialize, Deserialize)]
pub struct Record {
    pub name: String,
    pub typ: String,
    pub value: String,
}
```

Rust has great meta programming capabilities, meaning our types can all be enriched by [Serde](https://serde.rs/) to handle serialization through simple [derive macros](https://serde.rs/derive.html).

Next, we spec out some skeleton Pulumi types too:

```rust
use crate::cloudflare::{Record, Zone};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Serialize, Deserialize)]
pub struct Pulumi {
    pub resources: HashMap<String, Resource>,
}

#[derive(Serialize, Deserialize)]
#[serde(tag = "type")]
pub enum Resource {
    #[serde(rename = "cloudflare:Zone")]
    Zone { properties: Zone },
    #[serde(rename = "cloudflare:Record")]
    Record { properties: Record },
}
```

We represent all the "available" resources via the `Resource` enum, which has a special annotation to indicate the "type" for Pulumi. We also represent the top level YAML that Pulumi expects as the `Pulumi` type.

Lastly, we implement our `fn main` and create our resources, finishing by printing the YAML to `stdout`.

```rust
use serde_yaml;
use std::collections::HashMap;

mod cloudflare;
mod pulumi;

use cloudflare::Zone;
use pulumi::{Pulumi, Resource};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut pulumi: Pulumi = Pulumi {
        resources: HashMap::new(),
    };

    pulumi.resources.insert(
        "rawkode-dev".into(),
        Resource::Zone {
            properties: Zone {
                zone: "rawkode-dev.com".into(),
            },
        },
    );

    println!("{}", serde_yaml::to_string(&pulumi)?);

    Ok(())
}
```

## What's Next?

Obviously, this isn't entirely practical and we can make this 100 times better. So what am I working on next? Well, instead of manually creating all the types that we need for Pulumi to function - what if we could pull in the `schema.json` that all Pulumi providers have and automatically generate the types? Continuing with Rust's meta programming, we could achieve this with a procedural macro.

What might that look like?

```rust
use pulumi::import_schema;

import_schema!("pulumi/pulumi-cloudflare");
```

This would generate the types, add functions for requesting outputs, and work with any Pulumi provider.

Stay tuned, I'll be back with updates as soon as I can.
