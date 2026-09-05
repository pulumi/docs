---
title: What Is Immutable Infrastructure?
meta_desc: "Immutable infrastructure means never modifying a running server—you replace it with a new versioned image. Learn how it works and why it stops drift."
type: what-is
page_title: "What Is Immutable Infrastructure?"
authors: ["pulumi-content-team"]
---

**Immutable infrastructure is a model in which a server, container, or resource is never modified after it's deployed. When you need a change—a patch, a config edit, a new application version—you build a new, version-controlled image and replace the running instance instead of altering it in place.** The running fleet becomes a disposable artifact of a build pipeline rather than a hand-tuned, long-lived machine, which is what makes it reproducible.

The opposite model, *mutable* infrastructure, treats servers as long-lived pets you patch, reconfigure, and SSH into over months or years. Immutable infrastructure treats them as cattle: identical, replaceable, and rebuilt from a known image rather than repaired. That shift is the single most effective structural defense against [configuration drift](/what-is/what-is-infrastructure-drift/), because a machine that is never changed after boot has nothing to drift *to*.

In this article, we'll cover the key questions about immutable infrastructure:

* What is immutable infrastructure?
* Where did immutable infrastructure come from?
* How does immutable infrastructure work?
* How is it different from mutable infrastructure?
* What are the benefits of immutable infrastructure?
* What are the trade-offs of immutable infrastructure?
* How does immutable infrastructure relate to infrastructure as code and drift?
* How does Pulumi support immutable infrastructure?
* Frequently asked questions about immutable infrastructure

## What is immutable infrastructure?

Immutable infrastructure rests on one rule: once a resource is running, you don't touch it. AWS states the model plainly in its Well-Architected Framework—it "mandates that no updates, security patches, or configuration changes happen in-place on production workloads. When a change is needed, the architecture is built onto new infrastructure and deployed into production."

The practical consequence is a *replace-don't-patch* workflow. Every change—a kernel update, a new dependency, a one-line config tweak—goes through the same path: edit the source that defines the image, build a fresh versioned artifact, deploy new instances from it, shift traffic over, and discard the old ones. Nothing is ever hand-edited on a live box. As the O'Reilly primer on the subject put it, "once you instantiate something, you never change it. Instead, you replace it with another instance."

Because every running instance is a byte-for-byte product of a build you can rerun, the image *is* the source of truth for what's deployed. There are no accumulated manual tweaks that live only in one machine's memory and nowhere in version control.

## Where did immutable infrastructure come from?

The idea crystallized out of a cluster of related concepts at ThoughtWorks in 2012–2013, and the vocabulary is worth getting right because the names are often conflated.

* **Snowflake server** (Martin Fowler, July 2012). A production server made unique and impossible to reproduce by years of accumulated manual changes—"a unique snowflake: good for a ski resort, bad for a data center."
* **Phoenix server** (Martin Fowler, July 2012; term credited to his colleague Kornelis Sietsma). A server that is regularly destroyed and rebuilt from scratch, "rising from the ashes." Its stated purpose is "to avoid configuration drift: ad hoc changes to a system's configuration that go unrecorded."
* **Immutable server** (published June 2013 in a guest post by Kief Morris on Fowler's site; term credited to Ben Butler-Cole). The logical endpoint: "a server that once deployed, is never modified, merely replaced with a new updated instance. Fixes, changes, and updates are applied to the base image rather than to running systems."
* **Immutable infrastructure** (Chad Fowler, June 2013). In the essay "Trash Your Servers and Burn Your Code," Chad Fowler—a different person from Martin Fowler—coined the umbrella term, drawing an explicit analogy to immutability in functional programming languages like Erlang, Haskell, and Clojure: "If you absolutely know a system has been created via automation and never changed since the moment of creation, most of the problems I describe above disappear." Fowler was careful to note he was naming an existing practice, not inventing it.

This is also the era that popularized the "pets versus cattle" metaphor for the same distinction—servers you name and nurse back to health versus servers you number and replace. Containers later turned the metaphor into a default: a running container is expected to be disposable.

## How does immutable infrastructure work?

Immutable infrastructure is a build-and-replace pipeline. Three building blocks do the work.

**Golden images.** A golden (or "baked") image is a pre-built base image that bundles the operating system, security patches, monitoring and logging agents, and application dependencies, so nothing has to be configured at boot. HashiCorp's [Packer](https://developer.hashicorp.com/packer) is the canonical tool for baking them: it selects a base image (say, a current Ubuntu AMI), provisions it by copying files and running setup scripts, and publishes the result as a versioned artifact—for example, a new Amazon Machine Image (AMI)—that an autoscaling group can launch unchanged.

**Containers.** Containers are the mainstream embodiment of the idea. A container image is built once and run identically everywhere. Kubernetes states the expectation directly: containers are "intended to be stateless and immutable... you should not change the code of a container that is already running. If you have a containerized application and want to make changes, the correct process is to build a new image that includes the change, then recreate the container." An ad-hoc `docker exec` to patch a live container is exactly the anti-pattern immutability forbids.

**Replacement deployments.** Because you can't edit in place, you deploy by standing up new instances alongside the old ones and cutting over only once they're healthy:

* **Blue/green.** A "blue" fleet carries production traffic while a "green" fleet is built and deployed with the new image. You cut over by pointing the load balancer at the green fleet; rollback is pointing it back at blue.
* **Rolling / immutable updates.** AWS Elastic Beanstalk's immutable update, for instance, launches a second, temporary autoscaling group of new instances, waits for all of them to pass health checks, then retires the old group. A failed update is undone simply by terminating the new group—no in-place repair required.

## How is it different from mutable infrastructure?

Mutable infrastructure is the traditional model: you provision a server once, then keep changing it in place—applying patches, editing config files, running configuration-management tools like Ansible, Chef, or Puppet to converge it toward a desired state. That works, but every in-place change is an opportunity for one machine to diverge from its siblings, and over time you get snowflakes no one can confidently reproduce.

| | Mutable infrastructure | Immutable infrastructure |
|---|---|---|
| **Making a change** | Modify the running server in place | Build a new image, replace the server |
| **Server lifespan** | Long-lived; patched for months or years | Short-lived; replaced on every change |
| **Source of truth** | The running machine's current state | The versioned image and its build definition |
| **Config drift** | Accumulates with every manual edit | Structurally prevented—nothing changes after boot |
| **Rollback** | Reverse the change, hope it's clean | Redeploy the previous image |
| **Typical tooling** | Ansible, Chef, Puppet, SSH | Packer, Docker, container orchestrators, autoscaling groups |
| **Failure mode** | Snowflake servers, "works on that one box" | Longer builds, harder state handling |

Note that configuration-management tools aren't the enemy here—they're often used to *build* the golden image. The difference is *when* they run: at image-build time (immutable) versus against live production servers on an ongoing basis (mutable).

## What are the benefits of immutable infrastructure?

**It eliminates configuration drift.** This is the headline benefit, cited by AWS, HashiCorp, and Martin Fowler alike. When 100% of a server's state comes from a versioned image and nothing is edited afterward, there's no mechanism for the running fleet to silently diverge from what your code says. HashiCorp notes that with immutable containers, "every container across development, staging, and production matches its image exactly."

**Rollbacks are fast and reliable.** Because the previous version is just a previous image, reverting is a deploy, not a surgical repair. In AWS's immutable update model, rolling back a failed release is as simple as terminating the new autoscaling group.

**Deployments are reproducible and consistent.** The same image runs in dev, staging, and production, which collapses the "works on my machine" class of bugs. You can rebuild any environment from source at any time.

**It shrinks the attack surface.** A fleet that's routinely rebuilt and never logged into by hand gives an attacker far less to work with: no long-lived servers accumulating undocumented changes, no need for standing SSH access to patch boxes, and any compromise is wiped on the next replacement rather than persisting for months.

**It simplifies scaling.** Autoscaling is trivial when every instance is identical and launched from the same image—there's no per-machine configuration step that might succeed on one node and fail on another.

## What are the trade-offs of immutable infrastructure?

Immutability isn't free, and it fits some workloads better than others.

**Stateful data needs a home outside the instance.** If servers are disposable, anything you can't afford to lose—databases, uploaded files, caches you want to survive a redeploy—has to live in managed services or attached volumes, not on the instance's local disk. Designing that separation is the single biggest adjustment teams make when adopting the model.

**Every change means a build.** You can't hotfix a one-character typo by editing a live file; you rebuild and redeploy an image. That's healthier in the long run, but it adds image-build time to the change cycle and demands a mature, automated build-and-deploy pipeline. Immutable infrastructure without solid automation is painful.

**Image sprawl and storage.** Versioned images accumulate, and they consume registry and storage space. Teams need a lifecycle policy for pruning old artifacts.

**It's a poor fit for genuinely long-lived, hand-managed systems.** Legacy applications that expect a persistent local filesystem, or environments where operators routinely need to intervene by hand, can be forced into the model but rarely benefit from it.

## How does immutable infrastructure relate to infrastructure as code and drift?

[Infrastructure as code](/what-is/what-is-infrastructure-as-code/) and immutable infrastructure are complementary, not the same thing. IaC is about *declaring* your desired infrastructure in version-controlled code. Immutability is a discipline about *how you change what's running*: by replacement rather than in-place edits. You can practice IaC and still mutate servers by hand after they're created; immutable infrastructure closes that gap by making the image—produced from code—the only way anything reaches production.

The connection to [infrastructure drift](/what-is/what-is-infrastructure-drift/) is direct. Drift is the divergence between what your code says exists and what's actually running, and it's introduced by out-of-band changes to live resources. Immutable infrastructure attacks that problem at the root: if resources are never modified after deployment, the most common source of drift—someone editing a live server—simply can't happen. It's the preventive counterpart to drift *detection*: detection tells you when reality has diverged; immutability structurally reduces how often it can.

## How does Pulumi support immutable infrastructure?

Pulumi is [infrastructure as code](/what-is/what-is-infrastructure-as-code/) that models immutable patterns natively, because its engine already thinks in terms of desired state and replacement.

* **Replacement is a first-class operation.** When a change touches a property that a cloud provider can't modify in place, Pulumi replaces the resource—creating the new one and deleting the old—rather than attempting an illegal in-place edit. That's immutable infrastructure at the resource level, handled automatically.
* **You control replacement explicitly.** The [`replaceOnChanges`](/docs/iac/concepts/resources/options/replaceonchanges/) resource option forces a resource to be replaced when specified properties change, and [`deleteBeforeReplace`](/docs/iac/concepts/resources/options/deletebeforereplace/) lets you tune replacement ordering—create-before-delete by default, for zero-downtime cutovers.
* **It orchestrates the whole immutable pipeline.** Pulumi provisions the autoscaling groups, load balancers, container registries, and Kubernetes workloads that a golden-image or container strategy runs on—so building a new image and rolling it out with a blue/green or immutable-update pattern is all expressed in one program, in a real programming language.
* **It manages resources through provider APIs, not SSH.** Pulumi never logs into your servers to reconfigure them; it drives change through cloud provider APIs, which keeps the workflow aligned with the immutable model.

Immutability handles prevention; Pulumi also handles the other half of the problem. Scheduled [drift detection](/docs/deployments/concepts/drift/) in Pulumi Cloud catches the divergence that inevitably slips through—managed services and other actors can still change resources even in a mostly-immutable estate—so you get structural prevention *and* a safety net. See [Detecting and reconciling drift](/docs/iac/operations/stack-management/drift/) for the full workflow.

## Frequently asked questions about immutable infrastructure

### What is immutable infrastructure in simple terms?

It's a rule for running infrastructure: never change a server, container, or resource after you deploy it. To make any change, you build a new version-controlled image and swap the running instance for a fresh one built from it, instead of patching or reconfiguring the live machine.

### What is the difference between mutable and immutable infrastructure?

Mutable infrastructure keeps long-lived servers and changes them in place—patching, editing config, running tools like Ansible or Chef against production. Immutable infrastructure treats servers as disposable: you replace them with new instances built from an updated image rather than modifying the running ones. The practical payoff of the immutable approach is the elimination of configuration drift.

### Does immutable infrastructure eliminate configuration drift?

It eliminates the most common cause—manual, out-of-band edits to live servers—because there are no live servers to edit; each is a fixed product of a versioned image. It doesn't make drift categorically impossible: a managed service can still rotate a credential or an external process can still change a resource, which is why detection remains valuable even in an immutable estate.

### Are containers immutable infrastructure?

Containers are the most widely used form of it. A container image is built once and run unchanged across environments, and orchestrators like Kubernetes expect running containers to be disposable—you change an application by building a new image and recreating the container, not by editing the one that's running.

### What are golden images?

A golden (or baked) image is a pre-built base image containing the operating system, security patches, monitoring agents, and application dependencies, ready to launch without runtime configuration. Tools like HashiCorp Packer build them as versioned artifacts—such as an AWS AMI or a container image—that you deploy unchanged.

### When should you not use immutable infrastructure?

It's a weaker fit for stateful systems that expect a persistent local filesystem, for legacy applications that can't be cleanly containerized or re-imaged, and for teams without the build-and-deploy automation the model depends on. Stateful data always needs to live in managed services or attached storage rather than on the disposable instance itself.

## Learn more

Immutable infrastructure and Pulumi solve complementary halves of the same problem: immutability prevents most configuration drift by never modifying running resources, and Pulumi provisions the immutable pipeline while catching whatever drift slips through. [Read the drift detection and reconciliation guide](/docs/iac/operations/stack-management/drift/) to see how prevention and detection fit together.

Related reading:

* [What is infrastructure as code?](/what-is/what-is-infrastructure-as-code/)
* [What is infrastructure drift?](/what-is/what-is-infrastructure-drift/)
* [What is configuration management?](/what-is/what-is-configuration-management/)
* [What is cloud security?](/what-is/what-is-cloud-security/)
* [Resource options: replaceOnChanges](/docs/iac/concepts/resources/options/replaceonchanges/)
* [Detecting and reconciling drift](/docs/iac/operations/stack-management/drift/)
