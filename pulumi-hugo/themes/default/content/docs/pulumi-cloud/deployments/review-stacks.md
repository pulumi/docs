---
title_tag: "Review Stacks"
meta_desc: Pull request environments that deploy application and infrastructure code changes.
title: "Review Stacks"
h1: "Review Stacks"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    parent: deployments
    weight: 2
---

Review Stacks are dedicated cloud environments that get created automatically every time a pull request is opened, all powered by Pulumi Deployments. Open a pull request, and Pulumi Deployments will stand up a stack with your changes and the Pulumi GitHub App will add a PR comment with the outputs from your deployment. Merge the PR and Pulumi Deployments will destroy the stack and free up the associated resources. It has never been simpler to pick up an unfamiliar codebase, make changes to both application and infrastructure code, and share a live environment for review with your teammates.

![Review Stack Pull Request Comment](../comment.png)

Review Stacks enable you to iterate on both application code changes and infrastructure code changes at the same time. Just open a pull request and you can start testing changes against everything from simple static websites to API servers, microservices, data pipelines, Kubernetes clusters, and any other piece of infrastructure across Pulumi’s 100+ cloud providers. Review Stacks manage the full lifecycle of your cloud development environment including creating it when the PR is opened, updating it every time a new commit is pushed, and destroying and cleaning up all cloud resources when the pull request is merged or closed.

## Configuring Review Stacks

Review Stacks are powered by Pulumi Deployments, and require that your stacks are configured with [Deployment Settings](/docs/pulumi-cloud/deployments/reference/#deployment-settings). Review Stacks are configured at the branch level. If you utilize multiple branches for your development and release process, you will need to configure a Review Stack template for each one.

Configuring Review Stacks is a simple three-step process:

1. Create a new stack, by convention named `pr`, and corresponding `Pulumi.pr.yaml` configuration file - this config will be copied into every review stack that gets created, and can even be modified within a PR.
2. Configure [Deployment Settings](/docs/pulumi-cloud/deployments/reference/#deployment-settings) for the stack - this specifies how to acquire source code, cloud credentials and more when deploying via Pulumi Deployments.
3. Set the `pullRequestTemplate` Deployment Setting to true - this indicates that all pull requests against this stack’s branch should reference this stack as a Review Stack template.

You can use an existing stack as a Review Stack template, as long as it has Deployment Settings configured. This will result in Review Stacks being deployed into the same cloud account. If you want to separate the cloud resources in your production stack from the resources created via Review Stacks then you can create a separate stack and template that references a different cloud account (AWS, Azure, GCP, etc).

Review Stacks and Deployment Settings can be configured via the Pulumi Cloud console, the Pulumi Cloud REST API, or within a Pulumi Program using the Pulumi Cloud Resource Provider.

### Pulumi Cloud UI

It is just one click to turn on Review Stacks via the Pulumi Cloud console.

![Deployment Settings for Review Stacks](../pr-settings.gif)

### REST API

You can programmatically configure Review Stacks and Deployment Settings at scale across thousands of projects using the [Deployments REST API](/docs/pulumi-cloud/deployments/api/#patch-settings).

```
curl -i -XPOST -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/preview/org/project/stack/deployment/settings" \
-d '{
  "gitHub":{
    "pullRequestTemplate": true
    }
}'
```

### Pulumi Cloud Resource Provider

You can use Pulumi to manage and code review Deployment Settings and Review Stacks with the [Pulumi Cloud Provider](/registry/packages/pulumiservice).

```typescript
import * as pulumiservice from "@pulumi/pulumiservice";

const deploymentSettings = new pulumiservice.DeploymentSettings("deploymentSettings", {
	organization: pulumi.getOrganization(),
	project: "your project",
	stack: "your stack",
	github: {
		deployCommits: true,
		previewPullRequests: true,
		pullRequestTemplate: true,
		repository: "pulumi/deployment-automation",
	},
	sourceContext: {
		git: {
			branch: "refs/heads/main",
			repoDir: "pulumi-pet-shop",
		},
	},
});
```

## Common Patterns

Review Stacks are powered by Pulumi IaC, and as a result offer a high degree of flexibility by way of configuration, and even multiple Pulumi Programs. Here we outline a few common patterns.

### Utilizing Config

Each pull request template stack has a corresponding Pulumi config file that can be checked into source control. By convention this file is called `Pulumi.pr.yaml` and you can even modify these configuration values as a part of your pull request and the new configuration will be used to deploy your Review Stack.

Review Stack config can be used to customize your deployment environment. For instance, you may want to downsize the size of VMs and number of containers deployed to your review stack.

Your production (`Pulumi.production.yaml`) stack might have the following config:

```yaml
config:
  aws:region: us-west-2
  webserver:apiServiceDesiredCount: "32"
  webserver:clusterInstanceType: m6g.xlarge
  webserver:clusterNumInstances: "16"
```

And you may choose to downsize your corresponding Review Stack config (`Pulumi.pr.yaml`) to reduce cloud spend for development environments:

```yaml
config:
  aws:region: us-west-2
  webserver:apiServiceDesiredCount: "2"
  webserver:clusterInstanceType: t3.large
  webserver:clusterNumInstances: "1"
```

You can use Review Stack config in other creative ways, for instance to configure stacks to utilize shared development resources such as VPCs or databases rather than having a dedicated database per Review Stack. This can be useful to both optimize costs, and speed up deployment times.

### Single Stack

You can configure a single stack with `git push` to Deploy, pull request previews, and Review Stacks. This is the simplest, lowest configuration approach, but results in your Review Stacks getting created in the same cloud account as your primary or production stack. It also means that the same configuration will be used for your production and review stacks, meaning that patterns like downsizing Review Stacks won't be possible.

```ts
const deploymentSettings = new pulumiservice.DeploymentSettings("deploymentSettings", {
	organization: pulumi.getOrganization(),
	project: "your project",
	stack: "production",
	github: {
        // this single stack is used for both push to deploy + PR previews
        // as well as the review stack template
		deployCommits: true,
		previewPullRequests: true,
		pullRequestTemplate: true,
		repository: "pulumi/deployment-automation",
	},
	sourceContext: {
		git: {
			branch: "refs/heads/main",
			repoDir: "pulumi-pet-shop",
		},
	},
});
```

### Separate Stacks

If you need your Review Stacks to differ from your production stack in either configuration or Deployment Settings, creating a separate stack and template is necessary. This enables you to configure your Review Stacks for instance to deploy into a separate cloud account.

First you will need to `pulumi stack init` to create a `pr` stack, set any necessary config values, and commit this file to source control.

```ts
const productionSettings = new pulumiservice.DeploymentSettings("productionSettings", {
	organization: pulumi.getOrganization(),
	project: "your project",
	stack: "production",
	github: {
        // our production is configured with push to deploy
        // and pull request previews
		deployCommits: true,
		previewPullRequests: true,
		pullRequestTemplate: false,
		repository: "pulumi/deployment-automation",
	},
	sourceContext: {
		git: {
			branch: "refs/heads/main",
			repoDir: "pulumi-pet-shop",
		},
	},
});


const prSettings = new pulumiservice.DeploymentSettings("prSettings", {
	organization: pulumi.getOrganization(),
	project: "your project",
	stack: "pr",
	github: {
        // this stack acts as a review stack template only
        // and never actually gets updated.
        // push to deploy and PR previews are disabled.
		deployCommits: false,
		previewPullRequests: false,
		pullRequestTemplate: true,
		repository: "pulumi/deployment-automation",
	},
	sourceContext: {
		git: {
			branch: "refs/heads/main",
			repoDir: "pulumi-pet-shop",
		},
	},
});

```

### Customizing Behavior with Multiple Pulumi Programs

Sometimes you want your Review Stack to differ substantially from the stack that gets deployed to production. You might want to use multi-tenant development infrastructure for Review Stacks to both reduce the cost of development infrastructure, and also speed up Review Stack deployment times. Sometimes this can be accomplished with config alone, but occassionaly it can be useful to write separate Pulumi Programs for the review stack. One common pattern for this is:

- Production Program and Stack: the Pulumi Program that defines your complete, stand alone production (and often dev/test/staging) environment.
- Shared Kubernetes Stack: a Pulumi Program that deploys a Kubernetes cluster, designed to be shared by all Review Stacks.
- Review Stack: a Pulumi Program that builds containers, and deploys Kubernetes resources (pods, deployments, etc) to the shared cluster.

```ts
const productionSettings = new pulumiservice.DeploymentSettings("productionSettings", {
	organization: pulumi.getOrganization(),
	project: "your project",
	stack: "production",
	github: {
		deployCommits: true,
		previewPullRequests: true,
		repository: "pulumi/deployment-automation",
	},
	sourceContext: {
		git: {
			branch: "refs/heads/main",
			repoDir: "pulumi-pet-shop",
		},
	},
});

const sharedKubernetesSettings = new pulumiservice.DeploymentSettings("sharedKubernetesSettings", {
	organization: pulumi.getOrganization(),
	project: "your project",
	stack: "kubernetes-shared-cluster",
	github: {
		deployCommits: true,
		previewPullRequests: true,
		repository: "pulumi/deployment-automation",
	},
	sourceContext: {
		git: {
			branch: "refs/heads/main",
			repoDir: "shared-kubernetes-cluster",
		},
	},
});


const prSettings = new pulumiservice.DeploymentSettings("prSettings", {
	organization: pulumi.getOrganization(),
	project: "your project",
	stack: "pr",
	github: {
		deployCommits: false,
		previewPullRequests: false,
		pullRequestTemplate: true,
		repository: "pulumi/deployment-automation",
	},
	sourceContext: {
		git: {
			branch: "refs/heads/main",
			repoDir: "shared-kubernetes-pr-deployments",
		},
	},
});

```

### Customizing Behavior with Path Filters

Sometimes you want to vary the behavior of a Review Stack based on what kind of code changed. For instance, changes to the `migrations` folder should trigger a migrations container to be built and run, but otherwise we want to skip this step as it adds a few extra minutes to our deployment times. This can be accomplished by using path filters in combination with multiple Review Stack templates. When the pull request is opened, Pulumi Deployments will evaluate the code changes and select which template to use based on matches against the path filters. This allows you to customize Deployment Settings, config, or Pulumi Program, based on what code changes were made.

```ts
const productionSettings = new pulumiservice.DeploymentSettings("productionSettings", {
	organization: pulumi.getOrganization(),
	project: "your project",
	stack: "production",
	github: {
		deployCommits: true,
		previewPullRequests: true,
		repository: "pulumi/deployment-automation",
	},
	sourceContext: {
		git: {
			branch: "refs/heads/main",
			repoDir: "pulumi-pet-shop",
		},
	},
});

const prSettings = new pulumiservice.DeploymentSettings("prSettings", {
	organization: pulumi.getOrganization(),
	project: "your project",
	stack: "pr",
	github: {
		deployCommits: false,
		previewPullRequests: false,
		pullRequestTemplate: true,
		repository: "pulumi/deployment-automation",
        // use this template when migrations haven't changed
        paths: [
            "!migrations/*",
        ],
	},
	sourceContext: {
		git: {
			branch: "refs/heads/main",
			repoDir: "pulumi-pet-shop",
		},
	},
});

const prMigrationSettings = new pulumiservice.DeploymentSettings("prMigrationSettings", {
	organization: pulumi.getOrganization(),
	project: "your project",
	stack: "pr-migrations",
	github: {
		deployCommits: false,
		previewPullRequests: false,
		pullRequestTemplate: true,
		repository: "pulumi/deployment-automation",
        // use this template when migrations have changed in the PR contents
        paths: [
            "migrations/*",
        ],
	},
	sourceContext: {
		git: {
			branch: "refs/heads/main",
			repoDir: "pulumi-pet-shop",
		},
	},
});

```
