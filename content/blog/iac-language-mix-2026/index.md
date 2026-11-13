---
title: "IaC language mix in 2026: what public GitHub shows"
date: 2026-11-13
draft: false
meta_desc: "TypeScript leads general-purpose infrastructure as code on public GitHub, with Python second. Counts for Pulumi, AWS CDK, and CDKTF, plus the full method."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - infrastructure-as-code
    - typescript
    - python
category: general
faq_schema: true
social:
    twitter:
    linkedin:
    bluesky:
---

TypeScript is the most common language for infrastructure as code written in general-purpose languages on public GitHub, at about 58% of the 55,916 Pulumi, AWS CDK, and CDKTF project manifests we counted on November 13, 2026. Python is second at about 23%. Go, C#, JavaScript, and Java split the remaining 19%. Below you'll find every query and parsing rule, so you can rerun the study yourself.

<!--more-->

## Key findings

- TypeScript leads in each toolkit we measured: 65.6% of AWS CDK manifests, 68.1% of CDKTF manifests, and an estimated 37.7% of all Pulumi manifests (94.3% of Pulumi's Node.js projects, which we sampled to separate TypeScript from JavaScript).
- Python is the clear second choice for AWS CDK (21.9%) and CDKTF (16.9%), and in Pulumi it is the second most common runtime at 23.8%, with Go third at 18.2%.
- Pulumi manifests are spread across more languages than the other two toolkits. Go and C# together account for 27.9% of Pulumi manifests, against about 4% for AWS CDK.
- Among the formats we counted (HCL, CloudFormation, Bicep, and Pulumi YAML alongside the three toolkits), general-purpose languages are a minority. Depending on how you count HCL, they make up roughly 5% to 9%, and the range is wide because GitHub's search totals are approximate.
- On the package registries, the npm packages are downloaded 2.6 to 3.3 times as often as the matching PyPI packages, which points the same direction as the repository counts.

GitHub's own Octoverse report points the same direction for software in general. [It reports](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) that TypeScript overtook both Python and JavaScript in August 2025 to become the most used language on GitHub.

## How the counts were made

The unit of analysis is a *manifest*: a file that declares which language a project uses. One repository can contain several manifests, and one manifest is not always one deployed project, so every number here counts manifests (or repositories, where noted) and nothing more. All data comes from GitHub code search on public repositories, collected on November 13, 2026 (UTC), against default branches only.

| Toolkit | Query | What the match tells you |
| --- | --- | --- |
| Pulumi | `filename:Pulumi.yaml runtime -org:pulumi` | The `runtime` field names the language. The `pulumi` organization is excluded to keep Pulumi's own examples out. |
| AWS CDK | `filename:cdk.json "app"` | The `app` command reveals the language, for example `npx ts-node` or `python3 app.py`. |
| CDKTF | `filename:cdktf.json "language"` | The `language` field names the language. |
| Terraform and OpenTofu (HCL) | `filename:.terraform.lock.hcl` and `required_providers extension:tf` | Lockfile count is the lower bound for HCL projects. The `required_providers` count is a generous upper bound. |
| CloudFormation | `AWSTemplateFormatVersion extension:yaml`, plus `yml`, `json`, and `template` | Sum of four queries. |
| Bicep | `extension:bicep` | One file per match. |

GitHub caps each search at 1,000 results, so each query was split recursively by file size (`size:lo..hi`) until every bucket held 1,000 results or fewer, then paged 100 results at a time with text matches enabled. Code search allows roughly ten requests per minute, so the Pulumi enumeration took about 35 minutes and the AWS CDK enumeration about an hour. Results were deduplicated by repository and path.

Here is the core of the loop, using the GitHub CLI:

```bash
# Count results in a size bucket (split the bucket if the total exceeds 1000)
gh api -X GET search/code \
    -f q='filename:Pulumi.yaml runtime -org:pulumi size:100..200' \
    -f per_page=1 --jq '.total_count'

# Fetch one page of matches along with the matched text fragment
gh api -X GET search/code \
    -f q='filename:Pulumi.yaml runtime -org:pulumi size:100..200' \
    -f per_page=100 -f page=1 \
    -H "Accept: application/vnd.github.text-match+json" \
    --jq '.items[] | {repo: .repository.full_name, path: .path,
        fragment: ([.text_matches[]?.fragment] | join(" || "))}'
```

Parsing rules:

- **Pulumi:** read the runtime from `runtime: <name>` or from the nested form `runtime:` followed by `name: <name>`.
- **AWS CDK:** `ts-node`, `tsx`, or a `.ts` file means TypeScript. `python` or `.py` means Python. `mvn`, `gradle`, or `java` means Java (checked after Python, so `javascript` is not misread). `dotnet` means C#. `go` means Go. `node` or `.js` means JavaScript. Anything else is "other".
- **Pulumi `dotnet` and `yaml`:** reported as C# and YAML. Runtimes that are not one of the supported languages, such as `bun` or unrecognized values, fall under "other".
- **CDKTF:** take the `language` value as written.

### How TypeScript and JavaScript were separated for Pulumi

Pulumi's `nodejs` runtime runs both TypeScript and JavaScript, so `Pulumi.yaml` alone cannot tell them apart. To split them, one manifest per repository was kept for the 3,496 repositories that have at least one `nodejs` manifest, and 500 repositories were drawn at random with the seed `20261113`. For each, the project directory was listed through the GitHub contents API. A directory containing a `tsconfig.json` or any `.ts` or `.tsx` file (excluding `.d.ts`) counted as TypeScript. A directory with `.js`, `.mjs`, or `.cjs` files and no TypeScript signals counted as JavaScript.

Of the 500 sampled repositories, 464 were TypeScript, 28 were JavaScript, 7 were indeterminate, and 1 could not be fetched. That makes TypeScript 94.3% of the 492 classified repositories, with a 95% Wilson confidence interval of 91.9% to 96.0%. The estimate was applied to all 7,614 `nodejs` manifests, giving about 7,181 TypeScript and 433 JavaScript. Treat these two figures as sample-based estimates.

## Pulumi: Node.js leads, and Python, Go, and C# all have real footprints

The query returned 19,037 manifests across 6,512 repositories.

| Language | Manifests | Share of manifests |
| --- | --- | --- |
| TypeScript (estimated) | 7,181 | 37.7% |
| Python | 4,529 | 23.8% |
| Go | 3,458 | 18.2% |
| C# (`dotnet`) | 1,842 | 9.7% |
| YAML | 799 | 4.2% |
| Java | 296 | 1.6% |
| JavaScript (estimated) | 433 | 2.3% |
| Other or unparsed | 499 | 2.6% |

Counting by repository changes the picture a little, because some repositories hold dozens of manifests. When each repository is assigned its most common runtime (6,495 of the 6,512 repositories had a parseable runtime), `nodejs` accounts for 51.1%, Python for 26.0%, Go for 11.7%, C# for 6.1%, YAML for 2.7%, and Java for 1.4%. Go looks bigger by manifest than by repository, which is consistent with Go repositories that hold many stacks each, though this study did not test that.

## AWS CDK: TypeScript is the default

The `cdk.json` query returned 37,237 manifests in 24,408 repositories.

| Language | Manifests | Share |
| --- | --- | --- |
| TypeScript | 24,416 | 65.6% |
| Python | 8,171 | 21.9% |
| JavaScript | 1,772 | 4.8% |
| Java | 976 | 2.6% |
| C# | 771 | 2.1% |
| Go | 721 | 1.9% |
| Other | 410 | 1.1% |

Vendor sample organizations account for about 10% of public CDK manifests. Excluding the organizations `aws-samples`, `awslabs`, `aws`, `aws-solutions`, `aws-ia`, `cdklabs`, `aws-cdk`, and `aws-quickstart` leaves 33,543 manifests with almost the same mix: TypeScript 66.7%, Python 20.6%, JavaScript 4.8%, Java 2.6%, Go 2.0%, and C# 2.0%.

## CDKTF: small and now deprecated

The `cdktf.json` query found 1,353 manifests in 883 repositories: TypeScript 921 (68.1%), Python 228 (16.9%), Go 100 (7.4%), Java 61 (4.5%), C# 40 (3.0%), and 3 unparsed. HashiCorp's documentation now states that [the Cloud Development Kit for Terraform is deprecated as of December 10, 2025](https://developer.hashicorp.com/terraform/cdktf/develop-custom-constructs/publishing-and-distribution) and is no longer supported or maintained, so these counts describe an installed base that is not growing through the vendor.

## All general-purpose languages combined

Adding the three toolkits together gives 55,916 manifests that declare a language we could classify (AWS CDK "other" and unparsed CDKTF entries are left out).

| Language | Manifests | Share |
| --- | --- | --- |
| TypeScript | 32,518 | 58.2% |
| Python | 12,928 | 23.1% |
| Go | 4,279 | 7.7% |
| C# | 2,653 | 4.7% |
| JavaScript | 2,205 | 3.9% |
| Java | 1,333 | 2.4% |

The TypeScript total includes the estimated 7,181 Pulumi TypeScript manifests. Without any Pulumi data, AWS CDK and CDKTF alone contribute 25,337 TypeScript manifests.

## General-purpose languages against HCL, CloudFormation, and Bicep

To place those numbers in context, the same method counted domain-specific and configuration formats. Each of these is a count of files, so they are not directly comparable with project manifests, and GitHub's totals for large result sets are rounded approximations.

| Format | Count |
| --- | --- |
| General-purpose language manifests (Pulumi, AWS CDK, CDKTF) | 55,916 |
| Terraform lockfiles (`.terraform.lock.hcl`) | 167,424 |
| CloudFormation templates (four extensions summed) | 223,072 |
| Bicep files | 192,768 |
| Pulumi YAML manifests | 799 |
| `required_providers` in `.tf` files (HCL upper bound) | 579,584 |
| OpenTofu `.tofu` files | 4,744 |

Dividing the general-purpose total by the sum of itself, the Terraform lockfile count, CloudFormation, Bicep, and Pulumi YAML gives 8.7%. Using the larger `required_providers` count in place of lockfiles gives 5.3%. Between the two, a fair summary is that general-purpose languages account for somewhere between 5% and 9% of public infrastructure as code files.

That range moved between runs. An earlier run on October 31, 2026 returned a CloudFormation YAML total nearly twice as large as the one on November 13, and produced shares of 7.3% (lockfile basis) and 4.6% (`required_providers` basis). GitHub's search totals for very large result sets are estimates, so treat these shares as a rough band and ignore the decimal places.

## Cross-checks from package registries

Public download counts offer a second view. Over the 30 days ending November 12, 2026 for npm (and the most recent 30-day window on PyPI Stats, fetched on November 13), the totals were:

| Package pair | npm downloads | PyPI downloads | npm to PyPI ratio |
| --- | --- | --- | --- |
| `@pulumi/pulumi` and `pulumi` | 18,251,597 | 6,576,782 | 2.8 |
| `@pulumi/aws` and `pulumi-aws` | 11,832,070 | 4,577,157 | 2.6 |
| `aws-cdk-lib` (both registries) | 23,914,591 | 8,003,982 | 3.0 |
| `cdktf` (both registries) | 1,211,738 | 370,945 | 3.3 |

Download counts include CI runs, mirrors, and caches, so they overstate usage and cannot be read as unique users. They point the same direction as the repository counts, although the ratios are also affected by JavaScript users on npm.

Stack Overflow tag totals are a weaker signal because question volume has declined across the site. For context, the Stack Overflow tags on the day of the fetch held 20,188 questions for `terraform`, 8,365 for `aws-cloudformation`, 3,880 for `aws-cdk`, 1,083 for `azure-bicep`, 498 for `pulumi`, and 84 for `cdktf`.

## What this means when you choose an IaC language

The data says that if you pick TypeScript or Python for infrastructure code, you are in the company of most public projects that use real programming languages. It does not say those are the best choices for your team. Pick the language your team already ships and reviews code in. That keeps testing, packaging, and code review in one familiar workflow.

Pulumi supports [TypeScript, Python, Go, C#, Java, and YAML](/docs/iac/languages-sdks/), and the Pulumi numbers above show public manifests in each of them. If you are weighing toolkits, the documentation compares Pulumi with [Terraform](/docs/iac/comparisons/terraform/), [AWS CDK](/docs/iac/comparisons/aws-cdk/), and [CDKTF](/docs/iac/comparisons/cdktf/) in detail.

## Limitations

Read these numbers as a snapshot of public activity with the following caveats:

- Pulumi publishes this study. We excluded the `pulumi` organization to avoid counting our own examples, but you should weigh the Pulumi figures with that conflict of interest in mind.
- The data covers public repositories only. Most infrastructure code lives in private repositories, and the language mix there may differ.
- GitHub code search returns approximate totals for large result sets and indexes only default branches and files under 384 KB.
- Manifests are not projects. One repository can hold many manifests, and sample or template repositories inflate counts.
- CloudFormation templates overlap with AWS CDK and SAM output, so CloudFormation counts include some double counting with the CDK numbers.
- Terraform lockfiles exist only for projects on Terraform 0.14 or later, and some teams gitignore them. HCL counts are therefore bounded rather than exact.
- The count-only queries were run three times back to back and agreed exactly, yet totals moved between October 31 and November 13 (CloudFormation YAML most of all), so treat the shares as a band.
- The TypeScript and JavaScript split for Pulumi comes from a 500-repository sample and carries sampling error. Seven sampled repositories were indeterminate and one could not be fetched.
- GH Archive was not used, because its BigQuery access has a cost and does not include file paths. Maven and Go proxy download counts are not public, so no download cross-check exists for Java or Go.

## Frequently asked questions

### What is the most popular language for infrastructure as code?

Among toolkits that use general-purpose languages, TypeScript is the most common on public GitHub, at about 58% of 55,916 manifests, ahead of Python at about 23%. Among the formats we counted, HCL and CloudFormation files outnumber language-based manifests by a wide margin.

### Is Python or TypeScript more common for Pulumi?

TypeScript is more common. An estimated 37.7% of public Pulumi manifests are TypeScript against 23.8% for Python, and TypeScript is about 94% of Pulumi's Node.js projects in a 500-repository sample.

### How much infrastructure as code is written in general-purpose languages?

Roughly 5% to 9% of the public infrastructure as code files we counted (HCL, CloudFormation, Bicep, Pulumi YAML, and the three toolkits). The range depends on whether HCL is counted by lockfile or by `required_providers` blocks, and GitHub's search totals are approximate.

### Do AWS CDK users prefer TypeScript or Python?

TypeScript. It accounts for 65.6% of 37,237 public `cdk.json` manifests, with Python at 21.9%. Excluding vendor sample organizations barely changes the split.

### Can I reproduce these numbers?

Yes. Every query, the size-bucketing method, the parsing rules, and the sampling seed are described above, and the loop uses only the GitHub CLI. The Pulumi, AWS CDK, and CDKTF counts depend on the same parsing rules. Expect small differences, because GitHub's index changes daily and its totals are approximate.
