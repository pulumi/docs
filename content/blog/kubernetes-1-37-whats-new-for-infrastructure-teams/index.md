---
title: "Kubernetes 1.37: What's New for Infrastructure Teams"
date: 2026-08-26
draft: false
meta_desc: "Kubernetes 1.37 breaking changes, GA features, and deprecations infrastructure teams need to plan an upgrade around, from SELinuxMount to DRA."
authors:
    - pulumi-content-team
tags:
    - kubernetes
    - platform-engineering
    - infrastructure-as-code
    - devops
category: general
faq_schema: true

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Kubernetes 1.37 shipped. For an upgrade, the breaking changes matter more than the headline features: SELinuxMount on by default, static Pods losing Secrets/ConfigMap references, cAdvisor rejecting deprecated flags at startup. What to check first:
    linkedin: |
        Every Kubernetes release recap this week will lead with the graduations: metrics.k8s.io hitting GA after nine years in beta, HPAConfigurableTolerance, kubelet rootless mode reaching beta.

        Those matter. But for a platform team running an upgrade, the more urgent list is the one buried in the changelog: SELinuxMount going GA and on by default, static Pods losing the ability to reference Secrets and ConfigMaps with no opt-out, cAdvisor's slimmed-down flag set rejecting anything deprecated outright at kubelet startup.

        We broke down what actually needs your attention before you upgrade — the full rundown is below.
    bluesky: |
        Kubernetes 1.37 shipped. The breaking changes matter more than the feature list if you're planning an upgrade.

        SELinuxMount on by default, static Pods losing Secret/ConfigMap references, cAdvisor rejecting deprecated flags at kubelet startup. Here's what to check first.
---

Kubernetes 1.37 shipped on August 26, 2026. For infrastructure teams, the release matters less for any single headline feature than for a cluster of changes that can break an unprepared upgrade: SELinuxMount going GA and on by default, static Pods losing their ability to reference Secrets and ConfigMaps, and a slimmed-down cAdvisor that refuses to start on deprecated kubelet flags.

## The changes that can break your upgrade

Start here before you touch a cluster, because these are the items that turn a routine version bump into an incident.

**SELinuxMount is GA and enabled by default.** Volumes now mount with a fixed SELinux context (`-o context=<label>`) instead of the kubelet recursively relabeling every file, but only on CSI drivers that opt in via `CSIDriver.spec.seLinuxMount: true`. On SELinux-enabled nodes, Pods with different SELinux labels sharing the same volume can now fail to start where they previously worked. If that describes your environment, read Kubernetes' own [breaking-changes writeup on SELinux volume labeling](https://kubernetes.io/blog/2026/04/22/breaking-changes-in-selinux-volume-labeling/) before you upgrade, and set `seLinuxChangePolicy: Recursive` if you need the old behavior back. Clusters without SELinux nodes are unaffected.

**Static Pods can no longer reference Secrets or ConfigMaps.** This closes a long-standing correctness gap, and there is no escape hatch: the `PreventStaticPodAPIReferences` feature gate that used to let you opt back in has been removed entirely. If any static Pod manifests on your nodes reference a Secret or ConfigMap, they will fail after the upgrade, full stop.

**cAdvisor's slimmed-down module rejects deprecated flags outright.** The kubelet's embedded cAdvisor now runs on the leaner `github.com/google/cadvisor/lib` module, and the kubelet will fail to start if any of 18 long-deprecated flags are still set — `--containerd`, `--event-storage-age-limit`, `--boot-id-file`, and others; only `--housekeeping-interval` is kept ([kubernetes/kubernetes#139870](https://github.com/kubernetes/kubernetes/pull/139870)). Three `/metrics/cadvisor` series (`container_cpu_load_average_10s`, `container_cpu_load_d_average_10s`, `container_tasks_state`) and the `userDefinedMetrics` field in `/stats/summary` are also gone. Audit your kubelet configuration and any custom metrics scraping before you roll this out.

**Workload-Aware Scheduling requires a manual cleanup step.** The core `Workload` and `PodGroup` types move from `scheduling.k8s.io/v1alpha2` to `v1alpha3` in this release. If you were running v1alpha2 objects under 1.36, the changelog is explicit: delete them from the API server before you upgrade, or the migration will not complete cleanly.

**kubeadm's v1beta3 config API is gone.** Deprecated since v1.31, it's now removed outright: if you're still generating v1beta3 config, run `kubeadm config migrate` first.

**`eventRecordQPS: 0` finally means what it says.** A long-standing bug silently treated a value of `0` in kubelet config as "use the default" instead of "unlimited." That bug is fixed in 1.37. If you were relying on the old behavior, set the value explicitly (`50` restores the previous numeric default) rather than leaving it at `0`.

## What actually got better

Once the upgrade risks are accounted for, this release does move six things that infrastructure teams have been waiting on.

**`metrics.k8s.io` reaches GA after roughly nine years in beta.** This is the API underneath the Horizontal Pod Autoscaler and `kubectl top` — no new capability ships with the graduation, but it closes out one of the longest-running beta APIs in the project's history. Both `v1beta1` and `v1` remain usable during the transition.

**HPAConfigurableTolerance is GA.** Teams can now tune how sensitive the HPA is to metric fluctuations instead of living with the fixed 10% tolerance band, which should cut down on scale flapping for workloads with noisy metrics.

**Kubelet-in-user-namespace ("rootless mode") reaches beta.** Node components can now run inside a Linux user namespace — unprivileged on the host, root only inside the namespace — meaningfully shrinking the blast radius of a kubelet or container runtime CVE.

**Three storage and networking primitives move to beta enabled by default**, worth a look depending on your stack: `EtcdRangeStream`, which lets the API server's watch cache stream initial objects from etcd via a single RPC instead of paginated calls, a real scalability win for large clusters; `NFTablesNetlink`, where kube-proxy talks to the kernel directly over netlink instead of shelling out to the `nft` binary; and `PersistentVolumeClaimUnusedSinceTime`, which reports how long a PVC has gone unused so storage-cost cleanup can be automated instead of manual.

A handful of smaller but genuinely useful items also landed: `kubectl get -o kyaml` is stable for cleaner YAML output, `StorageVersionMigration` reaches GA, `ClusterTrustBundle` is stable for custom CA distribution, and Pod Certificates graduate to GA.

`PodLevelResourceManagers` (distinct from the longer-standing `PodLevelResources` API gate, unaffected here) was promoted to beta mid-cycle ([#140573](https://github.com/kubernetes/kubernetes/pull/140573)), then flipped back to disabled by default late in the cycle after critical issues turned up in testing ([#141209](https://github.com/kubernetes/kubernetes/pull/141209)). It ships in 1.37 as beta, disabled by default — worth knowing about if you're tracking pod-level resource management, but it won't affect your cluster's behavior unless you explicitly enable the feature gate.

## The accelerator story, without the hype

This release's answer to "AI infrastructure" is a set of incremental improvements to Dynamic Resource Allocation (DRA), the mechanism Kubernetes uses to model devices like GPUs beyond the old `nvidia.com/gpu`-style extended-resource counting, rather than any single headline feature.

DRA device taints and tolerations reach GA, so operators can taint a misbehaving GPU and have workloads avoid or tolerate it the same way they would a tainted node. DRA extended resources also reach GA, letting classic extended-resource requests be satisfied through DRA under the hood. On the alpha side, DRA device compatibility groups let drivers declare which devices genuinely can and can't be co-allocated — catching an incompatible GPU-and-NIC pairing at scheduling time instead of as a runtime failure — and a new CEL-based mechanism lets ResourceClaims derive attributes so devices from different domains can be matched for NUMA-aware co-allocation. None of this is branded "AI" anywhere in the changelog, and it shouldn't be: it's scheduling and device-management plumbing that happens to be exactly what GPU-heavy workloads need.

## The deprecation clock keeps running

Two long-running phase-outs continue in 1.37, neither urgent today but both worth putting on a calendar. kube-proxy's `ipvs` mode was formally deprecated back in v1.35 under [KEP-5495](https://github.com/kubernetes/enhancements/blob/master/keps/sig-network/5495-deprecate-ipvs-mode-in-kube-proxy/README.md); 1.37 is Stage 2 of that plan, adding a `KubeProxyIPVS` feature gate (default `true`) plus kubeadm warnings and updated docs ahead of a default-off flip planned for v1.40 and full removal planned for v1.43. Check which mode you're running with:

```
kubectl -n kube-system get configmap kube-proxy -o jsonpath='{.data.config\.conf}' | grep 'mode:'
```

Separately, the cgroup v1 phase-out that began with `failCgroupV1` defaulting to true in v1.35 continues; nodes still on cgroup v1 need an explicit override to keep the kubelet starting, and features like in-place pod resize require cgroup v2 outright.

## When does this actually reach your cluster?

Upstream GA is the start of the clock, not the end of it. If you run self-managed clusters with `kubeadm` or `kOps`, you can generally adopt 1.37 as soon as your node images and add-ons are validated against it. If you run a managed service, the timeline is entirely up to your provider: EKS, AKS, and GKE each pick up new minor versions on their own release cadence, historically weeks to a few months behind upstream GA, and each backports its own subset of fixes in the meantime. Our [guide to managed Kubernetes services](/tutorials/glossary/managed-kubernetes/) covers how EKS, AKS, and GKE differ in upgrade cadence, support windows, and what they manage for you versus what you're still responsible for — useful context before you assume upstream's GA date is also your cluster's availability date.

## Managing the churn with infrastructure as code

None of the changes above are reasons to avoid the upgrade. They're reasons to make the upgrade a reviewable change instead of a surprise. Pinning your cluster and node-pool versions in code means a version bump shows up as a diff in a pull request, not a silent drift discovered during an incident. The same applies to feature-gate configuration and the API-version migrations this release requires: a `Workload` object still on `v1alpha2` is something you can grep for in code before you run `pulumi up`, rather than something you discover when the upgrade fails halfway through.

For teams managing custom resources, [`crd2pulumi`](/docs/integrations/clouds/kubernetes/crd2pulumi/) generates typed SDK bindings straight from a CRD's OpenAPI schema, so a new CRD version is a type-checked change rather than a runtime surprise. And [Server-Side Apply](https://www.pulumi.com/registry/packages/kubernetes/how-to-guides/managing-resources-with-server-side-apply/), the default reconciliation strategy since the Kubernetes provider's v4 release, plus [built-in await logic](/blog/improved-kubernetes-await-logic/) that waits on real readiness signals rather than a bare "created" response, are both aimed at the same problem: making Kubernetes changes behave predictably under automation.

It's also worth being direct about where that model stops. Kubernetes reconciles the objects inside your cluster; it has no opinion about the cloud resources — the managed database, the load balancer, the IAM role — that the cluster and its workloads depend on. Our explainer on [whether Kubernetes itself counts as infrastructure as code](/what-is/is-kubernetes-infrastructure-as-code/) digs into that boundary, and our companion piece on [infrastructure as code for Kubernetes](/what-is/infrastructure-as-code-for-kubernetes/) covers the practical tooling landscape for managing the cluster, its workloads, and everything around them in one codebase.

One honest caveat: as of this release, the [`@pulumi/kubernetes` provider](https://www.pulumi.com/registry/packages/kubernetes/) has its schema generated against upstream Kubernetes 1.36.2, with 1.36.3 and 1.36.4 already queued for an upcoming release. A 1.37 schema update will follow in a subsequent provider release; recent minor-version bumps have landed anywhere from days to months after their upstream GA, so pin your provider version and watch the [provider's CHANGELOG](https://github.com/pulumi/pulumi-kubernetes/blob/master/CHANGELOG.md) rather than assuming a fixed lag. Nothing above requires waiting for that update to start reviewing your cluster configuration against the changes in this post.

## Frequently asked questions

### When was Kubernetes 1.37 released?

Kubernetes 1.37 was released on August 26, 2026, following its final release candidate on August 20. It follows the standard quarterly Kubernetes release cadence.

### What are the breaking changes in Kubernetes 1.37?

The changes most likely to break an upgrade are SELinuxMount reaching GA and defaulting to on for CSI drivers that opt in, static Pods losing the ability to reference Secrets or ConfigMaps with no remaining opt-out, and the kubelet's slimmed-down cAdvisor module refusing to start if deprecated flags are still set. Clusters using Workload-Aware Scheduling's older `v1alpha2` API also need those objects removed before upgrading.

### Does Kubernetes 1.37 deprecate kube-proxy's IPVS mode?

No — that happened in v1.35. Kubernetes 1.37 is Stage 2 of the [KEP-5495](https://github.com/kubernetes/enhancements/blob/master/keps/sig-network/5495-deprecate-ipvs-mode-in-kube-proxy/README.md) phase-out: it adds a `KubeProxyIPVS` feature gate, defaulting to `true`, along with updated kubeadm warnings and documentation. The plan calls for disabling `ipvs` by default in v1.40 and removing it entirely in v1.43. Clusters currently running in `ipvs` mode should plan a migration to `iptables` or `nftables` mode well before then.

### When will Kubernetes 1.37 be available on EKS, AKS, and GKE?

Each managed Kubernetes provider sets its own timeline for adopting a new minor version, and historically that has run from weeks to a few months after upstream GA. Check your provider's release notes directly rather than assuming day-one availability; our [guide to managed Kubernetes services](/tutorials/glossary/managed-kubernetes/) covers how EKS, AKS, and GKE differ on upgrade cadence and support windows.

### Does Pulumi support Kubernetes 1.37?

The `@pulumi/kubernetes` provider's schema is generated from a specific upstream Kubernetes version, and its most recent release tracks Kubernetes 1.36.2, with 1.36.3 and 1.36.4 already queued for an upcoming release. A 1.37 schema update will follow in a subsequent release; recent minor-version bumps have landed anywhere from days to months after upstream GA, so pin your provider version and watch the [provider's CHANGELOG](https://github.com/pulumi/pulumi-kubernetes/blob/master/CHANGELOG.md) rather than assuming a fixed timeline. Most Pulumi programs are unaffected in the meantime, since the provider's generated types are additive across most Kubernetes minor versions.

### How do I upgrade to Kubernetes 1.37 safely?

Before upgrading, check your nodes for SELinux usage and CSI driver `seLinuxMount` opt-in, search for static Pod manifests referencing Secrets or ConfigMaps, confirm your kubelet configuration doesn't set any of the flags cAdvisor's slimmed-down module now rejects, and remove any lingering `scheduling.k8s.io/v1alpha2` Workload-Aware Scheduling objects. Managing these settings as code makes each of these checks a reviewable diff rather than a manual audit performed under time pressure during the upgrade window.
