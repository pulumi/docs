---
title: Pulumi - Infrastructure as Code in any Programming Language
meta_desc: Pulumi's open source infrastructure as code SDK enables you to create, deploy, and manage infrastructure on any cloud, using your favorite languages.

block_external_search_index: true

type: page
layout: home-b

hero:
  title: [ "Infrastructure as code", "in any programming language" ]
  description: |
    Build infrastructure intuitively on any cloud using familiar languages.
  cta_text: Get Started
  cta_link: /docs/get-started
  secondary_cta_text: Contact Sales
  secondary_cta_link: /contact/?form=sales

code_faster:
  title: Code and ship faster
  description: |
    Author infrastructure code using programming languages you know and love. Write statements to define infrastructure using your IDE with autocomplete, type checking, and documentation.

    Test your code with unit tests and deliver it through CI/CD pipelines to validate and deploy to any cloud.
  code:
    - title: index.ts
      language: typescript
      code: |
        import * as pulumi from "@pulumi/pulumi";
        import * as awsx from "@pulumi/awsx";
        import * as eks from "@pulumi/eks";

        // Create a new VPC
        const eksVpc = new awsx.ec2.Vpc("eks-vpc", {
            enableDnsHostnames: true,
            cidrBlock: "10.0.0.0/16",
        });

        // Create the EKS cluster
        const eksCluster = new eks.Cluster("eks-cluster", {
            vpcId: eksVpc.vpcId,
            publicSubnetIds: eksVpc.publicSubnetIds,
            privateSubnetIds: eksVpc.privateSubnetIds,
            instanceType: "t2.medium",
            desiredCapacity: 3,
            minSize: 3,
            maxSize: 6,
            nodeAssociatePublicIpAddress: false,
        });

        // Export some values for use elsewhere
        export const kubeconfig = eksCluster.kubeconfig;
        export const vpcId = eksVpc.vpcId;
    - title: __main__.py
      language: python
      code: |
        import pulumi
        import pulumi_awsx as awsx
        import pulumi_eks as eks

        # Create a VPC for the EKS cluster
        eks_vpc = awsx.ec2.Vpc("eks-vpc",
            enable_dns_hostnames=True,
            cidr_block="10.0.0.0/16")

        # Create the EKS cluster
        eks_cluster = eks.Cluster("eks-cluster",
            vpc_id=eks_vpc.vpc_id,
            public_subnet_ids=eks_vpc.public_subnet_ids,
            private_subnet_ids=eks_vpc.private_subnet_ids,
            instance_type="t2.medium",
            desired_capacity=3,
            min_size=3,
            max_size=6,
            node_associate_public_ip_address=False)

        # Export values to use elsewhere
        pulumi.export("kubeconfig", eks_cluster.kubeconfig)
        pulumi.export("vpcId", eks_vpc.vpc_id)
    - title: main.go
      language: go
      code: |
            package main

            import (
              "github.com/pulumi/pulumi-awsx/sdk/go/awsx/ec2"
              "github.com/pulumi/pulumi-eks/sdk/go/eks"
              "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
              "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
            )

            func main() {
              pulumi.Run(func(ctx *pulumi.Context) error {
                // Create a new VPC, subnets, and associated infrastructure
                vpcNetworkCidr := "10.0.0.0/16"
                eksVpc, err := ec2.NewVpc(ctx, "eks-vpc", &ec2.VpcArgs{
                  EnableDnsHostnames: pulumi.Bool(true),
                  CidrBlock:          &vpcNetworkCidr,
                })
                if err != nil {
                  return err
                }

                // Create a new EKS cluster
                eksCluster, err := eks.NewCluster(ctx, "eks-cluster", &eks.ClusterArgs{
                  VpcId:                        eksVpc.VpcId,
                  PublicSubnetIds:              eksVpc.PublicSubnetIds,
                  PrivateSubnetIds:             eksVpc.PrivateSubnetIds,
                  InstanceType:                 pulumi.String("t2.medium"),
                  DesiredCapacity:              pulumi.Int(3),
                  MinSize:                      pulumi.Int(3),
                  MaxSize:                      pulumi.Int(6),
                  NodeAssociatePublicIpAddress: pulumi.Bool(false),
                })
                if err != nil {
                  return err
                }

                // Export some values in case they are needed elsewhere
                ctx.Export("kubeconfig", eksCluster.Kubeconfig)
                ctx.Export("vpcId", eksVpc.VpcId)
                return nil
              })
            }
    - title: MyStack.cs
      language: csharp
      code: |
        using Pulumi;
        using Awsx = Pulumi.Awsx;
        using Eks = Pulumi.Eks;
        using System.Collections.Generic;

        return await Deployment.RunAsync(() =>
        {
            // Create a new VPC
            var eksVpc = new Awsx.Ec2.Vpc("eks-vpc", new()
            {
                EnableDnsHostnames = true,
                CidrBlock = "10.0.0.0/16",
            });

            // Create the EKS cluster
            var eksCluster = new Eks.Cluster("eks-cluster", new()
            {
                VpcId = eksVpc.VpcId,
                PublicSubnetIds = eksVpc.PublicSubnetIds,
                PrivateSubnetIds = eksVpc.PrivateSubnetIds,
                InstanceType = "t2.medium",
                DesiredCapacity = 3,
                MinSize = 3,
                MaxSize = 6,
                NodeAssociatePublicIpAddress = false,
            });

            // Export some values for use elsewhere
            return new Dictionary<string, object?>
            {
                ["kubeconfig"] = eksCluster.Kubeconfig,
                ["vpcId"] = eksVpc.VpcId,
            };
        });
    - title: App.Java
      language: java
      code: |
        package my_eks_cluster;

        import com.pulumi.Context;
        import com.pulumi.Pulumi;
        import com.pulumi.core.Output;
        import com.pulumi.awsx.ec2.Vpc;
        import com.pulumi.awsx.ec2.VpcArgs;
        import com.pulumi.eks.Cluster;
        import com.pulumi.eks.ClusterArgs;
        import java.util.List;
        import java.util.ArrayList;
        import java.util.Map;
        import java.io.File;
        import java.nio.file.Files;
        import java.nio.file.Paths;

        public class App {
            public static void main(String[] args) {
                Pulumi.run(App::stack);
            }

            public static void stack(Context ctx) {
                var eksVpc = new Vpc("eksVpc", VpcArgs.builder()
                    .enableDnsHostnames(true)
                    .cidrBlock("10.0.0.0/16")
                    .build());

                var eksCluster = new Cluster("eksCluster", ClusterArgs.builder()
                    .vpcId(eksVpc.vpcId())
                    .publicSubnetIds(eksVpc.publicSubnetIds())
                    .privateSubnetIds(eksVpc.privateSubnetIds())
                    .instanceType("t2.medium")
                    .desiredCapacity(3)
                    .minSize(3)
                    .maxSize(6)
                    .nodeAssociatePublicIpAddress(false)
                    .build());

                ctx.export("kubeconfig", eksCluster.kubeconfig());
                ctx.export("vpcId", eksVpc.vpcId());
            }
        }
    - title: Pulumi.yaml
      language: yaml
      code: |
        name: pulumi-eks
        description: A simple EKS cluster
        runtime: yaml
        resources:
          # Create a VPC for the EKS cluster
          eks-vpc:
            type: awsx:ec2:Vpc
            properties:
              enableDnsHostnames: true
              cidrBlock: "10.0.0.0/16"
          # Create the EKS cluster
          eks-cluster:
            type: eks:Cluster
            properties:
              vpcId: ${eks-vpc.vpcId}
              publicSubnetIds: ${eks-vpc.publicSubnetIds}
              privateSubnetIds: ${eks-vpc.privateSubnetIds}
              instanceType: "t2.medium"
              desiredCapacity: 3
              minSize: 3
              maxSize: 6
              nodeAssociatePublicIpAddress: false
        outputs:
          # Output the Kubeconfig for the cluster
          kubeconfig: ${eks-cluster.kubeconfig}
          vpcId: ${eks-vpc.vpcId}


ai:
  title: Boost productivity with AI
  image: /images/home/ai-graphic.svg
  alt: AI prompted to 'Give me an AWS static website behind a CloudFront CDN' and outputting Pulumi code
  description: |
    Want help writing infrastructure code? Use Pulumi AI to generate code for your desired infrastructure – all through natural language commands.

    Ask Pulumi AI to iterate on your code to make changes and add new resources.

embed:
  title: Embed IaC anywhere
  image: /images/home/automation-api-diagram.svg
  alt: a flowchart with arrows going from Automation API program to Infrasctucture as Code programs to Pulumi Engine deploys stacks
  description: |
    With Automation API, embed Pulumi in your applications to power custom cloud infrastructure automation. No CLI - just code so you can manage 10x more resources.

    Package cloud architectures into reusable libraries that reduce complex infrastructure down to a few lines of code.

search:
  title: Search every cloud
  image: /images/home/search-example-graphic.svg
  alt: a search bar populated with 'show all my prod stack resources' returning a list of prod resources from different clouds
  description: |
    View and search for deployed resources across all your cloud providers – presented in a human-readable way.

    Export your data to gain insights into your infrastructure with your existing analytics tools.

customer_logos:
  title: You’ll be in good company
  logos:
    - name: mercedes-benz
      link: /case-studies/mercedes-benz
    - name: snowflake
      link: /case-studies/snowflake
    - name: lemonade
      link: /case-studies/lemonade
    - name: cockroach-labs
    - name: meta
    - name: webflow
    - name: bluenile
    - name: dutchie
      link: https://youtu.be/X1qetq7PjjY
    - name: panther-labs
      link: /case-studies/panther-labs
    - name: univision
    - name: washington-trust
      link: https://youtu.be/Q63ZaX340M4
    - name: nubank

customer_quotes:
  panther:
    text: |
      “Our developers needed a fast, modular, and testable platform for managing cloud infrastructure. <b>Nothing is better than having standard programming languages for building and managing infrastructure</b>”
    author: Austin Byers, Principal Platform Engineer
    logo: panther-labs
  starburst:
    text: |
      “Pulumi let us build and <b>automate cloud infrastructure projects</b> at a scale that simply wasn’t imaginable using prior-generation infrastructure as code technologies”
    author: Matt Stephenson, Senior Principal Software Engineer
    logo: starburst
  snowflake:
    text: |
      “Pulumi helped our team to ship a new product faster. We needed <b>one tool to setup and manage multi-cloud, multi-region Kubernetes clusters</b> that infrastructure and applications teams could use collaboratively”
    author: Justin Fitzhugh, VP of Cloud Platform Engineering
    logo: snowflake

get_started:
  tweets:
    -
      source: twitter
      username: "@BryanMigliorisi"
      avatar: https://pbs.twimg.com/profile_images/752334791782039552/BsVNGBaV_400x400.jpg
      link: https://twitter.com/BryanMigliorisi/status/1450123026901651460
      text: |
        There is no way around the fact that devops is complicated but @PulumiCorp is a game changer for me.  Blows away CloudForamtion, TerraForm, CDK, etc.
    -
      source: twitter
      username: "@krangarajan"
      avatar: https://pbs.twimg.com/profile_images/837774934805925888/I51_kI-H_400x400.jpg
      link: https://twitter.com/krangarajan/status/1580618068203479040
      text: |
        Continuing on my thread about @PulumiCorp from a while ago: holy shit I am a convert. I needed to setup a staging environment that was mostly identical to prod, and once I trued up our Pulumi stack with AWS, it took *minutes* to do this. How have I lived without this until now?
    -
      source: twitter
      username: "@Vetium"
      avatar: https://pbs.twimg.com/profile_images/1197754531335016449/etr4hfpJ_400x400.jpg
      link: https://twitter.com/Vetium/status/1589452885149900800
      text: |
        Without a doubt the most approachable tool in the IaaC space is
        @PulumiCorp.

        Somewhat enjoying provisioning a scheduled run of a Lambda.
    -
      source: twitter
      username: "@justedagain"
      avatar: https://pbs.twimg.com/profile_images/1576905831626440706/wigR9_hF_400x400.jpg
      link: https://twitter.com/justedagain/status/1583063827524251649
      text: |
        The developer experience of Pulumi is just sublime. As a prior Terraform user, the grass is substantially greener on this side. I'm so glad I made the switch two years back. Using Terraform for my current use case would be a massive downgrade.
    -
      source: twitter
      username: "@hossambarakat_"
      avatar: https://pbs.twimg.com/profile_images/1578466430739271681/FZnNwxcA_400x400.jpg
      link: https://twitter.com/hossambarakat_/status/1357640859018162176
      text: |
        Give Pulumi a shot and you will never look back @PulumiCorp
    -
      source: twitter
      username: "@matticala"
      avatar: https://pbs.twimg.com/profile_images/1289826906024693766/LOdbjWdW_400x400.jpg
      link: https://twitter.com/matticala/status/1369038327341531140
      text: |
        With @PulumiCorp I said goodbye to #YAML and JSON supersets.
        I went back to what I love: #code.
        Code. End to end. Functional, even.
        #Kubernetes is pleasant again.
    -
      source: twitter
      username: "@ddoomen"
      avatar: https://pbs.twimg.com/profile_images/1591057460940480517/d0xy4n3b_400x400.jpg
      link: https://twitter.com/ddoomen/status/1644343201459740673
      text: |
        Deploying cloud resources using @PulumiCorp is just amazing. Why would anybody bother with JSON, YAML or some other DSL?
    -
      source: twitter
      username: "@Meliora245"
      avatar: https://pbs.twimg.com/profile_images/1536753333972525056/WN2SVAmq_400x400.jpg
      link: https://twitter.com/Meliora245/status/1633110529420976130
      text: |
        Been using Pulumi with Typescript for a IaaC managing k8s and stateful databases. Don't see myself going back to using terraform after this.
    -
      source: twitter
      username: "@rybavery"
      avatar: https://pbs.twimg.com/profile_images/1146562967317520385/wuPwKFUZ_400x400.jpg
      link: https://twitter.com/rybavery/status/1576987704189128704
      text: |
        our team at @devseed is now gravitating toward using https://pulumi.com/docs/concepts/vs/terraform/ instead of terraform because it's all in python so it is easier to onboard new people to the tool and makes it easier to manage the same infra definition in different test, staging, and deploy envs.
    -
      source: twitter
      username: "@SparkyCodes"
      avatar: https://pbs.twimg.com/profile_images/1564710917014802433/k0QzTysD_400x400.jpg
      link: https://twitter.com/SparkyCodes/status/1572999315919978502
      text: |
        It wouldn't have been possible to build Sparky without @PulumiCorp. Shout out to the team and community for helping us get up and running!
    -
      source: twitter
      username: "@0xksure"
      avatar: https://pbs.twimg.com/profile_images/1560526743865360384/QBkajFhq_400x400.jpg
      link: https://twitter.com/0xksure/status/1570769681434415104
      text: |
        ok so pulumi is awesome. almost no clicking, just scripting go and up
    -
      source: twitter
      username: "@krangarajan"
      avatar: https://pbs.twimg.com/profile_images/837774934805925888/I51_kI-H_400x400.jpg
      link: https://twitter.com/krangarajan/status/1564712184717881344
      text: |
        New gig uses @PulumiCorp to manage AWS infra. Initially I was skeptical and was tempted to go back to Terraform, but after using pulumi imports and discovering the ability to write tests easily, I'm a convert. (1/4)
    -
      source: twitter
      username: "@swarupdonepudi"
      avatar: https://pbs.twimg.com/profile_images/1581098587034771457/9HrxXWw4_400x400.jpg
      link: https://twitter.com/swarupdonepudi/status/1644820071167201280
      text: |
        I love @PulumiCorp so much because it is like 50% of the reason why we dared to build https://planton.cloud.

        An equivalent of 50K lines of declarative infra code has been put behind APIs to support the features on the platform with https://www.pulumi.com/docs/using-pulumi/automation-api/
    -
      source: twitter
      username: "@iamjmoa"
      avatar: https://pbs.twimg.com/profile_images/1529025993893195777/Wo8EXvLO_400x400.jpg
      link: https://twitter.com/iamjmoa/status/1624702662456352768
      text: |
        Today is a good day.

        Finished no-code website builder.

        Managed to automate deploying a website created with said builder with @PulumiCorp

  title: Built by engineers for engineers. Open source.
  description: "[Join us](/community) in the community, and let’s build together."
---
