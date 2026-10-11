import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const vpc = new awsx.ec2.Vpc("vpc");

const securityGroup = new aws.ec2.SecurityGroup("group", {
    vpcId: vpc.vpcId,
});

const ami = aws.ec2.getAmiOutput({
    filters: [{ name: "name", values: ["amzn2-ami-hvm-*"] }],
    owners: ["amazon"],
    mostRecent: true,
});

const instance = new aws.ec2.Instance("instance", {
    ami: ami.id,
    instanceType: "t2.micro",
    vpcSecurityGroupIds: [securityGroup.id],
    subnetId: vpc.publicSubnetIds.apply(ids => ids[0]),
});

export const vpcId = vpc.vpcId;
