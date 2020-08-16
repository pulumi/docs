---
title: "How Pinpoint Manages Kubernetes Costs and Deployments"
date: 2020-08-17
meta_desc: "Pinpoint uses Pulumi to streamline deployments and scale Kubernetes"
meta_image: meta.png
authors:
    - sophia-parafina
tags:
    - Pinpoint
    - Kubernetes
---

{{% notes type="info" %}}
This guest blog was contributed by Andrew Kunzel and Michael Goode. Andrew is the Director of Backend Engineering and Michael is a Platform Operations Engineer at Pinpoint.
{{% /notes %}}

At Pinpoint, Kubernetes is the most powerful tool in our arsenal. It allows us to deploy and rapidly scale our applications with speed and efficiency that continues to delight our customers. In recent years, managed services like AWS EKS have made it easier than ever to leverage the power of Kubernetes in even the smallest of organizations. Yet even with these new conveniences, managing all of this infrastructure can be a daunting task. Right out of the gate, we knew that we wanted to avoid the burden of maintaining repositories full of home-brewed deployment scripts and domain-specific languages like YAML.

<!--more-->

Pulumi affords us the ability to streamline the development of our cloud infrastructure with open source libraries that integrate deeply into AWS service APIs and support many popular languages. This introduces powerful, high-level constructs like for-loops and strong type-checking alongside the more rigid declarative approach mandated by other available tools. And it’s not just limited to hardware! We also use Pulumi to substantially reduce the overhead required to deploy critical services that run on Kubernetes itself, which helps to consolidate our deployment configuration even further and makes updating these services a breeze.

In this blog post, we’ll share some simple and intuitive ways in which Pulumi has simplified our approach to infrastructure-as-code.

## Spot Instances

As a startup, we are always budget-conscious. Every tool we use has to justify either the up-front subscription cost or development time, or both. To tamp down our AWS EC2 costs, we decided to leverage EC2 spot instances as worker nodes in our development Kubernetes cluster. Spot instances are highly cost-efficient because they use spare compute capacity within a region at a fraction of the on-demand instance price. When you request a spot instance, you must offer the maximum price you are willing to pay. This price can fluctuate based on demand in a particular region, but will always be less than or equal to the current on-demand price. Knowing this, we could use Pulumi’s JavaScript AWS library to get the current on-demand price for a given instance type and plug that directly into the spotPrice property of the node group configuration.

```javascript

function getOnDemandPrice(instanceType: aws.ec2.InstanceType): pulumi.Output<any> {
  return pulumi.output(aws.pricing.getProduct({
    filters: [
      {
        field: "instanceType",
        value: `${instanceType}`,
      },
      {
        field: "operatingSystem",
        value: "Linux",
      },
      {
        field: "location",
        value: "US East (N. Virginia)",
      },
      {
        field: "preInstalledSw",
        value: "NA",
      },
      {
        field: "usageType",
        value: `BoxUsage:${instanceType}`,
      },
      {
        field: "termType",
        value: "OnDemand",
      },
    ],
    serviceCode: "AmazonEC2",
  }, { async: true })).apply(data => {
    let result = JSON.parse(data.result)
    let typeOnDemand = result.terms.OnDemand
    let skuTermCode = Object.keys(typeOnDemand)[0]
    let rateCode = Object.keys(typeOnDemand[skuTermCode].priceDimensions)[0]
    let price = typeOnDemand[skuTermCode].priceDimensions[rateCode].pricePerUnit.USD
    return price
  })
 }

  cluster.createNodeGroup(`${stack.env}-${name}`, {
    amiId: ami,
    version: kubernetesVersion,
    instanceProfile: nodeGroupInstanceProfile,
    minSize: 1,
    maxSize: 10,
    desiredCapacity: 5,
    nodeRootVolumeSize: 100,
    nodeAssociatePublicIpAddress: false,
    nodeSubnetIds: stack.privateSubnets,
    instanceType: instanceType,
    spotPrice: getOnDemandPrice(instanceType)
  })

function getOnDemandPrice(instanceType: aws.ec2.InstanceType): pulumi.Output<any> {
 return pulumi.output(aws.pricing.getProduct({
   filters: [
     {
       field: "instanceType",
       value: `${instanceType}`,
     },
     {
       field: "operatingSystem",
       value: "Linux",
     },
     {
       field: "location",
       value: "US East (N. Virginia)",
     },
     {
       field: "preInstalledSw",
       value: "NA",
     },
     {
       field: "usageType",
       value: `BoxUsage:${instanceType}`,
     },
     {
       field: "termType",
       value: "OnDemand",
     },
   ],
   serviceCode: "AmazonEC2",
 }, { async: true })).apply(data => {
   let result = JSON.parse(data.result)
   let typeOnDemand = result.terms.OnDemand
   let skuTermCode = Object.keys(typeOnDemand)[0]
   let rateCode = Object.keys(typeOnDemand[skuTermCode].priceDimensions)[0]
   let price = typeOnDemand[skuTermCode].priceDimensions[rateCode].pricePerUnit.USD
   return price
 })
}

 cluster.createNodeGroup(`${stack.env}-${name}`, {
   amiId: ami,
   version: kubernetesVersion,
   instanceProfile: nodeGroupInstanceProfile,
   minSize: 1,
   maxSize: 10,
   desiredCapacity: 5,
   nodeRootVolumeSize: 100,
   nodeAssociatePublicIpAddress: false,
   nodeSubnetIds: stack.privateSubnets,
   instanceType: instanceType,
   spotPrice: getOnDemandPrice(instanceType)
 })
```

And just like that, we can quickly provision spot instances on our cluster! Better yet, we don’t ever have to worry about setting a valid spot price or managing this process via custom scripts in a CI/CD pipeline. The entire deployment is easily managed within the same file.

## Managing Third-Party Services

Pulumi also helps us to manage the services that we run on our Kubernetes clusters by allowing us to efficiently configure these services consistently that avoid drift and minimizes complexity. Pulumi is extremely flexible in this regard because it offers native support for de-facto tools like Helm and Kustomize as well as individual Kubernetes components like pods and deployments. You can even render raw YAML, which greatly simplifies integration with legacy systems or custom components.

### Transformations with Helm

We prefer to use Helm for most of our deployments. It is an excellent tool for deploying third party services and customizing them with a useful but complicated templating system. These templates are great when they work, but if the chart's maintainer doesn’t make something configurable, you’re usually unable to alter the manifest when it comes time to deploy your chart. You’d likely have to fork and manage a custom version of the chart yourself in the worst case. Luckily, Pulumi can override just about anything in a manifest by using a Transformation. This property allows you to manipulate a manifest's content before it is rendered and applied to the cluster.

As an example, we recently discovered that some versions of the Traefik Helm chart do not include an explicit namespace definition on certain templates. This caused a few resources to install into the default namespace; without Pulumi, we would have been unable to fix this issue without forking the chart or writing a post-install script to wrangle them back. Luckily, all we really had to do was create a function to set the object metadata and then pass that function directly into the ‘transformations’ property of the Traefik Helm chart:

```javascript
 function setNamespace(obj: any) {
    if (obj.metadata.namespace === undefined) {
      obj.metadata.namespace = 'platform-services';
    }
  }

 new k8s.helm.v3.Chart("traefik", {
    repo: "traefik",
    chart: "traefik",
    version: "6.0.0",
    namespace: 'platform-services',
    transformations: [setNamespace],
    values: {
      deployment: {
        replicas: 3
      },
    },
  }, { provider: provider });
```

```javascript
function setNamespace(obj: any) {
   if (obj.metadata.namespace === undefined) {
     obj.metadata.namespace = 'platform-services';
   }
 }

new k8s.helm.v3.Chart("traefik", {
   repo: "traefik",
   chart: "traefik",
   version: "6.0.0",
   namespace: 'platform-services',
   transformations: [setNamespace],
   values: {
     deployment: {
       replicas: 3
     },
   },
 }, { provider: provider });
```

This will run the transformation on every manifest used by the chart, fixing our issue in only a few code lines.

Being able to manage all of our infrastructure as code and enhance the behavior of standard Kubernetes deployment tools has dramatically improved our ability to deploy services and maintain our configuration. We look forward to expanding our use of Pulumi as we grow as an organization and empower our developers further.

## About the Pinpoint Team

<iframe style="margin: 0px auto; display: block; border: 0;" title="Andrew Kunzel – Developer Profile" xml="lang" src="https://cards.pinpoint.com/profile?id=d160098419834b08&amp;env=edge" width="600" height="400" scrolling="no"></iframe>

Read more about [Andrew](https://insights.pinpoint.com/developer-spotlight-andrew-kunzel-director-of-backend-engineering) in his Developer Spotlight.

<iframe style="margin: 0px auto; display: block; border: 0;" title="Mike Goode – Developer Profile" xml="lang" src="https://cards.pinpoint.com/profile?id=aac75d10d212e12c&amp;env=edge" width="600" height="400" scrolling="no"></iframe>

Read more about [Mike](https://insights.pinpoint.com/developer-spotlight-michael-goode-platform-operations-engineer) in his Developer Spotlight.
