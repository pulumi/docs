import * as aws from "@pulumi/aws";

export const group = new aws.ec2.SecurityGroup("web-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

const userData = `#!/bin/bash echo "Hello, World!" > index.html nohup python3 -m http.server 80 &`;

// Look up the latest Amazon Linux 2 AMI.
const ami = aws.ec2.getAmiOutput({
    owners: ["amazon"],
    mostRecent: true,
    filters: [{ name: "name", values: ["amzn2-ami-hvm-*-x86_64-gp2"] }],
});

export const server = new aws.ec2.Instance("web-server-www", {
    instanceType: "t2.micro",
    securityGroups: [group.name], // reference the group object above
    ami: ami.id,
    userData: userData, // start a simple web server
});
