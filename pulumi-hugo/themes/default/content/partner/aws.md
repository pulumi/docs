---
title: Modern Infrastructure as Code for AWS
layout: aws
url: /aws

meta_desc: Pulumi provides huge productivity gains and a unified programming model for Devs and DevOps, through infrastructure as code on the AWS cloud.

hero:
    title: Cloud Engineering for AWS
    description: |
        Pulumi's [infrastructure as code](/what-is/what-is-infrastructure-as-code/)
        SDK helps create, deploy, and manage your AWS infrastructure, including containers,
        serverless functions, and other infrastructure using modern programming languages.

awsx_code: |
    import * as eks from "@pulumi/eks";

    // Create an EKS cluster with the default configuration.
    const cluster = new eks.Cluster("my-cluster", {
        desiredCapacity: 5,
        minSize: 3,
        maxSize: 5,
        deployDashboard: false,
        enabledClusterLogTypes: [
            "api",
            "audit",
            "authenticator",
        ],
    });

    // Export the cluster's kubeconfig.
    export const kubeconfig = cluster.kubeconfig;

automation_api_code: |
    func NewAddCmd() *cobra.Command {
        return &cobra.Command{
            Use:   "add",
            Short: "add deploys an additional vm stack",
            Run: func(cmd *cobra.Command, args []string) {
                stackName := fmt.Sprintf("vmgr%d", rangeIn(10000000, 99999999))
                s, err := auto.NewStackInlineSource(ctx, stackName, projectName, nil)
                subnetID, rgName, err := EnsureNetwork(ctx, projectName)
                stack.SetProgram(GetDeployVMFunc(subnetID, rgName))
                stdoutStreamer := optup.ProgressStreams(os.Stdout)

                res, err := s.Up(ctx, stdoutStreamer)
                if err != nil {
                    fmt.Printf("Failed to deploy vm stack: %v\n", err)
                    os.Exit(1)
                }
                fmt.Printf("deployed server running at public IP %s\n", res.Outputs["ip"].Value)
            },
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
