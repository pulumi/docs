import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const group = new aws.ec2.SecurityGroup("web-sg", {
    description: "Enable HTTP access",
    ingress: [
        {
            protocol: "tcp",
            fromPort: 80,
            toPort: 80,
            cidrBlocks: ["0.0.0.0/0"],
        },
    ],
});

const server = new aws.ec2.Instance("web-server", {
    ami: "ami-0319ef1a70c93d5c8",
    instanceType: "t2.micro",
    vpcSecurityGroupIds: [group.id],
});

export const publicIp = server.publicIp;
export const publicDns = server.publicDns;
