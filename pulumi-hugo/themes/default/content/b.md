---
title: Pulumi - Universal Infrastructure as Code
meta_desc: Pulumi's open source infrastructure as code SDK enables you to create, deploy, and manage infrastructure on any cloud, using your favorite languages.

block_external_search_index: true

type: page
layout: home-b

hero:
  title: [ "Ship", "Infrastructure", "Faster" ]
  description: |
    Deliver infrastructure with high velocity and scale through software engineering.
  cta_text: Get Started

overview:
  title: [ "Universal", "Infrastructure as Code" ]
  description: |
    Every cloud, every language, every architecture, every builder.
  logos:
    languages:
      - /logos/tech/typescript.svg
      - /logos/tech/dotnet.svg
      - /logos/tech/go.svg
      - /logos/tech/java.svg
      - /logos/tech/yaml.svg
      - /logos/tech/python.svg
      - /logos/tech/javascript.svg
      - /logos/tech/fsharp.svg
    clouds:
      - /logos/tech/aws.svg
      - /logos/tech/azure-logo.svg
      - /logos/tech/gcp-logo.svg
      - /logos/tech/kubernetes.svg
      - /logos/tech/digitalocean.svg
      - /logos/tech/alibaba.svg
    identity:
      - /logos/tech/github.svg
      - /logos/tech/atlassian.svg
      - /logos/tech/ci-cd/gitlab-ci.svg
      - /logos/tech/ci-cd/circleci.svg
      - /logos/tech/ci-cd/jenkins.svg
      - /logos/tech/ci-cd/spinnaker.svg
      - /logos/tech/ci-cd/teamcity.svg
      - /logos/tech/ci-cd/travis-ci.svg

templates:
  title: Get started
  description: Get started quickly with a project template that fits your use case.
  links:
    - label: Containers
      url: /templates/container-service/
      icon: tasks
    - label: Kubernetes App
      url: /templates/kubernetes-application/
      icon: cubes
    - label: Kubernetes Cluster
      url: /templates/kubernetes/
      icon: cloud
    - label: Serverless
      url: /templates/serverless-application/
      icon: sitemap
    - label: Static Website
      url: /templates/static-website/
      icon: folder
    - label: Virtual Machine
      url: /templates/virtual-machine/
      icon: server

build:
  title: Write infrastructure code faster
  description: |
    Pulumi speeds up your inner dev loop for Infrastructure as Code (IaC) by allowing you to use an IDE giving you statement completion, real-time type checking, and interactive documentation out of the box. In addition you can leverage all of the capabilities of the programming language of your choice so you can reduce the total number of lines of code you're writing.

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

deploy:
  title: Ship applications faster
  description: |
    Pulumi speeds up your outer dev loop by making CI/CD for your IaC seamless and the default experience. Pulumi has integrations with all the popular CI/CD platforms and testing frameworks, so you can validate every change with testing and built-in policies. You can also build Pulumi Packages to create best-practice abstractions available in all languages.

manage:
  title: Deliver ideas faster
  description: |
    Pulumi gives you a faster dev loop across the entire organization by guaranteeing the infrastructure software supply chain. Standard software packaging allows sharing and reuse of code across the organization along with org-wide policy enforcements, full change visibility and auditing across your entire organization, and automatic encryption for secrets and state. Pulumi provides the industry’s only automation workflow capability that allows software engineering to be applied to solve and manage cloud infrastructure at scale.

automation_api_examples:
  - name: Provision resources over HTTP (Node.js/Express)
    text: |
      ```typescript
      import * as express from "express";
      import * as aws from "@pulumi/aws";
      import * as auto from "@pulumi/pulumi/automation";

      const app = express();

      app.post("/update", async (req, res) => {

          // Create a new stack.
          const stack = await auto.createStack({
              stackName: req.body.stackName,
              projectName: req.body.projectName,
              program: () => {
                  return {
                      bucket: new aws.s3.Bucket("my-bucket");
                  };
              },
          });

          // Update the stack.
          await stack.up({ onOutput: console.info });
          return res.send("Update complete.");
      });

      app.listen(3000);
      ```

  - name: Create custom CLI tools (Go/Cobra)
    text: |
      ```go
      import (
          "fmt"

          "github.com/pulumi/pulumi/sdk/v3/go/auto"
          "github.com/pulumi/pulumi/sdk/v3/go/auto/optup"
          "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
          "github.com/ThorstenHans/stringer/pkg/stringer"
          "github.com/spf13/cobra"
      )

      func pulumiProgram(ctx *pulumi.Context) error {
          // Your Pulumi program.
      }

      var deployCmd = &cobra.Command{
          Use:   "deploy",
          Short:  "Deploy my infrastructure.",
          Run: func(cmd *cobra.Command, args []string) error {
              ctx := context.Background()
              projectName := "example"
              stackName := "dev"
              s, err := auto.UpsertStackInlineSource(ctx, stackName, projectName, pulumiProgram)
              if err != nil {
                return err
              }

              w := s.Workspace()

              // for inline source programs, we must manage plugins ourselves
              err = w.InstallPlugin(ctx, "aws", "v4.0.0")
              if err != nil {
                fmt.Printf("Failed to install program plugins: %v\n", err)
                os.Exit(1)
              }

              // set stack configuration specifying the AWS region to deploy
              s.SetConfig(ctx, "aws:region", auto.ConfigValue{Value: "us-west-2"})

              _, err = s.Refresh(ctx)
              if err != nil {
                return err
              }

              stdoutStreamer := optup.ProgressStreams(os.Stdout)

              res, err := s.Up(ctx, stdoutStreamer)
              if err != nil {
                return err
              }

              return nil
          },
      }

      func init() {
          rootCmd.AddCommand(deployCmd)
      }
      ```

  - name: Run database migrations (Python/MySQL)
    text: |
      ```python
      import sys
      import json
      import pulumi
      import pulumi_aws as aws
      from pulumi import automation as auto
      from mysql.connector import connect


      # This is our pulumi program in "inline function" form
      def pulumi_program():
          default_vpc = aws.ec2.get_vpc(default=True)
          public_subnet_ids = aws.ec2.get_subnet_ids(vpc_id=default_vpc.id)
          subnet_group = aws.rds.SubnetGroup("db_subnet", subnet_ids=public_subnet_ids.ids)

          # make a public security group for our cluster for the migration
          security_group = aws.ec2.SecurityGroup("public_group",
                                                ingress=[aws.ec2.SecurityGroupIngressArgs(
                                                    protocol="-1",
                                                    from_port=0,
                                                    to_port=0,
                                                    cidr_blocks=["0.0.0.0/0"]
                                                )],
                                                egress=[aws.ec2.SecurityGroupEgressArgs(
                                                    protocol="-1",
                                                    from_port=0,
                                                    to_port=0,
                                                    cidr_blocks=["0.0.0.0/0"]
                                                )])

          # example on, you should change this
          db_name = "hellosql"
          db_user = "hellosql"
          db_pass = "hellosql"

          # provision our db
          cluster = aws.rds.Cluster("db",
                                    engine=aws.rds.EngineType.AURORA_MYSQL,
                                    engine_version="5.7.mysql_aurora.2.10.2",
                                    database_name=db_name,
                                    master_username=db_user,
                                    master_password=db_pass,
                                    skip_final_snapshot=True,
                                    db_subnet_group_name=subnet_group.name,
                                    vpc_security_group_ids=[security_group.id])

          cluster_instance = aws.rds.ClusterInstance("db_instance",
                                                    cluster_identifier=cluster.cluster_identifier,
                                                    instance_class=aws.rds.InstanceType.T3_SMALL,
                                                    engine=aws.rds.EngineType.AURORA_MYSQL,
                                                    engine_version="5.7.mysql_aurora.2.10.2",
                                                    publicly_accessible=True,
                                                    db_subnet_group_name=subnet_group.name)

          pulumi.export("host", cluster.endpoint)
          pulumi.export("db_name", db_name)
          pulumi.export("db_user", db_user)
          pulumi.export("db_pass", db_pass)


      # To destroy our program, we can run python main.py destroy
      destroy = False
      args = sys.argv[1:]
      if len(args) > 0:
          if args[0] == "destroy":
              destroy = True

      project_name = "database_migration"
      stack_name = "dev"

      # create (or select if one already exists) a stack that uses our inline program
      stack = auto.create_or_select_stack(stack_name=stack_name,
                                          project_name=project_name,
                                          program=pulumi_program)

      print("successfully initialized stack")

      # for inline programs, we must manage plugins ourselves
      print("installing plugins...")
      stack.workspace.install_plugin("aws", "v4.0.0")
      print("plugins installed")

      # set stack configuration specifying the AWS region to deploy
      print("setting up config")
      stack.set_config("aws:region", auto.ConfigValue(value="us-west-2"))
      print("config set")

      print("refreshing stack...")
      stack.refresh(on_output=print)
      print("refresh complete")

      if destroy:
          print("destroying stack...")
          stack.destroy(on_output=print)
          print("stack destroy complete")
          sys.exit()

      print("updating stack...")
      up_res = stack.up(on_output=print)
      print(f"update summary: \n{json.dumps(up_res.summary.resource_changes, indent=4)}")
      print(f"db host url: {up_res.outputs['host'].value}")

      print("configuring db...")
      with connect(
              host=up_res.outputs['host'].value,
              user=up_res.outputs['db_user'].value,
              password=up_res.outputs['db_pass'].value,
              database=up_res.outputs['db_name'].value) as connection:
          print("db configured!")

          # make sure the table exists
          print("creating table...")
          create_table_query = """CREATE TABLE IF NOT EXISTS hello_pulumi(
              id int(9) NOT NULL PRIMARY KEY,
              color varchar(14) NOT NULL);
              """
          with connection.cursor() as cursor:
              cursor.execute(create_table_query)
              connection.commit()

          # seed the table with some data to start
          seed_table_query = """INSERT IGNORE INTO hello_pulumi (id, color)
          VALUES
              (1, 'Purple'),
              (2, 'Violet'),
              (3, 'Plum');
          """
          with connection.cursor() as cursor:
              cursor.execute(seed_table_query)
              connection.commit()

          print("rows inserted!")
          print("querying to verify data...")

          # read the data back
          read_table_query = """SELECT COUNT(*) FROM hello_pulumi;"""
          with connection.cursor() as cursor:
              cursor.execute(read_table_query)
              result = cursor.fetchone()
              print(f"Result: {json.dumps(result)}")

          print("database, table and rows successfully configured")
      ```

  - name: See more example code
    text: |
      [View examples](https://github.com/pulumi/automation-api-examples)

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - - name: mercedes-benz
        link: /case-studies/mercedes-benz
      - name: sans
        link: /case-studies/sans-institute
      - name: snowflake
        link: /case-studies/snowflake
    - - name: credijusto
        link: /case-studies/credijusto
      - name: skai
        link: /blog/kenshoo-migrates-to-aws-with-pulumi
      - name: lemonade
        link: /case-studies/lemonade
    - - name: panther-labs
        link: /case-studies/panther-labs
      - name: sourcegraph
        link: /case-studies/sourcegraph
      - name: whylabs
        link: /case-studies/whylabs
    - - name: webflow
      - name: cockroach-labs
      - name: washington-trust
    - - name: qi
      - name: univision
      - name: petcolove
    - - name: linktree
      - name: materialize
      - name: anitian
    - - name: clearsale
      - name: ware2go
      - name: meta
    - - name: angellist
      - name: bluenile
      - name: dutchie
    - - name: gusto
      - name: cisess
        link: /blog/managing-multi-cloud-open-data-noaa
      - name: altana


get_started:
  tweets:
    -
      source: twitter
      text: "@PulumiCorp is pretty awesome. Just nuked a couple of load balancers and recreated them, no big deal."
      username: "@joepferguson@phpc.social"
      avatar: https://pbs.twimg.com/profile_images/1593803782034423809/j53OblCR_400x400.jpg
      link: https://twitter.com/JoePFerguson/status/1593289950597976066

    -
      text: "All in all, I''m very happy with making the transition to Pulumi! I became way more productive managing my infrastructure. At the same time I ended up enjoying the work of doing so a lot more - which is really important too. (click to read blog post)"
      username: Erik Näslund
      avatar: https://hashnode.com/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1616450184066%2F-uXss6aRN.jpeg%3Fw%3D500%26h%3D500%26fit%3Dcrop%26crop%3Dfaces%26auto%3Dcompress%2Cformat%26format%3Dwebp&w=3840&q=75
      link: https://blog.ekik.org/my-experience-migrating-my-infrastructure-from-terraform-to-pulumi
      source: blog

    -
      source: twitter
      username: matticala
      avatar: https://pbs.twimg.com/profile_images/1289826906024693766/LOdbjWdW_400x400.jpg
      link: https://twitter.com/matticala/status/1369038327341531140
      text: |
        With @PulumiCorp I said goodbye to #YAML and JSON supersets. I went back to what I love: #code. Code. End to end. Functional, even. #Kubernetes is pleasant again.

    -
      avatar: https://pbs.twimg.com/profile_images/752334791782039552/BsVNGBaV_400x400.jpg
      text: "There is no way around the fact that devops is complicated but \n@PulumiCorp\n is a game changer for me.  Blows away CloudForamtion, TerraForm, CDK, etc."
      username: "@BryanMigliorisi"
      link: https://twitter.com/BryanMigliorisi/status/1450123026901651460
      source: twitter

    - source: twitter
      username: MartinDotNet
      avatar: https://pbs.twimg.com/profile_images/1525576597109096450/oA9QTWOb_400x400.jpg
      link: https://twitter.com/MartinDotNet/status/1367118630564020225
      text: |
        I'd like to congratulate @PulumiCorp on an AWESOME CLI experience... it's just beautiful

    -
      text: "Having used Pulumi the last 2 years after switching from Terraform I want to share some of my experience by comparing both infrastructure as code tools and explain why I prefer Pulumi in most situations. In general, I have successfully provisioned infrastructure with both tools, but from my experience Pulumi makes it easier for me. (click to read blog post)"
      username: Matthias Müller
      link: https://www.novatec-gmbh.de/en/blog/why-you-should-consider-pulumi-over-terraform-for-your-next-project-pt-1/
      source: blog

    -
      source: twitter
      username: monde_
      avatar: https://pbs.twimg.com/profile_images/1478919095/converse_400x400.png
      link: https://twitter.com/monde_/status/1355031516934332418?s=20
      text: |
        I'm actually learning more about TS/JS with Pulumi. It really has been a joy to use. Kudos to the team for making such an awesome tool!

    -
      text: Pulumi is better than Terraform. Hands down. It has all the features of Terraform, but written with the simplicity and power of a fully featured programming language.
      username: Christopher Lenard
      avatar: https://miro.medium.com/fit/c/176/176/1*kXxfMvZ4mXSvCQif2Iqpmg.png
      link: https://medium.com/@christopherlenard/the-benefits-of-moving-from-terraform-to-pulumi-7e01a3ab8f43
      source: blog

    -
      source: twitter
      username: JanDamaschke
      avatar: https://pbs.twimg.com/profile_images/1533370681093758976/8pU-VB_x_400x400.jpg
      link: https://twitter.com/JanDamaschke/status/1354861632082636805
      text: |
        I just spent a few hours getting used to @PulumiCorp SDK and I am already asking myself why I ever used #Terraform 😂  Real Infrastructure as Code all the way 💪 😍

    -
      source: twitter
      username: eliostruyf
      avatar: https://pbs.twimg.com/profile_images/1598282380665561092/BDF74Mm5_400x400.jpg
      link: https://twitter.com/eliostruyf/status/1379896780381372422?s=20
      text: |
       First, run of my new #dev environment. Love how easy it is with @PulumiCorp ❤️ 🚀 #InfrastructureAsCode

    -
      text: "Ok, Pulumi just got even more real. With “pulumi convert” and CrossCode support in YAML, it just overtook HCL and Terraform in position #1 for me. Sorry HashiCorp Pulumi is now in the lead."
      username: Eric Hendrickson, CTO Provisions Group
      avatar: https://media.licdn.com/dms/image/C5603AQHI5n0U3nsqXA/profile-displayphoto-shrink_800_800/0/1653244735916?e=1678924800&v=beta&t=p50cz6bH97VFWDf6MGzKFuNTp9-5dUGqjieUNi0AzfA
      link: https://www.linkedin.com/feed/update/urn:li:activity:6993614249331765250?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A6993614249331765250%2C6993718113632411648%29
      source: linkedin

    -
      text: "Continuing on my thread about @PulumiCorp from a while ago: holy **** I am a convert. I needed to setup a staging environment that was mostly identical to prod, and once I trued up our Pulumi stack with AWS, it took minutes to do this. How have I lived without this until now?"
      username: "@krangarajan\n"
      avatar: https://pbs.twimg.com/profile_images/837774934805925888/I51_kI-H_400x400.jpg
      link: https://twitter.com/krangarajan/status/1580618068203479040
      source: twitter

    -
      source: twitter
      username: BrandonBloom
      avatar: https://pbs.twimg.com/profile_images/1007413949925548032/8FmwYujD_400x400.jpg
      link: https://twitter.com/BrandonBloom/status/1344398906617073664
      text: |
        Just Pulumi-ified a ton of random AWS resources & it feels so good.

    -
      text: "From PoC in a week, to reaching production with confidence the week after, we’re super impressed by Pulumi’s focus on the developer experience and general ease of use. We have since expanded our usage of Pulumi to manage our infrastructure and have a GitHub Actions-powered workflow with automatic PR previews that is a breeze to use. (click to read blog post)"
      username: Tiago Sousa
      avatar: https://uploads-ssl.webflow.com/6350808bc45bd01da7af10ea/6350808bc45bd04065af1258_tiago-sousa-min-p-500.jpeg
      link: https://blog.amplemarket.com/using-pulumi-to-deal-with-growing-pains/
      source: blog

    -
      source: twitter
      username: sheeshee
      avatar: https://pbs.twimg.com/profile_images/458182231433826304/JQafPBkU_400x400.png
      link: https://twitter.com/sheeshee/status/1377562831948746756
      text: |
        I've been playing around with Pulumi a bit and I have to say this is really quite well done. The documentation is very polished and all tutorials I tried worked exactly copy paste out of the box.

    -
      source: twitter
      username: TorstenVolk
      avatar: https://pbs.twimg.com/profile_images/1575782906/110930-ENMA-115240-web_400x400.jpg
      link: https://twitter.com/TorstenVolk/status/1381716012131876869
      text: |
        #Pulumi is the fast growing new kit on the block. Great convo with @PulumiCorp at what the (near) future holds in terms of platform capabilities. Very exciting. #cloudengineering #devops #gitops @ema_research

    -
      text: "I just want to say that I''m amazed at what Pulumi can provide. I make twitch videos of my side projects and I was playing with Pulumi in creating my lambda function. I wanted to use my Pulumi code to..."
      username: "u/akali1987"
      link: https://www.reddit.com/r/devops/comments/y8418w/amazed_with_pulumi/
      source: reddit

    -
      source: twitter
      username: Frassle
      avatar: https://pbs.twimg.com/profile_images/1571260219/62070_434673459681_571169681_5323786_3642098_n_400x400.jpg
      link: https://twitter.com/Frassle/status/1355296248992038912
      text: |
        Save yourselves from the yaml, use pulumi

    -
      text: "Without a doubt the most approachable tool in the IaaC space is \n@PulumiCorp\n.\n\nSomewhat enjoying provisioning a scheduled run of a Lambda."
      username: "@Vetium"
      avatar: https://pbs.twimg.com/profile_images/1197754531335016449/etr4hfpJ_400x400.jpg
      link: https://twitter.com/Vetium/status/1589452885149900800
      source: twitter
    -
      text: "Why is \n@PulumiCorp\n so good, absolute minimum you can replicate everything you can do with other tools but that's just the start. If your #IaC is proper code you can use other sdks to fill gaps and it can be seamless. Used sdk to get secrets to pass to Pulumi, just worked 😍"
      username: "@ShahidDev"
      avatar: https://pbs.twimg.com/profile_images/1457067246241542145/YcmPSntF_400x400.jpg
      link: https://twitter.com/ShahidDev/status/1582965131629428736
      source: twitter
    -
      text: "The developer experience of Pulumi is just sublime. As a prior Terraform user, the grass is substantially greener on this side. I''m so glad I made the switch two years back. Using Terraform for my current use case would be a massive downgrade."
      username: "@justedagain"
      avatar: https://pbs.twimg.com/profile_images/1576905831626440706/wigR9_hF_400x400.jpg
      link: https://twitter.com/justedagain/status/1583063827524251649
      source: twitter

    - username: ItemLevel1
      avatar: https://pbs.twimg.com/profile_images/655703310545125376/7cI9yEyP_400x400.jpg
      link: https://twitter.com/ItemLevel1/status/1354888953166487555
      text: |
        Congratulations Joe. Loved the idea of pulumi since I did a talk with one of the first releases. I genuinely think this model is the future inside DevOps and out

    -
      source: twitter
      username: hossambarakat_
      avatar: https://pbs.twimg.com/profile_images/1578466430739271681/FZnNwxcA_400x400.jpg
      link: https://twitter.com/hossambarakat_/status/1357640859018162176
      text: |
        Give Pulumi a shot and you will never look back @PulumiCorp

    -
      source: twitter
      username: samcogan
      avatar: https://pbs.twimg.com/profile_images/970774602669412353/reTcugpM_400x400.jpg
      link: https://twitter.com/samcogan/status/1350392939755802627
      text: |
        Been using Pulumi to write C# IaC for a while now, very much prefer it to HCL.

    -
      source: twitter
      username: omerlh
      avatar: https://pbs.twimg.com/profile_images/1021467583193796608/9odUKQCb_400x400.jpg
      link: https://twitter.com/omerlh/status/1369281453213769736
      text: |
        Pulumi ❤️❤️❤️❤️

  title: Get started today
  description: Pulumi is open source and free to get started. Deploy your first stack today.
  cta_text: Get Started
---
