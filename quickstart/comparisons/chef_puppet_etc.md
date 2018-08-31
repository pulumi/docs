---
title: Chef, Puppet, etc.
---

Chef, Puppet, Ansible, and Salt are all popular _configuration management tools_. These help you install and manage
software on existing cloud infrastructure, either for bootstrapping a virtual machine, or patching one.

Pulumi is fundamentally different, and complements configuration management tools, because it focuses on the
provisioning and update of infrastructure itself. This is often because users of Pulumi prefer [cattle over pets](
https://www.engineyard.com/blog/pets-vs-cattle), tend to use more container-oriented systems where bootstrapping is
handled by a `Dockerfile` where patching "in place" is unnecessary, and/or are either happy to do configuration
management as a layer on top of Pulumi, or are moving away from it altogether as their shift to cloud native
architectures.
