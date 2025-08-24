---
title: Pulumi Insights
layout: pulumi-insights

meta_desc: Cloud security, compliance, and governance platform. Policy as code, asset management, and intelligence for your entire cloud estate.

aliases:
- /insights
- /crossguard
- /product/crossguard

overview:
    header: Pulumi Insights
    title: Cloud Security Posture Management (CSPM) that actually works
    body: |
      Pulumi Insights provides complete visibility, compliance, and control over your cloud infrastructure. Enforce policies before deployment, continuously scan for violations, auto-remediate issues, and maintain a real-time inventory of every resource across every cloud. Whether resources were created with Pulumi, Terraform, CloudFormation, or manually.
    items:
        - title: Policy as Code
          icon: shield
          icon_color: purple
          description: |
            Write policies in real programming languages. Enforce security and compliance rules automatically.

        - title: Asset Inventory
          icon: eye
          icon_color: yellow
          description: |
            Complete visibility into every cloud resource. Search, analyze, and track everything in one place.

        - title: Continuous Compliance
          icon: cycle
          icon_color: blue
          description: |
            Scan continuously for violations. Auto-remediate issues. Stay compliant 24/7.

policy_as_code:
    title: CrossGuard - Policy as Code
    description: |
        Stop misconfigurations before they reach production. Write policies in TypeScript, Python, or Go that run on every deployment. Block non-compliant infrastructure automatically.
    capabilities:
        - title: "Preventive Controls"
          description: "Enforce policies during deployment to prevent misconfigurations"
          example: "Block public S3 buckets, require encryption, enforce tagging"
          
        - title: "Detective Controls"
          description: "Continuously scan existing infrastructure for policy violations"
          example: "Find unencrypted databases, exposed endpoints, non-compliant resources"
          
        - title: "Corrective Controls"
          description: "Automatically fix violations when detected"
          example: "Enable encryption, add required tags, close security groups"
          
        - title: "Compliance Frameworks"
          description: "Pre-built policies for SOC2, PCI DSS, HIPAA, CIS, and more"
          example: "150+ policies across AWS, Azure, GCP, and Kubernetes"

asset_management:
    title: Complete Cloud Asset Inventory
    description: |
        See everything running in your cloud. Insights discovers and indexes all resources - whether created with Pulumi, other IaC tools, or manually through the console.
    features:
        - title: "Multi-Cloud Discovery"
          description: "Scan AWS, Azure, GCP, Kubernetes automatically"
          icon: clouds
        - title: "Relationship Mapping"
          description: "Understand dependencies and connections between resources"
          icon: network
        - title: "Change Tracking"
          description: "Track who changed what, when, and why"
          icon: clock
        - title: "Cost Attribution"
          description: "See costs by team, project, environment, or any tag"
          icon: gear

search_analytics:
    title: Powerful Search and Analytics
    description: |
        Query your entire cloud estate with SQL-like syntax or natural language. Find anything, analyze trends, export data.
    examples:
        - query: "SELECT * FROM resources WHERE type = 'aws:s3:Bucket' AND tags.environment != 'production'"
          description: "Find all non-production S3 buckets"
        - query: "Show me untagged EC2 instances larger than t2.medium"
          description: "Natural language search for cost optimization"
        - query: "Resources created in the last 24 hours by team=platform"
          description: "Track recent changes by team"

compliance_automation:
    title: Automated Compliance and Governance
    description: |
        Stop playing whack-a-mole with compliance violations. Set policies once, enforce them everywhere, continuously.
    workflow:
        - title: "Define Policies"
          description: "Write policies in code or use pre-built compliance packs"
        - title: "Enforce Everywhere"
          description: "Policies run on every deployment and continuously in production"
        - title: "Auto-Remediate"
          description: "Automatically fix violations or create tickets for manual review"
        - title: "Audit & Report"
          description: "Complete audit trail and compliance reports for regulators"

enterprise_compliance:
    title: Enterprise Compliance Packs
    description: |
        Business Critical customers get access to comprehensive compliance frameworks maintained by Pulumi.
    frameworks:
        - name: "SOC 2"
          description: "Complete SOC 2 compliance policies"
        - name: "PCI DSS"
          description: "Payment card industry standards"
        - name: "HIPAA"
          description: "Healthcare compliance requirements"
        - name: "CIS Benchmarks"
          description: "Center for Internet Security best practices"
        - name: "ISO 27001"
          description: "Information security management"
        - name: "NIST"
          description: "Cybersecurity framework policies"

remediation:
    title: Intelligent Auto-Remediation
    description: |
        Don't just detect problems - fix them automatically. Insights can remediate common violations without human intervention.
    examples:
        - title: "Security Remediation"
          items:
            - "Close overly permissive security groups"
            - "Enable encryption on storage resources"
            - "Rotate expired certificates and keys"
        - title: "Cost Remediation"
          items:
            - "Right-size over-provisioned instances"
            - "Delete unattached volumes and IPs"
            - "Schedule non-production resources"
        - title: "Compliance Remediation"
          items:
            - "Add required tags to resources"
            - "Enable audit logging"
            - "Configure backup policies"

drift_detection:
    title: Drift Detection and Prevention
    description: |
        Know immediately when infrastructure drifts from desired state. Automatically correct drift or alert the right team.
    features:
        - title: "Continuous Monitoring"
          description: "Detect drift within minutes of changes"
        - title: "Smart Notifications"
          description: "Alert only on meaningful drift, not noise"
        - title: "Automatic Correction"
          description: "Optionally auto-correct drift to maintain desired state"

customer_quotes:
  title: Security and Compliance Success Stories
  items:
    - text: |
        "Pulumi Insights reduced our compliance audit from 3 weeks to 3 days. The automated evidence collection alone saved us countless hours."
      author: "CISO, Healthcare Technology Company"
      
    - text: |
        "We went from 500+ policy violations to zero in under a month. Auto-remediation fixed 90% without any manual intervention."
      author: "Cloud Security Lead, Financial Services"
      
    - text: |
        "CrossGuard policies caught a misconfiguration that would have exposed customer data. It paid for itself on day one."
      author: "DevSecOps Engineer, E-commerce Platform"

integrations:
    title: Integrates with Your Security Stack
    description: |
        Pulumi Insights works with your existing security and compliance tools.
    tools:
        - category: "SIEM"
          items: ["Splunk", "Datadog", "New Relic", "Elastic"]
        - category: "Ticketing"
          items: ["Jira", "ServiceNow", "PagerDuty"]
        - category: "Data Warehouse"
          items: ["Snowflake", "BigQuery", "Redshift", "Databricks"]

pricing:
    title: Pricing
    description: |
        Pulumi Insights is included for all resources managed by Pulumi Cloud. Advanced compliance packs and unlimited scanning available on Enterprise plans.

get_started:
    title: Secure Your Cloud Today
    description: |
        Start with policy as code. Scale to complete cloud governance. Get visibility, compliance, and control over your entire cloud estate.
---