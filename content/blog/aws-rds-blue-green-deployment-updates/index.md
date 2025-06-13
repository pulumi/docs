---
title: "AWS RDS - Using Blue/Green Deployments for Low-Downtime Updates"
h1: "How to Achieve Low Downtime Updates on RDS with Blue/Green Deployments"
authors: ["lichtie"]
tags: ["aws", "rds", "postgres"]
meta_desc: "Pulumi can enable low downtime updates on your RDS instance using Blue/Green Deployments."
date: "2025-06-12"
meta_image: "pulumi-rds.png"

summary: |
    AWS RDS supports blue/green deployments to support database maintainence. In a blue/green deployment, you have one production (blue) and one staging (green) database. You can safely make changes to the green instance without affecting production and promote it to be the main instance. When you enable blue/green updates, Pulumi will temporarily set up a blue/green deployment for the duration of the update to minimize downtime. 
---

{{% notes %}}
Looking for more information on Blue/Green Deployments for RDS? Check out [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) from AWS.
{{% /notes %}}

AWS RDS supports blue/green deployments to support database maintainence. In a blue/green deployment, you have one production (blue) and one staging (green) database. You can safely make changes to the green instance without affecting production and promote it to be the main instance. When you enable blue/green updates, Pulumi will temporarily set up a blue/green deployment for the duration of the update to minimize downtime. 

There are many [benefits](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-overview.html#blue-green-deployments-benefits) to using blue/green deployments for updates, especially for critical databases that need to be kept available and safe from untested changes. 

## How it works

By default, updates to a database will be applied in-place, meaning there may be service interruptions while a database is modified especially when making long-running updates like changing the engine version, parameter groups, or storage settings. 

`blueGreenUpdate` can be enabled for [Low-Downtime Updates](https://www.pulumi.com/registry/packages/aws/api-docs/rds/instance/#low-downtime-updates). When this setting is on and an update is performed, the program starts the update by creating a blue/green deployment to maintain availability. Then, it performs the requested update on the green instance, performs a guardrail check, promotes the green instance, and finally deletes the old instance and removes the blue/green deployment. This leaves just the updated database running with minimal downtime during the update while minimizing the downtime.

Though this strategy typically increases the amount of time that updates need to run, it minimizes downtime for the application by keeping a current version of the database available during the update process. 

## How to use

## Additional Considerations
General [limitations and considerations for Amazon RDS blue/green deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-considerations.html#blue-green-deployments-limitations) are listed in the AWS documentation, but there are a few other considerations that should be taken into account when using them for updates with infrastructure as code (IaC).
* **No Custom Checks**: Because IaC will automatically perform the switchover when the update is complete, you will not have the opportunity to perform custom checks on the green instance before promoting it. RDS will run some basic [guardrails](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-switching.html#blue-green-deployments-switching-guardrails) checks before performing the switchover, but you will not be able to perform any additional checks.
* **Long Update Times**: Because the IaC program will deploy temporary resources before performing the update and destroy them after, blue/green updates will take considerably longer than their in-place counterparts. 
* **Manual Cleanup**: Because the green instance and blue/green deployment are temporary resources designed to decrease downtime during the update, they are not tracked in the IaC state. If the update fails partway through, these temporary resources may have to be cleaned up manually.
* **Resource ID Change**: On an update, the resource ID of the database might change since a new instance has been created. The endpoint and other details about the database will be maintained by AWS during switchover, but the resource ID should be dynamically retreived from the stack outputs whenever it is used to ensure it stays up to date.