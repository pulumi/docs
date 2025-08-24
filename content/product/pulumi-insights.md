---
title: Cloud Intelligence
layout: pulumi-insights

meta_desc: AI-powered cloud intelligence. Understand, optimize, and secure your infrastructure with natural language queries and automated insights.

aliases:
- /insights
- /product/ai-assistant

overview:
    header: Cloud Intelligence
    title: AI-powered insights for your infrastructure
    body: |
      Pulumi Cloud Intelligence combines AI assistance, search capabilities, and analytics to help you understand and optimize your cloud. Ask questions in natural language, find resources across clouds, detect security issues, and get cost optimization recommendations - all powered by AI that understands your infrastructure.
    items:
        - title: AI Assistant
          icon: bot
          icon_color: purple
          description: |
            Generate code, debug failures, and get answers about your infrastructure using natural language.

        - title: Smart Search
          icon: eye
          icon_color: yellow
          description: |
            Find any resource across all your clouds with structured queries or natural language prompts.

        - title: Cost Optimization
          icon: gear
          icon_color: blue
          description: |
            Identify waste, unused resources, and cost-saving opportunities automatically.

ai_copilot:
    title: Pulumi Copilot - Your AI Infrastructure Assistant
    description: |
        Pulumi Copilot understands your entire infrastructure context. Ask questions, generate code, debug issues, and get recommendations - all in natural language.
    capabilities:
        - title: "Generate Infrastructure Code"
          example: '"Create a serverless API on AWS with DynamoDB"'
          description: "Generate complete Pulumi programs from natural language descriptions"
          
        - title: "Debug Deployment Failures"
          example: '"Why did my deployment fail yesterday?"'
          description: "Analyze logs and errors to pinpoint and fix issues quickly"
          
        - title: "Find Security Issues"
          example: '"Do I have any public S3 buckets?"'
          description: "Scan for vulnerabilities and compliance violations automatically"
          
        - title: "Optimize Costs"
          example: '"What are my most expensive unused resources?"'
          description: "Identify waste and get specific recommendations to reduce spend"

search:
    title: Resource Search - Find Anything, Anywhere
    description: |
        Search across all your clouds, accounts, and regions with powerful queries. Use SQL-like syntax for precision or natural language for convenience.
    features:
        - title: "Multi-Cloud Search"
          description: "Query resources across AWS, Azure, GCP, Kubernetes, and 100+ providers"
        - title: "Natural Language"
          description: "Ask questions like 'Show me all untagged EC2 instances in production'"
        - title: "Saved Queries"
          description: "Save and share common searches with your team"
        - title: "API Access"
          description: "Integrate search results into your workflows and dashboards"

analytics:
    title: Analytics & Insights
    description: |
        Get automatic insights into your infrastructure health, costs, and compliance posture. Track trends, detect anomalies, and make data-driven decisions.
    dashboards:
        - title: "Cost Analytics"
          description: "Track spending trends, identify cost drivers, forecast future costs"
        - title: "Security Dashboard"
          description: "Monitor compliance violations, security risks, and remediation progress"
        - title: "Team Activity"
          description: "See who's deploying what, track productivity, audit changes"
        - title: "Resource Inventory"
          description: "Complete inventory of all cloud resources with metadata and relationships"

intelligence_features:
    title: Intelligent Automation
    items:
        - title: "Drift Detection"
          description: "Automatically detect when cloud resources have changed outside of Pulumi"
          icon: cycle
          
        - title: "Policy Violations"
          description: "Continuous scanning for security and compliance violations with auto-remediation"
          icon: shield
          
        - title: "Anomaly Detection"
          description: "AI-powered detection of unusual patterns in costs, deployments, or resource usage"
          icon: alert
          
        - title: "Smart Recommendations"
          description: "Proactive suggestions for cost savings, security improvements, and best practices"
          icon: lightning

customer_quotes:
  alkira:
    text: |
      "Pulumi Copilot and Insights make it really easy to find idle developer environments that need to be shut down, which reduces our cloud costs significantly. The AI understands our infrastructure and helps developers be more productive."
    author: Santosh Dornal, Head of Software Test & DevOps
    logo: alkira

how_it_works:
    title: How Cloud Intelligence Works
    steps:
        - title: "Connect Your Clouds"
          description: "Sync all your cloud accounts - including resources not managed by Pulumi"
        - title: "AI Learns Your Infrastructure"
          description: "Copilot builds understanding of your resources, relationships, and patterns"
        - title: "Ask Anything"
          description: "Query in natural language or structured search across everything"
        - title: "Get Actionable Insights"
          description: "Receive recommendations, detect issues, and automate fixes"

pricing:
    title: Pricing
    description: |
        Cloud Intelligence features are included with Pulumi Cloud. Copilot is available on all plans. Advanced analytics and unlimited queries available on Team and Enterprise plans.

get_started:
    title: Get started with Cloud Intelligence
    description: |
        Start asking questions about your infrastructure today. Pulumi Copilot is ready to help you understand, optimize, and secure your cloud.
---