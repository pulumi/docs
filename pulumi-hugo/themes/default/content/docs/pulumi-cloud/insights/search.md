---
title_tag: "Pulumi Insights: Resource search"
meta_desc: Documentation and query syntax for the Pulumi Insights search feature.
title: Resource search
h1: Resource search
menu:
  pulumicloud:
    parent: insights
    weight: 1
aliases:
  - /docs/intro/insights/search/
---

Resource Search allows you to explore your resources, stacks and projects in detail.

## Query Syntax

Resource Search supports a rich query language, described below.

### Simple Queries

The default search behavior is to return resources that match all terms in your query based on their name, URN, stack, or project.

For example, a query like

> bucket

will return resources having [types][types] like `aws:s3/bucket:Bucket` or `aws:s3/bucketobject:BucketObject`. It will also return resources in stacks named "bucket" or projects named "my-cool-bucket".

Similarly, a query for

> production

will return resources to belonging to stacks named "production".
It will also include any resources with "production" anywhere in its name.

A resource will only be returned if it matches all terms in the query.
If you search for

> foo bar

a resource named "foo" in the "bar" stack will be returned, but a resource only named "bar" will not be returned.

### Field Queries

The default search behavior is helpful for preliminary exploration but is often too broad for finer analysis.
To more precicesly control _how_ your queries match resources, you can explicitly limit part or all of your query to match specific fields.

For example, searching `name:production` will only return resources that include "production" in their [logical name](/docs/concepts/resources/names/#logicalname).

In general, any column visible in the UI can be queried as a field by taking the lowercase column name and adding a `:` followed by a query term.
The colon cannot be followed by whitespace.

The complete list of available fields is below.

#### created

The UTC time when the resource was created.

Resources created _or modified_ with CLI versions below 3.60 _do not_ have `created` set.

Examples:

- _created:2023-03-31_
- _created:2023-03-31T01:02:03.456_
- _created:[2023-01-01 to 2023-03-31]_
- _created:>=2023-01-01_

#### custom

Whether the resource is a CustomResource.

Examples: _custom:true_ | _custom:false_

#### delete

Whether the resource is marked for deletion in the next update.

Typically indicates a resource that was not cleaned up due to an error.

Examples: _delete:true_ | _delete:false_

#### dependency

The [URN][urn] of another resource this resource explicitly or implicitly [depends on](/docs/concepts/resources#dependson).

A resource can have multiple dependencies. When querying, `dependency:foo` returns resources with any dependency with a URN matching `foo`.

Examples:

- _dependency:access-logs_
- _dependency:urn:my-org:my-stack::my-app::aws:s3/bucket:Bucket::access-logs_

#### id

The [physical name](/docs/concepts/resources/names/#autonaming) of the resource, as assigned by the resource’s provider. May not be set if the resource is pending creation.

Example: _id:my-bucket-d7c2fa0_

#### modified

The UTC time when the resource's state was last modified during an update, refresh or import.

Stacks modified with CLI versions below 3.60 record this for all resources as the time of the stack operation, regardless of whether the resource was modified.
After CLI version 3.60 the resource's modified time is only updated when the resource's state is modified.

Examples:

- _modified:2023-03-31_
- _modified:2023-03-31T01:02:03.456_
- _modified:[2023-01-01 to 2023-03-31]_
- _modified:>=2023-01-01_

#### name

The [logical name](/docs/concepts/resources/names/#logicalname) of the resource.

Typically the first parameter provided to the resource when it was instantiated.

Example: _name:my-bucket_

#### package

The package component of the resource's [type][types].

This is `aws` for a resource of type `aws:s3/bucket:Bucket`.

Examples:

- _package:aws_
- _package:aws-native_
- _package:gcp_
- _package:pulumi_
- _package:random_

#### parent.urn

The [URN][urn] of the resource’s parent, if it has one.

Examples:

- _parent.urn:app-production_
- _parent.urn:urn:myorg:mystack::app::pulumi:pulumi:Stack::app-production_

#### pending

The state of the resource if it is pending.

Typically indicates an operation that was interrupted due to an error, possibly needing manual intervention to resolve.

Allowed values: `creating`, `deleting`, `updating`, `reading`, `importing`.

Examples:

- _pending:creating_
- _pending:deleting_
- _pending:updating_
- _pending:reading_
- _pending:importing_

#### project

The project the resource belongs to.

Example: _project:my-cool-repo_

#### protected

Whether the resource is [protected](/docs/concepts/options/protect) from deletion.

Examples: _protected:true_ | _protected:false_

#### provider.urn

The [URN][urn] of the resource's [provider](/docs/concepts/resources/providers/).

Examples:

- _provider.urn:aws::default_5_21_1_
- _provider.urn:urn:myorg:mystack::myproject::pulumi:providers:aws::default_5_21_1::86588ad9_

#### stack

The stack the resource belongs to.

Example: _stack:my-cool-stack_

#### type

The [type][types] of the resource.

Examples:

- _type:LogGroup_
- _type:aws:cloudwatch:LogGroup_
- _type:aws:cloudwatch/logGroup:LogGroup_

#### urn

The [URN][urn] of the resource.

Examples:

- _urn:my-log-group_
- _urn:my-org:my-stack::my-project::aws:cloudwatch/logGroup:LogGroup::my-log-group_

### Exact Matching

Surrounding terms with `"double quotes"` produces an exact match query.

Only resources matching the phrase in quotes _exactly_ (including punctuation and whitespace) will be returned.

An exact match can optionally have a field associated with it.
For example, `stack:"my-cool-stack"`.

### Negation

Terms can be excluded from results by prefixing them with a `-`.

For example, `-foo` will exclude all resources that would normally match a query for `foo`.

Negation can be applied to exact matches and fields. All of `name:-foo`, `name:-"foo"`, and `-"foo bar"` are valid.

Fields can be repeated for multiple exclusions: `name:-foo name:-bar` excludes all resources with names matching `foo` and `bar`.

### Logical Combinations

All terms are implicitly combined with a logical `AND`, but terms can also be combined with `OR`.
For example, `foo OR bar` returns resources that would normally match `foo` as well as resources that would normally match `bar`.

Precedence is simple left-to-write, so `foo bar OR baz` is interpreted as `(foo AND bar) OR baz`. Parentheses are strongly recommended when combining terms with OR to prevent unexpected results. In this case, you can query for `foo (bar OR baz)` if your intent is to match `bar` or `baz`.

Parentheses and `OR` can be combined with negation, exact matches, and field queries like so:

> "S3-bucket" (stack:prod OR stack:dev) project:-sandbox

### Range Queries

The `created` and `modified` fields can be queried for a range of values with `>`, `>=`, `<`, `<=`, and `[a to b]`.
The `[a to b]` form is inclusive on both sides.

For example, resources modified within the first quarter of 2023 (requires CLI 3.XX):

> modified:[2023-01-01 to 2023-03-31]

Ranges can also be one-sided. For example, to query everything modified after January 1, 2023:

> modified:>=2023-01-01

## Advanced Filtering

Expanding the "Advanced filtering" menu shows your results broken down by type, pacakge, stack, and project.
The values shown in each column and the top values for that particular dimension, along with a count of how many resources share that value.

![Resource Search Advanced Filters](../search-advanced.png)

In the example above, the query has been restricted to the "my-stack" stack.

The counts next to each value show that this stack has 18 subnets, and 366 AWS resources in total.

Clicking "Clear filters" will remove all previously selected filters.

## Download a CSV

{{% notes "info" %}}
The CSV Export feature is only available to organizations using the Enterprise and Business Critical editions.

If you don't see it in your organization, [contact sales](/contact?form=sales).
{{% /notes %}}

You can download a CSV with all resources matching your query by clicking the "Download CSV" buttong.

For a complete description of the CSV format returned, see the [Data Export](/docs/pulumi-cloud/insights/export/) documentation.

## API Access

Resources can also be queried programmatically. See the [Pulumi Cloud REST API](/docs/pulumi-cloud/cloud-rest-api#resource-search) for full details of the API endpoint to query resources.

## AI Assist

{{% notes "info" %}}
AI Assist is an experimental feature that lets you use natural-language prompts to generate queries for use with Resource Search.

If you don't see it in your organization, [contact sales](/contact?form=sales).
{{% /notes %}}

Organizations with AI Assist enabled will see an "AI Assist" button to the right of their search bar.

After clicking "AI Assist" you can input a natural language query, for example:

> How many VPCs do I have?

You will then be re-directed to the "Syntax" tab with a pre-populated search query that attempts to answer your question. The search bar will remain empty if it's not able to generate a valid query for your question.

You may need to refine the pre-populated query slightly to capture your intent. For example, if you ask, "How many buckets do I have?" it might give you a query like

> type:"aws:s3/bucket:Bucket"

This isn't accurate if you're using Google Cloud, however. In that case you could modify the query to be

> type:"gcp:storage:Bucket"

or, if you're not sure which type is appropriate, you can use AI Assist again to clarify:

> How many gcp buckets do I have?

You may want to expand the "Advanced fitlering" menu if you are interested in specific resource counts.

You do not need to query AI Assist with English:

![AI Assist](../search-ai.png)

> (type:aws:ec2/instance:Instance OR type:azure:compute:VirtualMachine OR type:gcp:compute:Instance)

## Access Controls

Resource Search is available to all members of an organization, but as a user you are only able to see and query resources that you have [permission](/docs/pulumi-cloud/projects-and-stacks/#stack-permissions) to access.
More specifically:

- Organization admins have access to all resources.
- If an organization has a default permission of read or write, then all users can query all resources.
- If an organization has no default permission, then users can only query resources they have access to via [Stack](/docs/pulumi-cloud/projects-and-stacks/#stack-permissions) or [Team](/docs/pulumi-cloud/access-management/teams/#team-permissions) permissions.

[types]: /docs/concepts/resources/names/#types
[urn]: /docs/concepts/resources/names/#urns
