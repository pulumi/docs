---
title_tag: "Platform Automation with Pulumi Deployments"
meta_desc: Examples of common cloud deployment platforms built with Pulumi Deployments
title: "Automation"
h1: "Platform automation"
menu:
  pulumicloud:
    parent: deployments
    weight: 1
aliases:
  - /docs/intro/deployments/platform/
---

## Golden Path to Prod

Without a well-defined path to deliver infrastructure in production, it is too easy for your team to end up with systems that are deployed manually, lack security best practices, or rely on workflows that are poorly documented and unmaintained. Pulumi Deployments offers a secure, and easy-to-configure CI/CD pipeline that can be consistently replicated across every environment in your organization without piles of GitHub Actions YAML.

Git Push to Deploy, with security best practices like temporary credentials via OIDC, can be configured in minutes via the Pulumi Cloud UI. You can also write a Pulumi Program to centrally manage Deployment Settings with the Pulumi Service Provider and define all your deployment configurations as code.

When you choose Pulumi Deployments for your golden path, you get productivity features like Click to Deploy, which normally requires separate “workflow_dispatch” YAML configuration in tools like GitHub Actions. Having the flexibility to refresh, or update a stack from the Pulumi Cloud console saves your team time when performing day-to-day operational tasks. You also get access to the Deployments REST API which enables the higher-level platform automation required to manage infrastructure at scale.

## Service Catalogs

Platform teams face ever-increasing pressure to enable self-service infrastructure within their organizations. Teams of a dozen platform engineers are expected to build tools for thousands of enterprise application developers that enable them to stand up new web services with minimal coordination. This includes:

1. Offering a menu of well-defined infrastructure components to choose from, such as Kubernetes clusters or MySQL databases.
2. Brokering and delegating access to sensitive cloud environments for development and production workloads in a safe and secure manner
3. Keeping track of everything that is deployed, providing updates, and security patches as needed.

Pulumi provides several useful building blocks that help you get the job done:

1. **[Component Resources](/docs/concepts/resources/components/)** are logical infrastructure groupings. Similar to Terraform modules but much more flexible as they can take advantage of classes, interfaces, control flow, and package managers from your language of choice. Defining Component Resources for VPCs, Databases, and Kubernetes Clusters that automatically enforce security, compliance, and reliability best practices is a platform engineering best practice.
2. **OIDC Integration** enables your deployments to exchange a signed, short-lived token issued by the Pulumi Cloud for short-term credentials from your cloud provider. This can improve the security of your deployments by eliminating the need for hardcoded cloud provider credentials. Many organizations drive all development through OIDC-enabled Pulumi Deployments workflows so that developers never need cloud credentials on their local machines. OIDC can be configured across multiple clouds and cloud accounts in just a few minutes.
3. **Deployment Settings REST APIs** enable configuring everything necessary for CI/CD on the fly. Normally what would require templating, generating, and checking in GitHub Actions YAML can be done through a REST API call. Everything including environment variables, OIDC and auth configuration, source control settings, and build steps can be configured through the REST API.
4. **Deployment Triggers** give you and your developer customers multiple ways to keep your infrastructure up to date. You can enable or disable `git push` to deploy, Click to Deploy, and Deploy via REST API. Not only can your users rely on deployment triggers to update their own infrastructure, but you can use those same triggers to apply patches and enforce compliance.

Platform teams are building self-service portals and service catalogs where Pulumi Component Resources are the menu of options. Users select a Component and a cloud environment that is translated by the platform team into OIDC configuration. The Deployment Settings REST API is used to configure self-service access to deployments and infrastructure updates, and Deployment Triggers are used to drive the infrastructure development and maintenance lifecycle.

## RESTful Infrastructure APIs

Increasingly, infrastructure updates happen in response to user action and not source control events like a git commit. For instance, a SaaS database company might need to spin up dedicated compute and storage when a customer puts in a credit card and self-serves onto a specific SKU. This signup workflow might happen hundreds or even thousands of times an hour. Traditional deployment systems are optimized for infrastructure that spans, at most, a handful of environments (dev/staging/production).

Leading SaaS and infrastructure companies want the best of both worlds:

1. Custom, domain-specific REST APIs to create infrastructure on demand.
2. Desired state configuration that keeps track of what is deployed, and where.

You can build on top of the Deployments REST API to build your own infrastructure APIs. Here we have a simple Go web server that offers a RESTful interface over top of a static website. Users can create, update, and delete static websites, specifying the content for the site in the POST payload. Here's our web server:

```go
	router := httprouter.New()
	router.POST("/sites", server.create)
	router.GET("/sites/:id", server.get)
	router.POST("/sites/:id", server.update)
	router.DELETE("/sites/:id", server.delete)

	http.ListenAndServe(*addr, router)

```

Within the `create` handler, we first dynamically configure Deployment Settings for the stack, including the branch of the Pulumi program to be deployed, the AWS OIDC provider used for cloud credentials, and the configuration of `git push` Deployment Triggers`:

```go
	err := s.client.patchDeploymentSettings(r.Context(), s.org, s.project, stack, DeploymentSettings{
		SourceContext: &sourceContext{
			Git: gitContext{
				Branch:  s.branch,
				RepoDir: s.dir,
			},
		},
		OperationContext: &operationContext{
			Environment: map[string]string{
				"AWS_REGION": s.region,
			},
			OIDC: &oidcContext{
				AWS: &awsOIDCContext{
					RoleARN:     s.roleARN,
					SessionName: s.sessionName,
				},
			},
		},
		GitHub: &gitHubContext{
			Repository:          s.repository,
			Paths:               paths,
			DeployCommits:       true,
			PreviewPullRequests: false,
		},
	})

```

These settings configure the stack to trigger an update when new commits are pushed to the branch. In addition, our create handler also kicks off the initial update to create the infrastructure:

```go
err = s.client.createDeployment(ctx, s.org, s.project, stack, createDeploymentRequest{
		DeploymentSettings: DeploymentSettings{
			OperationContext: &operationContext{
				Environment: map[string]string{
					"SITE_CONTENT": content,
				},
			},
		},
		InheritSettings: true,
		Operation:       "update",
	})

```

Notice how this REST API call specifies `InheritSettings: true` so that Deployment Settings are read from the Pulumi Cloud and merged with the incoming request payload to create deployment configuration for this run. This stack also has to Click to Deploy via the Pulumi Cloud UI, so operational tasks like refreshing the stack can be done on demand without pulling down source code onto your local machine.

The Deployments Platform does the heavy lifting of managing deployment compute, providing asynchronous workflow orchestration, queueing, status and logging API access, and more. In the end, you get a Pulumi Stack and state file containing a manifest of all cloud resources and their properties managed by the Pulumi Cloud.

Deployment Settings and Triggers can be combined to ship infrastructure in novel ways with just a few lines of code. See the full [RESTful infrastructure API example](https://github.com/pulumi/deploy-demos/tree/main/deployment-drivers/go/http) to try it out yourself.

## Drift Detection

Manual edits within the AWS console can wreak havoc on your infrastructure if those changes aren’t brought back into source control. The last thing you want is to scale out a service just to have the next CI run undo that change.

You can build drift detection into your platform and get automated alerts on unexpected infrastructure changes.

```ts
aws.cloudwatch.onSchedule("drift-lambda", "cron(0/5 * * * ? *)", async() => {
    const outstandingDeployments = [];
    for(let s of stacks) {
        const url = `https://api.pulumi.com/api/preview/${s.organization}/${s.project}/${s.stack}/deployments`;
        const response = await fetch(url, {
            method: "POST",
            headers,
            body: JSON.stringify(refreshPayload),
        });

        const deployment = await response.json();
        outstandingDeployments.push(deployment.id);
    }
}
```

This scheduled Lambda runs refresh operations through the Deployments REST API. When one of those deployments detects changes, we get notified. With platform automation that automatically and proactively detects changes, your cloud team can reduce the number of surprise incidents, freeing them up to focus on higher-leverage activities. The full source code is available for the [Drift Detection example](https://github.com/pulumi/deploy-demos/tree/main/pulumi-programs/drift-detection).

## Cost Control

Infrastructure waste is a common problem. It’s too easy to leave development infrastructure running accidentally and end up with a huge bill. Many companies have entire teams devoted to solving this problem.

With Pulumi Webhooks and the Deployments REST API we can build a system for tagging and reclaiming temporary infrastructure. Anyone in your organization can create temporary infrastructure with a simple workflow:

```console
$ pulumi stack tag set ttl 360 # this stack expires six hours after it deploys
$ pulumi up # with the `ttl` tag preset, the infrastructure will be automatically destroyed at expiration
```

![TTL Stack Processor Architecture](../ttl.png)

After the expiration period has elapsed, a deployment will be queued and the development infrastructure is automatically destroyed. The Deployments API can be embedded into your platform to reduce cloud waste and automate cost controls. The full source code is available for the [TTL Stack Processor](https://github.com/pulumi/deploy-demos/tree/main/pulumi-programs/ttl-stacks).

## Managed Infrastructure

Often you need to deploy and manage infrastructure into a cloud account that you don't own or have limited access to. You might be a SaaS company deploying a self-hosted appliance into a customer environment, or an infrastructure team within a security-conscious enterprise.

Pulumi Deployments with OIDC integration can easily enable this pattern. Account owners can configure an OIDC Identity Provider within their cloud account that enables narrowly scoped access for your Pulumi organization. Since claims such as project, stack, and user are included with the OIDC token exchange, they can write custom validation rules to further limit access.

With an OIDC provider configured within your customer’s account, you are free to use deployments to deploy and manage infrastructure on their behalf. This greatly reduces the burden of maintaining and supporting self-hosted infrastructure solutions.
