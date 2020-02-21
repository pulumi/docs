---
title: "Generate Kubernetes YAML with Real Programming Languages"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2020-02-21T13:11:29-07:00

# Draft posts are visible in development, but excluded from production builds.
# Set this property to `false` before submitting your post for review.
draft: false

# Use the optional meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. If omitted or left blank, the content preceding the `<!--more-->` token
# will be used in its place.
meta_desc: Stop writing Kubernetes YAML by hand, and start using the power of real programming languages! Pulumi now supports rendering YAML for Kubernetes resources.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - levi-blackstone

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - kubernetes
    - yaml
    - kubernetesx

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---

Stop writing Kubernetes YAML by hand, and start using the power of real programming languages! Pulumi now allows you to
generate Kubernetes manifests that can be easily integrated into existing CI/CD workflows.

<!--more-->

While Pulumi has great support for deploying and updating Kubernetes resources on a cluster, many users have asked for
the option to render YAML that they can integrate into existing workflows. The `v1.5.4` release of `pulumi-kubernetes`
adds the `renderYamlToDirectory` option, which enables this behavior.

This option is available in every Pulumi-supported language, including TypeScript/JavaScript, Python, and .NET
(Go support is coming soon!). Aside from easily templating configuration across resources, using a real programming
language allows you to write and consume libraries, and easily mix in infrastructure configuration (e.g., managed
database endpoints, object storage, etc.), all in the same program.

## Rendering YAML from TypeScript

First, choose a directory for the rendered manifests, and specify that path on a `Provider`.
```typescript
// Instantiate a Kubernetes Provider and specify the render directory.
const provider = new k8s.Provider("render-yaml", {
    renderYamlToDirectory: "rendered"
});
```

Next, use that `Provider` for any Kubernetes resources you want to render as YAML.
```typescript
// Create a Kubernetes PersistentVolumeClaim.
const pvc = new kx.PersistentVolumeClaim("data", {
    spec: {
        accessModes: [ "ReadWriteOnce" ],
        resources: { requests: { storage: "1Gi" } }
    }
}, { provider });

// Create a Kubernetes ConfigMap.
const cm = new kx.ConfigMap("cm", {
    data: { "config": "very important data" }
}, { provider });

// Create a Kubernetes Secret.
const secret = new kx.Secret("secret", {
    stringData: {
        "password": new random.RandomPassword("pw", {
            length: 12}).result,
    }
}, { provider });

// Define a Pod.
const pb = new kx.PodBuilder({
    containers: [{
        env: {
            CONFIG: cm.asEnvValue("config"),
            PASSWORD: secret.asEnvValue("password"),
        },
        image: "nginx",
        ports: {http: 8080},
        volumeMounts: [ pvc.mount("/data") ],
    }]
});

// Create a Kubernetes Deployment.
const deployment = new kx.Deployment("nginx", {
    spec: pb.asDeploymentSpec( { replicas: 3 })
}, { provider });

// Create a Kubernetes Service.
const service = deployment.createService({type: kx.types.ServiceType.LoadBalancer});
```

Now, run `pulumi update`, and Pulumi renders these resources to YAML. The update process resolves outputs as usual,
so the manifests can include other infrastructure configuration specified in your program. The rendered manifests are
kept in sync with changes to the program on each update.

Here's what the resulting directory looks like:

![Rendered Manifests](render-directory.png)

Note that `CustomResourceDefinitions` need to be applied first, so they are rendered in a separate subdirectory. You
could deploy these with `kubectl` like this:

```shell script
kubectl apply -f "${RENDER_DIRECTORY}/0-crd"
kubectl apply -f "${RENDER_DIRECTORY}/1-manifest"
```

Voilà! From 33 (44 with whitespace and comments) lines of TypeScript code to 102 lines of YAML! 

Here's the rendered `Deployment` resource.
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    foo: bar
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{"foo":"bar","pulumi.com/autonamed":"true"},"labels":{"app.kubernetes.io/managed-by":"pulumi"},"name":"nginx-nyn4tlkx"},"spec":{"replicas":3,"selector":{"matchLabels":{"app":"nginx"}},"template":{"metadata":{"labels":{"app":"nginx"}},"spec":{"containers":[{"env":[{"name":"CONFIG","valueFrom":{"configMapKeyRef":{"key":"config","name":"cm-5opqxhna"}}},{"name":"PASSWORD","valueFrom":{"secretKeyRef":{"key":"password","name":"secret-hfcg0l06"}}}],"image":"nginx","name":"nginx","ports":[{"containerPort":8080,"name":"http"}],"volumeMounts":[{"mountPath":"/data","name":"data-4qulussd"}]}],"volumes":[{"name":"data-4qulussd","persistentVolumeClaim":{"claimName":"data-4qulussd"}}]}}}}
    pulumi.com/autonamed: "true"
  labels:
    app.kubernetes.io/managed-by: pulumi
  name: nginx-nyn4tlkx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - env:
        - name: CONFIG
          valueFrom:
            configMapKeyRef:
              key: config
              name: cm-5opqxhna
        - name: PASSWORD
          valueFrom:
            secretKeyRef:
              key: password
              name: secret-hfcg0l06
        image: nginx
        name: nginx
        ports:
        - containerPort: 8080
          name: http
        volumeMounts:
        - mountPath: /data
          name: data-4qulussd
      volumes:
      - name: data-4qulussd
        persistentVolumeClaim:
          claimName: data-4qulussd
```

See [this gist](https://gist.github.com/lblackstone/686935edf7fdcd23d916f34d35bba64a) for the complete rendered output.

## Caveats

There are two important caveats to note about YAML rendering support:

1. The YAML-rendered resources are not created on a Kubernetes cluster, so information that is computed server-side
will not be available in your program. For example, a `Service` will not have IP assignments, so attempting to export
these values will not work as usual (the value will be `undefined`).
1. **Any Secret values will appear in plaintext in the rendered manifests.** This includes any values marked as
secret in Pulumi. A warning will be printed for any secret values being rendered to YAML, but it is your responsibility
to protect the rendered files.

## Learn More

If you'd like to learn about Pulumi and how to manage your
infrastructure and Kubernetes through code, [get started today]({{< relref "/docs/get-started" >}}). Pulumi is open
source and free to use.

For further examples on how to use Pulumi to create Kubernetes
clusters, or deploy workloads to a cluster, check out the rest of the
[Kubernetes tutorials]({{< relref "/docs/tutorials/kubernetes" >}}).

As always, you can check out our code on
[GitHub](https://github.com/pulumi), follow us on
[Twitter](https://twitter.com/pulumicorp), subscribe to our [YouTube
channel](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw), or
join our [Community Slack](https://slack.pulumi.com/) channel if you have
any questions, need support, or just want to say hello.
