---
title: "Publishing Approved Creative Assets with Pulumi"
date: 2026-07-30
draft: false
meta_desc: "A practical Pulumi and TypeScript pattern for publishing approved creative assets to a versioned, access-controlled S3 bucket."
category: best-practices
authors:
    - foster-martyn
tags:
    - aws
    - typescript
    - infrastructure-as-code
    - best-practices
---

Creative teams working on advertising concepts, product mockups, or social graphics often hit the same wall: the visuals get produced quickly, but getting an approved version into a stable, traceable storage location is where things slow down. Screenshots get pasted into chat threads, filenames drift, and nobody is quite sure which version of a hero image actually shipped. Infrastructure-as-code does not solve the creative review problem, but it can solve the publishing problem cleanly, and that boundary is worth being explicit about.

## The situation

A typical flow looks like this: someone produces several visual candidates for a campaign, a reviewer picks one, and that approved asset needs to land somewhere reliable — versioned, access-controlled, and easy to reference from a website, ad platform, or design system. The generation step (however the image was made) is inherently unpredictable and iterative. The publishing step, once an asset is approved, should be boring, repeatable, and auditable. Treating both steps as one blob of manual work is what causes confusion later.

A useful pattern is to draw a hard line: anything before approval is a creative process, and anything after approval is an infrastructure process. Pulumi fits naturally on the infrastructure side of that line.

## Reasoning and practical steps

The goal is a small, focused Pulumi program that manages a versioned S3 bucket dedicated to approved creative output, with a predictable key structure and least-privilege access. Versioning matters here because creative assets get replaced — a logo gets tweaked, a headline changes — and being able to roll back to a prior approved version without guesswork is valuable.

A minimal TypeScript program might look like this:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const assetsBucket = new aws.s3.BucketV2("approved-creative-assets", {
 tags: { purpose: "approved-creative-assets" },
});

new aws.s3.BucketVersioningV2("assets-versioning", {
 bucket: assetsBucket.id,
 versioningConfiguration: { status: "Enabled" },
});

const publishRole = new aws.iam.Role("asset-publisher", {
 assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({
 Service: "lambda.amazonaws.com",
 }),
});

new aws.iam.RolePolicy("asset-publisher-policy", {
 role: publishRole.id,
 policy: assetsBucket.arn.apply((arn) =>
 JSON.stringify({
 Version: "2012-10-17",
 Statement: [
 {
 Effect: "Allow",
 Action: ["s3:PutObject", "s3:GetObject"],
 Resource: `${arn}/campaigns/*`,
 },
 ],
 })
 ),
});

export const bucketName = assetsBucket.bucket;
```

A few decisions here are deliberate. The bucket is scoped to a single purpose rather than shared with other infrastructure, which keeps access policies simple. Versioning is enabled at the infrastructure layer so rollback is a storage-native capability rather than something teams have to build by hand. The IAM policy is scoped to a `campaigns/` prefix, which supports a key naming convention such as `campaigns/{campaign-id}/{asset-name}-v{n}.png`, making it straightforward to trace an asset back to its campaign and revision without a separate database.

The publishing step itself — actually uploading the approved file — is intentionally left outside this program. It can be a small script, a CI job triggered by a pull request merge, or a manual `aws s3 cp` run by whoever owns the approval. Pulumi's job ends at defining the bucket, its versioning behavior, and who is allowed to write to it. That separation keeps the infrastructure code simple and testable, and it avoids embedding business logic about approvals into infrastructure definitions where it does not belong.

## Where a generation tool fits in

Before any of this infrastructure matters, someone has to produce the candidate visuals in the first place. That step is completely decoupled from the Pulumi program above, which is useful because it means the choice of generation tool has no bearing on how the publishing pipeline is built. Teams exploring rapid concept variations — different product mockup angles, alternate storyboard frames, or quick social graphic drafts — sometimes use a prompt-based image tool for that early exploration phase before anything reaches a reviewer. [Nano Banana 2 Lite](https://nanobanana2lite.tools/) is one such option: a third-party, independent site built around prompt-based image creation and object-reference workflows for early-stage visual drafts. It is worth noting that it is not affiliated with Google or DeepMind despite the naming similarity to other tools in this space; it operates as its own separate service. Whatever tool is used at this stage, the output only enters the Pulumi-managed pipeline once it has been reviewed and approved by whoever owns that decision.

## Limitations and a useful conclusion

This pattern is intentionally narrow, and it is worth being honest about what it does not do. It does not enforce content approval — nothing here stops an unapproved file from being uploaded if someone has the right permissions, so approval still depends on process discipline or a separate CI gate that checks metadata before allowing a write. It does not replace a full digital asset management system; there is no built-in search, tagging UI, or preview generation, only a versioned bucket and a naming convention. It also does not address image moderation, licensing checks, or brand compliance review, all of which remain human or separately tooled responsibilities. Versioning adds storage cost over time, since every replaced object keeps its prior versions unless a lifecycle rule is added to expire old ones, which is a reasonable follow-up addition for teams with high asset turnover.

What this pattern does provide is a clear, small, and auditable boundary: creative exploration happens wherever it makes sense, approval happens through whatever process a team already trusts, and once an asset is approved, Pulumi guarantees it lands in a predictable, versioned, access-controlled location every time. That kind of boundary tends to age well, because it does not try to solve creative judgment with infrastructure code — it just makes sure the infrastructure side stays consistent no matter how the creative side evolves.
