---
title: Resource properties
expanded_url: /docs/tour/programs/
menu:
  tour:
    parent: programs
    weight: 5
---

Each resource object has two kinds of properties: *inputs* and *outputs*.

At creation time, you supply *input* properties to control the desired state of the resource:

{{< langchoose >}}

```javascript
const bucket = new aws.s3.Bucket("photos", { versioning: { enable: true } });
```

```typescript
let bucket = new aws.s3.Bucket("photos", { versioning: { enable: true } });
```

```python
bucket = s3.Bucket('my-bucket', versioning={ 'enable': True })
```

```go
_, err := s3.NewBucket(ctx, "my-bucket", &s3.BucketArgs{
    Versioning: map[string]interface{}{
        "enable": true,
    },
})
```

Input properties are key to how Pulumi works; the diffing of them instructs Pulumi how to do its deployments.  And
they are what the resource provider uses to perform actual creations and updates.

The resulting resource object offers *output* properties that communicate its final state:

{{< langchoose >}}

```javascript
bucket.bucketDomainName.apply(function (name) {
    console.log(name);
});
```

```typescript
bucket.bucketDomainName.apply((name: string) => {
    console.log(name);
});
```

```python
print(bucket.bucketDomainName)
```

```go
bucket.BucketDomainName.Apply(func (name string) error {
    fmt.Println(name)
    return nil
})
```

A resource often has different output properties than input properties, because cloud providers may compute outputs.
For instance, the URL for an API, the IP address of a load balancer, etc, are typically auto-assigned.

A resource's output properties are promise-like in nature, because they aren't known until creation finishes.  Hence the
use of the "apply"-style functions above.  Outputs will, in fact, not even resolve to a value during previews.

Output properties also carry dependency information, so that if an output from one resource is supplied as input to
another, Pulumi can track dependencies accurately for purposes of parallelism, safe deletion order, and visualizations.

***

<div class="tour-nav">
    <a class="tour-button enabled" href="{{< relref "programs-resources.md" >}}" title="Resources">◀</a>
    <span class="tour-index"><strong>6</strong>/8</span>
    <a class="tour-button enabled" href="{{< relref "programs-configuration.md" >}}" title="Custom configuration">▶</a>
</div>
