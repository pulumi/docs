---
title: "Deployments"
---

A deployment occurs any time a stack is updated.  During a deployment, the Pulumi program is executed to determine the desired state of the stack, and this is compared with the current state to determine a set of create, update and delete operations to apply to resources associated with the stack.  A deployment can be previewed, which will also run the program, but will not apply the resulting changes to the actual resources.

### Preview updates to a stack

Before updating your stack, `pulumi update` first shows a preview of changes, which shows the impact of deploying the current project to the active stack. To view just the preview, run `pulumi update --preview`.

```
$ pulumi update --preview
Previewing stack 'webserver-testing'
Previewing changes:

#: Resource Type          Name                         Plan      Extra Info
1: pulumi:pulumi:Stack    webserver-webserver-testing  + create
2: aws:ec2:SecurityGroup  webserver-secgrp             + create
3: aws:ec2:Instance       webserver-www                + create

info: 3 changes previewed:
    + 3 resources to create
```

Because the changes are not actually applied during the preview phase, it is not possible for `pulumi update` to know for sure whether a change will occur or not when it is dependent on the output of some resource being created or replaced.  Because of this, `pulumi update --preview` always presents a conservative summary of the changes that will be applied.  This means that when changes are actually applied, it may observe fewer changes being needed, but will never observe more than what was shown during preview.

For more information, see [the Pulumi programming model](./programming-model.html).

### Update and deploy a Pulumi program

To deploy a Pulumi program to a stack for the first time, or to apply program changes to a running stack, use the `pulumi update` command.  This will execute the program in the current project and create, update and delete resources in the active stack to match the desired state.

```
Do you want to proceed? yes
Updating stack 'webserver-testing'
Performing changes:

#: Resource Type          Name                         Status     Extra Info
1: pulumi:pulumi:Stack    webserver-webserver-testing  + created
2: aws:ec2:SecurityGroup  webserver-secgrp             + created
3: aws:ec2:Instance       webserver-www                + created

info: 3 changes performed:
    + 3 resources created
Update duration: 24.875321975s

Permalink: https://pulumi.com/lindydonna/-/-/webserver-testing/updates/1
```

### Delete all stack resources

To delete all resources in the selected stack, use the `pulumi destroy` command. 

```
$ pulumi destroy
This will permanently destroy all resources in the 'jane-dev' stack!
Please confirm that this is what you'd like to do by typing ("jane-dev"): jane-dev
Performing changes:
- aws:ec2/instance:Instance: (delete)
    [id=i-01aedebaf8fe019c2]
    [urn=urn:pulumi:jane-dev::webserver::aws:ec2/instance:Instance::web-server-www]
    ami            : "ami-f6035893"
    instanceType   : "t2.nano"
    securityGroups : [
        [0]: "web-secgrp-e31b7dd"
    ]
    sourceDestCheck: true
- aws:ec2/securityGroup:SecurityGroup: (delete)
    [id=sg-6bf88900]
    [urn=urn:pulumi:jane-dev::webserver::aws:ec2/securityGroup:SecurityGroup::web-secgrp]
    description        : "Enable HTTP access"
    ingress            : [
        [0]: {
            cidrBlocks: [
                [0]: "0.0.0.0/0"
            ]
            fromPort  : 80
            protocol  : "tcp"
            self      : false
            toPort    : 80
        }
    ]
    name               : "web-secgrp-e31b7dd"
    revokeRulesOnDelete: false
- pulumi:pulumi:Stack: (delete)
    [urn=urn:pulumi:jane-dev::webserver::pulumi:pulumi:Stack::webserver-jane-dev]
info: 3 changes performed:
    - 3 resources deleted
Update duration: 33.233230686s
```