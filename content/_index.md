---
title: The infrastructure as code platform for the AI era – Pulumi
meta_desc: Pulumi is an open-source infrastructure as code platform that helps humans and agents build and manage cloud infrastructure with real programming languages.
meta_image: /images/home/home-meta.png

include_organization_schema: true

sections:
  - type: hero
    layout: split
    badge_highlight_text: "New Release:"
    badge_text: "Building for the Agentic Era"
    badge_link: /releases/agentic-infrastructure-era/
    title_primary: "Next-level"
    title_secondary: "infrastructure as code \n for humans and agents."
    description: |
      Ship cloud infrastructure at the speed of AI with languages and tools that stay out of your way.
    anchor: hero
    code_overlay_image: /images/home/home-hero-code-overlay.svg
    code_aspect_ratio: "666/513"
    code_offsets:
      top: "0%"
      right: "0%"
      left: "23%"
      bottom: "30%"
    code_title: "index.ts"
    code_snippets:
      - language: typescript
        label: TypeScript
        title: "index.ts"
        code: |
          import * as aws from "@pulumi/aws";
          import * as awsx from "@pulumi/awsx";

          const vpc = new awsx.ec2.Vpc("vpc");
          const azs = await aws.getAvailabilityZones({ state: "available" });

          const subnets = azs.names.map((az, i) =>
            new aws.ec2.Subnet(`subnet-${i}`, {
              vpcId: vpc.vpcId,
              cidrBlock: `10.0.${i}.0/24`,
              availabilityZone: az,
            })
          );

      - language: python
        label: Python
        title: "__main__.py"
        code: |
          import pulumi_aws as aws
          import pulumi_awsx as awsx

          azs = aws.get_availability_zones(state="available")
          vpc = awsx.ec2.Vpc("vpc")

          for i, az in enumerate(azs.names):
              aws.ec2.Subnet(f"subnet-{i}",
                  vpc_id=vpc.vpc_id,
                  cidr_block=f"10.0.{i}.0/24",
                  availability_zone=az,
              )

      - language: go
        label: Go
        title: "main.go"
        code: |
          package main

          import (
              "fmt"

              "github.com/pulumi/pulumi-aws/sdk/v6/go/aws"
              "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
              awsx "github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
              "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
          )

          func main() {
              pulumi.Run(func(ctx *pulumi.Context) error {
                  vpc, _ := awsx.NewVpc(ctx, "vpc", nil)
                  azs, _ := aws.GetAvailabilityZones(ctx, &aws.GetAvailabilityZonesArgs{State: pulumi.StringRef("available")}, nil)

                  for i, az := range azs.Names {
                      ec2.NewSubnet(ctx, fmt.Sprintf("subnet-%d", i), &ec2.SubnetArgs{
                          VpcId:            vpc.VpcId,
                          CidrBlock:        pulumi.String(fmt.Sprintf("10.0.%d.0/24", i)),
                          AvailabilityZone: pulumi.String(az),
                      })
                  }
                  return nil
              })
          }

      - language: csharp
        label: C#
        title: "MyStack.cs"
        code: |
          using System.Linq;
          using Pulumi;
          using Pulumi.Aws;
          using Pulumi.Aws.Ec2;

          return await Deployment.RunAsync(() =>
          {
              var vpc = new Pulumi.Awsx.Ec2.Vpc("vpc");
              var azs = GetAvailabilityZones.Invoke(new() { State = "available" });

              var subnets = azs.Apply(result =>
                  result.Names.Select((az, i) =>
                      new Subnet($"subnet-{i}", new()
                      {
                          VpcId = vpc.VpcId,
                          CidrBlock = $"10.0.{i}.0/24",
                          AvailabilityZone = az,
                      })
                  ).ToList()
              );
          });
      - language: java
        label: Java
        title: "App.java"
        code: |
          package myproject;

          import com.pulumi.Pulumi;
          import com.pulumi.aws.ec2.Vpc;
          import com.pulumi.aws.ec2.Subnet;
          import com.pulumi.aws.ec2.SubnetArgs;
          import com.pulumi.aws.AwsFunctions;
          import com.pulumi.aws.inputs.GetAvailabilityZonesPlainArgs;

          public class App {
              public static void main(String[] args) {
                  Pulumi.run(ctx -> {
                      var vpc = new Vpc("vpc");

                      var azs = AwsFunctions.getAvailabilityZonesPlain(
                          GetAvailabilityZonesPlainArgs.builder()
                              .state("available")
                              .build()
                      ).join();

                      var names = azs.names();
                      for (int i = 0; i < names.size(); i++) {
                          new Subnet("subnet-" + i, SubnetArgs.builder()
                              .vpcId(vpc.id())
                              .cidrBlock("10.0." + i + ".0/24")
                              .availabilityZone(names.get(i))
                              .build());
                      }
                  });
              }
          }
      - language: yaml
        label: YAML
        title: "Pulumi.yaml"
        code: |
          variables:
            azs:
              fn::invoke:
                function: aws:getAvailabilityZones
                arguments:
                  state: available

          resources:
            vpc:
              type: awsx:ec2:Vpc

            subnet-0:
              type: aws:ec2:Subnet
              properties:
                vpcId: ${vpc.vpcId}
                cidrBlock: "10.0.0.0/24"
                availabilityZone: ${azs.names[0]}

            subnet-1:
              type: aws:ec2:Subnet
              properties:
                vpcId: ${vpc.vpcId}
                cidrBlock: "10.0.1.0/24"
                availabilityZone: ${azs.names[1]}

  - type: logo_carousel
    title: Trusted by over 4,000 innovative companies
    logos:
      - name: bmw
        link: /case-studies/
      - name: snowflake
        link: /case-studies/
      - name: nvidia
        link: /case-studies/
      - name: moderna
        link: /case-studies/
      - name: docker
        link: /case-studies/
      - name: unity
        link: /case-studies/
      - name: supabase
        link: /case-studies/
      - name: ae-networks
        link: /case-studies/
      - name: deloitte
        link: /case-studies/
      - name: stokespace
        link: /case-studies/
      - name: univision
        link: /case-studies/
      - name: washington-trust
        link: /case-studies/
      - name: kyruus
        link: /case-studies/
      - name: modular-ai
        link: /case-studies/
      - name: korber
        link: /case-studies/
      - name: lemonade
        link: /case-studies/
      - name: pinecone
        link: /case-studies/
      - name: ware2go
        link: /case-studies/
      - name: nubank
        link: /case-studies/
      - name: mindbody
        link: /case-studies/
      - name: fenergo
        link: /case-studies/
      - name: webflow
        link: /case-studies/
      - name: bluenile
        link: /case-studies/
      - name: dutchie
        link: /case-studies/
      - name: panther-labs
        link: /case-studies/
      - name: materialize
        link: /case-studies/
      - name: altana
        link: /case-studies/
      - name: mercedes-benz
        link: /case-studies/
      - name: bt
        link: /case-studies/
      - name: portx
        link: /case-studies/
      - name: tivityhealth
        link: /case-studies/
      - name: starburst
        link: /case-studies/
      - name: linktree
        link: /case-studies/
    anchor: logos

  - type: feature_split
    heading: The **complete platform** for infrastructure teams
    description: |
      **From open source IaC to AI-driven workflows, Pulumi gives platform teams all they need to build and scale cloud infrastructure.**

      A unified platform built on real programming languages that covers the full infrastructure stack, so your team can focus on shipping.
    cta_text: Explore the platform
    cta_link: /product/
    cards:
      - image: /images/home/languages-card-image.svg
        image_alt: Programming language logos
        title: Real languages
        description: Write infrastructure code in TypeScript, Python, Go, C#, or Java — the same languages your team already uses to build software.
      - image: /images/home/secure-card-image.svg
        image_alt: Security shield illustration
        title: Secure by default
        description: Meet compliance requirements with encrypted secrets, dynamic credentials, and full audit trails. Pulumi is SOC 2 Type II certified.
      - image: /images/home/ai-card-image.svg
        image_alt: AI for infrastructure illustration
        title: AI for infrastructure
        description: Generate, debug, and refactor your infrastructure code with built-in best practices and full organizational context.
    anchor: platform

  - type: testimonial
    quote: Pulumi helped our team to ship a new product faster. We needed one tool to set up and manage multi-cloud, multi-region Kubernetes clusters that infrastructure and applications teams could use collaboratively.
    author: Justin Fitzhugh
    title: VP of Cloud Platform Engineering
    company: Snowflake
    logo: logos/customers/snowflake.svg
    anchor: testimonial

  - type: card_grid
    large_cards:
      - title: Don't just write IaC — compose it
        description: |
          Take advantage of your language of choice to build reusable components and share them with package managers like npm, PyPI, and NuGet. Get all of the benefits of your IDE, including type checking, code navigation, inline docs, testing, and more.

        image: /images/home/iac-card-image.svg
        image_alt: Pulumi infrastructure as code editor
        cta_text: Learn more about IaC
        cta_link: /product/infrastructure-as-code/
      - title: Meet Neo, your AI platform engineer
        description: |
          The first AI agent built for infrastructure. Pulumi Neo understands your code and organizational context, respects your policies, and executes complex tasks end-to-end — with or without a human in the loop.
        image: /images/home/neo-card-image.svg
        image_alt: Pulumi Neo AI platform engineer
        cta_text: Learn more about Neo
        cta_link: /product/neo/
    small_cards:
      - title: Centralized configuration & secrets
        description: |
          A single interface across all of your secrets. Pull in Vault, AWS Secrets Manager, Azure Key Vault, and more, plus support for short-lived creds with OIDC.
        image: /images/home/esc-card-image.svg
        image_alt: Pulumi ESC secrets management
        cta_text: Learn more about Pulumi ESC
        cta_link: /product/secrets-management/
      - title: Insights & governance
        description: |
          Use natural language queries to find managed and unmanaged resources — even across clouds. Enforce policies, track compliance in real-time, and find vulnerabilities before they become incidents.
        image: /images/home/ig-card-image.svg
        image_alt: Pulumi Insights governance dashboard
        cta_text: Learn more about insights & governance
        cta_link: /product/insights-governance/
      - title: Self-service infrastructure
        description: |
          Define golden paths for approved infrastructure with configurable components and customizable templates that enable developers while keeping platform teams in control.
        image: /images/home/idp-card-image.svg
        image_alt: Pulumi internal developer platform
        cta_text: Learn more about IDP
        cta_link: /product/internal-developer-platforms/
    anchor: products

  - type: case_study_cards
    title: Trusted by 4,000+ innovative companies
    description: See how engineering teams use Pulumi to ship infrastructure faster, improve security, and reduce cloud complexity.
    cta_text: Read our customer stories
    cta_link: /case-studies/
    cards:
      - slug: bmw
        size: half
      - slug: wiz
        size: half
      - slug: snowflake
        size: full
      - slug: supabase
        size: full
      - slug: atlassian
        size: half
      - slug: mercedes-benz
        size: half
      - slug: lemonade
        size: full
      - slug: unity
        size: full
      - slug: starburst
        size: half
      - slug: panther-labs
        size: half
    anchor: case-studies

  - type: social_carousel
    title: Open source. Built by engineers for engineers.
    description: Join the Pulumi community, and let's build together.
    cta_text: Join us on Slack
    cta_link: https://slack.pulumi.com/
    tweets:
      - source: twitter
        username: "@BryanMigliorisi"
        avatar: https://pbs.twimg.com/profile_images/752334791782039552/BsVNGBaV_200x200.jpg
        link: https://twitter.com/BryanMigliorisi/status/1450123026901651460
        text: |
          There is no way around the fact that devops is complicated but @PulumiCorp is a game changer for me.  Blows away CloudForamtion, TerraForm, CDK, etc.
      - source: twitter
        username: "@justedagain"
        avatar: https://pbs.twimg.com/profile_images/1576905831626440706/wigR9_hF_200x200.jpg
        link: https://twitter.com/justedagain/status/1583063827524251649
        text: |
          The developer experience of Pulumi is just sublime. As a prior Terraform user, the grass is substantially greener on this side. I'm so glad I made the switch two years back. Using Terraform for my current use case would be a massive downgrade.
      - source: twitter
        username: "@hossambarakat_"
        avatar: https://pbs.twimg.com/profile_images/1578466430739271681/FZnNwxcA_200x200.jpg
        link: https://twitter.com/hossambarakat_/status/1357640859018162176
        text: |
          Give Pulumi a shot and you will never look back @PulumiCorp
      - source: twitter
        username: "@ddoomen"
        avatar: https://pbs.twimg.com/profile_images/1591057460940480517/d0xy4n3b_200x200.jpg
        link: https://twitter.com/ddoomen/status/1644343201459740673
        text: |
          Deploying cloud resources using @PulumiCorp is just amazing. Why would anybody bother with JSON, YAML or some other DSL?
      - source: twitter
        username: "@Meliora245"
        avatar: https://pbs.twimg.com/profile_images/1536753333972525056/WN2SVAmq_200x200.jpg
        link: https://twitter.com/Meliora245/status/1633110529420976130
        text: |
          Been using Pulumi with Typescript for a IaaC managing k8s and stateful databases. Don't see myself going back to using terraform after this.
      - source: twitter
        username: "@rybavery"
        avatar: https://pbs.twimg.com/profile_images/1146562967317520385/wuPwKFUZ_200x200.jpg
        link: https://twitter.com/rybavery/status/1576987704189128704
        text: |
          our team at @devseed is now gravitating toward using https://pulumi.com/docs/iac/comparisons/terraform/ instead of terraform because it's all in python so it is easier to onboard new people to the tool and makes it easier to manage the same infra definition in different test, staging, and deploy envs.
      - source: twitter
        username: "@SparkyCodes"
        avatar: https://pbs.twimg.com/profile_images/1564710917014802433/k0QzTysD_200x200.jpg
        link: https://twitter.com/SparkyCodes/status/1572999315919978502
        text: |
          It wouldn't have been possible to build Sparky without @PulumiCorp. Shout out to the team and community for helping us get up and running!
      - source: twitter
        username: "@krangarajan"
        avatar: https://pbs.twimg.com/profile_images/837774934805925888/I51_kI-H_200x200.jpg
        link: https://twitter.com/krangarajan/status/1564712184717881344
        text: |
          New gig uses @PulumiCorp to manage AWS infra. Initially I was skeptical and was tempted to go back to Terraform, but after using pulumi imports and discovering the ability to write tests easily, I'm a convert. (1/4)
      - source: twitter
        username: "@swarupdonepudi"
        avatar: https://pbs.twimg.com/profile_images/1581098587034771457/9HrxXWw4_200x200.jpg
        link: https://twitter.com/swarupdonepudi/status/1644820071167201280
        text: |
          I love @PulumiCorp so much because it is like 50% of the reason why we dared to build https://planton.cloud.

          An equivalent of 50K lines of declarative infra code has been put behind APIs to support the features on the platform with https://www.pulumi.com/docs/using-pulumi/automation-api/
    anchor: community
---
