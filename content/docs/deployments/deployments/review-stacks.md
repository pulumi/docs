---
title_tag: "Review stacks"
meta_desc: Pull request environments that deploy application and infrastructure code changes.
title: "Review stacks"
h1: "Review stacks"
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
- /docs/pulumi-cloud/deployments/review-stacks/
- /docs/platform/deployments/review-stacks/
menu:
  deployments:
    name: Review stacks
    parent: deployments-deployments
    weight: 70
    identifier: deployments-deployments-review-stacks
---

Review stacks are dedicated cloud environments powered by Pulumi Deployments. They are created automatically when a pull request is opened, updated on each new commit, and destroyed when the pull request is merged or closed. They work with [GitHub](/docs/integrations/version-control/github-app/), [Azure DevOps](/docs/integrations/version-control/azure-devops-integration/), and [GitLab](/docs/integrations/version-control/gitlab/). When a pull request is opened, Pulumi Deployments stands up a stack with your changes and adds a comment to the PR with the outputs from your deployment.

## Configuring review stacks

Review stacks require that your stacks are configured with [Deployment Settings](/docs/deployments/deployments/reference/#deployment-settings). They are configured at the branch level. If you utilize multiple branches for your development and release process, you will need to configure a review stack template for each one.

Configuring review stacks is a three-step process:

1. Create a new stack, by convention named `pr`, and corresponding `Pulumi.pr.yaml` configuration file - this config will be copied into every review stack that gets created, and can even be modified within a PR.
2. Configure [Deployment Settings](/docs/deployments/deployments/reference/#deployment-settings) for the stack - this specifies how to acquire source code, cloud credentials and more when deploying via Pulumi Deployments.
3. Set the `pullRequestTemplate` Deployment Setting to true - this indicates that all pull requests against this stack’s branch should reference this stack as a review stack template.

You can use an existing stack as a review stack template, as long as it has Deployment Settings configured. This will result in review stacks being deployed into the same cloud account. If you want to separate the cloud resources in your production stack from the resources created via review stacks then you can create a separate stack and template that references a different cloud account (AWS, Azure, GCP, etc.).

Review stacks and Deployment Settings can be configured via the Pulumi Cloud console, the Pulumi Cloud REST API, or within a Pulumi program using the Pulumi Cloud resource provider.

### Pulumi Cloud UI

Enable review stacks for a stack in the deployment settings section of the Pulumi Cloud console.

### REST API

You can programmatically configure review stacks and Deployment Settings at scale across thousands of projects using the [Deployments REST API](/docs/deployments/deployments/api/#patch-settings).

```bash
curl -i -XPOST -H "Content-Type: application/json" -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stacks/org/project/stack/deployments/settings" \
-d '{
  "gitHub":{
    "pullRequestTemplate": true
    }
}'
```

### Pulumi Cloud Service provider

You can use Pulumi to manage and code review Deployment Settings and review stacks with the [Pulumi Cloud Service provider](/registry/packages/pulumiservice).

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

## Common patterns

Review stacks are powered by Pulumi IaC, and as a result offer a high degree of flexibility by way of configuration, and even multiple Pulumi programs. The following sections outline common patterns.

### Utilizing config

Each pull request template stack has a corresponding Pulumi config file that can be checked into source control. By convention this file is called `Pulumi.pr.yaml`. You can modify review stack configuration values as part of your pull request, and the new configuration will be used to deploy your review stack.

Review stack config can be used to customize your deployment environment. For instance, you may want to downsize the size of VMs and number of containers deployed to your review stack.

Your production (`Pulumi.production.yaml`) stack might have the following config:

```yaml
config:
  aws:region: us-west-2
  webserver:apiServiceDesiredCount: "32"
  webserver:clusterInstanceType: m6g.xlarge
  webserver:clusterNumInstances: "16"
```

And you may choose to downsize your corresponding review stack config (`Pulumi.pr.yaml`) to reduce cloud spend for development environments:

```yaml
config:
  aws:region: us-west-2
  webserver:apiServiceDesiredCount: "2"
  webserver:clusterInstanceType: t3.large
  webserver:clusterNumInstances: "1"
```

You can use review stack config in other creative ways, for instance to configure stacks to utilize shared development resources such as VPCs or databases rather than having a dedicated database per review stack. This can be useful to both optimize costs, and speed up deployment times.

### Single stack

You can configure a single stack with `git push` to deploy, pull request previews, and review stacks. This is the simplest, lowest configuration approach, but results in your review stacks getting created in the same cloud account as your primary or production stack. It also means that the same configuration will be used for your production and review stacks, meaning that patterns like downsizing review stacks won't be possible.

The following example shows how to configure this pattern using the [Pulumi Cloud Service provider](/registry/packages/pulumiservice):

```typescript
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

### Separate stacks

If you need your review stacks to differ from your production stack in either configuration or Deployment Settings, you will need to create a separate stack and template. This enables you to configure your review stacks for instance to deploy into a separate cloud account.

First you will need to run `pulumi stack init` to create a `pr` stack, set any necessary config values, and commit this file to source control.

The following example shows how to configure this pattern using the [Pulumi Cloud Service provider](/registry/packages/pulumiservice):

```typescript
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

### Customizing behavior with multiple Pulumi programs

Sometimes you want your review stack to differ substantially from the stack that gets deployed to production. You might want to use multi-tenant development infrastructure for review stacks to both reduce the cost of development infrastructure, and also speed up review stack deployment times. Sometimes this can be accomplished with config alone, but occasionally it can be useful to write separate Pulumi programs for the review stack. One common pattern for this is:

- Production program and stack: the Pulumi program that defines your complete, stand-alone production (and often dev/test/staging) environment.
- Shared Kubernetes stack: a Pulumi program that deploys a Kubernetes cluster, designed to be shared by all review stacks.
- Review stack: a Pulumi program that builds containers, and deploys Kubernetes resources (pods, deployments, etc.) to the shared cluster.

The following example shows how to configure this pattern using the [Pulumi Cloud Service provider](/registry/packages/pulumiservice):

```typescript
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

### Customizing behavior with path filters

Sometimes you want to vary the behavior of a review stack based on what kind of code changed. For instance, changes to the `migrations` folder should trigger a migrations container to be built and run, but otherwise we want to skip this step as it adds a few extra minutes to our deployment times. This can be accomplished by using path filters in combination with multiple review stack templates. When the pull request is opened, Pulumi Deployments will evaluate the code changes and select which template to use based on matches against the path filters. This allows you to customize Deployment Settings, config, or Pulumi program, based on what code changes were made.

The following example shows how to configure this pattern using the [Pulumi Cloud Service provider](/registry/packages/pulumiservice):

```typescript
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

### Gating review stacks by GitHub label

By default, every pull request against a configured branch creates a review stack. Set `reviewStackLabels` in your GitHub deployment settings to limit review stack creation to pull requests that carry at least one of the specified labels. Matching is case-sensitive. Labels added after a pull request is opened will also trigger creation.

The following example shows how to configure this pattern using the [Pulumi Cloud Service provider](/registry/packages/pulumiservice):

```typescript
const reviewSettings = new pulumiservice.DeploymentSettings("reviewSettings", {
	organization: pulumi.getOrganization(),
	project: "your project",
	stack: "pr",
	github: {
		pullRequestTemplate: true,
		repository: "pulumi/deployment-automation",
        // only create review stacks for PRs with one of these labels
        reviewStackLabels: ["review-stack", "reviewStack", "rs"],
	},
	sourceContext: {
		git: {
			branch: "refs/heads/main",
			repoDir: "pulumi-pet-shop",
		},
	},
});
```
