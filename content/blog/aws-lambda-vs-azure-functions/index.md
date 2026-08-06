---
title: "AWS Lambda vs Azure Functions: What Changes When You Deploy"
allow_long_title: true
h1: "AWS Lambda vs Azure Functions: What Changes When You Deploy"
date: 2026-07-31T06:00:00-07:00
draft: true
meta_desc: "The Azure equivalent of AWS Lambda is Azure Functions. The concept mapping is mostly boring. Deployment is where the two models actually diverge."
authors:
    - adam-gordon-bell
tags:
    - azure
    - dotnet
    - serverless
category: tutorials
---

*I built a dad-joke API on Azure Functions for a recent C# user-group workshop, in Bicep and in Pulumi, and the interesting difference wasn't where I expected it.*

<!--more-->

If you know Lambda and someone just handed you an Azure subscription, most of what you need is a translation table. Handler, trigger, environment variables, logs, IAM. The names change, the shapes mostly hold, and you can be productive in an afternoon.

Then you go to deploy, and none of the translation table helps. Azure isn't missing anything. The two clouds just drew the line between "infrastructure" and "code" in different places, and the getting-started guides don't mention it.

So: the translation table first, because you need it. Then the part that actually cost me an afternoon.

## What's the Azure equivalent of AWS Lambda?

**Azure Functions is the Azure equivalent of AWS Lambda.** Both are event-driven, serverless compute: you write a handler, attach a trigger, and the platform runs it on demand and scales it to zero when nothing is calling. You'll sometimes see people search for "Azure Lambda." There is no such product, and Azure Functions is what they mean. If you're looking for the AWS Lambda equivalent in Azure, that's it: the Lambda equivalent in Azure is a Function, running inside a Function App.

One structural difference matters from the start. In Lambda, the function is the unit of everything: deployment, permissions, scale. In Azure, the unit is the **Function App**, a container that holds one or more Functions and owns the deployment package, the app settings, and the managed identity, and is assigned to a hosting plan. Microsoft says it plainly: "the unit of deployment for functions in Azure is the function app. You deploy all functions in a function app at the same time, usually from the same deployment package."

Almost every rough edge in the table below is a consequence of that one sentence.

## AWS Lambda vs Azure Functions: the concept mapping

Most Azure Functions vs AWS Lambda comparisons stop at this table. The rows that matter are the ones that say "no equivalent."

The table assumes the **Flex Consumption** plan, which is what Microsoft now recommends for new serverless apps. Several rows differ on Premium, Dedicated, or the legacy Consumption plan, and I've flagged the ones that bite.

| AWS Lambda | Azure Functions |
|---|---|
| Lambda function (the handler + its trigger) | Function |
| Lambda function (the deployable, permissioned, configured resource) | **Function App** — one package, one identity, one set of settings, shared by every Function in it |
| Event sources (API Gateway, SQS, SNS, Kinesis, DynamoDB Streams, S3, EventBridge Scheduler) | Triggers (HTTP, Queue Storage / Service Bus, Event Grid, Event Hubs, Cosmos DB change feed, Blob Storage, Timer) |
| *No equivalent* — you call the AWS SDK from inside the handler | **Input and output bindings** — declarative connections to other services that replace SDK plumbing |
| Layers | *No equivalent.* Shared dependencies go in the deployment zip, in NuGet/npm/pip, on mounted storage, or in a container image (containers need Premium, Dedicated, or Container Apps — not Flex Consumption) |
| Execution role (IAM role + policies, **per function**) | Managed identity + Azure RBAC role assignments, **per Function App** |
| Environment variables (per function) | Application settings (per Function App, surfaced to code as env vars) |
| Secrets Manager / SSM Parameter Store | Azure Key Vault, Azure App Configuration |
| CloudWatch (metrics, logs, alarms) + X-Ray (tracing) | Azure Monitor, with Application Insights as its APM/tracing feature and Log Analytics as the log store |
| Concurrency and scaling knobs | Hosting plan: Flex Consumption, Premium, Dedicated, Container Apps (Consumption is now legacy). Per-instance concurrency is **configurable and greater than 1**, where Lambda's is always 1 |
| Reserved concurrency | *No equivalent.* Isolate the function into its own Function App and cap that app's scale-out |
| Provisioned concurrency | "Always ready" / pre-provisioned instances (Flex Consumption, Premium) |
| Versions and aliases (immutable, per-function, ARN-addressable) | *No direct equivalent.* Deployment slots (not available on Flex Consumption) or CI/CD-driven blue-green (Flex Consumption instead offers rolling site updates for zero-downtime deploys, in preview) |
| 900-second max timeout; 128–10,240 MB memory in 1 MB increments | Flex Consumption defaults to 30 minutes with no documented hard maximum; instance sizes are 512 / 2,048 / 4,096 MB. **HTTP-triggered functions still have to answer within 230 seconds** — that's the Azure Load Balancer idle timeout, not the function timeout, and still eight times more generous than API Gateway's 29-second default integration timeout |

Three rows resolve to "no equivalent," and they all cluster around the same thing: Lambda's isolation boundary is the function, Azure's is the app. If you want per-function least privilege, per-function concurrency limits, or per-function versioning on Azure, the answer is to split into more Function Apps. That's the real migration cost: you're redrawing app boundaries, not renaming fields.

One Azure instance handles several simultaneous executions at a time, where Lambda's is always one. Any instance-count or memory-sizing intuition you carried over from Lambda is wrong by a factor you'll have to measure.

## Triggers: what an event source looks like in Azure

Azure Functions triggers map cleanly onto Lambda event sources. Here's the HTTP-triggered function from the workshop, the whole handler signature:

```csharp
[Function("GetJoke")]
public async Task<HttpResponseData> GetJoke(
    [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post", Route = "joke")] HttpRequestData req)
{
    string? keywords = req.Query["keyword"] ?? req.Query["keywords"];
    // ...
}
```

If you've written a Lambda behind API Gateway, nothing here should surprise you. The trigger is an attribute on the parameter rather than a separate event-source-mapping resource, the route is declared inline, and `AuthorizationLevel.Anonymous` is the "no auth in front of this" setting. Swap `HttpTrigger` for `QueueTrigger`, `TimerTrigger`, or `EventGridTrigger` and the shape holds.

Azure Functions bindings are the half with no Lambda counterpart. In Lambda you pull the AWS SDK into your handler to read from a queue or write to a table. In Azure, an output binding is another attribute, and the runtime does the write. It's the one place in the table where Azure gives you something you'll miss going the other direction.

## Where the models actually diverge: deploying your code

**AWS pulled code packaging into the IaC workflow. Azure kept it in a separate push.** Both clouds can do both things. The difference is which side of the seam the packaging sits on, and the seam is the part you end up maintaining.

Start with the history, because AWS was not born with this solved.

Raw CloudFormation has exactly the hole people complain about in ARM. `AWS::Lambda::Function`'s `Code` property can only point at an artifact the service can already fetch: a .zip in S3 (`S3Bucket`/`S3Key`), or a container image in ECR (`ImageUri`). It never takes a local path. There's an inline escape hatch, `ZipFile`, and it's deliberately narrow: Node.js and Python only, a single file that CloudFormation names `index`, a 4 MB cap on the resulting zip, and no way to bring your own dependencies. It exists for glue code and custom resources, not for shipping an application. Getting your code to S3 is a separate step before the deploy: your own script, your CI job, or AWS's own `aws cloudformation package`, which rewrites the template's local paths into `s3://` URIs.

AWS's answer wasn't to change CloudFormation. It was to put a build step in front of it. SAM lets you write `CodeUri: ./src` against local source; on `sam deploy`, the SAM CLI zips it, uploads it to a managed S3 bucket, and rewrites `CodeUri` to the resulting `s3://` URI before CloudFormation ever sees the template. CDK does the same from code: `lambda.Code.fromAsset('./handler')` points at a local directory, and `cdk deploy` publishes it to the bucket that `cdk bootstrap` created, keyed by content hash. The S3 hop never went away. AWS's own SAM docs still open by conceding that "CloudFormation requires that your local files are first uploaded to an accessible AWS service." What went away was your having to own it.

Azure drew the line at the ARM control plane instead. Bicep can *point* a Function App at a package. `Microsoft.Web/sites/extensions` with a `ZipDeploy` or `onedeploy` child resource takes a `packageUri`, and the app setting `WEBSITE_RUN_FROM_PACKAGE` takes either `1` or a URL. What Bicep cannot do is *produce* that package. It can't build your project, can't zip it, and can't upload the artifact. Microsoft's guidance is explicit that the `packageUri` "must be a location that Functions can access," and suggests blob storage with a SAS. Something outside the template has to have already compiled, zipped, and pushed the thing.

One plan caveat, since the table above assumes Flex Consumption: the workshop runs on the legacy Linux Consumption plan (Y1), because that's the plan where `WEBSITE_RUN_FROM_PACKAGE` with a package URL applies. On Flex Consumption the mechanism differs. The package goes to a deployment storage container and the ARM child resource is `onedeploy`, not `ZipDeploy`. The boundary is identical either way: Bicep can point at a package, it still can't produce one.

You can escape-hatch out of this with `Microsoft.Resources/deploymentScripts` — Bicep will spin up an Azure Container Instance, run your shell script, and tear it down. But look at what that is: a shell script wearing a declarative costume, with a container instance *and a storage account* the service spins up on your behalf and bills you for, a user-assigned managed identity if the script needs to talk to Azure, a `retentionInterval`, a `cleanupPreference`, and its own error-code table. It proves the boundary rather than erasing it.

And before anyone says "just use `azd`" — that's a fair rebuttal and it works. But `azd`'s provision stage *is* your `infra/main.bicep`, and its deploy stage isn't. `azd deploy` pushes packaged artifacts through the Functions deployment API. SAM and CDK also upload out of band, so that alone isn't the difference. The difference is what lands in the template afterward. On AWS the artifact *reference* becomes part of the stack's desired state: CloudFormation diffs the S3 key, updates the function on it, and rolls it back with the stack. `azd deploy`'s push leaves nothing behind in the ARM deployment to diff or roll back. `func azure functionapp publish`, `az functionapp deploy`, the GitHub Action, and `azd deploy` all end up on the same publish data plane: zip deploy on Consumption, Premium, and Dedicated, OneDeploy on Flex Consumption. Different endpoint, same seam. `azd` is the polished front door, not a different mechanism. The boundary runs straight through the middle of it: infra is declarative, code is a push, and `azure.yaml` is the seam.

### What the seam costs

That's the abstract version. Here's mine, from the workshop repo.

`src/05-bicep/main.bicep` is 119 lines and it's fine. Storage account, Azure OpenAI account, model deployment, Linux consumption plan, Function App. It takes the package as a parameter:

```bicep
@description('The SAS URL for the function app package zip file')
param functionPackageSasUrl string
```

…and hands it to the app:

```bicep
{
  name: 'WEBSITE_RUN_FROM_PACKAGE'
  value: functionPackageSasUrl
}
```

Where does that SAS URL come from? `src/05-bicep/deploy.sh`, 128 lines of bash that: create the resource group, `dotnet publish` and `zip` the function, **spin up a throwaway storage account purely to stage the zip**, create a container, upload the blob, generate a SAS URL (branching on `$OSTYPE` because macOS `date` and GNU `date` disagree about how to say "one year from now"), pass that URL into the template as a parameter, and then **delete the throwaway storage account** on the way out.

None of that is Bicep's fault. It's what falls out when the packaging step lives outside the template.

The Pulumi version, `src/04-ai/infra/Program.cs`, is 184 lines of C#. That's not a line-count win. 184 lines in one file against 247 across two is about a quarter fewer, not a rout, and I'd rather make the honest argument. Line count isn't the argument anyway. Half of the Bicep deployment lives in bash: the build, the staging account, the SAS minting, the cleanup, all in a language the IaC tool can't see, can't preview, and can't roll back. `az deployment group create` has no idea that storage account ever existed.

In the Pulumi program, the build is a resource:

```csharp
var publish = new Command("publish-function", new CommandArgs
{
    Create = "rm -rf bin/publish bin/function-app.zip && dotnet publish -c Release -o bin/publish && (cd bin/publish && zip -qr ../function-app.zip .)",
    Dir = "../function",
    Triggers = /* every .cs and .csproj file, plus its last-write time */
});
```

…and the upload is a resource that depends on it:

```csharp
var packageBlob = new Blob("function-app.zip", new BlobArgs
{
    ResourceGroupName = rg.Name,
    AccountName = stg.Name,
    ContainerName = container.Name,
    Source = publish.Stdout.Apply(_ => (AssetOrArchive)new FileAsset("../function/bin/function-app.zip")),
    ContentType = "application/zip",
}, new CustomResourceOptions { DependsOn = { publish } });
```

One detail worth stealing: I shell out to `zip` rather than using Pulumi's built-in `FileArchive`, because `FileArchive` doesn't preserve Unix file permissions and the Functions host needs the published files executable. That took a while to find. The `Triggers` array is how the build re-runs when source changes and not otherwise.

That last part is the whole point of putting the build in the graph. A cold `pulumi up` takes 96 seconds and creates ten resources. Run it again with nothing changed and it reports `10 unchanged` in four seconds — no rebuild, no re-upload, no app restart, because the build is a node in the dependency graph and its inputs didn't move. The bash version has no such notion. Every run publishes, zips, uploads, and mints a fresh SAS, so the app setting changes and the app bounces whether or not you touched a line of C#.

The SAS comes from `ListStorageAccountServiceSAS.Invoke(...)` in the same program, and feeds `WEBSITE_RUN_FROM_PACKAGE` directly. There is no throwaway storage account, because the real one is already a resource in the graph. There is no `$OSTYPE` branch, because there's no `date` call. And nothing needs cleaning up by hand: `pulumi destroy` already knows about everything that got made.

Both versions end up at the same place, an Azure Function App reading a zip out of blob storage via `WEBSITE_RUN_FROM_PACKAGE`. Only one of them can tell you what it did.

## Migrating a real function

Concretely, to migrate that dad-joke API from AWS Lambda to Azure Functions, here's the AWS-to-Azure migration checklist:

1. **Handler → Function.** The `[HttpTrigger]` attribute replaces the API Gateway event-source mapping. The request object changes shape (`HttpRequestData` instead of `APIGatewayProxyRequest`), the business logic doesn't.
2. **Group your handlers into Function Apps deliberately.** This is the decision Lambda never made you make. Functions that need different permissions, different scale limits, or different release cadence belong in different apps.
3. **Execution role → managed identity plus role assignments.** Remember the scope change: the identity is on the app, so everything in that app shares it.
4. **Environment variables → application settings.** Same idea, app-scoped, and secrets should go to Key Vault with the managed identity reading them rather than sitting in settings.
5. **Decide where packaging lives before you write the first template.** Moving it later means rewriting both the template and whatever is calling it. This is the one that cost me the afternoon.

## Get started

The workshop code is in the [pulumi/workshops](https://github.com/pulumi/workshops) repo under `az-csharp-app`, staged so you can start anywhere. To try it out:

1. Clone the repo:

   ```bash
   git clone https://github.com/pulumi/workshops
   ```

2. Move into the finished stage:

   ```bash
   cd workshops/az-csharp-app/src/04-ai/infra
   ```

3. Deploy it:

   ```bash
   pulumi up
   ```

4. Ask for a joke:

   ```bash
   curl "$(pulumi stack output jokeEndpoint)"
   ```

You'll need an Azure subscription with access to Azure OpenAI, the Pulumi CLI, and the .NET 8 SDK. `src/01-cli` through `src/04-ai` build up in stages. `src/05-bicep` is the Bicep-plus-bash version of the same infrastructure, if you want to run both and compare. The workshop uses account keys and a SAS to keep the stages small; in anything real, use the Function App's managed identity for storage, OpenAI, and the package fetch.

For the building blocks, see the [Azure Native provider](https://www.pulumi.com/registry/packages/azure-native/) in the Pulumi Registry, and the [Command provider](https://www.pulumi.com/registry/packages/command/) for the build step. If you're coming from existing templates, [arm2pulumi](https://www.pulumi.com/arm2pulumi/) will convert them.

I built this for a C# user group that mostly came from AWS, and the translation table wasn't the part anyone had questions about afterward. Run both versions. The deploy script tells you more about the two platforms than any comparison chart does.
