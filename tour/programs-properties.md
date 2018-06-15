---
title: Resource properties
---

Each resource object has properties.

At creation time, you supply *input* properties to control the desired state of the resource:

```javascript
var buck = new aws.s3.Bucket("photos", { versioning: { enable: true } });
```

The resulting resource object offers *output* properties that communicate its final state:

```javascript
export domainName = buck.bucketDomainName;
```

These properties are key to how Pulumi works; the diffing of them instructs Pulumi how to do its deployments.

A resource often has different output properties than input properties, because cloud providers may compute outputs.
For instance, the URL for an API, the IP address of a load balancer, etc, are typically auto-assigned.

A resource's output properties a promise-like in nature, because they aren't known until creation finishes.
[We will explore this shortly](./deployments-outputs.html) to see what this implies about interacting with them.

***

<div class="tour-nav">
    <a class="tour-button enabled" href="programs-resources.html" title="Resources">◀</a>
    <span class="tour-index"><strong>6</strong>/9</span>
    <a class="tour-button enabled" href="programs-configuration.html" title="Custom configuration">▶</a>
</div>
