# Stack README

This README documents the infrastructure for the Pulumi Website which encompasses the following areas:

- Marketing Site
  - URL:  [pulumi.com/](https://www.pulumi.com)
  - Repo: [github.com/pulumi/docs](https://github.com/pulumi/docs)
- Docs Site
  - URL: [pulumi.com/docs](https://www.pulumi.com/docs) 
  - Repo: [github.com/pulumi/docs](https://github.com/pulumi/docs)
- Registry
  - URL: [pulumi.com/registry](https://www.pulumi.com/registry)
  - Repo: [github.com/pulumi/registry](https://github.com/pulumi/registry)
- Answers
  - URL: [pulumi.com/answers](https://www.pulumi.com/answers)
  - Repo: [github.com/pulumi/answers](https://github.com/pulumi/answers)
- AI
  - URL: [pulumi.com/ai](https://ai.pulumi.com)
  - Repo: [github.com/pulumi/pulumi.ai](https://github.com/pulumi/pulumi.ai)


## Infrastructure

The main infrastructure for the Pulumi Website is managed here in the `infrastructure` directory, which houses the Pulumi program that provisions the website's infrastructure for the marketing and docs site, as well as the CloudFront distribution that serves the other areas of the sites managed by the other repos, i.e. registry, answers, and ai. This Pulumi program has dependencies on the infrastructure managed in the following repositories:

- [pulumi/registry](https://github.com/pulumi/registry)
- [pulumi/answers](https://github.com/pulumi/answers)
- [pulumi/pulumi.ai](https://github.com/pulumi/pulumi.ai)

The infrastructure resources for each of the respective areas of the site are managed in their own repos under their `infrastructure` directories. They export the necessary dependent properties using Stack References which are then consumed by the main infrastructure program here. Each of the above areas manages their own infrastructure and deploy independently from this repo which manages the marketing and docs content. The infrastructure in this repo has CloudFront origins and behaviors that are configured to route to the other areas of the site. The origin to route to is exported as a stack reference from registry and answers programs. Anything concerning the other areas of the site is managed in their respective repos and not here. The only thing managed here is the CloudFront distribution and the DNS records for the Pulumi Website.

## Infrastructure Resources

The infrastructure program here provisions the following resources:

- S3 buckets
    - an ephemeral bucket that gets newly generated on every deploy and hosts the built website artifacts from the marketing and docs sites.
    - uploads bucket to host larger assets such as videos, gifs, large photos, etc, under the /uploads route (the assets residing in this bucket are manually uploaded by the Docs team whenever a user needs to upload a large asset to the site such as a gif or video).
- CloudFront distribution
    - the main Cloudfront Distribution that acts as the front door to the Pulumi Website and routes to the appropriate origin (e.g. registry, answers, ai) based on the request.
    - lambda@edge functions to handle the redirects for the ai, registry, and answers sites.
- Route 53 records
    - the DNS records for the Pulumi Website that get added to the Route 53 hosted zone that is dedicated to the Pulumi `www` subdomain.


## Areas of special interest

### Handling of Redirects

There are three main ways that we handle redirects for the Pulumi Website:

1. **CloudFront Lambda@Edge Functions**: These functions are used to handle a subset of redirects for the ai, registry, and answers sites.
2. **S3 Bucket Redirects**: The static website hosting for the Pulumi Website is configured to redirect specific redirects that are declared in the following file. Once the site deploys we push all these redirects to the newly configured s3 Bucket for the site.
3. **Hugo Aliasing**: The Hugo site for the docs site is configured to alias the redirects that are declared in the `aliases` front matter of the content files. When Hugo builds the site it then generates a page at the aliased route to handle the redirect. This establishes a permanent redirect to the new location and stops the old page being indexed via a robots meta tag that gets added to the page.

### Limitations of Hugo Aliasing

Hugo Aliasing is a great solution for handling redirects for the docs and marketing site if redirecting from other pages that are local to that build, however it does have some limitations. Since our overall webite is composed of separate builds managed by separate repos and also deploy independently, we can't use Hugo Aliasing to redirect from pages that are managed by other processes. For these areas we need to use redirecting at the CloudFront level which is why we have the Lambda@Edge functions for those areas. This is because Hugo Aliasing deposits a page at the old url route, which will never be served via the CloudFront distribution since it would route all those requests to the other separate build and never serve that page when once deployed.

### Limitations of S3 Bucket Redirects

Secondly we use s3 bucket redirects for redirects from pages that are code genned by some external process and not managed as part of the repository. For example, the CLI docs are generated by the pulumi CLI and those pages are not managed as part of the docs repo. We would need to have the aliases tracked as part of that code gen process and not here if we were to use Hugo Aliasing for those areas. In these cases we use the s3 bucket redirects to handle the redirect and are listed in the files in the `scripts/redirects` directory, where we have a script that iterates through all the redirects and pushes them to the s3 bucket at the end of the deployment process.


For all other redirects that cannot be handled by the above methods we use the CloudFront Lambda@Edge functions to handle them at the cloudfront level. These cases typically involve redirecting from pages that are managed as part of an external build or repository and thus cannot be handled by the above methods.

### Handling of Redirects for answers pages

The original AI answers project was hosted under the `/ai` route which lives under the Pulumi AI webapp which is a Next.js app. We moved the answers project to its own dedicated repo we and is now hosted under the `/answers` route. Therefore we are forced to handle the redirects for the answers site at the CloudFront level since it is being redirected from pages that are managed under a different top level route, i.e. `/ai`, and app which has its own routing behaviour. Therefore we needed to create a Lambda@Edge function to handle the redirects for the answers site from the CloudFront distribution before the request gets routed to the ai origin.
## Atomic S3 Bucket Deployments

We generate a new S3 bucket for the website on every deploy. This bucket gets generated with a name that includes the commit sha of the commit that it is deployed at. This bucket is managed outside of the Pulumi program and is provisioned using the script, scripts/sync-and-test-bucket.sh. This script syncs the built website artifacts from the marketing and docs sites to the new bucket. It then generates a metadata file that contains the name of the bucket that was created for this build which is then referenced by the pulumi program to update the CloudFront distribution origin to route to the new bucket at deployment time.

This approach allows us to have an atomic deploy of the website since the only thing that changes when we deploy is the S3 bucket that the CloudFront distribution origins are updated to route to. Under normal circumstances (i.e. no infrastructure changes) this means that the only thing that changes when we run `pulumi up` is the origin that the CloudFront distribution points to.