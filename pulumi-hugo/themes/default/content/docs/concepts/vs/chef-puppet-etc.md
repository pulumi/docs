---
title_tag: "Pulumi vs. Chef, Puppet, Ansible, and Salt"
meta_desc: Learn about the major differences between Pulumi and configuration management tools like Chef, Puppet, Ansible, Salt, and more.
title: Chef & Puppet
h1: Chef, Puppet, Ansible, & Salt vs Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    parent: vs
    weight: 9
aliases:
- /docs/reference/vs/chef_puppet_etc/
- /docs/intro/vs/chef_puppet_etc/
---

Chef, Puppet, Ansible, and Salt are all popular _configuration management tools_. These tools help you install and
manage software on existing cloud infrastructure, either for bootstrapping a virtual machine, or patching one. They do
not attempt to solve the problem of provisioning or updating infrastructure, containers, or serverless resources.

Pulumi is fundamentally different than these tools and works great alongside them. Pulumi manages provisioning and
updating of your cloud infrastructure and applications, including virtual machines, containers, databases, hosted
cloud services, and serverless functions.

Pulumi uses expressive, general-purpose languages, much like some configuration management tools, to define cloud requirements and
desired infrastructure state. The Pulumi tool then takes these descriptions and can manage multiple environments to
ensure that your infrastructure is always up to date, either through its CLI or in a hosted CI/CD scenario.

Pulumi works well with modern "immutable infrastructure" architectures, where bootstrapping and patching are
unnecessary. In such cases, configuration management is not needed in the usual sense. Pulumi also works well with
classical approaches to infrastructure, however, which often entail virtual machines and where continuing to use a
configuration tool in conjunction is easy. In either case, Pulumi will help on your path to cloud native architectures.
