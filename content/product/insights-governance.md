---
title: Insights & Governance - Continuous Compliance, By Construction
type: page
layout: product-page
meta_desc: Automated compliance made simple — continuously audit, remediate, and enforce policies to keep your cloud secure and reliable.
meta_image: /images/product/insights-governance/ig-meta.png

aliases:
- /insights
- /pulumi-policies
- /product/pulumi-insights
- /product/pulumi-insights/
- /product/crossguard
- /crossguard

sections:
  - type: hero
    title_primary: "Continuous compliance,"
    title_secondary: "by construction."
    description: Audit, remediate, and enforce compliance policies across all your cloud infrastructure automatically.
    image: /images/product/insights-governance/ig-hero.svg
    image_alt: Pulumi Insights & Governance dashboard showing cloud resource compliance
    anchor: hero

  - type: feature_split
    heading: Stop compliance violations before they become problems.
    description: |
      Govern your cloud automatically.

      Pulumi Insights & Governance gives you a complete lifecycle for cloud compliance: audit existing infrastructure, fix violations with AI-powered remediation, and prevent future issues with policy as code. Neo closes the loop to keep your infrastructure secure and well-governed automatically.

    cards:
      - icon: fa-sync-alt
        title: Compliance without friction
        description: |
          Continuously audit and block non-compliant deployments across CIS, NIST, HITRUST, and PCI DSS without disrupting developer workflows.
      - icon: fa-bolt
        title: Auto-remediate violations
        description: |
          AI generates infrastructure-as-code fixes automatically, turning hours of manual remediation into a simple review-and-merge.
      - icon: fa-eye
        title: Full cloud visibility
        description: |
          Search and govern every resource across all your cloud, including unmanaged resources, with natural language queries and full configuration history.
    anchor: overview

  - type: video_embed
    youtube_id: mwcrOTEf1EQ
    title: Pulumi policy automation
    poster_image: /images/product/insights-governance/ig-poster.png
    poster_alt: Pulumi policy automation – watch the demo
    anchor: demo

  - type: section_header_with_image
    tag_line: Always-On Auditing
    title: Audit existing infrastructure against compliance standards
    description: |
      Works with any infrastructure, whether provisioned with Pulumi, Terraform, CloudFormation, or manual processes.

      Continuous audit scans evaluate your entire infrastructure against industry frameworks without disrupting deployment pipelines. Non-blocking compliance checks provide instant visibility into your security posture across CIS Controls, NIST SP 800-53, HITRUST CSF, and PCI DSS standards.

      - Pre-built compliance frameworks ready to deploy
      - Evaluate existing infrastructure on demand with audit mode
      - Automatic triggers after deployments
      - Auditor-friendly compliance reporting
    image: /images/product/insights-governance/ig-auditing.png
    image_alt: Audit findings dashboard showing compliance posture
    anchor: audit

  - type: section_header_with_image
    flip: true
    tag_line: AI-Powered Remediation
    title: Automatically generate fixes for policy violations
    description: |
      Pulumi Neo identifies policy issues and fixes them automatically. For resources created outside your control (manual console changes, unmanaged deployments), Neo finds and fixes compliance violations in a single workflow, eliminating surprise audit findings and cost overruns. Transform hours of manual work into simple review-and-merge processes.

      - AI-generated infrastructure-as-code fixes
      - Import and remediate unmanaged resources
      - Integrated approval workflows
      - Complete audit trails for compliance
      - Governance-aware remediation with policy compliance checks
    image: /images/product/insights-governance/ig-neo-policy.png
    image_alt: AI-powered remediation workflow in Pulumi Neo
    anchor: remediate

  - type: testimonial
    quote: |
      We gave our auditors access to our policy packs because it's far easier to understand and prove controls in code than in docs and diagrams. With Pulumi's Policy as Code approach, that manual review process has gone away. We've reduced our Authority to Operate (ATO) timeline from a year and a half to expecting approval in three months.
    author: Michael Hunter
    title: CEO
    company: Spear AI
    logo: /logos/customers/spearAI.svg
    anchor: testimonial

  - type: section_header_with_image
    tag_line: Shift-Left Governance
    title: Prevent non-compliant deployments before production
    description: |
      Write governance policies in TypeScript or Python, languages your team already knows. Deploy pre-built compliance packs or create custom rules that enforce your organization's standards. Policies block problematic configurations during deployment, providing immediate feedback to developers within their existing workflows.

      - Policy-as-code in TypeScript/Python (no DSLs)
      - Pre-built packs for CIS, NIST, HITRUST, PCI DSS
      - Progressive enforcement (advisory → mandatory)
      - Immediate feedback during deployment workflows
      - Neo-generated infrastructure automatically complies with policy standards
    image: /images/product/insights-governance/ig-shift-left.png
    image_alt: Policy enforcement blocking a non-compliant deployment
    anchor: prevent

  - type: section_header_with_image
    flip: true
    tag_line: Full Cloud Visibility
    title: Search and understand your entire cloud footprint
    description: |
      Query any resource across major clouds with natural language or advanced filters. Track configuration changes, analyze relationships between resources, and get answers about your infrastructure in seconds. Pulumi discovers all resources, including those created outside infrastructure-as-code, providing complete visibility for governance and troubleshooting.

      - Natural language search with AI
      - Multi-cloud resource discovery
      - Configuration change history
      - Resource relationship mapping
    image: /images/product/insights-governance/ig-visibility.png
    image_alt: Cloud resource search interface
    anchor: search

  - type: section_header_with_image
    tag_line: Developer-First Compliance
    title: Give developers AI-powered guardrails, not red tape
    description: |
      Developers get immediate policy feedback during deployment, with AI-generated fixes when issues arise. Platform teams get measurable compliance improvements without becoming bottlenecks. Policy enforcement accelerates development velocity.

      - Shift-left security with pre-deployment validation
      - Clear, actionable error messages
      - Policy-aware AI remediation
      - Measurable compliance improvements without velocity loss
    image: /images/product/insights-governance/ig-developer-first.png
    image_alt: AI-powered developer guardrails in practice
    anchor: guardrails

  - type: section_header
    title: Pre-built compliance frameworks ready to deploy
    description: |
      Stop building compliance policies from scratch. Deploy expert-authored policy packs that map directly to industry standards and audit requirements.
    cta_text: Explore the Policy Packs
    cta_link: /docs/insights/policy/get-started/
    anchor: frameworks

  - type: logo_banner
    bordered: true
    logos:
      - src: /images/product/insights-governance/ig-logo-cis.png
        alt: CIS Controls
      - src: /images/product/insights-governance/ig-logo-nist.png
        alt: NIST SP 800-53
      - src: /images/product/insights-governance/ig-logo-pci-dss.png
        alt: PCI DSS
      - src: /images/product/insights-governance/ig-logo-hitrust.png
        alt: HITRUST CSF
      - src: /images/product/insights-governance/ig-logo-aicpa.png
        alt: AICPA SOC
      - src: /images/product/insights-governance/ig-logo-fedramp.png
        alt: FedRAMP
      - src: /images/product/insights-governance/ig-logo-iso27001.png
        alt: ISO 27001
    anchor: frameworks-logos

  - type: feature_split
    heading: The complete governance lifecycle
    compact: true
    cards:
      - icon: fa-search
        title: "Step 1: Audit"
        description: |
          Continuous scans reveal compliance posture across existing infrastructure.

          - Discover violations across your entire infrastructure
          - Track compliance by framework (CIS, HITRUST, PCI DSS)
      - icon: fa-tasks
        title: "Step 2: Remediate"
        description: |
          AI generates infrastructure-as-code fixes for policy violations.

          - AI-powered fixes for policy violations
          - Automated pull requests with verified solutions
      - icon: fa-shield-alt
        title: "Step 3: Prevent"
        description: |
          Policy guardrails block non-compliant deployments automatically.

          - Block non-compliant deployments before production
          - Shift governance left to the development workflow
    anchor: lifecycle

  - type: two_column
    highlight_first_card: true
    columns:
      - title: Start with complete visibility
        description: |
          Get instant visibility into all your cloud resources. Add governance policies and AI-powered remediation to maintain compliance automatically.
        cta_primary_text: Get Started with Insights
        cta_primary_link: /docs/insights/get-started/
        cta_text: Book a Demo
        cta_link: /contact/?form=request-a-demo
      - title: Enforce compliance with policy as code
        description: |
          Deploy pre-built compliance packs for CIS, NIST, HITRUST, and PCI DSS, or write custom policies in TypeScript and Python.
        cta_primary_text: Get Started with Policies
        cta_primary_link: /docs/insights/policy/get-started/
        cta_text: Learn More
        cta_link: /docs/insights/policy/
    anchor: get-started
---
