---
title: "Using the Custom API"
layout: topic
date: 2021-12-15
draft: false
description: |
    Explore uses of the Automation API with some working examples and possible
    additional builds to try.
meta_desc: |
    Explore uses of the Automation API with some working examples and possible
    additional builds to try.
index: 3
estimated_time: 15
meta_image: meta.png
authors:
    - santamaria
tags:
    - learn
links:
    - text: Examples from Pulumi
      url: https://github.com/pulumi/automation-api-examples
block_external_search_index: false
---

Now that we've set everything up and explored the codebase, let's run it! Well, almost. We need to do a couple more things first.

## Configuring the build

We need to configure everything before it can run. Almost there!

Pass the following configuration values into Pulumi to the **local program** (that's `api/burner.py`, remember?).

* `aws:profile` (if you're using sso or have a number of configurations for AWS)
* `aws:region`

If you don't remember how, here's a quick step-by-step:

1. Open a terminal.
1. Change into the `api/` directory.
1. Run `pulumi config set aws:region <region>`, replacing `<region>` with your AWS region.

## Running our program

Now, let's run it! From the root of the repo in a terminal, run `python infra_api.py`. Notice that we're not running a `pulumi up`! Here's what you should get:

```bash
Serving on port 8000...
```

Now, we'll try `curl`ing the `location` endpoint. Open a new terminal window and run `curl localhost:8000/location`:

```bash
$ curl localhost:8000/location
{"response": "{'location': '\"us-west-2\"'}"}
```

What's happening in the terminal window where we're running the API? Flip back to the terminal window running the API, and check it out:

```bash
$ python infra_api.py
Serving on port 8000...
info: Preparing a virtual environment...
info: Successfully prepared virtual environment
info: Initializing stack...
info: Successfully initialized stack
info: Setting project config...
info: Successfully set project config
info: Refreshing stack...
Refreshing (dev)

View Live: https://app.pulumi.com/<org>/learn-auto-api/dev/updates/120



Resources:

Duration: 1s

info: Successfully refreshed stack
info: Updating stack...
Updating (dev)

View Live: https://app.pulumi.com/<org>/learn-auto-api/dev/updates/121


 +  pulumi:pulumi:Stack learn-auto-api-dev creating
 +  aws:iam:Role role-2 creating
 +  aws:iam:Role role-2 created
 +  aws:iam:RolePolicyAttachment role-policy creating
 +  aws:lambda:Function location-finder creating
 +  aws:iam:RolePolicyAttachment role-policy created
@ Updating....
 +  aws:lambda:Function location-finder created
 +  aws:lambda:Invocation test-invoke creating
 +  aws:lambda:Invocation test-invoke created
 +  pulumi:pulumi:Stack learn-auto-api-dev created

Outputs:
    location: "\"us-west-2\""

Resources:
    + 5 created

Duration: 24s

info: Successfully updated stack
info: Summary:
{
    "create": 5
}
info: Output: "us-west-2"
info: Destroying stack...
Destroying (dev)

View Live: https://app.pulumi.com/<org>/learn-auto-api/dev/updates/122


 -  aws:lambda:Invocation test-invoke deleting
 -  aws:lambda:Invocation test-invoke deleted
 -  aws:iam:RolePolicyAttachment role-policy deleting
 -  aws:lambda:Function location-finder deleting
 -  aws:iam:RolePolicyAttachment role-policy deleted
 -  aws:lambda:Function location-finder deleted
 -  aws:iam:Role role-2 deleting
 -  aws:iam:Role role-2 deleted
 -  pulumi:pulumi:Stack learn-auto-api-dev deleting
 -  pulumi:pulumi:Stack learn-auto-api-dev deleted

Outputs:
  - location: "\"us-west-2\""

Resources:
    - 5 deleted

Duration: 5s

The resources in the stack have been deleted, but the history and configuration associated with the stack are still maintained.
If you want to remove the stack completely, run 'pulumi stack rm dev'.
info: Successfully destroyed stack
127.0.0.1 - - [26/May/2022 17:49:02] "GET /location HTTP/1.1" 200 45
```

There are all the logs we added! Pretty cool!

You'll notice that we destroyed all of the infrastructure that was running after the endpoint was touched and the function returned. This is part of the beauty of the Automation API: No more leftover infrastructure! If you needed to destroy the stack manually, though, you can change into the `api` directory and run Pulumi commands as normal, including `pulumi destroy`, because we updated `api/__main__.py` to point to and run the same `burner.pulumi_program()` call that the Automation API is running.

## Exploring other examples

Our community has explored a number of different common use cases and shared what they've built. Check them out!

### Wiring a self-service platform

One of the common examples is a self-service platform. To give credit where credit is due, a fantastic Flask-based, in-depth example can be found in the [self-service-platyform repo](https://github.com/komalali/self-service-platyform) by one of the Pulumi community members. There also is a smaller example of the same idea in [Go](https://github.com/pulumi/automation-api-examples/tree/main/go/pulumi_over_http), [Python](https://github.com/pulumi/automation-api-examples/tree/main/python/pulumi_over_http), and [TypeScript/Javascript](https://github.com/pulumi/automation-api-examples/tree/main/nodejs/pulumiOverHttp-ts), in the Pulumi Automation API examples repo.

In general, all of these examples create a simple web page that provides a user interface for your Pulumi programs. The interface has standard use cases defined with the actual infrastructure for those use cases abstracted away in a RESTful manner. So, for example, if a user wanted a static site, a request for that use will spin up a storage spot, a policy for that storage, and a basic HTML file in that storage that's delivered as a webpage.

You'll notice that these examples don't just wrap the CLI commands as callable functions. The Automation API is embedded as part of the various larger calls to the platform's API. Pretty cool!

### Migrating databases

What if you could migrate a database with Pulumi? It's possible! The examples in [Go](https://github.com/pulumi/automation-api-examples/blob/main/go/database_migration), [Python](https://github.com/pulumi/automation-api-examples/tree/main/python/database_migration), [TypeScript/Javascript](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/databaseMigration-ts), and [C#/.NET](https://github.com/pulumi/automation-api-examples/blob/main/dotnet/DatabaseMigration) show a basic creation of a table with insertion and verification of data. If we combine this idea with the same type of idea of a web portal, we could make a plain migration tool that takes data from one table and generates a new one from that data, effectively migrating the table from one database to another.

<br/>
<br/>

These examples are only a small sample of the power of the Automation API.

---

Congratulations! You've now finished this pathway on embedding Pulumi in other programs, platforms, and systems! In this pathway, you've learned about wrapping the standard Pulumi commands into a program with the Automation API, considering where Pulumi could be run and building out logging and error handling accordingly, and working with the Automation API to integrate your infrastructure into other workflows.

Go build new things, and watch this space for more learning experiences with Pulumi!
