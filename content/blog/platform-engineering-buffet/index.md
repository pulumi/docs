---
title: "Platform Engineering Buffet"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-05-23T11:42:43-04:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc:

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - joe-duffy

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - change-me


# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

# Here are some examples of posts we have made in the past for inspiration:
# https://www.linkedin.com/feed/update/urn:li:activity:7171191945841561601
# https://www.linkedin.com/feed/update/urn:li:activity:7169021002394296320
# https://www.linkedin.com/feed/update/urn:li:activity:7155606616455737345
# https://twitter.com/PulumiCorp/status/1763265391042654623
# https://twitter.com/PulumiCorp/status/1762900472489185492
# https://twitter.com/PulumiCorp/status/1755637618631405655

social:
    twitter:
    linkedin:

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

What you put here will appear on the index page. In most cases, you'll also want to add a Read More link after this paragraph (though technically, that's optional. To do that, just add an HTML comment like the one below.

<!--more-->
# Building a Platform as a Buffet: How SEITENBAU Serves 20+ Projects with Pulumi

*By Nico Thomas and Adam Furmanek*

[VIDEO EMBED: Building a Platform as a Buffet with Pulumi]

## When One Size Doesn't Fit All

> **"Imagine your company isn't Spotify with one product pipeline, but 20 independent government portal-style projects running on Ansible-provisioned VMs, some on Kubernetes, some delivered into other customer data centers, some operated by clients themselves. Each team building their own CI/CD, their own secrets management, their own integrations - it just leaves you with a million wheels that you can reinvent."**
> *- Adam Furmanek*

This is the reality at SEITENBAU, a German software company specializing in custom development for both public and private sectors. Unlike the typical platform engineering stories you hear—where teams build infrastructure for a single product with multiple microservices—we faced a fundamentally different challenge: how do you build a platform that serves dozens of completely independent projects, each with their own technology choices, deployment targets, and operational models?

The answer? Stop trying to force everyone onto the same plate. Instead, build a buffet.

## The Buffet Philosophy

> **"We came up with this buffet concept to offer people ready-made pizzas which they don't have to cook themselves, so to speak, and they still have a lot of flexibility to pick what they need."**
> *- Nico Thomas*

[SLIDE EMBED: Slide 2 - Buffet visualization with labeled containers showing NPM Artifact Storage, Container Registry, and various infrastructure components]

Think of a traditional platform as a prix fixe menu—everyone gets the same courses, prepared the same way. But what if your diners include vegans, carnivores, and people with various dietary restrictions? What if some want a quick snack while others need a seven-course meal?

That's exactly our situation at SEITENBAU. We have:
- Government projects that must run on-premises due to data sovereignty requirements
- Modern cloud-native applications using Kubernetes and GitOps
- Legacy systems still running on VMs managed with Ansible
- Projects we operate as a service, and others we simply deliver to customers
- Teams using different CI/CD tools, artifact repositories, and deployment strategies

A one-size-fits-all platform would have been a disaster. Instead, we built a platform that offers a rich selection of pre-configured, production-ready components that teams can mix and match according to their needs.

## The Challenge: Beyond Microservices

> **"A lot of resources for platform engineering are focused on a single product... We can't just take off-the-shelf solutions like Backstage because they're often more tailored to the single product scenario."**
> *- Nico Thomas*

Most platform engineering resources assume you're building for a single product. Spotify's Backstage, for example, excels at managing microservices that are all part of one cohesive system. But what happens when you have 20+ completely different products, each with unique requirements?

At SEITENBAU, we work primarily on citizen service portals for German government agencies, alongside projects for private sector clients. Each project is independent, with its own:
- Technology stack (though Java predominates, we support various frameworks and languages)
- Infrastructure requirements (cloud, on-premises, or hybrid)
- Security and compliance needs
- Operational model (managed by us, the client, or shared)
- Release cadence and deployment strategies

[SLIDE EMBED: Slide 7 - "Choose Your Menu" showing different project configurations with GitLab CI, various registries, Kubernetes, OpenShift, and VM deployments]

This diversity might seem like chaos, but we discovered that beneath the variations, common patterns emerged. Every project needs source control, CI/CD pipelines, artifact storage, secrets management, and deployment targets. The key insight was that we didn't need to standardize *what* teams choose—we needed to standardize *how* they connect these pieces together.

That's where Pulumi entered the picture, providing the flexibility to build a true infrastructure buffet that could satisfy everyone's appetite.

## Building the Kitchen: Architecture with Pulumi

[SLIDE EMBED: Slide 9 - "A Look in the Kitchen" showing the complete architecture with Pulumi at the center]

Behind every great buffet is a well-organized kitchen. In our case, that kitchen is powered by Pulumi and Python, orchestrating a complex web of infrastructure services, configurations, and deployments.

> **"We're using Pulumi together with Python - this turned out to be super nice for us to maintain in day-to-day tasks and super easy to understand."**
> *- Nico Thomas*

### The Multi-Stack Approach

Rather than building one monolithic infrastructure program, we opted for a modular approach using multiple Pulumi stacks. This decision proved crucial for managing complexity and enabling team autonomy.

[SLIDE EMBED: Slide 10 - Program and Stack architecture showing GitLab, clusters, and system configurations]

Our architecture consists of several specialized Pulumi programs:
- **GitLab System**: Manages GitLab installations and configurations
- **Project Configuration**: Handles team-specific GitLab groups, CI/CD runners, and agents
- **Cluster Management**: Provisions Kubernetes clusters with standard add-ons
- **VM Infrastructure**: Manages traditional VM-based deployments with Ansible
- **Platform Services**: Configures shared services like artifact repositories and identity providers

Each program can have multiple stacks (dev, staging, prod), allowing us to manage different environments independently while sharing the same infrastructure code.

### The Secret Sauce: Unified Configuration

> **"Definitely to go into the centralized configuration part earlier. It's been almost a year until we figured out that the central configuration is super useful."**
> *- Nico Thomas*

The breakthrough came when we realized we needed a single source of truth for project configuration. Instead of scattering configuration across multiple systems, we created a unified YAML-based configuration schema:

[SLIDE EMBED: Slide 11 - Unified Project Configuration YAML example]

```yaml
name: example-project
ldapTeamGroup: example-project_developers
gitlab:
  - instance: "prod"
    path: "group-a/example-project"
    runner:
      kubeconfigVaultPath: "prod/buildcluster1/kubeconfig"
    agent:
      kubeconfigVaultPath: "dev/example/sample-config"
binRepo:
  - type: "docker"
    name: "example-project-repo"
cluster:
  - type: "vcluster"
    name: "example-project-testing"
```

This configuration serves as the menu for each project. Teams declare what they need, and our Pulumi programs provision and wire everything together automatically. The LDAP team group, for example, is used across multiple systems for permissions, SSO configuration, and access control.

### Type Safety with Python and Pydantic

We leverage Python's type system with Pydantic to ensure configuration consistency:

```python
from typing import List, Optional
from pydantic import BaseModel

class ClusterConfig(BaseModel):
    type: ClusterType
    name: str
    hostKubeconfigVaultPath: str
    
class Project(BaseModel):
    name: str
    ldapTeamGroup: str
    gitlab: Optional[List[GitlabConfig]] = []
    binRepo: Optional[List[BinRepoConfig]] = []
    cluster: Optional[List[ClusterConfig]] = []
```

This approach gives us validation for free and makes our infrastructure code more maintainable. The configuration is stored in Git, providing version history and enabling GitOps workflows.

## From Ingredients to Ready-Made Dishes: Reusable Components

[SLIDE EMBED: Slide 6 - Platform vision showing the complete self-service platform]

The real magic happens in our component library. Just as a buffet offers complete dishes rather than raw ingredients, we've built high-level components that encapsulate complex infrastructure patterns.

### Example: The Kubernetes Storage Component

[SLIDE EMBED: Slide 15 - KubeLonghorn component diagram]

Consider our Longhorn storage component. Instead of requiring teams to understand Helm charts, storage classes, and snapshot configurations, they simply declare they need persistent storage:

```python
class KubeLonghorn(pulumi.ComponentResource):
    def __init__(self, name, cluster_config, opts=None):
        super().__init__('buffet:storage:Longhorn', name, None, opts)
        
        # Install Longhorn with sensible defaults
        helm.v3.Release('longhorn',
            chart='longhorn',
            values={
                'defaultSettings': {
                    'defaultReplicaCount': 1 if cluster_config.is_test else 3
                }
            }
        )
        
        # Configure snapshot support
        # Set up default storage classes
        # Handle internal CA certificates
```

The component handles all the complexity: installing Longhorn, configuring appropriate replication for test vs. production environments, setting up snapshot classes, and integrating with our internal certificate authority.

### Example: GitOps with Flux

[SLIDE EMBED: Slide 16 - KubeFlux component diagram]

Our Flux component demonstrates how we handle multi-system integration:

```python
class KubeFlux(pulumi.ComponentResource):
    def __init__(self, name, project_config, opts=None):
        # Generate SSH key pair for Flux
        flux_key = tls.PrivateKey(f"{name}-flux-key")
        
        # Add deploy key to GitLab
        gitlab.DeployKey(f"{name}-deploy-key",
            project=project_config.gitlab.path,
            key=flux_key.public_key_openssh
        )
        
        # Bootstrap Flux with the private key
        flux.FluxBootstrapGit(f"{name}-flux",
            ssh_private_key=flux_key.private_key_pem,
            # Additional Flux configuration
        )
```

Teams get GitOps with a single configuration flag. Behind the scenes, we're creating SSH keys, configuring GitLab deploy keys, and bootstrapping Flux—all the tedious work that typically takes "half a day" is reduced to minutes.

## The Menu in Action

> **"You don't have to take every course - you can just go with a salad."**
> *- Nico Thomas*

The flexibility of our approach means a government project running on OpenShift with strict compliance requirements uses the same platform as a modern cloud-native application with Kubernetes and GitOps. Each team takes what they need from the buffet, and our Pulumi components ensure everything works together seamlessly.

## Two Years Later: Results and Lessons

After two years of running this platform in production, we've learned what works and what we'd do differently.

> **"The main benefit is that you can find the things that work for you with the flexibility to put in legacy systems with relatively low effort because you can use dynamic providers."**
> *- Nico Thomas*

### What's Working Well

**Developer Experience:** Teams can now spin up fully configured environments in minutes instead of days. A new project gets source control, CI/CD pipelines, artifact repositories, and deployment targets—all properly integrated and secured—with a simple YAML configuration.

**Flexibility at Scale:** We're successfully supporting over 20 projects with vastly different requirements without forcing standardization. The buffet approach has proven its worth.

**Legacy Integration:** Pulumi's dynamic providers have been a game-changer for integrating legacy systems. We can wrap any API in a provider and treat it like any other infrastructure resource.

### Key Lessons Learned

The biggest lesson? **Start with centralized configuration from day one.** We spent nearly a year before realizing how powerful a unified configuration model would be. This single source of truth transformed how we manage cross-cutting concerns like permissions and team access.

We also learned that using a real programming language (Python) for infrastructure gives us tremendous power. Type checking, IDE support, and the ability to write tests for our infrastructure code have made the platform maintainable as it grows.

## Why Not Just Use Backstage?

> **"With Backstage you can use plugins and customize it... The main benefit [of our approach] is that you can find the things that work for you with the flexibility to put in legacy systems with relatively low effort."**
> *- Nico Thomas*

Backstage is excellent for what it does, but it assumes a level of standardization that doesn't fit our reality. Our approach lets us:
- Support any infrastructure pattern, not just Kubernetes
- Integrate legacy systems alongside modern cloud-native stacks
- Give teams genuine choice without sacrificing governance
- Build exactly what our organization needs without fighting the framework

## The Buffet is Open

Building a platform for diverse, independent projects requires a different mindset than traditional platform engineering. Instead of forcing standardization, we've embraced flexibility while maintaining consistency where it matters.

The buffet approach—powered by Pulumi's flexibility and Python's expressiveness—has allowed us to serve 20+ different projects efficiently while giving teams the autonomy they need. It's not about having one perfect dish; it's about having a kitchen flexible enough to satisfy everyone.

If you're facing similar challenges with diverse project requirements, consider building a buffet instead of a prix fixe menu. Your teams will thank you for it.

---

*Want to build your own infrastructure buffet? [Get started with Pulumi](https://www.pulumi.com/docs/get-started/) and join [our community Slack](https://slack.pulumi.com/) to connect with engineers solving similar challenges.*