import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

const userData = `
    #!/bin/bash
    sudo yum update -y
    sudo yum upgrade -y
    sudo amazon-linux-extras install nginx1 -y
    sudo systemctl enable nginx
    sudo systemctl start nginx`;

// [Step 2: Create a security group.]
const securityGroup = new aws.ec2.SecurityGroup("webserver-secgrp2", {
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

// [Step 1: Create an EC2 instance.]
const server = new aws.ec2.Instance("webserver-www2", {
    instanceType: "t2.micro",
    ami: "ami-09538990a0c4fe9be",
    userData: userData,
    vpcSecurityGroupIds: [securityGroup.id],
});

export const publicIp = server.publicIp;
