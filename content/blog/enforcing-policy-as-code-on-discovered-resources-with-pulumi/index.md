---
title: Enforcing Policy as Code on Discovered Resources with Pulumi  
date: 2025-02-04  
meta_desc: "Learn how Pulumi's new feature enables policy as code on discovered resources, including how to set it up and view policy violations."  
meta_image: crossguard.png  
authors:  
   - Tyler Dunkel  
tags:  
   - "Policy as Code"  
   - "Pulumi"  
   - "CrossGuard"  
   - "AWS"  
   - "Azure" 
   - "OCI"
   - "K8s" 
---

In this post, we’re introducing a powerful new feature in Pulumi that allows you to run policy as code (PaC) on discovered resources. Previously, PaC was limited to infrastructure as code (IaC) resources. Now, you can extend policy enforcement to resources discovered in your cloud environment. This new feature allows you to ensure that your cloud resources remain compliant with your policies, even after they’ve been provisioned outside of Pulumi.

### What is Policy as Code (PaC)?

Policy as Code (PaC) is a way to define and enforce infrastructure policies using code. Instead of relying on manual processes or static configuration files, PaC enables automated policy enforcement in a consistent, versioned way. Pulumi’s CrossGuard feature allows you to write policies in TypeScript, applying them across various cloud platforms such as AWS, Azure, GCP, and Kubernetes.

You can read more about CrossGuard in Pulumi’s documentation [here](/docs/iac/using-pulumi/crossguard/).

---

### Accounts and Insights

Before diving into how you can configure PaC for discovered resources, it's important to understand how Pulumi organizes resources and accounts for policy enforcement. Pulumi Insights provide visibility into the state of your cloud resources. The **Accounts** page in Pulumi shows all the accounts linked to your organization. On this page you can add new accounts which you can then add to policy groups to begin running policy packs against those accounts.

![Accounts Page](accounts-list-page.png)

You can integrate these accounts with Policy Groups to enforce policies across stacks and accounts. Once linked to a Policy Group, your resources will be automatically evaluated against the policies you define.

---

### Setting Up Policy Groups for Discovered Resources

To apply policies to your discovered resources, you first need to set up a **Policy Group**. A Policy Group in Pulumi enforces policies across a group of stacks and accounts in your organization. Each Policy Group can contain multiple of each stacks and acconts, and you can assign multiple Policy Packs to these groups.

Here’s a screenshot of the **Policy Group** configuration page, where you can create and manage policy groups:

![Policy Group Configuration](policy-group-config.png)

Once your Policy Group is set up, you can add discovered accounts to the group, which will ensure that the resources in those accounts are evaluated against the policies in the group.

![Policy Group Configuration](policy-group-add-account.png)

---

### Running Policies on Discovered Resources

Now that your Policy Group is set up, you can start running policies against your discovered resources. Currently Pulumi Insights supports running `resource` policies against all resource types supported by Pulumi Insights. Currently, stack policies are not supported. Pulumi will evaluate each resource against the policies defined in your Policy Pack. Violations will show up on the **Policy Violations** page, which gives you a detailed view of any non-compliant resources.

![Policy Violations](policy-violations-page.png)

Each violation includes details about the resource and the reason for the violation, helping you quickly identify and address issues.

---

### Key Takeaways

With Pulumi’s new PaC over discovered resources feature, you can now apply the same policies to both IaC and discovered resources across your cloud environment. You can now write a policy once and have it apply across all of your cloud resources. This enables you to maintain a consistent, compliant infrastructure no matter how resources are provisioned.

- **Set up Policy Groups** to enforce policies across stacks and accounts.
- **Link discovered accounts** to your Policy Groups.
- **View violations** on the Policy Violations page and take action to resolve them.

This new capability is available for AWS, Azure, OCI, and Kubernetes. Stay tuned for more updates on policy enforcement and discover how you can leverage Pulumi for cloud security and compliance.

For more information on getting started with Policy as Code, check out the following resources:

- [CrossGuard Overview](/docs/iac/using-pulumi/crossguard/)
- [Getting Started with Policy as Code](/blog/getting-started-with-pac)
