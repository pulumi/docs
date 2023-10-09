---
title: "Pulumi ESC: Environments, Secrets and Configurations"
layout: esc

meta_title: "Compliance-Ready Engineering Policies: The Future of Policy-as-Code"
meta_desc: Centralized environments, secrets, and configurations management for cloud applications and infrastructure
aliases:
    - /esc

benefits:
    title: Benefits of Pulumi ESC
    items:
        - icon: lock
          icon_color: purple
          title: Frictionless Security
          description: Easy-to-use single source of truth for all configurations with guardrails. Seamlessly adopt short-lived dynamic secrets.
        - icon: lightning
          icon_color: yellow
          title: Improve Developer Efficiency
          description: Never have downtime over changed configurations. Change once and have it updated everywhere. 
        - icon: gavel
          icon_color: salmon
          title: Control Access and Compliance
          description: Enforce least-privileged access through role-based access controls. All changes are fully logged for auditing.

diagram:
    items:
        - number: 1
          description: Pulumi ESC enables you to define environments, which are collections of secrets and configurations. Each environment can be composed from multiple environments.
        - number: 2
          description: Pulumi ESC supports a variety of configuration and secrets sources, and it has an extensible plugin model that allows third-party sources. 
        - number: 3
          description: Pulumi ESC has a rich API that allows for easy integration.  Every value in an environment can be accessed from any execution environment. 
        - number: 4
          description: Every environment can be locked down with RBAC, versioned, and audited. 

screenshot:
    items:
        - title: Composable
          description: Define environments that are collections of secrets and configurations. Compose environments together from multiple other environments to allow easy inheritance of shared configurations,  eliminating “copy and paste errors”.
        - title: Traceable
          description: Never lose track of where configurations are being used and where. Trace the downstream impact of any configuration to see if the impact matches your expectations. 
        - title: Versionable
          description: Enforce least-privileged access through role-based access controls. All changes are fully logged for auditing.
---