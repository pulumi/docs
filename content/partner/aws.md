---
title: Modern Infrastructure as Code for AWS
layout: aws
url: /aws

meta_desc: Pulumi provides huge productivity gains and a unified programming model for Devs and DevOps, through infrastructure as code on the AWS cloud.

hero:
    title: Cloud Engineering for AWS
    description: |
        Pulumi's infrastructure as code SDK helps create, deploy, and manage your
        AWS infrastructure, including containers, serverless functions, and
        other infrastructure using modern programming languages.
    cta_text: See what's new
    cta_url: "/blog/announcing-nextgen-azure-provider"
    ide:
        tabs:
            - title: index.ts
              language: typescript
              code: |
                import * as pulumi from "@pulumi/pulumi";
                import * as aws from "@pulumi/aws";

                const example = new aws.ec2.Instance("example", {
                    ami: "ami-0c55b159cbfafe1f0",
                    instanceType: "t2.micro",
                    tags: {
                        Name: "pulumi-example",
                    },
                    userData: `#!/bin/bash
                echo "Hello, World" > index.html
                nohup busybox httpd -f -p 8080 &

                `,
                });
            - title: __main__.py
              language: python
              code: |
                import pulumi
                import pulumi_aws as aws

                example = aws.ec2.Instance("example",
                    ami="ami-0c55b159cbfafe1f0",
                    instance_type="t2.micro",
                    tags={
                        "Name": "pulumi-example",
                    },
                    user_data="""#!/bin/bash
                echo "Hello, World" > index.html
                nohup busybox httpd -f -p 8080 &
                """)
            - title: main.go
              language: go
              code: |
                package main

                import (
                    "fmt"

                    "github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ec2"
                    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
                )

                func main() {
                    pulumi.Run(func(ctx *pulumi.Context) error {
                        _, err := ec2.NewInstance(ctx, "example", &ec2.InstanceArgs{
                            Ami:          pulumi.String("ami-0c55b159cbfafe1f0"),
                            InstanceType: pulumi.String("t2.micro"),
                            Tags: pulumi.StringMap{
                                "Name": pulumi.String("pulumi-example"),
                            },
                            UserData: pulumi.String(fmt.Sprintf("%v%v%v%v", "#!/bin/bash\n", "echo \"Hello, World\" > index.html\n", "nohup busybox httpd -f -p 8080 &\n", "\n")),
                        })
                        if err != nil {
                            return err
                        }
                        return nil
                    })
                }
            - title: MyStack.cs
              language: csharp
              code: |
                using Pulumi;
                using Aws = Pulumi.Aws;

                class MyStack : Stack
                {
                    public MyStack()
                    {
                        var example = new Aws.Ec2.Instance("example", new Aws.Ec2.InstanceArgs
                        {
                            Ami = "ami-0c55b159cbfafe1f0",
                            InstanceType = "t2.micro",
                            Tags =
                            {
                                { "Name", "pulumi-example" },
                            },
                            UserData = @"#!/bin/bash
                echo ""Hello, World"" > index.html
                nohup busybox httpd -f -p 8080 &

                ",
                        });
                    }

                }



contact_us_form:
    section_id: contact-us
    hubspot_form_id: 8a0e0f30-b43e-468e-98cc-6b5d481e8660
    headline: Need help with cloud-native infrastructure as code on AWS?
    quote:
        title: Learn how top engineering teams are using Pulumi's SDK to create, deploy, and manage AWS resources.
        name: Josh Imhoff
        name_title: Site Reliability Engineer, Cockroach Labs
        content: |
            We are building a distributed-database-as-a-service product that runs on Kubernetes clusters across
            multiple public clouds including GCP, AWS and others. Pulumi's declarative model, the support for real
            programming languages, and the uniform workflow on any cloud make our SRE team much more efficient.
---
