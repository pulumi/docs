import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Get the default VPC for the current region.
const vpc = new awsx.ec2.DefaultVpc("default-vpc");

// Create a security group to allow traffic to and from the virtual machine.
const securityGroup = new aws.ec2.SecurityGroup("web-sg", {
    vpcId: vpc.vpcId,
    ingress: [
        {
            protocol: "tcp",
            fromPort: 80,
            toPort: 80,
            cidrBlocks: ["0.0.0.0/0"],
        },
    ],
    egress: [
        {
            protocol: "-1",
            fromPort: 0,
            toPort: 0,
            cidrBlocks: ["0.0.0.0/0"],
        },
    ],
});

// Create an ALB in the default VPC listening on port 80.
const alb = new awsx.lb.ApplicationLoadBalancer("web-traffic", {
    listener: {
        port: 80,
    },
    securityGroups: [securityGroup.id],
});

vpc.publicSubnetIds.apply(subnetIds => {
    // Get the latest Amazon Linux 2 AMI.
    const ami = aws.ec2.getAmiOutput({
        filters: [{ name: "name", values: ["amzn2-ami-hvm-*"] }],
        owners: ["amazon"],
        mostRecent: true,
    });

    // In each VPC subnet, create an EC2 instance and attach it to the ALB.
    subnetIds.forEach((subnetId, i) => {
        const vm = new aws.ec2.Instance(`web-${i}`, {
            ami: ami.id,
            instanceType: "t2.micro",
            subnetId,
            vpcSecurityGroupIds: alb.loadBalancer.securityGroups,
            userData: [`#!/bin/bash`, `echo "Hello World, from Server ${i + 1}!" > index.html`, `nohup python -m SimpleHTTPServer 80 &`].join("\n"),
        });

        const attachment = new awsx.lb.TargetGroupAttachment(`attachment-${i}`, {
            targetGroup: alb.defaultTargetGroup,
            instance: vm,
        });
    });
});

// Export the resulting URL so that it's easy to access.
export const endpoint = alb.loadBalancer.dnsName;
