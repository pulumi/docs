---
title: "Manage Any Infrastructure with Policy as Code"
date: 2020-02-18
meta_desc: "Manage AWS, Azure, GCP, and Kubernetes with Policy as Code"
meta_image: crossguard.png
authors:
   - sophia-parafina
tags:
   - "Policy as Code"
   - "AWS"
   - "Azure"
   - "GCP"
   - "Kubernetes"
---
 
In an [earlier article]({{< relref "/blog/getting-started-with-pac" >}}), we introduced examples of Policy as Code to prevent two of the most common causes of data breaches. Policies are the guardrails of infrastructure. They control access, set limits, and manage how infrastructure operates. In many systems, policies are created by clicking on a GUI, making it difficult to replicate or version. Pulumi implements policy by writing it in Typescript, which ensures that you can write policies using software development practices such as automated testing, deployment, and version control.

<!--more-->

[Gareth Rushgrove](http://twitter.com/garethr) said in a QCon [presentation](https://www.infoq.com/presentations/policy-as-code/):

> “My policy kit doesn’t need to just be about bits on disk and packages, and files, and my SSH config, and my firewall rules, and my network rules. It can be about my cloud instances and how they’re actually configured and set up at the API level. Ultimately, there’s an API somewhere, and I have a bunch of resources, and I want to set some policies about them.”

Pulumi released the CrossGuard preview last fall. CrossGuard lets you verify, enforce, and apply custom policies on resources in your infrastructure. You can run policies against any Pulumi stack, which means that you can apply policies written in TypeScript to stacks written in any language supported by Pulumi such as Python, Go, and .NET languages. Policy Packs are bundles of policies, and when you run `pulumi up`, CrossGuard evaluates every resource in the stack against the Policy Pack. CrossGuard works in AWS, Azure, Google Cloud Platform, and Kubernetes.

The CrossGuard preview provides the following key features:

1. [Policy SDK](https://github.com/pulumi/pulumi-policy) for coding custom policies using TypeScript or Javascript
2. [Running a Policy Pack locally]({{< relref "/docs/get-started/crossguard/authoring-a-policy-pack#testing-the-policy-pack-locally" >}}) to speed up development and testing of policies. Validate infrastructure before deployment.
3. [AWSGuard](https://github.com/pulumi/pulumi-policy-aws) is a ready-to-apply playbook for enforcing AWS best practices for security, reliability, and cost
4. [Apply a Policy Pack]({{ < relref “/docs/get-started/crossguard/enforcing-a-policy-pack” >}}) across an organization to validate all the infrastructure deployed

CrossGuard ensures that you can enforce best practices for cost, compliance, security, and team practices for a single project or across your organization. Let’s look at how we can apply policies to infrastructure deployed across cloud providers and Kubernetes.

## Controlling cost on AWS

The amount of an AWS monthly bill has become a cliché in the tech industry. From services using improperly sized AMIs to orphaned infrastructure left running, there are many ways to incur a huge bill. One way to limit infrastructure spend is to set a `not to exceed` policy. We want to calculate the costs before deployment. The pricing data is available online, but calculating the cost using configuration data to enumerate resources and services can be a manual process. However, if your infrastructure as code solution is Pulumi, you can use your preferred programming language to calculate the cost before deployment and check it against your policy.

The example below shows how the policy finds all the instances and validates the aggregate cost against the maximum monthly amount allowed. It does this by finding the monthly on-demand price and aggregating all the costs.

```ts
import * as aws from "@pulumi/aws";
import { PolicyPack, validateStackResourcesOfType } from "@pulumi/policy";
import { getMonthlyOnDemandPrice, formatAmount } from "./utils";
import { maxMonthlyCost } from "./config";

new PolicyPack("aws", {
    policies: [
        {
            name: "instance-cost-estimate",
            description: `Limit instance costs to $${maxMonthlyCost}.`,
            enforcementLevel: "mandatory",
            validateStack: validateStackResourcesOfType(aws.ec2.Instance, (instances, args, reportViolation) => {
                // Aggregate costs.
                let totalMonthlyAmount = 0;
                instances.forEach(instance => {
                    totalMonthlyAmount += getMonthlyOnDemandPrice(instance.instanceType);
                });

                if (totalMonthlyAmount > maxMonthlyCost) {
                    reportViolation(`Estimated monthly cost [${formatAmount(totalMonthlyAmount)}] exceeds [${formatAmount(maxMonthlyCost)}].`);
                }
            }),
        }
    ],
});
```

Setting the maximum amount and calculating the monthly on-demand price for all `ec2` instances is aided by two helper classes `config` and `utils`. You can set variables such as `maxMonthlyCost` in `config.ts`. The utils can calculate costs from either a static file of prices, as demonstrated in the example, or through the [Amazon Pricing API](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html). Because we’re using a modern programming language, we can go beyond what a policy encoded in YAML or JSON can do.

config.ts

```ts
export const maxMonthlyCost = 500;
```

utils.ts

```ts
import * as fs from "fs";
import * as zlib from "zlib";

/**
* Cost-related helpers
*/
export const getPricingData = function (): (any) {
   const localFilePath = "./offers-ec2-us-east-1.json.gz";
   if (!fs.existsSync(localFilePath)) {
       throw new Error();
   }
   const localPricingDataGz = fs.readFileSync(localFilePath);
   const localPricingData = zlib.gunzipSync(localPricingDataGz);
   return JSON.parse(localPricingData.toString());
}

export const getMonthlyOnDemandPrice = function (instanceType: string): (number) {
   const pricingData: any = getPricingData();
   const pricingDataProducts: any = pricingData["products"];
   const pricingDataTermsOnDemand: any = pricingData["terms"]["OnDemand"];

   const arrValues = Array.from(Object.values(pricingDataProducts));
   const skus: any[] = arrValues.filter((it: any) =>
       it["attributes"]["instanceType"] === instanceType
       && it["attributes"]["operatingSystem"] === "Linux"  // TODO: use AMI to determine this
       && it["attributes"]["preInstalledSw"] === "NA"
       && it["attributes"]["usagetype"] === `BoxUsage:${instanceType}`
   );
   if (skus.length > 1) {
       console.log("Shouldn't find more than one sku. Continuing with first...");
   }
   const sku = skus[0]["sku"];

   const skuCode = `${sku}.JRTCKXETXF`; // JRTCKXETXF = On demand offer term code
   const skuPricing: any = pricingDataTermsOnDemand[sku][skuCode];

   const priceRateCode = `${skuCode}.6YS6EN2CT7`; // 6YS6EN2CT7 = Price per hour rate code
   const priceDimension: any = skuPricing["priceDimensions"][priceRateCode];

   const pricePerHour = Number(priceDimension["pricePerUnit"]["USD"]);
   const costPerMonth = pricePerHour * 24 * 30;
   return costPerMonth;
}

export const formatAmount = function (amount: number): (string) {
   return '$' + amount.toFixed(2);
}

```

## Compliance with Azure

The breadth and depth of services provided by cloud providers are vast. Beyond infrastructure services, you can access machine learning, image recognition, and voice services. If you can think of a service, it’s very likely a product offering. However, it’s best practice to operate your infrastructure under the principle of least privilege, i.e., only allowing access to resources needed to perform a job.

Azure Cloud Computing Services provides a list of services such as blockchain, mixed reality, Internet of Things. A best security practice is not to let unknown devices attach to your network. The policy below prohibits the use of IoT services because the endpoints are potentially untrusted and could be an entry point for bad actors.

```ts
import * as azure from "@pulumi/azure";
import * as pulumi from "@pulumi/pulumi";
import { PolicyPack, ReportViolation, ResourceValidationArgs, } from "@pulumi/policy";

const policies = new PolicyPack("azure", {
   policies: [
       {
           name: "prohibited-iot",
           description: "Use of IOT services is prohibited.",
           enforcementLevel: "mandatory",
           validateResource: (args: ResourceValidationArgs, reportViolation: ReportViolation) => {
               if (args.type.startsWith("azure:iot")) {
                   reportViolation(`Use of [${args.type}] is prohibited.`);
               }
           },
       },
   ],
});
```

## Control Ingress and Egress with Google Cloud Platform

Access control to resources is a fundamental part of infrastructure security. While production deployments may be tightly controlled, it’s not uncommon to spin up a dev infrastructure for testing during the development cycle. It isn’t unknown for devs to leave resources with public addresses on the Internet for a quick test and forget to tear it down after completing testing.

It’s a best practice to control ingress and egress of resources and not expose them on the Internet unless needed. The policy below issues a warning if a compute instance, or virtual machine has a public IP address, and it prohibits ingress from the public internet. When we run `pulumi up` or `pulumi preview`, the resource graph will show if either condition is met, and the deployment can be revised to follow the policies.

```ts
import * as gcp from "@pulumi/gcp";
import { validateResourceofType, PolicyPack, } from "@pulumi/policy";

const policies = new PolicyPack("gcp", {
   policies: [
       {
           name: "discouraged-gcp-public-ip-address",
           description: "Associating public IP addresses is discouraged.",
           enforcementLevel: "advisory",
           validateResource: validateResourceOfType(gcp.compute.Instance, (instance, _, reportViolation) => {
               const publicIps = instance.networkInterfaces.find(net => net.accessConfigs !== undefined);
               if (publicIps !== undefined) {
                   reportViolation("`accessConfigs` should be undefined in most cases.");
               }
           }),
       },
       {
           name: "prohibited-public-internet",
           description: "Ingress rules with public internet access are prohibited.",
           enforcementLevel: "mandatory",
           validateResource: validateResourceOfType(gcp.compute.Firewall, (firewall, _, reportViolation) => {
               const publicInternetRules = (firewall.sourceRanges || []).find(ranges =>
                   ranges === "0.0.0.0/0"
               );
               if (publicInternetRules !== undefined) {
                   reportViolation("`sourceRanges` should not be '0.0.0.0/0'");
               }
           }),
       },
   ],
});

```

## Enforcing best practices with Kubernetes

Immutability was one of the fundamental concepts behind containers. All application dependencies were locked in place, guaranteeing that the application would run regardless of where it was deployed. That principle can be carried forward to Kubernetes; a deployment should pin the containers to a specific version to keep the infrastructure consistent.

During development, an application may use containers tagged `latest`. Given the complexity of modern applications, these containers may pass testing and go into production. It isn’t until the application is in production and a new pod spins up to replace a failing pod that the containers tagged `latest` break a dependency. The new pod with the `latest` tags would cause the application to fail. The policy example below would prevent deploying pods from using containers tagged `latest`.

```ts
import * as k8s from "@pulumi/kubernetes";
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";

new PolicyPack("k8s", {
    policies: [
        {
            name: "pin-image-versions",
            description: "Images should be pinned to a specific version",
            enforcementLevel: "advisory",
            validateResource: validateResourceOfType(k8s.apps.v1.Deployment, (deployment, _, reportViolation) => {
                (deployment?.spec?.template?.spec?.containers || []).forEach(container => {
                    if (container.image && container.image.endsWith(":latest")) {
                        reportViolation("Image version should not be 'latest'.");
                    }
                })
            }),
        },
    ],
});
```

## Conclusion

Whether you deploy your infrastructure on AWS, Azure, GCP, or Kubernetes, Pulumi’s CrossGuard can help manage your infrastructure. We’ve shown four policies for controlling cost on AWS, ensuring that Azure infrastructure is compliant by allowing only approved resources, controlled access to and from VMs in Google Cloud Platform, and enforced best practices on Kubernetes by pinning container versions by tag. These policies work across many different resources because they use a real programming language that provides the ability to create policies that can use external data sources to determine costs, reuse the same policy on different providers, and allow us to see any violations, advisory or mandatory, before deployment. Learn more about policy as code:

- [Running AWS IAM Access Analyzer at Deployment Time]({{< relref "/blog/aws-iam-access-analyzer-and-crossguard" >}})
- [Enforcing Different Kinds of Policies for Cloud Resources]({{< relref "/blog/enforcing-different-kinds-of-policies-for-cloud-resources" >}})
- [Getting Started With PaC]({{< relref "/blog/getting-started-with-pac" >}})
