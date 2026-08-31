---
title: Pricing
meta_desc: Pulumi IaC and Pulumi ESC are available in various editions and are free to individuals
type: page
layout: pricing
schema_type: product
schema_name: Pulumi
include_floqer: true
outputs:
    - HTML
    - markdown
menu:
    header:
        weight: 2
aliases:
    - /blog/tf-migration-offer

testimonial:
    quote: Pulumi helped our team ship a new product faster. We needed one tool to set up and manage multi-cloud, multi-region Kubernetes clusters that infrastructure and applications teams could use collaboratively.
    author: Justin Fitzhugh
    role: VP of Cloud Platform Engineering
    logo: snowflake

customers:
    - stat: "**5x faster** time to market"
      logo: unity
      link: /case-studies/unity
    - stat: "**100 days saved** each year with Pulumi Cloud instead of DIY state management"
      logo: starburst
      link: /case-studies/starburst
    - stat: "**10x faster deployments**, from weeks to hours"
      logo: snowflake
      link: /case-studies/snowflake

faq:
    - category: Pricing
      id: pricing
      items:
        - question: Do I pay as I go, or prepaid up-front?
          answer: |
            If you self-serve by entering a credit card, you will be charged an up-front fee at the beginning of each monthly term. The up-front fee will create a pool of Pulumi Credits. If your usage exceeds your Pulumi Credit pool, you will be billed in arrears for your usage at the end of the monthly term.

            If you prefer to pay annually, you can [contact sales](/contact/?form=sales) to receive a discount for a committed amount of usage paid up-front. If you subsequently consume all up-front purchased usage, you will be billed in arrears as you go beyond that amount of usage. The details are specified in your contract.
        - question: What are Pulumi Credits?
          answer: |
            Pulumi Credits are the single currency for Pulumi Cloud. One Pulumi Credit costs $1 USD, and you can pre-purchase Pulumi Credits as needed to cover expected usage either through a monthly up-front fee or annual agreement. All usage of Pulumi services will draw from the pool of Pulumi Credits at the rates above or as listed on your order form. Once the pool of Pulumi Credits is exhausted, you'll be billed in arrears for additional use at the rates above or as listed on your order form.
        - question: How are IaC resources billed?
          answer: |
            IaC resources are billed hourly at the rate of $0.00025 for Team ($0.1825 per resource per month) and starting at $0.0005 for Enterprise ($0.365 per resource per month). This is the cost of managing an IaC resource for a full hour.

            Enterprise plans receive volume discounts, so that the more resources you consume, the lower the incremental rate. This is true of self-serve pay-as-you-go plans, although prepaid plans offer more considerable discounts.

            For billing purposes, a partial resource hour used is billed as a full hour and we count any resource that's declared in a Pulumi program. This includes [provider resources](/docs/iac/concepts/resources/) (e.g., an Amazon S3 bucket), [component resources](/docs/iac/concepts/components) which are groupings of resources (e.g., an Amazon EKS cluster), and [stacks](/docs/iac/concepts/stacks) which contain resources (e.g., dev, test, prod stacks).
        - question: What can I do with 500 IaC resources per month?
          answer: |
            The Team edition includes up to 500 IaC resources to get started with.

            You could manage 500 EKS clusters or EC2 instances for a month using this amount. As another example, you could manage something more complex like a production Amazon EKS cluster with associated IAM roles, VPC, subnets, gateway route tables, and a small microservice deployed into the cluster.

            This is more than enough to get started with production workloads. The Enterprise plan includes up to 2,000 resources.
        - question: How do I find out how many IaC resources I have?
          answer: |
            There are several ways you can estimate the number of resources you have managed with Pulumi.

            - <u>If you are using Pulumi Cloud</u>: Navigate to the dashboard and review the resource graph titled “Resource Count over Time.”

            - <u>If using Pulumi with a DIY backend</u>: Export your stack state and count the number of lines with a universal resource name (URN). You can pipe the state through a grep command for "urn" to estimate the number of resources.

            - <u>If you haven't deployed anything with Pulumi</u>: See the previous FAQ for a few examples of applications and their number of resources.
        - question: What are some examples of how many IaC resources are needed for my use case?
          answer: |
            [**Serverless API with Amazon API Gateway and AWS Lambda**](https://github.com/pulumi/examples/tree/master/aws-ts-apigatewayv2-http-api)
            (Estimated resources: 9)

            This scenario is a stack with an Amazon API Gateway, an AWS Lambda event handler, and associated IAM roles.

            [**Amazon EKS running in a VPC**](https://github.com/pulumi/examples/tree/master/aws-py-eks)
            (Estimated resources: 20)

            This scenario is a stack with an Amazon VPC (including subnets, internet gateway, security groups, and route table), Amazon EKS cluster and node group, and associated IAM roles.

            [**Amazon ECS cluster and RDS backend running in a VPC**](https://github.com/pulumi/examples/tree/master/aws-py-wordpress-fargate-rds)
            (Estimated resources: 24)

            This scenario is a stack with an Amazon VPC (including subnets, security groups, and route table associations), Amazon ECS (including cluster and service, load balancer resources, and IAM resources), and Amazon RDS (including RDS instance and subnet group). Each group of resources (VPC, ECS, RDS) is represented by a component resource.
        - question: How are ESC secrets billed?
          answer: |
            ESC secrets are billed hourly at the rate of $0.000685 for Team ($0.50 per secret per month) and $0.001 for Enterprise ($0.75 per secret per month). This is the cost of managing an ESC secret for a full hour.

            For example, if you have your secrets stored for 4 days on Pulumi Cloud Team Edition, the price you pay would be 4 x 24 x 0.5 / 730 = $0.0657

            Secrets include both static secrets and dynamic secrets/credentials. When using the Pulumi ESC Document Editor, each definition of fn::secret:* and fn::open::* (except Pulumi-stacks provider) is counted as a secret. The number of secrets only from the latest environment revision is counted towards your billing.
        - question: How are ESC secrets API calls metered?
          answer: |
            You pay $0 for the first free 10K API calls / month to the [ReadOpen API](/docs/reference/cloud-rest-api/environments/) endpoint. Once you hit 10,000 API calls, you are metered at $0.1 for 10K API calls. If you use 5K API calls you will be billed $0.05.

            API usage includes any calls from the [CLI](/docs/iac/cli/commands/pulumi_env/), [SDK](/docs/esc/languages-sdks/), [Pulumi Cloud provider](/registry/packages/pulumiservice/api-docs/environment/), direct [REST API](/docs/reference/cloud-rest-api/environments/) call that hits the ReadOpen API endpoint
        - question: What are workflow minutes?
          answer: |
            Workflow minutes represent the total time used across both Discovery and Deployments. All usage draws from a single, shared pool of minutes. For Discovery, workflow minutes measure the time spent on discovery and policy execution. Deployments also consume workflow minutes by measuring the duration of each deployment process.
        - question: Can I prepay for resources, secrets, and secrets API calls?
          answer: Yes, you can! Please contact us to discuss the Enterprise and Business Critical editions, which include volume pricing for paying in advance.

        - question: What are Neo tokens?
          answer: |
            Neo tokens are the metering method for Neo-powered features (Neo tasks, pull-request annotations, and natural-language search) and cost $3 per million tokens. The volume of tokens used by any given activity varies with the number, complexity, and duration of Neo activities.

        - question: Can I manage Neo usage for my organization?
          answer: |
            Neo features can be managed in the Pulumi Cloud dashboard under Settings → Neo Settings. Neo integration with your version control system is located under Management → Version Control.

    - category: Product
      id: product
      items:
        - question: What are Pulumi open source and Pulumi Cloud?
          answer: |
            Pulumi's Infrastructure as Code CLI and SDK are an open-source project that is supported by an active community. [Pulumi Cloud](/product/) is a managed service for the open source CLI and SDK. It tracks your infrastructure’s state and coordinates updates with the CLI, which creates or updates resources to reach your infrastructure’s desired state. It also manages secrets, supports SAML SSO, integrates with CI/CD pipelines, enforces compliance rules, and much more.

            You're not required to use Pulumi Cloud. You can use any cloud or on-premises storage to build and run your own backend.
        - question: Can I use Pulumi for free?
          answer: |
            Yes! There are three ways to use Pulumi for free.

            First, Pulumi Cloud is free to use, now and forever, for individuals. You get all of the convenience of automatic state management, unlimited updates, and many other great features without needing to pay anything at all for it.

            Second, Pulumi is an [open-source project](https://github.com/pulumi/pulumi). You can [run Pulumi entirely offline](/docs/iac/concepts/state-and-backends#using-a-diy-backend) without the online service's features, and manage state yourself, instead of using the online service. There are no restrictions — it's all there in the open for you to use freely as you'd like.

            Finally, we offer a 14-day free trial for the Business Critical edition. Once the trial is over, you can continue to use the Business Critical Edition by chatting with sales or changing to Team or Enterprise Edition. After your trial expires, no data will be lost, and there is a grace period.
        - question: What is an organization? What are projects and stacks?
          answer: |
            The Individual Edition is great for single users with private projects. However, if you are working within a team, you'll typically want to share your projects, for which you need to create an organization. The Team Edition is designed for teams to collaborate on shared infrastructure projects. The Enterprise Edition offers more sophisticated organization management facilities, including RBAC for advanced policy controls.

            Pulumi [projects](/docs/iac/concepts/projects/) and [stacks](/docs/iac/concepts/stacks/) are a way to organize Pulumi code. You can consider a Pulumi project to be analogous to a GitHub repo: a single place for code — and a stack to be an instance of that code which has a separate configuration. For instance, a single project may have multiple stacks for dev, test, prod, or perhaps for different cloud configurations (e.g., geographic region) or developer environments.
        - question: How do I get started?
          answer: Follow the [Getting Started guide](/docs/get-started/), which walks you through creating and deploying your first Pulumi project.
        - question: How do I move from Starter or Pro to the new Team Edition?
          answer: We recommend moving from the old SKUs to get access to our latest capabilities like Pulumi Deployments, Discovery, and Neo. [Contact us](/contact/?form=sales) to move to the new Team Edition.
        - question: Is Pulumi SOC 2 compliant?
          answer: Yes, Pulumi has completed the SOC 2 Type 2 compliance process. Pulumi is committed to operational excellence for our customers.
        - question: Can I host Pulumi Cloud in my cloud or datacenter?
          answer: Yes, we offer a self-hosted Pulumi Cloud for companies that have specific data control requirements and want to maintain complete control over hosting Pulumi Cloud. This option is available in Business Critical Edition. You can [request a Proof of Concept (PoC)](/product/self-hosted/#self-hosted-trial) to get started.
        - question: How do I convince my boss?
          answer: |
            Do you want to use Pulumi in your organization, but aren't sure how to bring it up with your boss? We've created a sample email to help you explain its benefits. Feel free to use the full letter or pieces of it. We are always happy to meet to learn more about your needs and explain these benefits in person — just [contact us](/contact/?form=sales).

            **Sample Email**

            >Dear {Name},
            >
            >I'd like to propose that we use Pulumi for our cloud infrastructure needs. I've researched the top infrastructure as code platforms, and Pulumi stands out because of its maturity, strong open source community, support for many clouds, and mix of productivity and enterprise controls, meaning it works great for developers and infrastructure teams alike.
            >
            >I discovered that Pulumi's community is over 10,000 people and growing, and their customer base includes a diverse array of companies, from startups to some of the largest Fortune 500 and Global 2000 organizations. The top four reasons people are choosing Pulumi are 1) it tames cloud complexity and reduces infrastructure risks, 2) it lets teams use software engineering best practices with infrastructure, 3) it helps teams adopt modern cloud architectures, and 4) it increases collaboration between infrastructure teams, developers, and security engineers.
            >
            >Here are some examples of their customers to give you an idea of who is using it and why:
            >
            >- [BMW](/case-studies/bmw/) and Fenergo can now release new features faster by empowering their developers to deploy cloud infrastructure easily.
            >- [Snowflake migrated to](/case-studies/snowflake/) Kubernetes across multiple clouds in three months.
            >- [Mercedes-Benz](/case-studies/mercedes-benz/) Research & Development North America improved collaboration between its infrastructure and application development teams.
            >- [Skai](/blog/kenshoo-migrates-to-aws-with-pulumi/) managed a complex public cloud migration project.
            >- [Wiz](/case-studies/wiz/), [Supabase](/case-studies/supabase/), and [Lemonade](/case-studies/lemonade/) created innovative engineering cultures.
            >
            >Pulumi is open source and has a SaaS product that helps organizations like ours manage infrastructure with advanced security and policies. Because it's a SaaS, we can start small and grow as our success with the product grows.
            >
            >You can learn more on the Pulumi website or view a short introduction video.
            >
            >I have many ideas on how Pulumi would deliver immediate value to our team. Should I write a more detailed proposal and share it with you or other members of the team for feedback? The Pulumi team has also offered to have a meeting with us to learn more about our use cases, and discuss potential ways we can work together. Should I set that up?
            >
            >Thanks,
            >
            >{Your Name}

    - category: Billing and Support
      id: billing
      items:
        - question: How can I keep track of my usage?
          answer: You can keep track of current usage and upcoming charges by navigating to Settings and then Billing & Usage in the Pulumi Cloud console.
        - question: When will I be billed for using Team or Enterprise Edition?
          answer: In addition to your monthly up-front fee, you will be billed for the previous month’s on-demand usage on the first day of each month.
        - question: What payment options do you accept?
          answer: For the Pulumi Team Edition, you can pay with a credit card (we use Stripe for processing). Pulumi Enterprise Edition offers additional payment options. Please [contact us](/contact/?form=sales) for those options.
        - question: What if I have billing or account issues?
          answer: For any billing or related issues, please [contact us](/contact/).
        - question: What if I am not satisfied with my Pulumi purchase?
          answer: If you're not satisfied with Pulumi, we offer a 14-day money-back guarantee, no questions asked. [Contact us](/contact/).
        - question: How do I get support for Pulumi?
          answer: 12 x 5, 24 x 7 support, professional and advising services, and private Slack channel are available to purchase in the Enterprise and Business Critical editions of Pulumi Cloud. [Contact us](/contact/?form=sales) if you need help or have any questions.
        - question: Does Pulumi charge sales tax?
          answer: You may be charged a sales tax in addition to your usage fees in certain jurisdictions. It will be a separate line item on your bill.
---
