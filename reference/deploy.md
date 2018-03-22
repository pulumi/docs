---
title: "Deployments"
---

A deployment occurs any time a stack is updated.  During a deployment, the Pulumi program is executed to determine the desired state of the stack, and this is compared with the current state to determine a set of create, update and delete operations to apply to resources associated with the stack.  A deployment can be previewed, which will also run the program, but will not apply the resulting changes to the actual resources.

### Preview updates to a stack

Before updating your stack, it is recommended that you first view a preview of your the changes via `pulumi preview`.  This will preview the impact of deploying the program in the current project to the active stack.

```
$ pulumi preview
Previewing changes:
* pulumi:pulumi:Stack: (same)
    [urn=urn:pulumi:jane-dev::webserver::pulumi:pulumi:Stack::webserver-jane-dev]
---outputs:---
publicDns: "ec2-18-218-85-197.us-east-2.compute.amazonaws.com"
publicIp : "18.218.85.197"
    ~ aws:ec2/instance:Instance: (update)
        [id=i-01aedebaf8fe019c2]
        [urn=urn:pulumi:jane-dev::webserver::aws:ec2/instance:Instance::web-server-www]
        ami            : "ami-f6035893"
      - instanceType   : "t2.micro"
      + instanceType   : "t2.nano"
        securityGroups : [
            [0]: "web-secgrp-e31b7dd"
        ]
        sourceDestCheck: true
---outputs:---
publicDns: computed<string>
publicIp : computed<string>
info: 1 change previewed:
    ~ 1 resource to update
      2 resources unchanged
```

Because the changes are not actually applied during a preview, it is not possible for `pulumi preview` to know for sure whether a change will occur or not when it is dependent on the ouput of some resource being created or replaced.  Because of this, `pulumi preview` always presents a conservative summary of the changes that will be applied.  This means that when the corresponding `pulumi update` is run, it may observe fewer changes being needed, but will never observe more than what was shown during preview.

For more information, see [the Pulumi programming model](./programming-model.html).

### Update and deploy a Pulumi program

To deploy a Pulumi program to a stack for the first time, or to apply program changes to a running stack, use the `pulumi update` command.  This will execute the program in the current project and create, update and delete resources in the active stack to match the desired state.

```
$ pulumi update
Performing changes:
* pulumi:pulumi:Stack: (same)
    [urn=urn:pulumi:jane-dev::webserver::pulumi:pulumi:Stack::webserver-jane-dev]
---outputs:---
publicDns: "ec2-18-218-85-197.us-east-2.compute.amazonaws.com"
publicIp : "18.218.85.197"
    ~ aws:ec2/instance:Instance: (update)
        [id=i-01aedebaf8fe019c2]
        [urn=urn:pulumi:jane-dev::webserver::aws:ec2/instance:Instance::web-server-www]
        ami            : "ami-f6035893"
      - instanceType   : "t2.micro"
      + instanceType   : "t2.nano"
        securityGroups : [
            [0]: "web-secgrp-e31b7dd"
        ]
        sourceDestCheck: true
    ---outputs:---
    associatePublicIpAddress : true
    availabilityZone         : "us-east-2b"
    disableApiTermination    : false
    ebsOptimized             : false
    id                       : "i-01aedebaf8fe019c2"
    instanceState            : "running"
    monitoring               : false
    networkInterfaceId       : "eni-3037a664"
    primaryNetworkInterfaceId: "eni-3037a664"
    privateDns               : "ip-172-31-29-149.us-east-2.compute.internal"
    privateIp                : "172.31.29.149"
    publicDns                : "ec2-18-219-35-110.us-east-2.compute.amazonaws.com"
    publicIp                 : "18.219.35.110"
    rootBlockDevice          : {
        deleteOnTermination: true
        iops               : "100"
        volumeId           : "vol-0948a0c6d05c55daa"
        volumeSize         : "8"
        volumeType         : "gp2"
    }
    subnetId                 : "subnet-fa248781"
    tenancy                  : "default"
    vpcSecurityGroupIds      : [
        [0]: "sg-6bf88900"
    ]
---outputs:---
publicDns: "ec2-18-219-35-110.us-east-2.compute.amazonaws.com"
publicIp : "18.219.35.110"
info: 1 change performed:
    ~ 1 resource updated
      2 resources unchanged
Update duration: 58.328243145s
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