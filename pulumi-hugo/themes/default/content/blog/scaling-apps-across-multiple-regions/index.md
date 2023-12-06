---
title: "Scaling Applications Across Multiple Regions"
date: 2023-12-05T20:24:40Z
draft: false
meta_desc: Learn about deploying applications to multiple regions globally. Uncover strategies for achieving high availability in a distributed environment.
meta_image: meta.png
authors:
    - adora-nwodo

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - multi-region-scaling
    - cloud-deployment
    - application-scalability
    - distributed-systems
    - geographic-distribution
    - high-availability

---

As a team building a distributed cloud service that will be used by different people around the world, you will need strategies to cater to users globally, ensuring uninterrupted service even in the face of disruptions. Have you ever wondered how businesses operate and deliver high-level performance across different regions?  Well, that is the result of scaling applications across multiple regions --- in a bid to ensure constant access and flexibility, organizations distribute their applications and databases across various geographic regions so that if one part faces issues, the service remains available elsewhere.

In this article, we will explore the significance of multi-region scaling and show using Pulumi for multi-region deployment.

## Understanding multi-region scaling

When distributed systems adapt (or implement) multi-region scaling, they already position themselves for high availability because the redundancy minimizes downtime and ensures that the service stays up and running. If one region experiences issues, such as server downtime or network problems, the application remains accessible to users in other regions. This also leads to better performance in their systems because a fast and responsive experience for users across the globe is achieved.

It is easier to reach a global audience when you have scaled geographically. This means that if you have customers in Europe and the US and you’re a multi-regional cloud service, by distributing your traffic across different instances, you can improve your customers' experience by serving users worldwide and also catering to diverse regions and time zones. Specific data protection and privacy regulations are also met, as multi-region scaling allows systems to adhere to these regulations by keeping data within defined boundaries.

Although multi-region deployments are needed for scaling, availability, and performance, there could be downsides associated with them if the design process for being multi-region isn’t well thought out. Some of the challenges that could be encountered are:

- **Complexity:** Each region may have unique requirements, and ensuring consistency in configuration can be challenging. Troubleshooting across regions can add complexity to the infrastructure setup.

- **Cost:** Expanding to multiple regions often increases infrastructure costs. Businesses need to balance the cost of maintaining multiple resources with the benefits of high availability and performance.

- **Deployment consistency:** Inconsistencies in resource configuration can lead to performance issues and errors, impacting the user experience.

- **Security compliance:** Meeting security and compliance standards in different regions may require additional effort. Each jurisdiction may have unique data protection and privacy regulations, and this can be a challenge.

## The Pulumi solution

A stack is a distinct deployment target within a Pulumi project. Stacks enable you to organize, version, and manage your infrastructure code effectively. They are flexible enough to do more than merely plan deployments across different stages of development. You may better control infrastructure orchestration with them as an adaptable tool for managing deployments in a variety of circumstances. Each stack represents a separate instance of your infrastructure, allowing you to deploy and manage your resources in different environments or configurations. To learn more about stacks, you can read [this](https://www.pulumi.com/docs/concepts/stack/).

Consider how Pulumi Stacks can be used effectively in the following ways:

- **Deploying to different environments:** You can use stacks to deploy into different environments, like development, staging, and production. Stacks allow separate configurations to be maintained throughout these contexts.

- **Deploying to different regions:** You can use stacks to effortlessly manage deployments in multiple regions (e.g. westus2, westeurope, northeurope etc.). This enables you to scale your infrastructure across geographical locations while maintaining a centralized and consistent approach to resource allocation. These deployments could be in the same environment, but different regions (e.g. production westeurope, and production westus2), and you can use stacks to handle the different permutations.

- **Deploying to different cloud provider accounts:** Stacks can also be used to automate deployments across several cloud provider accounts. Even when working with different cloud platforms, your deployment process can be unified and consistent.

Each of these stacks have their own configuration, but there are also some configuration values that are shared across stacks. To obey the DRY (Don't Repeat Yourself) programming rule, you can pair stacks with Pulumi ESC (Environments, Secrets, and Configuration). This pairing results in a flexible deployment strategy. The combination empowers users to segregate configurations for each environment, manage secrets securely, and maintain a centralized store for configuration data. This ensures a clean separation of concerns, contributing to improved security and maintainability in multi-environment deployments. Pulumi ESC is a pivotal aspect of managing stacks, especially as the number of stacks grows. The idea is to store configuration settings separately from your code, ensuring that each stack has configuration values tailored to its specific needs.

In the next section, we'll show how to deploy applications across different regions using Pulumi stacks and Pulumi ESC.

### Define regions and stacks

Let's look at an example of deploying to three distinct regions — `production westus2`, `production westeurope`, and `staging southeastasia` — using stacks. In this scenario, we will use three stacks: `prodwu2`, `prodwe`, and `stagingsea`. Each of these stacks will have a stack configuration file associated with it, named `Pulumi.<stack>.yaml`. In this example, we are using stacks both to deploy into different environments (production and staging), but also to deploy into different regions (West US 2, West Europe, and Southeast Asia).

You can create your stacks by running:

```bash
pulumi stack init prodwu2
pulumi stack init prodwe
pulumi stack init stagingsea
```

After creating your stacks, you can update your Pulumi configuration YAML files with their corresponding values.

**Pulumi.devwe.yaml:**

```yaml
config:
  multi-region:appServiceTier: Free
  multi-region:appServiceSize: F1
  multi-region:environment: development
  multi-region:location: westeurope

environment:
  imports:
    - shared-multi-region
```

**Pulumi.prodwu2.yaml:**

```yaml
config:
  multi-region:appServiceTier: PremiumV2
  multi-region:appServiceSize: P1V2
  multi-region:environment: production
  multi-region:location: westus2
```

**Pulumi.prodwe.yaml:**

```yaml
config:
  multi-region:appServiceTier: PremiumV3
  multi-region:appServiceSize: P1V3
  multi-region:environment: production
  multi-region:location: westeurope
```

**Pulumi.stagingsea.yaml:**

```yaml
config:
  multi-region:appServiceTier: Standard
  multi-region:appServiceSize: S1
  multi-region:environment: staging
  multi-region:location: southeastasia
```

#### Leveraging ESC

For configuration values that are shared across stacks, you should use ESC so that you can create them once and reference them everywhere. In the referenced codebase, there are other values e.g. `resourceNamePrefix`, `storageKind`, `storageSkuName`, and `tenantId`. Since these values are the same across all our stacks, we can leverage ESC so that we can declare them once and reuse them everywhere.

{{% notes type="info" %}} Pulumi ESC is a feature of Pulumi Cloud and in order to use ESC, you should be using Pulumi Cloud as your backend. {{% /notes %}}

To leverage ESC, you first need to initialize a new environment like this:

```bash
esc env init shared-multi-region
```

{{% notes type="info" %}} You can use the esc CLI, as shown, or you can use the `pulumi env` command. {{% /notes %}}

After which, you can set all the value for the configurations you need. Remember to add it as part of the `pulumiConfig` object, so that your Pulumi stack understands and can pick it up.

```bash
esc env set shared-multi-region pulumiConfig.resourceNamePrefix mrapp
esc env set shared-multi-region pulumiConfig.storageKind "Standard_LRS"
esc env set shared-multi-region pulumiConfig.storageSkuName "Standard_LRS"
esc env set shared-multi-region pulumiConfig.tenantId "00000000-0000-0000-0000-000000000000" # Your tenantId
```

After successfully adding your config values to your new environment, you can reference it across all your stacks like this:

```yaml
config:
  multi-region:appServiceTier: Free
  multi-region:appServiceSize: F1
  multi-region:environment: development
  multi-region:location: westeurope

environment:
  imports:
    - shared-multi-region
```

Here, `shared-multi-region` has more configurations and you can add references to them in your stack without copying and pasting multiple lines.

### Update Pulumi code

Once you have set up the Pulumi ESC environment and linked it to your Pulumi stack configuration, you also need to update your Pulumi code to use the configuration values instead of any hard-coded values. This is shown in the code snippet below using the `config.require` method:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure from "@pulumi/azure";

// Define the configuration
const stackName: string = pulumi.getStack();
const config = new pulumi.Config();

const appServiceTier = config.require("appServiceTier");
const appServiceSize = config.require("appServiceSize");
const resourceNamePrefix = config.require("resourceNamePrefix"); // gotten from ESC
const storageKind = config.require("storageKind"); // gotten from ESC

// ... more code

// Create an Azure Resource Group
const resourceGroup = new azure.resources.ResourceGroup(resourceGroupName, {
    resourceGroupName: resourceGroupName,
    location: location,
    tags
});

// Create an Azure Storage Account
const storageAccount = new azure.storage.StorageAccount(storageAccountName, {
    accountName: storageAccountName,
    resourceGroupName: resourceGroup.name,
    kind: storageKind,
    location: location,
    sku: {
        name: storageSkuName
    },
    tags
});

// ... more code
```

### Deploy stacks

Your Pulumi stacks should be ready to deploy now---you've updated the code to use configuration values that either come from the stack or from Pulumi ESC, and you've done both the per-stack configurations and the Pulumi ESC configuration values. Now it's just a matter of running `pulumi up`:

```bash
pulumi up --stack prodwu2
pulumi up --stack prodwe
pulumi up --stack stagingsea
```

Now, you have seen how to use stacks to represent regions and environments. With this approach, the dynamism happens through your configuration and your code doesn’t have to change per region.

To see a full application with more detail, click [here](https://github.com/pulumi/pulumitv/tree/master/2023/december/multi-region).

## Considerations for high availability

Once you’ve configured your multi-region deployments, you should consider strategies for high availability to ensure that applications remain operational and accessible even in the face of failures.

### Placing workloads across multiple regions

Effectively distributing workloads across various geographic regions is a key strategy for maintaining high availability. You can employ one of the following methods to distribute traffic across multiple regions:

- **Active/Passive with hot standby:** In this approach, one region actively handles traffic while the other remains on hot standby, meaning the services in the secondary region are always running.

- **Active/Passive with cold standby:** Similar to hot standby, in this case, the services in the secondary region aren't allocated until needed for failover. This minimizes costs but might increase recovery time.

- **Active/Active:** Both regions are active, and requests are load-balanced between them. If one region becomes unavailable, it is taken out of rotation.

In the context of infrastructure-as-code using Pulumi, these strategies often translate to the management of multiple stacks. In active/hot standby and active/active configurations, there will typically be two Pulumi stacks, each with its allocated set of resources. This allows for the independent management and deployment of resources in each region.

On the other hand, in an active/cold standby scenario, while there might be a Pulumi stack defined for the cold standby site, it won't have any resources initially allocated. Part of the failover process would involve running a `pulumi up` specifically for the cold standby region, triggering the allocation of resources as needed. This dynamic resource allocation during failover helps optimize costs, as resources are provisioned only when necessary, contributing to a more efficient use of cloud resources.

### Replicating data

Implementing appropriate data replication solutions is an important factor in enhancing system resilience. This involves creating duplicates of our databases and storing them in several locations to ensure that our data remains consistent and accessible. Such replication is especially important for sustaining smooth operations if one region has disruptions or malfunctions.

Exploring the details of data replication exposes the most difficult aspects of being multi-region with high availability. Finding the correct balance between Recovery Point Objective (RPO) and Recovery Time Objective (RTO) is an important factor. RPO refers to how frequently we store our data, but RTO refers to how soon we can get things back on track if there is a problem. Finding the correct balance entails considering how frequently we update our data and how long it takes to recover from unanticipated errors.

Services such as AWS Aurora Global Databases or Azure Cosmos DB can be used to simplify this complex operation. These services are intended to enable multi-region database replication as simple as possible, while also maintaining high availability across distributed systems.

### Configuring load balancing, failover, and disaster recovery

Configuring load balancing, failover, and disaster recovery is needed to achieve high availability in a system. These strategies help distribute traffic efficiently, ensure continuous operation, and mitigate the impact of potential failures or disasters.

- **Load balancing:** Choose a way to balance the work of your servers—it could be by using a cloud service like Azure Traffic Managers. Then, decide how you want to divide the job among your servers, like taking turns or picking the one with the least number of tasks to process. Make sure you set up health checks to keep an eye on how well your servers are doing. If you're working in different parts of the world, use global balancing to send people to the closest or healthiest place for your data.

- **Failover:** Think about things that might go wrong, like servers crashing or network problems. If something breaks, set up a plan to automatically switch to a healthy backup. Monitor your servers to catch anomalies quickly. Make sure you have failover infrastructure ready to take over if there is ever an outage. Also, make sure the tool that shares the work (the load balancer) doesn't break itself. If something goes wrong, set up a way for your system to keep working, even if it's not at full power. This is known as graceful degradation.

- **Graceful degradation:** Graceful degradation is a concept that prepares systems for potential failures. When faced with unanticipated challenges such as server crashes or network outages, a system designed with graceful degradation adjusts its performance to maintain key functionality. Consider a web application that is significantly reliant on external APIs for real-time data. If one of these APIs experiences a temporary glitch, a system that embraces graceful degradation may seamlessly switch to presenting cached data or simplifying functionality, ensuring users maintain access to core functionalities even when service outages occur. This strategy is also applicable to cloud-based services, where a system intelligently scales down non-essential features under high loads in order to prioritize key activities, proving the robustness of systems designed using gentle degradation principles.

- **Disaster recovery:** Be ready for the worst by copying your important data to different places. Have clear steps on how to bring back your data and programs if everything goes wrong. Spread your tools and services in different areas to reduce problems if one place has a big issue. Make sure your system can easily switch to another area if a big problem happens. Plan for disasters by making step-by-step guides on what to do. Test your disaster plans often to be sure they work well and to find any areas that need fixing.

## Security considerations

It is one thing to multi-scale, it’s another responsibility to secure the infrastructure. Securing a multi-regional infrastructure introduces challenges. In multi-region setups, data privacy can be tricky due to different regulations, like GDPR in Europe, or The California Consumer Privacy Act (CCPA). Using differential privacy and data residency controls are important when handling data according to each region's rules. Pulumi policy as code also enables the proactive design and enforcement of compliance-ready policies. Ensuring compliance in industries like healthcare and finance adds complexity, requiring a tailored approach based on specific regulations.

Expanding infrastructure in multi-regional setups makes them more vulnerable to cyber threats. To tackle this, it's important to use good security practices like micro-segmentation, intrusion detection systems, and regular penetration testing. Being proactive in incident response planning, controlling access effectively, and employing strong encryption methods are also important for a secure cloud infrastructure.

## Conclusion

As we navigate the complexities of multi-region deployments, Pulumi can help in simplifying infrastructure management. It is important to note that embracing the challenges of multi-region scaling is a strategic move for technology projects navigating the global landscape. With Pulumi stacks and ESC configurations, you can seamlessly manage deployments and configurations, ensuring adaptability and security.

Did you learn something new? We’d like to know. If you’d like to explore further or discuss your specific use case, you can schedule a consultation with a solutions engineer. You can also join our community to be a part of the continuous conversation, and we can’t wait to see what you build!
