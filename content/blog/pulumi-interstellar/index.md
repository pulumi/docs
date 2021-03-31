---
title: "Pulumi Interstellar"
date: 2021-04-01
meta_desc: "Infrastructure as code was just the start. Today we announce Pulumi Interstellar for Terraforming as Code."
meta_image: meta.png
authors:
    - joe-duffy
tags:
    - rockets
    - terraforming
    - domes

---

Earth is just the beginning. We are putting down the foundations of space so our children can build their future.  At Pulumi, we are committed to making life multiplanetary. We are excited to announce Pulumi Interstellar, a collection of resource providers that will help us reach the future of a space-faring and multi-planet species.

<!--more-->

For our first offering of space related resource providers, we have aligned closet with the current priorities in the space industry today:

1. Getting to New Planets
1. Making Planets Habitable

We believe that solving those two areas for our customers will enable people to build the future they imagine, on the planets they desire to inhabit. One challenging aspect of achieving our goals is that each new planet represents a different operational environment.

One might think the right solution for provision and managing resources in space would be a proprietary domain-specific language designed from the ground up to operate in these new environments. However 10 out of 10 leading rocket scientists confirm that the heterogeneous diversity of existing programming languages allows us to move faster and with less frustration.

In the following sections we will take a closer look at the two main areas defined above and how you too can begin building the future in a familiar programming language like JavaScript, TypeScript, Python, Go, or .NET.

## Rockets As Code

Rockets are the first step to making humans a multi-planet species to enable you and your resources to travel to new planets. Today, we are extremely excited to introduce the Pulumi Rocket Provider, which allows users to configure rocket fuel requirements, initiation sequences, configure deployment payloads, reserve seats, and much more.

In the initial release of the Rocket Provider we are happy to enable two key use cases: Resource Deployment and Planetary Travel.

### Resource Deployment

```typescript
import * as spacex from "@pulumi/spacex"

/**
* Provision rocket
*/
const engineId = spacex.rocket.getEngine({
   owners: ["420"], //SpaceX
   mostRecent: true,
   filters: [{name: "SuperDraco", values: ["spacex/engines/super-draco-15.03-*]}]
});

const spaceship = new spacex.spaceship.Instance("Edward Isreal", {
   instanceType: spacex.spaceship.InstanceTypes.interplanetary,
   engine: engineId,
   capability: kuiper_belt,
   tags,
}]
```

On Day 1 you can deploy resources via reusable rockets. By declaring a payload on your Rocket, you tell Pulumi  to deliver the payload to the location specified. Resource Deployments will be particularly useful when configuring a new planet in the initial stages, as you can deploy new resources and terraforming equipment in a consistent, repeatable, and scalable manner.

Once the rocket arrives at its destination Pulumi’s Space AI Assistant, nicknamed IRWIN, will take control to ensure your resources are deployed efficiently and correctly. By using Resource Deployments you can ensure your applications and workloads are up and running before arriving on your new planet.

![Spaceship](spaceship.png)

### Planetary Travel

```typescript

const config = pulumi.Config();
const passengers = config.require("passengers")

const seats = spacex.spacex.PassengerGroup("Robinsons", {
   spaceshipId: spaceship.then(it => it.id),
   seats: passengers,
   departure: "Luna",
   destination: "Mars",
   berth: "Colonist",
   tags,
}]
```

Once a planet is habitable and configured to your specifications, you will need a way to travel to your new home. Simply adding a `seats` argument to any Rocket will reserve those seats on the rocket (as they eventually become available).

When your program completes deployment, you will receive a reservation confirmation via the email you used to register for the Pulumi Service. If you are an open source user, you will need to provide a valid email address via the `--confirmation-email` flag to receive your confirmation email.

## Terraforming As Code

One of the most challenging obstacles preventing humans from becoming a multi-planet species is that Earth is the only planet in the known solar system that supports life. While there are many options for making other planets liveable, the team at Pulumi believes in the two step model towards habitability.

First, we need to provision dome-based communities in a repeatable and scalable manner. Once we have established our dome communities, we can then terraform any planet using the latest terraforming technology, i.e., nuclear missiles.

### Dome-Based Communities

```typescript
import * as thecompany from "@pulumi/weyland-yutani"

const domeId = thecompany.dome.getDome({
    owners: ["099720109477"], // Weyland-Yutani
    mostRecent: true,
    filters: [{ name: "name", values: ["weyland-yutanu/terraforming/acheron-*"] }],
}).then(it => it.id);

const terradome = thecompany.dome,Instance("Hadley's Hope", {
   instanceType: thecompany.dome.InstanceType.LV_246,
   dome: domeId,
   type: atmospheric-processor,
   tag,
}]
```

The first step to establish humanity on other planets is to provision dome-based communities and build critical infrastructure and resources while we work to terraform the planet. Out of the box Pulumi provides boilerplate communities that are flexible and resilient enough to support any use case.

![Domes](dome.png)

### Nuclear Terraforming

While we will not be able to support nuclear terraforming on Day 1, we are working extremely diligently to ensure our customers have access to state of the art terraforming techniques. We hope to bring a preview of Nuclear Terraforming to customers in early Q3 of 2022. Be on the lookout for monthly updates as we develop this new groundbreaking technology.

![Terraforming](nuke.png)

How To Get Started
Getting started is as simple as getting started with any other resource provider, you just need to download the package with your preferred language’s package manager, configure the provider, and then start building. All space resources are billed via Dogecoin, so you will need to provide a wallet address in your provider’s arguments.

```bash
$ pulumi config set --secret doge DilB3JrTyGm55FiMyRlhM7NZmfj0J9QVX
```

Don't worry, we'll encrypt your wallet address. Your Dogecoin wallet will go straight to you provider and Pulumi never receives or handles your secrets.

## Summary

Today is one of the most exciting days in Pulumi's short history and we are incredibly excited to partner with our customers and leading space companies to make our multi-planetary dreams a reality. We cannot wait to see what you’ll build!
