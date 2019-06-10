---
title: "CI/CD Made Easy with Pulumi and Azure Pipelines"
authors: ["praneet-loke"]
tags: ["Azure", "CI/CD"]
date: "2019-05-06"

description: "Announcing a new open-source extension to Azure Pipelines. You can now use Pulumi in your Azure Pipelines workflows."
---

[Azure DevOps is very popular among teams that want a single place to
manage their development pipelines, Git repositories, builds, releases,
and test plans. Pulumi's open-source tools are a great choice for
developers and operators deploying infrastructure as code on Azure. With
these two tools at hand, adopting CI and CD for your Azure
infrastructure is just a few steps away for you and your teams. 

To make it easy to use Pulumi with Azure, we are announcing an
open-source task extension for Azure Pipelines! The task extension will
manage the installation of the Pulumi CLI, and run the [Pulumi
commands](https://pulumi.io/reference/commands.html) you specify against
your stack.

You can install the task extension directly from the [Visual Studio
Marketplace](https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task).
Click the **"Get It Free"** button to install the extension into your
Azure DevOps organization. If you do not have the permissions to add it
to your organization, please contact your org admin to have the
extension installed. The source code for the open source task extension
can be found on
[GitHub](https://github.com/pulumi/pulumi-az-pipelines-task).

To use the Pulumi task extension in Azure Pipelines, there are two
options. The
full [example](https://github.com/pulumi/pulumi-az-pipelines-task/tree/master/examples) is
in the source repo. For contrast, without this task extension,
[here's](https://pulumi.io/reference/cd-azure-devops.html#using-scripts-manual-approach) how
you would achieve the same, but with scripts.
]{#hs_cos_wrapper_post_body .hs_cos_wrapper .hs_cos_wrapper_meta_field

OPTION 1: Using the Classic Editor Console {#aNIACA1C00o}
------------------------------------------

Pasted below is a typical view of the Editor User Interface. Click on
the **"+"** button next to the job. As visible in the screenshot, the
job is called **"Agent job 1"**. The agent pool you choose does not
matter. The Pulumi task can run on both Linux as well as Windows
images.


::: {section-style="11" style="max-width: 100%;"}
![](https://quip.com/blob/aNIAAAb1O8e/xOwBXoso6iLooC1l5K5AaQ?a=vzdcNmORxglaR1DXB06AH8abt22mViudVkPg67D2zdYa){#aNIACAfCLLX}
