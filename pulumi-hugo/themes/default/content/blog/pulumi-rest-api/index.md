---
title: "Announcing the Pulumi REST API"
date: 2021-09-20
meta_desc: "The Pulumi REST API lets you manage projects, stacks, cloud resources, policies, and more, all with a simple, programmatic web interface."
meta_image: rest-api.png
authors:
    - joe-duffy
tags:
    - pulumi-news
    - rest-api
---

Pulumi was designed to be highly extensible from the outset. That includes core languages and cloud providers, of course, but our community is often using Pulumi as a central part of building and connecting their cloud engineering and automation systems, using features like the Automation API. Today we are happy to announce the next major step in enabling these kind of scenarios: the Pulumi REST API. This REST API offers functionality to manage projects and stacks, cloud resources, policies, and more. It has, in fact, been there all along, powering the Pulumi SDK, CLI, and Console behind the scenes, although we haven't fully documented or supported it until now. That changes today! We've already seen some amazing things built with this API and we're excited to see what you build with it too.

<!--more-->

## Overview

Pulumi provides a lot of functionality out of the box. But we understand that modern cloud engineering systems are highly interconnected and complex, and that many teams have unique needs. Therefore, we set out to design the Pulumi platform to be extensible in many ways. The Pulumi client (SDK, CLI, etc) was designed to interoperate with the Pulumi server and, though the SDK has a specific set of needs, this protocol has always been designed to be public and easy to consume for custom scenarios and integrations.

## Manage Stacks, Updates, Teams, and More

The Pulumi REST API is available at <https://api.pulumi.com> and includes functionality to interact with and manipulate any kind of metadata managed by Pulumi. That includes:

* **Projects and Stacks**
    * List all projects and stacks for a user or organization
    * Get metadata about a specific stack, including stack config and resource states
    * Transfer a stack between a user and/or organization
    * Delete a stack
    * Manage stack tags
* **Previews and Updates**
    * List all stack previews and updates
    * Get the status of an ongoing or past stack preview or update
    * List the detailed events occurring during a stack's update, such as the resource changes, policy checks, or stdout/stderr messages
* **Organizations**
    * List or manage users of an organization
    * Manage RBAC teams and user roles within an organization
    * List or manage access tokens within an organization
* **Audit Logs**
    * Get audit log events as JSON
    * Export audit log events as CSV or CEF

Authentication and authorization is governed by the Pulumi identity and RBAC systems. As we add functionality to the Pulumi SDK and Service, we are committed to shipping and supporting the underlying REST APIs. If it's used in our web console or CLI, we want it to be available to so you can add custom features and functionality.

[Read complete details about the REST API here]({{< relref "/docs/reference/service-rest-api" >}}) or keep reading for examples and scenarios.

## The REST API for Cloud Engineering

We have already seen Cloud Engineering teams using the Pulumi REST API to build all sorts of custom functionality. These new capabilities are especially powerful when used in combination with the [Automation API]({{< relref "/automation" >}}), which lets you use infrastructure as code as a library embedded into a larger system, and [Webhooks]({{< relref "/docs/intro/pulumi-service/webhooks" >}}), which lets you invoke your own REST API in response to a Pulumi event such as a stack update.

Examples of scenarios we've seen include:

* Custom dashboards, including "click to deploy".
* Programmatically getting stack outputs to integrate with other automation needs.
* Making more metadata-driven Automation API projects that consume project, stack, config, resource, or other service state to make provisioning decisions.
* Exposing a full set of projects and stacks into other systems, such as a portal for managed service providers.
* Querying resource metadata to find stacks containing resources with certain properties (such as, for example, in response to a security incident).
* Managing teams, users, and access tokens for specific automation needs.
* Pulling audit logs into other systems (e.g., SIEM).
* Enforcing certain policies such as ensuring that stack tags are applied consistently.
* Performing automated resource drift and remediation.

With the Pulumi cloud engineering platform, if you can dream it, you can build it!

## Example: Finding Stacks with RDS Databases

Let's take a look at the Pulumi REST API in action. This example will demonstrate querying stacks and resource metadata across an entire organization.

Imagine that there is suddenly a MySQL vulnerability or EOL notice that we need to respond to. We use Amazon RDS and would like to query our entire organization to find projects and stacks that currently have RDS databases deployed using version 5.6 of MySQL. Thankfully the Pulumi REST API makes all metadata about all of my cloud projects and stacks &mdash; across all clouds &mdash; available for easy querying and inspection. So a dozen lines of bash will do the trick!

The first step is to [generate an API access token]({{< ref "/docs/intro/pulumi-service/accounts#access-tokens" >}}). The Pulumi Service lets you manage many access tokens (the same as what's used for `pulumi login`) and it's easiest to just create one specific to this project's purpose. This will let us revoke that token after we're done and know that there is no lingering access.

To do that, go to <https://app.pulumi.com/account/tokens> (or click your avatar in the upper right and go to Settings, where you'll see Access Tokens on the left-hand nav):

![Access Tokens](access-tokens-1.png)

Click the Create Token button. That will pop a box that lets us enter a description:

![Create a Token](access-tokens-2.png)

This then gives us the access token text. We need to copy it and put it somewhere for safekeeping, because once we leave this page, we won't be able to recover it:

![Access Token Created](access-tokens-3.png)

We will use this token for all API calls and the token dictates what authorization we will have to perform actions within a given user or organization account. As we will see, all APIs pertain to given permission scopes, much like GitHub, which will determine the permissions granted. If we're using `curl`, for example, we will pass the `"Authorization: token XYZ"` header, with `-H`, as [described in the Authorization section of the REST API documentation]({{< relref "/docs/reference/service-rest-api/#authentication" >}}).

If we forget to do that, we'll receive a 4xx error. For instance, 401:

```bash
{"code":401,"message":"Unauthorized: No credentials provided or are invalid."}
```

To test that this is working, let's curl the /api/user endpoint, which gives us information about the currently "logged in" user (i.e., the user to which the token we're using belongs):

```bash
$ curl \
    -H "Authorization: token pul-fa..REDACTED..fa" \
    https://api.pulumi.com/api/user
{"githubLogin":"joeduffy","name":"Joe Duffy","email":"joe@pulumi.com",...}
```

OK, looks like everything's working! Let's get back to our scenario of finding unpatched RDS instances. To do that, well use a combination of `bash`, `curl`, and `jq` (payloads are JSON).

Here is the full script. We set up the auth header as noted above, enumerate all stacks in the `acmecorp` organization, export the stack's metadata including its resources, and then check to see if there are any RDS instances with `"mysql"` version `"5.7"` that we need to patch:

```bash
# Set up our auth token info.
export AUTH_HEAD="Authorization: token $PAPI_TOKEN"
export ORG_NAME=acmecorp

# Enumerate all stacks in our organization.
for stack in $(
    curl -s -H "$AUTH_HEAD" \
            https://api.pulumi.com/api/user/stacks?organization=$ORG_NAME |
            jq -c '.stacks[]'); do
    ORG=$(echo $stack | jq -r '.orgName')
    PROJ=$(echo $stack | jq -r '.projectName')
    STACK=$(echo $stack | jq -r '.stackName')

    # Query each stack to see if we have RDS instances.
    RDS_INSTANCES=$(curl -s -H "$AUTH_HEAD" \
        https://api.pulumi.com/api/stacks/$ORG/$PROJ/$STACK/export |
        jq -c '.deployment?.resources[]? | select (.type == "aws:rds/instance:Instance")')
    if [[ ! -z $RDS_INSTANCES ]]; then
        for rds in $RDS_INSTANCES; do
            # For each RDS instance, warn on any instance that is 'mysql'
            # version '5.7', and error out so we can patch our instances!
            URN=$(echo $rds | jq -r '.urn')
            ENGINE=$(echo $rds | jq -r '.engine')
            ENGINE_VERSION=$(echo $rds | jq -r '.engineVersion')
            if [[ "$ENGINE"="mysql" && "$ENGINE_VERSION"="5.7" ]]; then
                >&2 echo -e "error: vulnerable MySQL 5.7 RDS instance found:"
                >&2 echo -e "    URN=$URN"
                >&2 echo -e "    ORG/PROJ/STACK=$ORG/$PROJ/$STACK"
                >&2 echo -e "    DETAILS=$rds"
            fi
        done
    fi
done
```

Now all we need to do is generate a token, set our `PAPI_TOKEN` environment variable to contain it, and run this script &mdash; voila, all of our vulnerable RDS databases will be revealed. Now we can go update those stacks, perhaps programmatically with the [Automation API]({{< relref "/automation" >}}), and then possibly even [write a Policy as Code rule]({{< relref "/crossguard" >}}) to prohibit new 5.6 instances from getting created in the future.

## Give It a Try Today

As we have seen, the Pulumi REST API gives us easy access to projects, stacks, cloud resources, teams, and more. It is now generally available to all users of the Pulumi Service, both free and paying customers. To give it a try today, [sign up for your free account now](https://app.pulumi.com/signup), give our [Getting Started guide]({{< relref "/docs/get-started" >}}) a try, and then check out the [Pulumi REST API documentation]({{< relref "/docs/reference/service-rest-api" >}}).

We can't wait to see the powerful automation you build for your team using the Pulumi REST API! Have fun spelunking in the cloud.
