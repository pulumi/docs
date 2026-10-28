---
title: "Faster Pulumi deployments, part 5: Persist runner caches"
# TODO: Replace the series placeholder dates before publication.
date: 2099-01-05
draft: true
meta_desc: "Reuse dependencies on customer-managed Kubernetes runners with persistent caches and ESC-authenticated private npm installation."
feature_image:
authors:
    - jonathan-davenport
tags:
    - pulumi-deployments
    - kubernetes
    - esc
category: tutorials
series: faster-pulumi-deployments
schema_type: auto
social:
    twitter:
    linkedin:
    bluesky:
---

Ephemeral job Pods are useful because each deployment begins with a separate execution environment and can discard it when the job finishes. The same lifecycle becomes wasteful, however, when dependencies downloaded into that environment disappear even though the next deployment needs identical files. Persistent cache storage separates the lifetime of those reusable files from the lifetime of an individual job.

For teams already using customer-managed Kubernetes runners, this provides a way to retain preparation without giving up per-job workspaces. It also applies to TypeScript and Python programs that continue to install dependencies during deployment. You can keep the program in its existing language while reusing files that earlier jobs have already downloaded.

<!--more-->

## Establish a baseline on your own runners

Use the program and measurement method from [part 1](/blog/speed-up-pulumi-deployments/). If you move from managed runners, collect a new baseline on Kubernetes before adding persistent storage. Changing the machine, network, and cache together would leave you uncertain which change affected deployment time.

The [managed dependency cache](/docs/deployments/concepts/settings/dependency-caching/) setting has no effect on customer-managed pools. You control dependency persistence through the runner environment instead.

Start with one agent and serial test jobs. First establish that one job can reuse another job's cache. Then test concurrent access and scheduling; those introduce different storage requirements.

## Persist the cache where the program actually runs

The first thing to establish is where the program actually executes. The long-lived agent creates a separate runner Pod for each job, and those Pods do not automatically inherit volumes mounted on the agent. Adding storage to the agent Deployment may therefore leave the deployment's filesystem unchanged. Configure the job template, then inspect an actual execution container to verify that the cache is mounted where the package manager expects it.

Create a [persistent volume claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) using a storage class suitable for your cluster. For example, this claim uses the cluster's default storage class:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pulumi-package-cache
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

Choose capacity from your dependency sizes, and create the claim in the namespace used for runner jobs. Understand the access mode before increasing concurrency: `ReadWriteOnce` permits read-write mounting from one node, not necessarily one Pod. If jobs run on different nodes, they may need different storage or separate caches.

Customize the runner job's Pod template to mount the claim. Merge these Kubernetes fields into the existing template, preserving the agent's other required settings:

```yaml
spec:
  containers:
    - name: <existing-execution-container-name>
      env:
        - name: npm_config_cache
          value: /cache/npm
      volumeMounts:
        - name: package-cache
          mountPath: /cache
  volumes:
    - name: package-cache
      persistentVolumeClaim:
        claimName: pulumi-package-cache
```

Confirm the Pod-template configuration supported by your agent version. Preserve its existing command, environment, and mounts. Set ownership or the Pod security context so the execution user can write to `/cache`.

Inspect an actual job Pod after changing the template. Confirm that it has the mount and that `npm config get cache` reports `/cache/npm`. Check this in the job container, not the agent container.

## Share downloaded packages and keep installations separate

For a Node.js project, a committed `package-lock.json` and `npm ci` give each job a defined installation to create in its own workspace. The download cache can be shared without requiring the installed dependency tree to be shared as well. This distinction matters once jobs run concurrently: reusing downloaded packages is different from allowing two installers to change the same `node_modules` directory. Start with the download cache, where the reuse is easier to separate from each job's working files.

If packages come from Artifactory, store the npm token in an ESC environment and expose it as `NPM_TOKEN`. Configure the project's `.npmrc` to reference that variable:

```ini
@acme:registry=https://<artifactory-host>/artifactory/api/npm/<npm-repository>/
//<artifactory-host>/artifactory/api/npm/<npm-repository>/:_authToken=${NPM_TOKEN}
```

Replace the scope, host, and repository with your settings. The file contains the variable reference, not the token.

Move the private package installation into a pre-run command so you can open its ESC environment explicitly. Automatic dependency installation happens earlier, before that command can supply credentials. Enable **Skip package manager dependency installation**, then add:

```bash
pulumi env run <org>/build/artifactory -- npm ci
```

Give the deployment identity permission to open the ESC environment used by this command. Referencing that environment only from stack configuration does not make its values available to the earlier installation step, which is why the explicit invocation matters. Also keep the two download mechanisms distinct: an npm token authenticates package-manager requests, not separate provider plugin requests to another endpoint.

Run a job to populate the cache, then repeat it in a new job Pod. Verify that the second Pod sees the same claim. Compare installation durations and network activity rather than assuming a mounted directory guarantees a cache hit.

For Python, direct the package manager's cache to its own directory on the volume. For Go programs that still compile during deployment, persist both `GOMODCACHE` and `GOCACHE`. Change one cache at a time and repeat the same measurement.

## Persist plugins without sharing credentials

After measuring the package cache, persist `$PULUMI_HOME/plugins` at the location used by the execution container. Resolve the actual home path before editing the Pod template; Kubernetes mount paths do not expand shell variables.

Mount the plugin directory rather than the whole Pulumi home. The home can contain credentials that have no place in a shared dependency cache. Keep caches separate across trust boundaries, and test concurrent plugin installation before sharing a writable cache across agents.

Consider how persistent storage interacts with the release approach you already use. If [part 3's artifact](/blog/version-pulumi-deployment-artifacts/) supplies the plugins, another cache is useful only if it removes work that the artifact still repeats. If [part 4's image](/blog/prebuilt-pulumi-executor-images/) already contains them, mounting an empty volume over their directory would hide the prepared files. These techniques can be combined, but adding every technique does not necessarily produce a better process.

Avoid sharing `node_modules` or a Python virtual environment between concurrent installations. If you reuse installed environments, distinguish the lock file, runtime version, operating system, and architecture. Native dependencies can depend on each of these.

## Test persistence and concurrency separately

Record first-run and repeat-run timings on the same runner configuration. Include volume scheduling or attachment delays and cache access time. A slow network volume can cost more than downloading a small dependency set.

Once serial jobs reuse the cache successfully, repeat the experiment with two concurrent jobs and inspect both storage scheduling and installation behavior. A design that helps one agent can introduce contention when several agents need the same files. Storage access modes can also force jobs to wait for an attachment or constrain which nodes can run them. Include those delays in the result rather than treating them as unrelated to the cache design.

Keep the cache when it reduces total job time under the concurrency you actually use. Once repeated preparation is under control, examine how much of the rollout is spent waiting for execution. [Part 6](/blog/reduce-pulumi-rollout-time/) applies the same measurement method to scheduling.
