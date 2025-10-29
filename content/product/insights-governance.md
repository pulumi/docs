---
title: Cloud Asset and Compliance Management – Pulumi Insights
layout: insights-governance

heading: Insights & Governance
subheading: |
    Complete visibility and control for your cloud

meta_desc: Join us on November 5 to see how Neo helps you get clean and stay clean - automatically. Watch it in action. Live demo + Q&A.
meta_image: /images/product/insights-neo-launch-meta.png

aliases:
- /insights
- /product/pulumi-insights
- /product/crossguard
- /crossguard

preview:
  header:  Pulumi Neo just got smarter about infrastructure policy automation
  description: "Join us on November 5 at 10:00 AM PT / 18:00 UTC for Pulumi Policies: Get Clean and Stay Clean Automatically. Watch the live demo and join the Q&A."
  hubspotID: 4031229e-1370-4118-9379-ee2be1fd64fd
  videoID: mwcrOTEf1EQ?si=Fx77RxM-uCjJLN-6

overview:
    header: Complete visibility and control for your cloud
    title: Continuous Compliance, By Construction
    subtitle: See everything. Control everything. Ship with confidence.
    body: |
      Stop compliance violations before they become problems. Pulumi Insights & Governance provides a complete lifecycle for auditing existing infrastructure, fixing violations with AI-powered remediation, and preventing future infrastructure issues using policy-as-code guardrails.
      
      Pulumi Policies and Neo close the loop from detection to remediation, ensuring your infrastructure stays secure, compliant, and well-governed automatically.

    items:
        - title: Policy as Code
          icon: shield
          icon_color: purple
          description: |
            Write policies in TypeScript or Python. Hundreds of built-in policies. Block bad configurations before they ship. Auto-remediate existing violations.

        - title: Cloud Resource Search
          icon: eye
          icon_color: yellow
          description: |
            Search across all your clouds using structured queries or natural language. Find resources, track dependencies, identify security risks and compliance violations.

        - title: Complete Cloud Visibility
          icon: global
          icon_color: blue
          description: |
            See every resource across AWS, Azure, GCP, and thousands of providers. Track relationships, monitor drift, identify unused resources. 


features:
  - header: Audit Existing Infrastructure Against Compliance Standards
    body: |
      Works with ANY infrastructure—Pulumi, Terraform, CloudFormation, or manual deployments.

      Continuous audit scans evaluate your entire infrastructure against industry frameworks without disrupting deployment pipelines. Non-blocking compliance checks provide instant visibility into your security posture across CIS Controls, NIST SP 800-53, HITRUST CSF, and PCI DSS standards.
    items:
      - Pre-built compliance frameworks ready to deploy
      - Evaluate existing infrastructure on demand with audit mode
      - Automatic triggers after deployments
      - Auditor-friendly compliance reporting
    graphic: /images/product/insights-findings.png
  - header: Automatically Generate Fixes for Policy Violations
    body: Pulumi Neo analyzes policy issues and automatically generates infrastructure-as-code remediation. For resources created outside your control (shadow IT, manual console changes), Neo discovers them, imports them into Pulumi, and fixes compliance violations in a single workflow, eliminating surprise audit findings and cost overruns. Transform hours of manual work into simple review-and-merge processes.
    items:
    - AI-generated infrastructure-as-code fixes
    - Import and remediate unmanaged resources
    - Integrated approval workflows
    - Complete audit trails for compliance
    - Governance-aware remediation with policy compliance checks
    graphic: /images/product/insights-remediate.png
  - header: Prevent Non-Compliant Deployments Before Production
    body: Write governance policies in TypeScript or Python, languages your team already knows. Deploy pre-built compliance packs or create custom rules that enforce your organization's standards. Policies block problematic configurations during deployment, providing immediate feedback to developers within their existing workflows.
    items:
    - Policy-as-code in TypeScript/Python (no DSLs)
    - Pre-built packs for CIS, NIST, HITRUST, PCI DSS
    - Progressive enforcement (advisory → mandatory)
    - Immediate feedback during deployment workflows
    - Neo-generated infrastructure automatically complies with policy standards
    graphic: /images/product/insights-blocking.png
  - header: Search and Understand Your Entire Cloud Footprint
    body: Query any resource across major clouds with natural language or advanced filters. Track configuration changes, analyze relationships between resources, and get answers about your infrastructure in seconds. Pulumi discovers all resources, including those created outside infrastructure-as-code, providing complete visibility for governance and troubleshooting.
    items:
    - Natural language search with AI
    - Multi-cloud resource discovery
    - Configuration change history
    - Resource relationship mapping
    graphic: /images/product/insights-search.png
  - header: Give Developers AI-Powered Guardrails, Not Red Tape
    body: Developers get immediate policy feedback during deployment, with AI-generated fixes when issues arise. Platform teams get measurable compliance improvements without becoming bottlenecks. Policy enforcement accelerates development velocity.
    items:
    - Shift-left security with pre-deployment validation
    - Clear, actionable error messages
    - Policy-aware AI remediation
    - Measurable compliance improvements without velocity loss
    graphic: /images/product/insights-advisory.png
compliance_frameworks:
    title: Pre-Built Compliance Frameworks Ready to Deploy
    description: Stop building compliance policies from scratch. Deploy expert-authored policy packs that map directly to industry standards and audit requirements.
    items:
    - /images/product/cis.png
    - /images/product/nist.png
    - /images/product/pci-dss.png
    - /images/product/hitrust.png
    - /images/product/aicpa.png
    - /images/product/fedramp.png
    - /images/product/iso-20071.png

governance:
    title: The Complete Governance Lifecycle
    image: /images/product/insights-diagram.svg
    items:
    - header: "Step 1: Audit"
      body: Continuous scans reveal compliance posture across existing infrastructure
    - header: "Step 2: Remediate"
      body: AI generates infrastructure-as-code fixes for policy violations
    - header: "Step 3: Prevent"
      body: Policy guardrails block non-compliant deployments automatically

customer_quotes:
  spear:
    text: |
      “We gave our auditors access to our policy packs because it's far easier to understand and prove controls in code than in docs and diagrams. With Pulumi's Policy as Code approach, that manual review process has gone away. We've reduced our Authority to Operate (ATO) timeline from a year and a half to expecting approval in three months.”
    author: Michael Hunter, CEO, Spear AI
    logo: spearAI

analytics:
    title: Analytics & Intelligence
    subtitle: Data-driven infrastructure decisions
    image: /images/product/pulumi-insights-analytics.png
    description: |
        Transform infrastructure data into actionable intelligence. Track costs, identify trends, detect anomalies, and measure compliance. Export to Snowflake, BigQuery, or any data warehouse. Build custom dashboards, automate reports, and integrate with your existing BI tools. Make informed decisions backed by comprehensive cloud analytics.

pricing:
    title: Pricing
    description: |
         Insights & Governance capabilities are included with Pulumi Cloud. Get visibility and control over all your cloud resources, whether managed by Pulumi or not.

         **Pulumi Neo's policy remediation capabilities and pre-built compliance frameworks.** CIS Controls, NIST SP 800-53, PCI DSS v4.0, and HITRUST CSF v11.5 compliance packs are available starting with Team tier. Continuous compliance monitoring and AI-powered fix generation are available in Team, Enterprise, and Business Critical editions.

learn:
    title: Take control of your cloud
    items:
        - title: Start with complete visibility
          description: |
            Get instant visibility into all your cloud resources. Add governance policies and optimize with AI-powered insights.
          buttons:
            - link: /docs/insights/get-started/
              type: primary
              action: Get Started with Pulumi Insights
            - link: /contact/?form=request-a-demo
              type: secondary
              action: Book a Demo
        - title: Transform Governance from Bottleneck to Competitive Advantage
          description: |
            Start with audit scans to understand your compliance posture. Add AI-powered remediation to eliminate issue backlogs. Deploy preventive policies to maintain compliance automatically.
          buttons:
            - link: /docs/insights/policy/get-started/ 
              type: primary
              action: Get Started with Pulumi Policies
            - link: https://app.pulumi.com/signup
              type: secondary
              action: Try Pulumi Cloud for Free
---
