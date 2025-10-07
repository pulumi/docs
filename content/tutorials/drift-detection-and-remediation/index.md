---
title_tag: "Detect and Remediate Infrastructure Drift"
title: "Detect and Remediate Infrastructure Drift"
layout: single
description: |
   Learn to detect and remediate infrastructure drift with Pulumi Deployments.
meta_desc: In this tutorial, learn to detect and remediate infrastructure drift in AWS using Pulumi Deployments and GitHub integration.
meta_image: meta.png
weight: 90
summary: |
   In this tutorial, you will learn how to detect and remediate infrastructure drift in AWS using Pulumi Deployments. You'll create an EC2 instance, introduce drift by making manual changes via the AWS CLI or console, and then use Pulumi Deployments to detect and correct the drift.
youll_learn:
 - How to set up and configure Pulumi Deployments for drift detection
 - How to introduce and identify infrastructure drift in an AWS environment
 - How to remediate drift ensuring your cloud infrastructure matches your desired state
prereqs:
   - Completion of the [Getting Started](/docs/get-started/) guide or familiarity with the basics of the Pulumi workflow
   - A [Pulumi Cloud account](https://app.pulumi.com/signup) and organization subscribed to the Enterprise or Business Critical editions
   - An [Amazon Web Services](https://aws.amazon.com/) account, access key ID, and secret access key
   - The [AWS CLI](https://aws.amazon.com/cli/)
   - Git installed and a [GitHub account](https://github.com/) with admin rights to a repository or organization
   - The [GitHub app](/docs/iac/packages-and-automation/continuous-delivery/github-app/) installed and configured for all repositories
estimated_time: 15
---

[Drift detection and remediation](/docs/platform/deployments/drift/) is a feature of Pulumi Cloud that automates the detection and correction of drift in your cloud environments. It integrates seamlessly with Pulumi Deployments and can be incorporated into CI/CD workflows and tools using the [Pulumi CLI](/docs/cli/) or [Automation API](/docs/using-pulumi/automation-api/). When changes occur outside Pulumi, such as manual updates in the cloud provider's console, Pulumi reports these discrepancies. Auto-remediation can also be configured to refresh your last known desired state, correcting any drift without manual intervention.

Using Pulumi Deployments, drift detection can be initiated via the CLI, performed on-demand in Pulumi Cloud with [click-to-deploy](/docs/platform/deployments/#deployment-triggers) actions, or [scheduled](/docs/platform/deployments/schedules/) to run at regular intervals. During each run, Pulumi compares the actual state of your cloud resources with the expected state stored in Pulumi Cloud. Any discrepancies are logged in the Drift tab, which also provides a history of detection runs, details of the drift detected, and triggered notifications. [Notifications](/docs/platform/deployments/drift/#configuring-notifications-for-drift-detection) can be sent via webhooks, Slack, Microsoft Teams, or email and detail the nature and scope of the drift.

Drift detection isn’t limited to Pulumi Deployments, you can integrate it into your own CI/CD pipelines using `pulumi refresh`. See [running drift detection from the CLI](/docs/platform/deployments/drift/#running-drift-detection-from-the-cli) for more information.

## Provision infrastructure

Let’s begin by using the Pulumi CLI to create a web server environment on AWS using a [Pulumi template](/templates/). In this example, you will select a template that provisions an EC2 instance within a VPC with a public subnet, an internet gateway, and a security group allowing HTTP traffic. You can also use [Pulumi AI](https://www.pulumi.com/ai) to create a scenario based on your cloud and language of choice.

Initialize a new Pulumi project and pick your programming language of choice:

{{< chooser language "typescript,python,go,csharp,yaml" / >}}

{{% choosable language typescript %}}

```bash
$ mkdir learn-pulumi-drift-detection && cd learn-pulumi-drift-detection
$ pulumi new vm-aws-typescript
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ mkdir learn-pulumi-drift-detection && cd learn-pulumi-drift-detection
$ pulumi new vm-aws-python
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
$ mkdir learn-pulumi-drift-detection && cd learn-pulumi-drift-detection
$ pulumi new vm-aws-go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
$ mkdir learn-pulumi-drift-detection && cd learn-pulumi-drift-detection
$ pulumi new vm-aws-csharp
```

{{% /choosable %}}
{{% choosable language yaml %}}

```bash
$ mkdir learn-pulumi-drift-detection && cd learn-pulumi-drift-detection
$ pulumi new vm-aws-yaml
```

{{% /choosable %}}

Follow the prompts to set up your project and accept the default values or specify new values, such as `aws-region`.

Run `pulumi preview` to see the changes that will be made.

```bash
pulumi preview
```

Now you can deploy the stack to see the outputs of your EC2 instance, which in this case will be `hostname`, `ip` and `url`.

```bash
pulumi up
```

```bash
View in Browser (Ctrl+O): https://app.pulumi.com/tutorials/learn-pulumi-drift-detection/dev/updates/1

    Type                              Name                   Status
+   pulumi:pulumi:Stack               drift3-dev             created (36s)
+   ├─ aws:ec2:Vpc                    vpc                    created (11s)
+   ├─ aws:ec2:Subnet                 subnet                 created (10s)
+   ├─ aws:ec2:InternetGateway        gateway                created (0.55s)
+   ├─ aws:ec2:SecurityGroup          secGroup               created (2s)
+   ├─ aws:ec2:RouteTable             routeTable             created (0.91s)
+   ├─ aws:ec2:RouteTableAssociation  routeTableAssociation  created (0.51s)
+   └─ aws:ec2:Instance               server                 created (12s)

Outputs:
   hostname: "ec2-18-236-205-169.us-west-2.compute.amazonaws.com"
   ip      : "18.236.205.169"
   url     : "http://ec2-18-236-205-169.us-west-2.compute.amazonaws.com"

Resources:
   + 8 created
```

Now you can view your new stack in Pulumi Cloud by following the **View in Browser** link. Click on the **Drift** tab, and you will see that Drift is unavailable as your stack's deployments are not yet configured. Click **Configure deployment settings** to see your Deployments source control settings.

To use drift detection with Deployments you will first need to create a new GitHub repository.

## Create a new repository on GitHub

1. Go to [GitHub](https://github.com/new) and create a new repository named `learn-pulumi-drift-detection`.
2. Copy the repository URL provided by GitHub.
3. Replace the origin with your new GitHub repo using the following commands:

```bash
git init
git add .
git commit -m "Initial commit for my Pulumi Drift tutorial"
git branch -M main
git remote add origin https://github.com/your-username/learn-pulumi-drift-detection.git
git push -u origin main
```

## Configure drift detection

Now return to your browser to set your deployment configuration source control settings. Navigate to your stack `Settings` and `Deploy` tab. Next, configure the required Deployment settings, including your source control.

1. Choose your GitHub organization/repository and the branch you created.

2. Add your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as environment variables, making sure to check the **Secret** option for both.

{{% notes type="info" %}}
Secret environment variables, such as `AWS_SECRET_ACCESS_KEY`, are encrypted end-to-end with Pulumi and can be set on each stack. However, by creating an [environment](/docs/pulumi-cloud/esc) with Pulumi ESC, you can centralize secrets and set up OIDC for secure authentication. This allows you to manage and share sensitive configuration data across multiple stacks efficiently.
{{% /notes %}}

Click **Save deployment configuration**.

{{< video title="Your description" src="pulumi-configure-drift.mp4" autoplay="true" loop="true" >}}

Once you have configured Pulumi Deployments, open the Actions menu and choose `Detect Drift`, then click `Deploy` to validate your stack, program and deployments are all running before you introduce drift.

![Screenshot of the Pulumi Cloud console to run a drift detection](./pulumi-detect-drift-action.png)

After the drift detection is complete, you will see a new drift run on the **Drift** tab timeline. Since this is the initial check and no deviations have been introduced, you will not receive any notifications indicating that drift has been detected, nor will you see any resources with changes.

## Introduce drift

To see drift detection in action, you will now manually introduce drift by making changes to your newly created EC2 resource. One example is adding a new tag, but you can also modify other aspects of the resource, such as changing the instance type, security group rules, or even stopping the instance. Any change outside Pulumi will cause drift, and Pulumi will detect these deviations during the next drift detection run.

### Add a tag to the EC2 instance using the AWS CLI

To add a tag via the AWS CLI, you'll first need to retrieve the EC2 instance ID. Use the the following command:

```bash
aws ec2 describe-instances --filters "Name=tag:Name,Values=webserver" --query "Reservations[*].Instances[*].InstanceId" --output text
```

Now, add the tag with the key `Description` and the value `Pulumi drift detection`:

```bash
   aws ec2 create-tags --resources <instance-id> --tags Key=Description,Value="Pulumi drift detection"
```

Replace `<instance-id>` with the actual instance ID of your EC2 instance.

## Run drift detection

Return to the Pulumi Cloud console and your stack, and again choose the **Detect drift** action and click **Deploy**.

After your run completes you will see a warning icon on the Drift tab indicating that drift has been detected. You can see a detailed summary of what resources have been updated or deleted, the properties that have changed, when the drift run happened, and a link to the deployment with further details.

{{< video title="Your description" src="pulumi-drift-detected.mp4" autoplay="true" loop="true" >}}

## Remediate drift

Now that you have detected and reviewed your infrastructure drift, you can choose to remediate and overwrite the changes made in your cloud provider with the most recently specified desired state of your Pulumi program.

To do so, open the **Actions** menu, select the **Remediate drift** option, and click **Deploy**. Once the deployment is complete, your infrastructure will be restored to the desired state expressed in your code.

## Automate drift detection

In addition to manually triggering drift detection, you can automate this process by scheduling regular drift detection runs using [deployment schedules](/docs/platform/deployments/schedules/). This ensures that any unexpected changes in your infrastructure are promptly identified and remediated without manual intervention.

## Clean up your resources

To avoid incurring any unwanted charges, clean up the resources you created:

1. Navigate to your stack in Pulumi Cloud and open the **Actions** menu.
2. Select the **Destroy** option to delete all resources in this stack, and click the confirmation checkbox.
3. Delete the stack by navigating to the **Settings** tab and choose **Delete stack** to remove the stack, including all its deployment history and state files from Pulumi Cloud.
4. Delete the GitHub repository you created.

## Next steps

In this tutorial, you learned how to set up automated drift detection and remediation with Pulumi Deployments. First you created an EC2 instance, including a VPC with a public subnet, an internet gateway, and a security group allowing HTTP traffic. Then, you introduced drift by manually adding a tag to your EC2 resource via the AWS console.

To learn more about drift detection with Pulumi, take a look at the following resources:

- [Pulumi drift detection](/docs/platform/deployments/drift/)
- [Pulumi Deployments](/docs/platform/deployments/)
- [Pulumi refresh](/docs/iac/cli/commands/pulumi_refresh/)
