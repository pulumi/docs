---
title: "Managing GitHub Webhooks with Pulumi"
authors: ["matt-ellis"]
tags: ["Serverless"]
meta_desc: "Use Pulumi to write a hook that would clean up branches after a pull request got merged."
date: "2018-07-13"
---

At Pulumi, we do all of our development on GitHub, with a workflow built
around topic branches. When a developer wants to make a change, they
push a branch to GitHub, open a pull request and (in theory) once it's
merged, delete the branch. In practice, we'll often forget to delete the
topic branch (I'm probably the worst offender), which means we end up
having topic branches linger on our main repository until they are
explicitly cleaned up. While it's a lot of fun to go a click through the
GitHub UI from time to time, deleting merged branches, it's even more
fun to build automation to do this for us. Since GitHub has a rich set
of [webhooks](https://developer.github.com/webhooks/) and Pulumi makes
it easy to write serverless functions, it felt like it would be natural
to use Pulumi to write a hook that would clean up branches after a pull
request got merged. In addition, Pulumi lets us leverage real
programming languages to build abstractions, which means we can build a
simple framework that hides much of the ceremony behind defining a hook
and lets us focus on the core logic of our hook, without worrying about
how it is deployed and managed.
<!--more-->

## A simple hook

When you register a webhook with GitHub, you provide an HTTP endpoint
and a set of events you'd like to listen for. When one of the events
happens on GitHub, it makes a POST request to your HTTP endpoint with a
payload that describes the event. We'll start by creating a simple
endpoint that just logs when an event happens. We'll start by using the
[`aws-serverless`](https://www.npmjs.com/package/@pulumi/aws-serverless)
package to define an API that just calls `console.log` to write the
`X-GitHub-Event` header that is sent with the request:

```typescript
import * as serverless from "@pulumi/aws-serverless";

const api = new serverless.apigateway.API("hook", {
    routes: [{
        path: "/",
        method: "POST",
        handler: async (req, ctx) => {
            console.log(`Got event ${req.headers['X-GitHub-Event']}`);
            return {
                statusCode: 200,
                body: ""
            }
        }
    },],
});

export const url = api.url;
```

After running `pulumi update`, we'll have a HTTP endpoint we can give to
GitHub:

    Updating stack 'github-hook-blog-dev'
    Performing changes:

         Type                                Name                                   Status      Info
     +   pulumi:pulumi:Stack                 github-hook-blog-github-hook-blog-dev  created
     +   ├─ aws-serverless:apigateway:API    hook                                   created
     +   │  ├─ aws:apigateway:RestApi        hook                                   created
     +   │  ├─ aws:apigateway:Deployment     hook                                   created
     +   │  ├─ aws:lambda:Permission         hook-980655da                          created
     +   │  └─ aws:apigateway:Stage          hook                                   created
     +   └─ aws:serverless:Function          hook980655da                           created
     +      ├─ aws:iam:Role                  hook980655da                           created
     +      ├─ aws:iam:RolePolicyAttachment  hook980655da-32be53a2                  created
     +      └─ aws:lambda:Function           hook980655da                           created

    ---outputs:---
    url: "https://t1vyz1x203.execute-api.us-west-1.amazonaws.com/stage/"

Now that we have our Webhook deployed, we'll add it to GitHub. In this
case, I have a little throwaway GitHub repository I use for testing this
sort of stuff. In that repository, I go to Settings -> Webhooks -> Add
webhook and fill in my information:

- Payload URL: The value of the `url` output of my Pulumi program (in
  this case it is
  `https://t1vyz1x203.execute-api.us-west-1.amazonaws.com/stage/`).
- Content Type: `application-json`. I know we'll be inspecting this
  content as we develop the hook and since we're writing the
  implementation in TypeScript, it will be easier to interact with
  JSON encoded data.
- Secret: Generate a random string and put it here. I used
  [random.org](https://www.random.org/) to do so, but any random
  string will suffice. We'll use this string to validate that the
  request came from GitHub.
- Events: I only care about `pull_request` events, so I picked "Let me
  select individual events" and then checked "Pull requests" and
  unchecked the other event types.
- Active: Since we want GitHub to deliver events, we'll keep this
  checked.

Once that's done, we can test our hook by opening a pull request,
waiting a few moments and then use `pulumi logs` to ensure our hook was
triggered:

    $ pulumi logs
    Collecting logs for stack github-hook-blog-dev since 2018-07-09T09:06:51.000-07:00.

     2018-07-09T10:06:00.610-07:00[          hook980655da-d0462d4] START RequestId: 5aab2d71-839a-11e8-a7ae-93a25d68b5a9 Version: $LATEST
     2018-07-09T10:06:00.612-07:00[          hook980655da-d0462d4] 2018-07-09T17:06:00.611Z 5aab2d71-839a-11e8-a7ae-93a25d68b5a9    Got event ping
     2018-07-09T10:06:00.630-07:00[          hook980655da-d0462d4] END RequestId: 5aab2d71-839a-11e8-a7ae-93a25d68b5a9
     2018-07-09T10:06:00.630-07:00[          hook980655da-d0462d4] REPORT RequestId: 5aab2d71-839a-11e8-a7ae-93a25d68b5a9   Duration: 10.99 ms  Billed Duration: 100 ms     Memory Size: 128 MB Max Memory Used: 20 MB

     2018-07-09T10:06:23.241-07:00[          hook980655da-d0462d4] START RequestId: 68445127-839a-11e8-80a6-759a29eb6005 Version: $LATEST
     2018-07-09T10:06:23.243-07:00[          hook980655da-d0462d4] 2018-07-09T17:06:23.243Z 68445127-839a-11e8-80a6-759a29eb6005    Got event pull_request
     2018-07-09T10:06:23.250-07:00[          hook980655da-d0462d4] END RequestId: 68445127-839a-11e8-80a6-759a29eb6005
     2018-07-09T10:06:23.250-07:00[          hook980655da-d0462d4] REPORT RequestId: 68445127-839a-11e8-80a6-759a29eb6005   Duration: 1.32 ms   Billed Duration: 100 ms     Memory Size: 128 MB Max Memory Used: 20 MB

Here we can see our hook got two events, the first is the
[`ping`](https://developer.github.com/webhooks/#ping-event) event, which
GitHub sends to verify the hook. The second event is from when I opened
a pull request in the repository.

Before we go any further, let's start using the secret we set to
validate the Webhook payload. When GitHub sends an event to a Webhook,
it sets a special header
[`X-Hub-Signature`](https://developer.github.com/webhooks/#delivery-headers)
which is an HMAC digest of the request body. The value we placed in the
Secret field when configuring the Webhook is the key. So I'll take that
secret value, set it as a configuration value in my project:

    $ pulumi config set --secret hookSecret [READACTED]

Once that's done, I can use this value to validate the signiture. We'll
use some functions from node's `crypto` library at runtime to handle
this. If the signature we computed doesn't match what was provided with
the request, we'll return error code 400. Our program now looks like
this:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as serverless from "@pulumi/aws-serverless";

const cfg = new pulumi.Config(pulumi.getProject());
const hookSecret = cfg.require("hookSecret");

const api = new serverless.apigateway.API("hook", {
    routes: [{
        path: "/",
        method: "POST",
        handler: async (req, ctx) => {
            // Compute the HMAC of the body, using `hookSecret` as the key and `sha1` as the algorithm

            // First, grab the body. It may be base64 encoded, depending on if `req.isBase64Encoded` is set. If so, we
            // should decode it.
            let body = req.body;
            if (req.isBase64Encoded) {
                body = Buffer.from(body, 'base64').toString();
            }

            // Now compute the HMAC.
            const crypto = await import("crypto");
            const hmac = crypto.createHmac("sha1", hookSecret);
            hmac.update(body);

            const computedSignature = `sha1=${hmac.digest("hex")}`;

            // Compare the signature that came in with the request to what we computed.
            if (req.headers['X-Hub-Signature'] === undefined ||
                !crypto.timingSafeEqual(Buffer.from(req.headers['X-Hub-Signature']), Buffer.from(computedSignature)))
            {
                console.log(`error: bad signature ${req.headers['X-Hub-Signature']} !== ${computedSignature}`);
                return {
                    statusCode: 400,
                    body: "bad signature"
                }
            }

            console.log(`Got event ${req.headers['X-GitHub-Event']} and signature ${computedSignature} matched`);
            return {
                statusCode: 200,
                body: ""
            }
        }
    },],
});

export const url = api.url;
```

After deploying, we can trigger another event by closing an existing
pull request or opening a new one, and then use `pulumi logs` to confirm
that our validation is working as intended:

    $ pulumi logs
    Collecting logs for stack github-hook-blog-dev since 2018-07-09T12:43:05.000-07:00.

     2018-07-09T13:43:00.630-07:00[          hook980655da-d0462d4] START RequestId: ab363ec7-83b8-11e8-a7ae-93a25d68b5a9 Version: $LATEST
     2018-07-09T13:43:00.693-07:00[          hook980655da-d0462d4] 2018-07-09T20:43:00.693Z ab363ec7-83b8-11e8-a7ae-93a25d68b5a9    Got event pull_request and signature sha1=b83320205edc7cb9aeea1a845b85de0c83092e1d matched
     2018-07-09T13:43:00.731-07:00[          hook980655da-d0462d4] END RequestId: ab363ec7-83b8-11e8-a7ae-93a25d68b5a9
     2018-07-09T13:43:00.731-07:00[          hook980655da-d0462d4] REPORT RequestId: ab363ec7-83b8-11e8-a7ae-93a25d68b5a9   Duration: 128.75 ms Billed Duration: 200 ms     Memory Size: 128 MB Max Memory Used: 20 MB

## Building an abstraction

We now have a nice little skeleton that we can use when writing a
webhook on GitHub. Let's start to leverage some other Pulumi features to
make things simpler and provide a nicer interface for writing hooks.
Let's start by abstracting away the code that handles validating the
request and returning a response behind a helper method. We'll pass a
function to this helper which will be called after the validation has
completed. We'll also parse the body into a JSON object that our handler
can use.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as serverless from "@pulumi/aws-serverless";

const cfg = new pulumi.Config(pulumi.getProject());
const hookSecret = cfg.require("hookSecret");

function createWebhook(name: string, handler: ((req: serverless.apigateway.Request, body: any) => Promise<void>)) {
    return new serverless.apigateway.API(name, {
        routes: [{
            path: "/",
            method: "POST",
            handler: async (req, ctx) => {
                // Compute the HMAC of the body, using `hookSecret` as the key and `sha1` as the algorithm

                // First, grab the body. It may be base64 encoded, depending on if `req.isBase64Encoded` is set. If so, we
                // should decode it.
                let body = req.body;
                if (req.isBase64Encoded) {
                    body = Buffer.from(body, 'base64').toString();
                }

                // Now compute the HMAC.
                const crypto = await import("crypto");
                const hmac = crypto.createHmac("sha1", hookSecret);
                hmac.update(body);

                const computedSignature = `sha1=${hmac.digest("hex")}`;

                // Compare the signature that came in with the request to what we computed.
                if (req.headers['X-Hub-Signature'] === undefined ||
                    !crypto.timingSafeEqual(Buffer.from(req.headers['X-Hub-Signature']), Buffer.from(computedSignature)))
                {
                    console.log(`error: bad signature ${req.headers['X-Hub-Signature']} !== ${computedSignature}`);
                    return {
                        statusCode: 400,
                        body: "bad signature"
                    }
                }

                // Call the handler after parsing the body as JSON
                await handler(req, JSON.parse(body));

                return {
                    statusCode: 200,
                    body: ""
                }
            }
        },],
    });
}

const api = createWebhook("hook", async (req, body) => {
    console.log(`Got event ${req.headers['X-GitHub-Event']} with action ${body.action}`);
});

export const url = api.url;
```

The shape of the JSON object for this event is
[documented](https://developer.github.com/v3/activity/events/types/#pullrequestevent)
on GitHub. Here we're pulling out the action field, which tells us
something about the state of the pull request. For our bot, we only care
about PRs where the `action` is `closed` and the `merged` key is set to
`true`. When this holds, we'll want to delete the branch the pull
request came from, if it was a topic branch (instead of a PR opened from
a fork). We'll leverage the existing [`@octokit/rest` NPM package](https://www.npmjs.com/package/@octokit/rest) to do this. We can
generate a [personal access token](https://github.com/settings/tokens),
and give it `repo` level scope, so it can act as us and delete branches.
We'll then add this key to our configuration:

    $ pulumi config set --secret githubToken [REDACTED]

And we can now update our handler to use this API:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as serverless from "@pulumi/aws-serverless";

const cfg = new pulumi.Config(pulumi.getProject());
const hookSecret = cfg.require("hookSecret");

function createWebhook(name: string, handler: ((req: serverless.apigateway.Request, body: any) => Promise<void>)) {
    /* Same as the previous version */
}

const githubToken = cfg.require("githubToken");

const api = createWebhook("hook", async (req, body) => {
    if (body.action === "closed" && body.pull_request.merged &&
        body.pull_request.base.user.login === body.pull_request.head.user.login &&
        body.pull_request.base.repo.name === body.pull_request.head.repo.name)
    {
        const octokit = require('@octokit/rest')()
        octokit.authenticate({
            type: 'token',
            token: githubToken
        });

        console.log(`Deleting reference heads/${body.pull_request.head.ref}`);

        await octokit.gitdata.deleteReference({
            owner: body.pull_request.head.user.login,
            repo: body.pull_request.head.repo.name,
            ref: `heads/${body.pull_request.head.ref}`
        });
    }
});

export const url = api.url;
```

After `pulumi updating`, try merging a pull request! Shortly after you
click the merge button, the source branch should be deleted
automatically. You can also see our log message in the output of
`pulumi logs`:

    $ pulumi logs
    [matell@matell throwaway]$ pulumi logs
    Collecting logs for stack github-hook-blog-dev since 2018-07-09T13:30:26.000-07:00.

     2018-07-09T14:28:52.254-07:00[          hook980655da-d0462d4] START RequestId: 1368afec-83bf-11e8-bf0d-cf623578c325 Version: $LATEST
     2018-07-09T14:28:52.431-07:00[          hook980655da-d0462d4] 2018-07-09T21:28:52.371Z 1368afec-83bf-11e8-bf0d-cf623578c325    Deleting reference heads/test-branch
     2018-07-09T14:28:53.478-07:00[          hook980655da-d0462d4] END RequestId: 1368afec-83bf-11e8-bf0d-cf623578c325
     2018-07-09T14:28:53.478-07:00[          hook980655da-d0462d4] REPORT RequestId: 1368afec-83bf-11e8-bf0d-cf623578c325   Duration: 1221.97 ms    Billed Duration: 1300 ms    Memory Size: 128 MB Max Memory Used: 33 MB

So, in about 75 lines of code, we've defined a small abstraction for
authoring a GitHub Webhook and we've used it to write a little bot that
deletes topic branches after pull requests from them have been merged.
In itself, that's pretty cool, but we can do some more cool stuff with
Pulumi. As is, while we can create the Webhook using Pulumi, we have to
register it using the GitHub console, which is a little tedious. What if
we could manage the registration of the hook with Pulumi itself? We'd
really like to model the hook's association with GitHub as a resource
that can be created, updated and deleted. Is there a way we can do that?
Yes, there is!

## Managing all the things with Pulumi

Pulumi [uses gRPC](https://github.com/pulumi/pulumi/blob/master/sdk/proto/provider.proto)
to define a contract between resource providers and the rest of Pulumi.
So, we could go implement that contract in a language like go, like we
do in our [Kubernetes](https://github.com/pulumi/pulumi-kubernetes)
provider. Another option would be to take the existing
[Terraform GitHub Provider](https://github.com/terraform-providers/terraform-provider-github)
and use [Pulumi's terraform bridge](https://github.com/pulumi/pulumi-terraform/) wrap it into a
Pulumi resource provider, like we do with our
[pulumi-aws](https://github.com/pulumi/pulumi-aws) provider. There's one
final option, which is to use the "[dynamic provider](https://github.com/pulumi/pulumi/blob/ad3b5e7ee88346bc7e960de9f953957a72f84516/sdk/nodejs/dynamic/index.ts#L109)",
which allows us to implement a resource provider in JavaScript itself.
We wrote this provider to help us with testing, so we could mock out
resources and control their lifecycle, but we can also use it to create
a resource that manages registration of a webhook with GitHub. To do so,
we need to implement `dynamic.ResourceProvider` interface. Once we have
the provider, we can also write a resource that uses it.

```typescript
class GithubWebhookProvider implements dynamic.ResourceProvider {

    // Check ensures that all required properties are set. In this case we have three required parameters.
    check = async (olds: any, news: any) => {
        const failedChecks = [];

        for (const prop of ["url", "owner", "repo"]) {
            if (news[prop] === undefined) {
                failedChecks.push({property: prop, reason: `required property '${prop}' missing`});
            }
        }

        return { inputs: news, failedChecks: failedChecks };
    }

    // Today the engine does the diff between properties to detect if there is a change but this method does
    // tell the engine if the changes between the old and new values require the resource to be "replaced"
    // (that is a new one is created and the old one is deleted) vs being edited in place. For us, if the owner
    // or repo the hook is installed on changes, we'll trigger a replacement.
    diff = async (id: pulumi.ID, olds: any, news: any) => {
        const replaces = [];

        for (const prop of ["owner", "repo"]) {
            if (olds[prop] !== news[prop]) {
                replaces.push(prop);
            }
        }

        return { replaces: replaces };
    }

    // Create actually creates the hook. We use octokit under the hood and return the ID of the hook that was created.
    // Pulumi retains this ID and gives it to us when we need to update or delete the hook.
    create = async (inputs: any) => {
        const octokit = require("@octokit/rest")();
        octokit.authenticate({
            type: "token",
            token: githubToken,
        });

        const res = await octokit.repos.createHook({
            owner: inputs["owner"],
            repo: inputs["repo"],
            name: "web",
            events: ["pull_request"],
            config: {
                content_type: "json",
                url: inputs["url"],
                secret: hookSecret,
            },
        });

        if (res.status !== 201) {
            throw new Error(`bad response: ${JSON.stringify(res)}`);
        }

        // The engine expects that the ID property is a string.
        return {
            id: `${res.data.id}`,
        };
    }

    update = async (id: pulumi.ID, olds: any, news: any) => {
        const octokit = require("@octokit/rest")();
        octokit.authenticate({
            type: "token",
            token: githubToken,
        });

        const res = await octokit.repos.editHook({
            hook_id: id,
            owner: news["owner"],
            repo: news["repo"],
            events: ["pull_request"],
            config: {
                content_type: "json",
                url: news["url"],
            },
        });

        if (res.status !== 200) {
            throw new Error(`bad response: ${JSON.stringify(res)}`);
        }

        return {}
    }

    delete = async (id: pulumi.ID, props: any) => {
        const octokit = require("@octokit/rest")();

        octokit.authenticate({
            type: "token",
            token: githubToken,
        });

        const res = await octokit.repos.deleteHook({
            hook_id: id,
            owner: props["owner"],
            repo: props["repo"],
        });

        if (res.status !== 204) {
            throw new Error(`bad response: ${JSON.stringify(res)}`);
        }
    }
}

interface GitHubWebhookResourceArgs {
    url: pulumi.Input<string>;
    owner: pulumi.Input<string>;
    repo: pulumi.Input<string>;
}

class GitHubWebhookResource extends dynamic.Resource {
    constructor(name: string, args: GitHubWebhookResourceArgs, opts?: pulumi.ResourceOptions) {
        super(new GithubWebhookProvider(), name, args, opts);
    }
}
```

With this new dynamic resource, registering the hook itself becomes
easy:

```typescript
new GitHubWebhookResource("hook-registration", {
    url: api.url,
    owner: "ellismg",
    repo: "testing",
});
```

Before running `pulumi update` go and manually delete the hook
registration on GitHub. Now, when you `pulumi update` you'll see the new
resource created:

    Updating stack 'github-hook-blog-dev'
    Performing changes:

         Type                               Name                                   Status      Info
     *   pulumi:pulumi:Stack                github-hook-blog-github-hook-blog-dev  done
     +   └─ pulumi-nodejs:dynamic:Resource  hook-registration                      created

    ---outputs:---
    url: "https://t1vyz1x203.execute-api.us-west-1.amazonaws.com/stage/"

    info: 1 change performed:
        + 1 resource created
          10 resources unchanged
    Update duration: 4.649249758s

And if you look on GitHub, the hook should once again be registered!
Now, if the URL for our handler ends up changing or we destroy our
stack, the hook registration will be updated accordingly. Since our
little program is getting large (~200 lines at this point), let's do a
little more work on our abstraction.

## Building a Component

Pulumi has the concept of a `ComponentResource` which is a resource that
aggregates other resources. Many resources that we interact with day to
day in Pulumi are actually `ComponentResources` (In fact, the API
resource we're using here is itself a component). In another file, we
can create the component resource and move much of our logic into there:

The interesting new code looks like this:

```typescript
export interface GitHubWebhookArgs {
    owner: pulumi.Input<string>;
    repo: pulumi.Input<string>;
    handler: (req: serverless.apigateway.Request, body: any) => Promise<void>;
}

export class GitHubWebhook extends pulumi.ComponentResource {
    public readonly url: pulumi.Output<string>;

    constructor(name: string, args: GitHubWebhookArgs, opts?: pulumi.ResourceOptions) {
        super("github:webhooks:Hook", name, {}, opts);

        const api = new serverless.apigateway.API("hook", {
            routes: [
                {
                    path: "/",
                    method: "POST",
                    handler: async (req, ctx) => {
                        // Compute the HMAC of the body, using `hookSecret` as the key and `sha1` as the algorithm

                        // First, grab the body. It may be base64 encoded, depending on if `req.isBase64Encoded` is set. If so, we
                        // should decode it.
                        let body = req.body;
                        if (req.isBase64Encoded) {
                            body = Buffer.from(body, 'base64').toString();
                        }

                        // Now compute the HMAC.
                        const crypto = await import("crypto");
                        const hmac = crypto.createHmac("sha1", hookSecret);
                        hmac.update(body);

                        const computedSignature = `sha1=${hmac.digest("hex")}`;

                        // Compare the signature that came in with the request to what we computed.
                        if (req.headers['X-Hub-Signature'] === undefined ||
                            !crypto.timingSafeEqual(Buffer.from(req.headers['X-Hub-Signature']), Buffer.from(computedSignature)))
                        {
                            console.log(`error: bad signature ${req.headers['X-Hub-Signature']} !== ${computedSignature}`);
                            return {
                                statusCode: 400,
                                body: "bad signature"
                            }
                        }

                        // Call the handler after parsing the body as JSON:
                        await args.handler(req, JSON.parse(body));

                        return {
                            statusCode: 200,
                            body: ""
                        }
                    },
                },
            ],
        }, {
            parent: this,
        });

        new GitHubWebhookResource(`${name}-registration-${args.owner}-${args.repo}`, {
            owner: args.owner,
            repo: args.repo,
            url: api.url,
        }, {
            parent: this,
        });

        this.url = api.url;
    }
}
```

Here, we've transformed our `createWebhook` method into an actual
`GitHubWebhook` component that manages both the API of the hook as the
hook's registration with GitHub. With this abstraction (and all of this
complexity hidden off in a separate `github.ts` file), the code we focus
on when actually writing our bot is quite small:

```typescript
import * as pulumi from "@pulumi/pulumi";
import { GitHubWebhook } from "./github";

const cfg = new pulumi.Config(pulumi.getProject());
const githubToken = cfg.require("githubToken");

const hook = new GitHubWebhook("hook", {
    owner: "ellismg",
    repo: "testing",
    handler: async (req, body) => {
        if (body.action === "closed" && body.pull_request.merged &&
            body.pull_request.base.user.login === body.pull_request.head.user.login &&
            body.pull_request.base.repo.name === body.pull_request.head.repo.name)
        {
            const octokit = require('@octokit/rest')()
            octokit.authenticate({
                type: 'token',
                token: githubToken
            });

            console.log(`Deleting reference heads/${body.pull_request.head.ref}`);

            await octokit.gitdata.deleteReference({
                owner: body.pull_request.head.user.login,
                repo: body.pull_request.head.repo.name,
                ref: `heads/${body.pull_request.head.ref}`
            });
        }
    },
});

export const url = hook.url;
```

## Going Further

From here, there's a lot of ways we could extend this code. For example,
while we require the configuration value `hookSecret` to be set before
using this abstraction, we could manage this on behalf of the user. To
do so, we could use the dynamic provider to create a special "random"
resource, this resource would generate a new random string when created,
but update calls would not impact the resource. Since Pulumi stores the
state of every resource across invocations in the checkpoint, our random
resource would not need to be backed by any cloud infrastructure. We
could change the shape of the `GitHubWebhook` component to allow
multiple owner/repository pairs to be provided and it would generate a
single AWS API and then multiple `GitHubWebhookResource`'s to register
the same hook across multiple repositories. We could even extend this to
allow registration of both repository and organization level webhooks.
Or instead of hard-coding in the `pull_request` event as the only event
we care about take it as another input property to `GitHubWebhook`.

One of my favorite things about Pulumi is while it is easy to *build*
these abstractions, it's also easy to share them. For example, I've
implemented a few of these ideas to build a framework for our use at
Pulumi. You can find the source on
[GitHub](https://github.com/ellismg/github-webhooks-serverless) and I've
published it as an NPM package at
[`@ellismg/pulumi-github-webhooks`](https://www.npmjs.com/package/@ellismg/pulumi-github-webhooks).
